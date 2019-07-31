import json
tweetFile = open("./twitter.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id: ", tweetData[0]["id"])

print("Tweet text: ", tweetData[0]["text"])

for i in range(len(tweetData)):
    print("All texts: ", tweetData[i]["text"])
