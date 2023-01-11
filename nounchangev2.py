from flask import Flask, request, render_template
from pynlpi import NLPI

app = Flask(__name__)
nlpi = NLPI()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/noun_detector", methods=["POST"])
def noun_detector():
    input_text = request.form.get("input_text")
    if input_text:
        # tokenize the input text
        sentences = nlpi.sentence_tokenize(input_text)
        
        # perform part-of-speech tagging on the input text
        pos_tags = nlpi.pos_tag(sentences)
        
        # find all nouns in the input text
        nouns = []
        for sentence in pos_tags:
            for token, pos_tag in sentence:
                if pos_tag.startswith("NN"):
                    nouns.append(token)
        return " ".join(nouns)
    else:
        return "Please enter some text"
        
if __name__ == "__main__":
    app.run()
