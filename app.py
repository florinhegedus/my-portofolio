from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create a database model for storing form messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Message {self.name}>"

# Create the database (only needs to be done once)
with app.app_context():
    db.create_all()

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/work-with-me', methods=['GET', 'POST'])
def work_with_me():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message_text = request.form['message']

        # Create a new message and save it to the database
        new_message = Message(name=name, email=email, message=message_text)
        db.session.add(new_message)
        db.session.commit()

        return redirect(url_for('thank_you', name=name))

    return render_template('work_with_me.html')

@app.route('/thank-you')
def thank_you():
    name = request.args.get('name', 'Guest')
    return render_template('thank_you.html', name=name)

@app.route('/messages')
def view_messages():
    messages = Message.query.all()
    return render_template('view_messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
