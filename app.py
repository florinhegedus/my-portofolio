import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv


# Check if running inside a container
in_container = os.getenv('IN_CONTAINER', 'False')  # Default to 'False' if not found
if not in_container:
    load_dotenv()

app = Flask(__name__)

# Configure Flask-Mail with SMTP settings (example uses Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")

mail = Mail(app)

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

        # Compose the email message
        subject = f"my-portofolio: New message from {name} ({email})"
        body = f"Name: {name}\nEmail: {email}\nMessage: {message_text}"

        # Send email
        msg = Message(subject, recipients=[app.config['MAIL_USERNAME']])
        msg.body = body
        mail.send(msg)

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
