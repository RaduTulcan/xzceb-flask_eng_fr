from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(textToTranslate)['translations'][0]['translation']

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(textToTranslate)['translations'][0]['translation']

@app.route("/")
def renderIndexPage():
    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
