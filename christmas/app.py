from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = ""
    message = ""
    sender = ""

    if request.method == "POST":
        name = request.form.get("username", "")
        sender = request.form.get("sender", "")
        message = request.form.get("message", "")

    return render_template(
        "index.html",
        name=name,
        sender=sender,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
