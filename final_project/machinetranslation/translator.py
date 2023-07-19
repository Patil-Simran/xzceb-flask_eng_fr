from deep_translator import MyMemoryTranslator

translator = MyMemoryTranslator(source='en-US', target='fr-CA')

def english_to_french(text):
    return translator.translate(text)

def french_to_english(text):
    translator.source = 'fr-CA'
    translator.target = 'en-US'
    return translator.translate(text)
