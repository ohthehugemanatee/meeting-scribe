from yapsy.IPlugin import IPlugin

class multistep_keyphrase(IPlugin):
    def process(self, text):
        textByTopic = self.breakIntoTopics(text)
        topicPhrases = {}
        for topic, topicText in textByTopic.items():
            topicPhrases[topic] = self.getKeyPhrases(topicText)

        return {
                'topicPhrases': topicPhrases
                }

    # Break the transcript into an array of topic groupings.
    def breakIntoTopics(self, text):
        return {
                'topic1': 'some text here',
                'topic2': 'another topic here',
                'topic3': 'yet another topic here'
                }

    # Return keyphrases for a given chunk of text.
    def getKeyPhrases(self, text):
       return [
               'A keyphrase describes the core of what was discussed',
               'another keyphrase elaborates on the core of what was discussed'
               ]
