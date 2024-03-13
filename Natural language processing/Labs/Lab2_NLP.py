
import nltk
from nltk.corpus import wordnet
import re
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer


sentence = """He was a Dutch Post-Impressionist painter who is among 
    the most famous and influential figures in the history of Western art.
    In just over a decade he created about 2,100 artworks, 
    including around 860 oil paintings, most of them in the last two years of his life.
    They include landscapes, still lifes, portraits and self-portraits,
    and are characterised by bold colours and dramatic, impulsive and expressive brushwork
    that contributed to the foundations of modern art.
    His suicide at 37 followed years of mental illness and poverty."""

### Task1: Tokenize Text

#(1)	Word tokenizing using regex

words = re.split('[-_,.\s]', sentence)
print(words)

#(2)	Word tokenizing using NLTK

tokens = nltk.word_tokenize(sentence)
print(tokens)

#(3)	Sentence tokenizing using NLTK

sentences = nltk.sent_tokenize(sentence)
print(sentences)

#----------------------------------------------------

### Task2: Stemming

#This statement prints defined NLTK built-in stemmers
print([x for x in dir(nltk) if 'stemmer' in x.lower()])

porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()
snowball_stemmer = SnowballStemmer("english")

#the least aggressive
stem = porter_stemmer.stem("maximum")
print(stem)
stem = snowball_stemmer.stem("painter")
print(stem)
stem = porter_stemmer.stem("owed")
print(stem)

#moderate
stem = snowball_stemmer.stem("maximum")
print(stem)
stem = snowball_stemmer.stem("painter")
print(stem)
stem = lancaster_stemmer.stem("owed")
print(stem)

#the most aggressive
stem = lancaster_stemmer.stem("maximum")
print(stem)
stem = snowball_stemmer.stem("painter")
print(stem)
stem = lancaster_stemmer.stem("owed")
print(stem)
#comparative example:
#A list of words to be stemmed
word_list = ["friend", "friendship", "friends", "friendships","stabil","destabilize","misunderstanding","railroad","moonlight","football"]
print("{0:20}{1:20}{2:20}{3:20}".format("Word","Porter Stemmer","Snowball Stemmer","lancaster Stemmer"))
for word in word_list:
    print("{0:20}{1:20}{2:20}{3:20}".format(word,porter_stemmer.stem(word),snowball_stemmer.stem(word),lancaster_stemmer.stem(word)))

#----------------------------------------------------

### Task3: Lemmatizing
wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize("owed"))
print(wordnet_lemmatizer.lemmatize("owed",pos="v"))#pos = parts-of-speech
print(wordnet_lemmatizer.lemmatize("is"))
print(wordnet_lemmatizer.lemmatize("is", pos="v"))

#----------------------------------------------------

### Task4: Part-Of-Speech (POS) Tagging
tags = nltk.pos_tag(tokens)
print (nltk.pos_tag(tokens))

#----------------------------------------------------

### Task5: Using Wordnet
syns = wordnet.synsets("motorcar")
print("Synset name:\n",				syns[0].name())         	# get name or its code in wordnet
print("synset definition:\n",		syns[0].definition())   	# get the definition of word like dictionary
print("synset example:\n",			syns[0].examples())
print("synset hypernyms:\n",		syns[0].hypernyms())     	# is a   Generalize like person -> chef
print("synset hyponyms:\n",			syns[0].hyponyms())      	# is a   Specific    like chef -> person
print("synset member_holonyms:\n",	syns[0].member_holonyms())#is a member of
print("synset part_meronyms:\n",	syns[0].part_meronyms())  #is a contains  or the  parts

# Synsets to dog
print(wordnet.synset('car.n.01').lemma_names())

#Wu-Palmer Similarity

octopus = wordnet.synsets("octopus")[1]
nautilus = wordnet.synsets("paper_nautilus")[0]
shrimp = wordnet.synsets("shrimp")[2]
pearl = wordnet.synsets("pearl")[0]
print("sim of octopus,nautilus= ",octopus.path_similarity(nautilus))   #check the semantic similarity
print("sim of octopus,shrimp= " ,octopus.path_similarity(shrimp))

#----------------------------------------------------

## This Code take string as input
## Check this string is type of cat or dog
def getWord(n):
    k=((wordnet.synsets(n)))
    print (k)
    for h in k:
        hypernymsToG(h.name())
def hypernymsToG(n):
    if n == "entity.n.01":
        return
    if n != "dog.n.01":
        if n != "cat.n.01":
            print(n)
            print((wordnet.synset(n)))
            word = (wordnet.synset(n)).hypernyms()
            for dogs in word:
                print(dogs)
                return hypernymsToG(dogs.name())
        else:
            print("cat")
    else:
        print("dog")
getWord("husky")
getWord("shepherd_dog")
getWord("great_dane")
getWord("boxer")
