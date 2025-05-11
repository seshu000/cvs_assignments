from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
model = ChatMistralAI(model="mistral-small", temperature=0.7, api_key=api_key)

app = Flask(__name__, static_folder="build", static_url_path="/")
CORS(app)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI assistant. Respond helpfully."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{message}")])

chat_chain = chat_prompt | model
chat_history_store = {}
def get_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in chat_history_store:
        chat_history_store[session_id] = InMemoryChatMessageHistory()
    return chat_history_store[session_id]

chat_handler = RunnableWithMessageHistory(
    chat_chain,
    get_history,
    input_messages_key="message",
    history_messages_key="chat_history"
)
@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.get_json()
    user_message = user_data.get('message')
    session_id = user_data.get('session_id', 'default')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    result = chat_handler.invoke(
        {"message": user_message},
        config={"configurable": {"session_id": session_id}}
    )

    return jsonify({"response": result.content})
@app.route('/history', methods=['GET'])
def get_all_history():
    all_histories = {
        session_id: [msg.content for msg in history.messages]
        for session_id, history in chat_history_store.items()
    }
    return jsonify({"history": all_histories})

@app.route('/clear', methods=['POST'])
def clear_history():
    chat_history_store.clear()
    return jsonify({"message": "History cleared successfully"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
