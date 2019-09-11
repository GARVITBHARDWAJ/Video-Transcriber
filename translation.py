# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()
translate_client = translate_client.from_service_account_json("C:/Users/steve/Downloads/samkey.json")
def translate(input ,target):
    translation = translate_client.translate(
        input,
        target_language=target)
    return translation['translatedText']



