'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

from wordcloud import WordCloud

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

# Get the JSON data
tweetFile = open("twitter.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
#
# Textblob sample:

polvalues= []
subjvalues =[]
TotalTweets = []


for i in range(len(tweetData)):
    tb = TextBlob(tweetData[i]["text"])
    polvalues.append(tb.polarity)
    subjvalues.append(tb.subjectivity)
    print(tb.polarity) #[-1, 1]
    print(tb.subjectivity) #[0, 1]





plt.hist(polvalues, bins = 15)


plt.xlabel('Tweets')
plt.ylabel('Polarity')
plt.title('Polarity')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([1, len(polvalues) -1, 1])
# plt.grid(True)
plt.show()

plt.hist(subjvalues, bins = 15)

plt.xlabel('Tweets')
plt.ylabel('Subjectivity')
plt.title('Subjectivity')


tweets = ""
for tb in TotalTweets:
    tweets = "" += str(tb)

print(tweets)
tweetblob =textblob [tweets]
wordList = textBlob.words

print(wordList)


# textBlob.word_counts = {}
keys = ["and", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "the", "an", "who", "a", "how"]
filteredDict {}
for eachword in wordlist:
