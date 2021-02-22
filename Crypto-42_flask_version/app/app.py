from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/contact-us', methods=["GET", "POST"])
def contact_us():
    return "Thank you for getting in touch! We'll get back to you soon in 5 working days!"

if __name__ == '__main__':
    app.run()