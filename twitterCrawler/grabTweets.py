#!/usr/bin/python3
import tweepy
import helpers
import os

# Set file path to wherever you are storing
# your twitter application's tokens
twitterTokens = "/home/connor/Documents/Etc/twitterCrawler.txt"

# Grab access tokens
with open(twitterTokens) as file:
    data = file.read().splitlines()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(data[0], data[1])
auth.set_access_token(data[2], data[3])
api = tweepy.API(auth, wait_on_rate_limit=True)

# Verifies credentials
try:
    api.verify_credentials()
    print("LET'S GATHER SOME TWEETS")
except:
    print("Invalid Creditials")
    exit(0)

# Grab keyword
subject = input("What the search about? (One word please)\n")

# Grab list of buzzwords to look up
searchFile = input("What's the path to your list of words?\n")
if os.path.exists(searchFile) and os.path.isfile(searchFile):
    with open(searchFile, "r") as file:
        search = file.read().splitlines()
else:
    print("Sorry can't seem to find that file\n")
    exit(0)

# Grabs tweets from time frame
timeFrame = input("How many days do you want to search back? (0 if just today)\n")

# Start search
crawlerData = {}
for word in search:
    print("Gathering data for tweets for the word: {}".format(word))
    
    # Count total of tweets in range
    count = 0
    total = 0
    check = True
    while check == True:
        print("Checking...")
        check = False
        try:
            for tweet in tweepy.Cursor(api.search, q=word, lang="en").items(1000000):
                total += 1
                if helpers.checkDate(tweet.created_at, int(timeFrame)) == True:
                    if(tweet.text.find(word) >= 0):
                        check = True
                        count += 1
                else:
                    check = False
                    break

        except tweepy.TweepError as err:
            print(err)

    # Store stats
    crawlerData[word] = (count, total)
    print("{} was referenced {} within your time frame of {}\n".format(word, count, timeFrame))

# Check to save data & exit
save = input("Do you want to save this data to a file? Y|N\n")
if save == 'Y' or save == 'y':
    with open("tData/"+subject+".tData", "w") as file:
        for data in crawlerData:
            file.write("{} || {}\n".format(data, crawlerData[data]))
print("Program Shutting Down...")
