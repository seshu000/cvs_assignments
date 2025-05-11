import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [userMessage, setUserMessage] = useState(''); 
  const [conversation, setConversation] = useState([]); 
  const [fullConversation, setFullConversation] = useState([]); 
  const [displayFullHistory, setDisplayFullHistory] = useState(false); 

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!userMessage.trim()) return;

    setConversation(prev => [...prev, { sender: 'user', text: userMessage }]);

    try {
      const response = await axios.post('/chat', { message: userMessage }); 
      const botResponse = response.data.response; 

      setConversation(prev => [...prev, { sender: 'bot', text: botResponse }]);
    } catch (error) {
      console.error('Error:', error);
    }

    setUserMessage(''); 
  };

  const fetchFullHistory = async () => {
    try {
      const res = await axios.get('/history'); 
      setFullConversation(res.data.history); 
      setDisplayFullHistory(true); 
    } catch (err) {
      console.error('Error fetching full history:', err);
    }
  };

  const clearHistory = async () => {
    try {
      await axios.post('/clear'); 
      setFullConversation([]);
      setConversation([]); 
      setDisplayFullHistory(false);
    } catch (err) {
      console.error('Error clearing history:', err);
    }
  };

  return (
    <div className="App">
      <h1>AI Chatbot</h1>
      <div className="button-group">
        <button onClick={() => displayFullHistory ? setDisplayFullHistory(false) : fetchFullHistory()}>
          {displayFullHistory ? 'Hide History' : 'Show Full History'}
        </button>
        <button onClick={clearHistory}>Clear History</button>
      </div>

      <div className="chatbox">
        <div className="chat-display">
          {conversation.map((entry, index) => (
            <div key={index} className={`message ${entry.sender}`}>
              <strong>{entry.sender === 'user' ? 'You' : 'AI'}:</strong>
              <p>{entry.text}</p>
            </div>
          ))}
        </div>
        <form onSubmit={handleSendMessage} className="input-form">
          <input
            type="text"
            value={userMessage}
            onChange={(e) => setUserMessage(e.target.value)}
            placeholder="Ask something..."
            required
          />
          <button type="submit">Send</button>
        </form>

        {displayFullHistory && (
          <div className="full-history">
            <h2>Full Conversation History</h2>
            {fullConversation.map((entry, index) => (
              <div key={index} className={`message ${entry.sender}`}>
                <strong>{entry.sender === 'user' ? 'You' : 'AI'}:</strong>
                <p>{entry.text}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
