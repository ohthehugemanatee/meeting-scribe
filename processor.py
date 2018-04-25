from gensim.summarization import summarize, keywords
import requests

def summary(text):
    return "Summary: \n" +   summarize(text)

def keyword(text):
     return "Keywords: \n" +   keywords(text)
