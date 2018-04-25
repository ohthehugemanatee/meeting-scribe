from yapsy.IPlugin import IPlugin
from gensim.summarization import keywords

class keyword(IPlugin):
    def process(self, text):
        keywordResult = keywords(text)
        keywordResult = keywordResult.decode("utf-8").replace('\n', ', ')
        return {
                'keywords': keywordResult
                }
