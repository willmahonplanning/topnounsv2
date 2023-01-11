import spacy
import en_core_web_sm
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def noun_detector():
    if request.method == "POST":
        input_string = request.form["input_string"]
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(input_string)
        modified_string = " ".join("top " + token.text if token.pos_ == "NOUN" else token.text for token in doc)
        return render_template("nounchangev2.html", modified_string=modified_string)
    return render_template("nounchangev2.html")

if __name__ == "__main__":
    app.run(debug=True)
