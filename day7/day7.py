
from flask import Flask, request

app = Flask(__name__)
my_content = ""

@app.route("/updatefortoday", methods=["GET", "POST"])
def handle_note():
    global my_content
    if request.method == "POST":
        input_data = request.form.get("note")
        if input_data is not None:
            my_content = input_data
        return "<p>Note saved</p>"
    html_form = f'''
        <h3>HI!</h3>
        <h4>Edit Today's Note</h4>
          <form method="post" style="background-color: ; padding: 20px; border-radius: 50px;">
            <textarea name="note" style="width:400px; height:200px;">{my_content}</textarea><br>
            <button type="submit" style="padding: 10px 20px; background-color:green; color: white; border: none; border-radius: 5px;">Submit</button>
        </form>
    '''
    return html_form

@app.route("/share", methods=["GET"])
def display_note():
    return f"<h2>Note Preview</h2><div style='white-space:pre-wrap;'>{my_content}</div>"

@app.route("/clearnotepadtxt", methods=["GET"])
def erase_note():
    global my_content
    my_content = ""
    return "<p>YOU cleared the content.</p>"

if __name__ == "__main__":
    app.run(debug=True)
