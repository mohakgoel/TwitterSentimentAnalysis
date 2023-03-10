# TwitterSentimentAnalysis
Python based Twitter Sentiment Analysis project that is used to analyze sentiment of tweets and also analyzes the context of tweets as an add on feature
Sentiment Analysis:
Sentiment Analysis is the process of determining whether the text is positve, negative or neutral.
It is mainly used in e-commerce industries to understand whether a customeris happy about their product or not satisfied by their product.

The Project uses the Python Library TextBlob which is commonly used to process the text and also anayze sentiments

Textblob API can be used to retrieve Polarity and Subjectivity:
1. Polarity refers to emotions expressed in text (Sad, Happy, Angry) Polarity number ranges from -1 to +1, -1 indicates negative statement 0 indicates neutral statement and 1 indicates a positive statement
2. Subjetivity is expressing one's own feelings, beliefs or opinion also ranges from -1 to +1

The Project uses Regular Expression Library to clean tweets of any links, hashtags, mentions, retweets
The Project uses Pandas Library to read csv file in Data Frame and to store back the data in new csv file
The Project uses Matplotlib to plot data in form of Pie Chart and Bar Graph such that we can analyze the aggregate of tweets for sentiment and context

The sentiment is given by positive, neutral and negative
The context is given by opinion, fact based opinion and factual
