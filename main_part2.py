# Natural language processing

from nltk.stem import WordNetLemmatizer
import nltk

lemmatizer = WordNetLemmatizer()


# lemmatize a word
x = "is"
y = "was"

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

lemma1 = lemmatizer.lemmatize(x, 'v')
lemma2 = lemmatizer.lemmatize(y, 'v')


print(x==y)
print(lemma1==lemma2)

# lemmatize a sentence

sentence = "vegetables are types of plants."
sentence1 = "a vegetable is a types of plant."

def lemma_me(sentence):
  sen_tokens = nltk.word_tokenize(sentence.lower())
  #print(sen_tokens)
  pos_tags = nltk.pos_tag(sen_tokens)
  #print(pos_tags)
  
  sen_lemma =[]
  
  for token,tag in zip(sen_tokens,pos_tags):
    if tag[1][0].lower() in ['n', 'v', 'a', 'r']:
      lemma1 = lemmatizer.lemmatize(token, tag[1][0].lower())
      sen_lemma.append(lemma1)

  return sen_lemma
  
print(lemma_me(sentence))
print(lemma_me(sentence1))
print(lemma_me(sentence)==lemma_me(sentence1))

# sentiment analysis
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('twitter_samples')
nltk.download("vader_lexicon")

analzer = SentimentIntensityAnalyzer()

text1 = "Hey, what a beauiful day! How amazing it is!"

print(analzer.polarity_scores(text=text1))
if analzer.polarity_scores(text=text1)['compound'] > 0:
  print("positive sentence")

tweet1 = nltk.corpus.twitter_samples.strings()[30]  # get sample from twitter
print(tweet1)
print(analzer.polarity_scores(text=tweet1))
if analzer.polarity_scores(text=tweet1)['compound'] > 0:
  print("positive sentence")

