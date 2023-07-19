from flask import Flask, request, jsonify
from deep_translator import MyMemoryTranslator

app = Flask(__name__)
translator = MyMemoryTranslator(source='en-US', target='fr-CA')

def english_to_french(text):
    return translator.translate(text)

def french_to_english(text):
    translator.source = 'fr-CA'
    translator.target = 'en-US'
    return translator.translate(text)

@app.route("/englishToFrench", methods=['POST'])
def englishToFrench():
    data = request.json
    textToTranslate = data.get('textToTranslate', '')
    translated_text = english_to_french(textToTranslate)
    return jsonify({"translatedText": translated_text})

@app.route("/frenchToEnglish", methods=['POST'])
def frenchToEnglish():
    data = request.json
    textToTranslate = data.get('textToTranslate', '')
    translated_text = french_to_english(textToTranslate)
    return jsonify({"translatedText": translated_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
