import snscrape.modules.twitter as sntwitter

query = "from:elonmusk"
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    print(f"{tweet.date} - @{tweet.user.username}: {tweet.content}")
    if i >= 4:
        break

