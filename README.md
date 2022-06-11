# Twitter stalking tool
### Powered by Python
#### _I swear I'm not creepy_

A simple tool written in Python that is powered by [woluxwolu's fork of twint](https://github.com/woluxwolu/twint),
chosen instead of the [official repository](https://github.com/twintproject/twint) due to installation issues.

## Features

- Exports all results to an 'index.html' file in the same directory that includes clickable links
- May further narrow down results with parameters like time posted and geolocation

## Installation

**Create Python virtual environment**
```bash
python -m venv ./venv
```

**Install dependencies and libary**
```bash
git clone --depth=1 https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
```

## Further configuration

- Done by modifying the declared "c" variable before the search is ran

## Important: Limiting results
In order for the results to export to the HTML file, they must be complete. Searching without extremely specific
parameters is unwise due to this reason, and Twitter may begin rate limiting after several thousand requests. The
built-in "c.Limit" attribute isn't completely reliable, as it may accidentally gather several more than the amount
requested. It will only be by tens of results though. In order to fully narrow the array, you must include an integer
in the place of "[:limitInt]" after "tweets" has been declared. For example, if you would like at most 30 results, you
must include both of these lines in your code:

```python
c.Limit = 30
```

```python
tweets = twint.output.tweets_list[:30]
```

**Example: gathers 10 Tweets from a 3km radius of downtown Los Angeles that contain the word "fun," prints each message to console**
```python
import twint

c = twint.Config()
c.Search = 'fun'
c.Geo = '34.052235,-118.243683,3km'
c.Limit = 10
c.Hide_output = True
c.Store_object = True
twint.run.Search(c)
tweets = twint.output.tweets_list[:10]

if tweets:
    for tweet in tweets:
        # Prints just the message in results arary
        print(tweet.tweet)
```

**Another example: gathers 15 Tweets from a 10km radius of downtown Chicago that contain the word "excited," exports to HTML**
```python
import twint
import pandas as pd
from datetime import datetime
today = datetime.now().strftime('%Y-%m-%d')

c = twint.Config()
c.Search = 'excited'
c.Geo = '41.881832,-87.623177,10km'
c.Since = today
c.Limit = 15
c.Hide_output = True
c.Store_object = True
twint.run.Search(c)
tweets = twint.output.tweets_list[:15]

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
```

## License

MIT