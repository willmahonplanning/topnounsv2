from flask import Flask, render_template, request
from textblob import TextBlob
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(text.split())
nltk.download('punkt')

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def noun_detector():
    if request.method == "POST":
        input_string = request.form["input_string"]
        blob = TextBlob(input_string)
        modified_string = " ".join("top " + word if word.pos_ == "NN" else word for word in blob.words)
        return render_template("nounchangev2.html", modified_string=modified_string)
    return render_template("nounchangev2.html")

if __name__ == "__main__":
    app.run(debug=True)
