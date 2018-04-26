from yapsy.IPlugin import IPlugin
from gensim.summarization import keywords

class keyword(IPlugin):
    def process(self, text):
        keywordResult = keywords(text)
        keywordResult = keywordResult.replace('\n', ', ')
        return {
                'keywords': keywordResult
                }
