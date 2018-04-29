from yapsy.IPlugin import IPlugin
import re
import nltk
from nltk.corpus import stopwords

class multistep_keyphrase(IPlugin):
    def process(self, text):
        text = self.cleanText(text)
        topicPhrases[topic] = self.getKeyPhrases(text)

        return {
                'topicPhrases': topicPhrases
                }

    # Clean up punctuation etc.
    def cleanText(self, text):
        stop = stopwords.words('english')
        document = ‘ ‘.join([i for i in document.split() if i not in stop])
        sentences = nltk.sent_tokenize(document)V

        text = re.sub('[^A-Za-z .-]+', ' ', text)
        text = ' '.join(text.split())
        text = ' '.join([i for i in text.split() if i not in stop])
        return text

    # Break the transcript into an array of topic groupings.
    def breakIntoTopics(self, text):
        return {
                'topic1': 'some text here',
                'topic2': 'another topic here',
                'topic3': 'yet another topic here'
                }

    # Return keyphrases for a given chunk of text.
    def getKeyPhrases(self, text):
        # Get most frequently used nouns.
        words = nltk.tokenize.word_tokenize(text)
        words = [word.lower() for word in words if word not in stop]
        fdist = nltk.FreqDist(words)
        most_freq_nouns = [w for w, c in fdist.most_common(10)
                                   if nltk.pos_tag([w])[0][1] in NOUNS]
        # Extract entities.

        return [
               'A keyphrase describes the core of what was discussed',
               'another keyphrase elaborates on the core of what was discussed'
               ]
