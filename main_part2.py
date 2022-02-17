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



