from deep_translator import GoogleTranslator

def translate_hello_world_multiple():
    text = "Hello World!"
    print(f"Original: {text}")

    languages = {
        'Spanish': 'es',
        'French': 'fr',
        'German': 'de',
        'Italian': 'it',
        'Japanese': 'ja'
    }

    for language_name, language_code in languages.items():
        translation = GoogleTranslator(source='auto', target=language_code).translate(text)
        print(f"{language_name}: {translation}")

translate_hello_world_multiple()