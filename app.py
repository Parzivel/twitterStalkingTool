import twint
import pandas as pd
from datetime import datetime
today = datetime.now().strftime('%Y-%m-%d')

# Prompts user for input
print("Enter username:")
username = input()
print("Enter search query:")
query = input()

# Configure
c = twint.Config()
# Checks for username before declaring to avoid errors
if username:
    c.Username = username
c.Search = query
c.Limit = 50
c.Hide_output = True
c.Store_object = True
twint.run.Search(c)
tweets = twint.output.tweets_list[:50]

print("Found", len(tweets), "tweets.")

messages = []
links = []

if tweets:
    for tweet in tweets:
        # Separates message content and links between two arrays
        messages.append(tweet.tweet)
        # Encloses each Twitter link in the HTML a tag
        links.append('<a target="_blank" href="{0}">{0}</a>'.format(tweet.link))

titled = {
    'message': messages,
    'link': links
    }

df = pd.DataFrame(titled)
df.columns.name = 'index'
html = df.to_html('index.html', escape=False)