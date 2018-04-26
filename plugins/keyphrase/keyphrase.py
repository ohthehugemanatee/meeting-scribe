from yapsy.IPlugin import IPlugin
import requests
import math

class keyphrase(IPlugin):
    def process(self, text):
        response = self.make_request(self.build_body(text))
        return {
            'keyphrases': ['missing cognitive services subscription key in keyphrase.py'] # self.unique_key_phrases(response['documents'])
        }
    
    def make_request(self, body):
        headers   = {"Ocp-Apim-Subscription-Key": ""}
        response  = requests.post('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases', headers=headers, json=body)
        return response.json()
        
    def build_body(self, text):
        docs_count = self.documents_count(text)
        documents = {}
        documents['documents'] = []
        start_position = 0
        end_position = 5120

        for x in range(0, docs_count):
            documents['documents'].append(self.build_document(x, text, start_position, end_position))
            start_position = end_position
            end_position = end_position + 5120
        return documents
    
    def build_document(self, index, text, start_position, end_position): 
        document = { 'id': index, 'language': 'en', 'text': text[start_position:end_position] } # TDOO: set constant 5120 as class property
        # TODO: modify so that text end with a period
        return document

    def documents_count(self, text):
        # document limit is 5120 character and limited to 1000 documents, so 
        # cognitive services key phrases endpoint is only able to proces a 
        # 5,120,000 chracter document
        document_character_limit = 5120
        char_count = len(text)
        return math.ceil(char_count/document_character_limit)

    def unique_key_phrases(self, key_phrase_collection):
        unique_key_phrases = []
        for x in key_phrase_collection:
            unique_key_phrases.extend(x['keyPhrases'])
        list(set(unique_key_phrases))
        return unique_key_phrases

