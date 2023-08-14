from flask import Flask, render_template, request

from newsletter import generate_newsletter, parse_textarea_input


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        raw_link_text = request.form["links"]
        links = parse_textarea_input(textarea=raw_link_text)
        newsletter = generate_newsletter(links=links)
        return render_template("index.html", newsletter=newsletter)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)
