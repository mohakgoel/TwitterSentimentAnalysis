from textblob import TextBlob
import pandas as pd
import re
import matplotlib.pyplot as plt


def tweetClean(txt):
    txt = re.sub(r'@[A-Za-z0-9_]+', ' ', txt)
    txt = re.sub(r'#', ' ', txt)
    txt = re.sub(r'RT ', ' ', txt)
    txt = re.sub(r'https?://[A-Za-z0-9./]+', ' ', txt)
    return txt

def getTextSubjectivity(txt):
    return TextBlob(txt).sentiment.subjectivity


def getTextPolarity(txt):
    return TextBlob(txt).sentiment.polarity


def getTextSentiment(a):
    if a < 0:
        return "Negative"
    elif a == 0:
        return "Neutral"
    else:
        return "Positive"

def getTextContext(a):
    if a < 0.5:
        return "Factual"
    elif a == 0.5:
        return "Fact based Opinion"
    else:
        return "Opinion"


df = pd.read_csv('tweets.csv')
df = df.drop(df[df['content'] == ''].index)
df['content'] = df['content'].apply(tweetClean)
df['Subjectivity'] = df['content'].apply(getTextSubjectivity)
df['Polarity'] = df['content'].apply(getTextPolarity)
df['Sentiment'] = df['Polarity'].apply(getTextSentiment)
df['Context'] = df['Subjectivity'].apply(getTextContext)
df.to_csv('analyzed_tweets.csv', index=False)

positive = df[df['Sentiment'] == "Positive"]
print(str(positive.shape[0]/(df.shape[0])*100)+"% of positive tweets")
pos = positive.shape[0]/df.shape[0]*100
negative = df[df['Sentiment'] == "Negative"]
print(str(negative.shape[0]/(df.shape[0])*100)+"% of negative tweets")
neg = negative.shape[0]/df.shape[0]*100
neutral = df[df['Sentiment'] == "Neutral"]
print(str(neutral.shape[0]/(df.shape[0])*100)+"% of neutral tweets")
ntr = neutral.shape[0]/df.shape[0]*100

explode = (0, 0.1, 0)
labels = 'Positive','Negative','Neutral'
sizes = [pos, neg, ntr]
colors = ['lightgreen','lightcoral','gold']
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', startangle=120)
plt.legend(labels, loc=(-0.10, 0.00), shadow=True)
plt.savefig("Sentiment_Analysis_PieChart.png")
plt.show()
plt.clf()

labels = df.groupby('Sentiment').count().index.values
values = df.groupby('Sentiment').size().values
plt.bar(labels,values)
plt.savefig("Sentiment_Analysis_BarGraph.png")
plt.show()
plt.clf()

factual = df[df['Context'] == "Factual"]
print(str(factual.shape[0]/(df.shape[0])*100)+"% of factual tweets")
fact = factual.shape[0]/df.shape[0]*100
opinion = df[df['Context'] == "Opinion"]
print(str(opinion.shape[0]/(df.shape[0])*100)+"% of opinion tweets")
opn = opinion.shape[0]/df.shape[0]*100
factBasedOpinion = df[df['Context'] == "Fact based Opinion"]
print(str(factBasedOpinion.shape[0]/(df.shape[0])*100)+"% of fact based opinion tweets")
fbo = factBasedOpinion.shape[0]/df.shape[0]*100

explode = (0, 0.1, 0)
labels = 'Factual','Opinion','Fact based Opinion'
sizes = [fact, opn, fbo]
colors = ['lightblue','lightcoral','gold']
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', startangle=120)
plt.legend(labels, loc=(-0.30, -0.10), shadow=True)
plt.savefig("Context_Analysis_PieChart.png")
plt.show()
plt.clf()

labels = df.groupby('Context').count().index.values
values = df.groupby('Context').size().values
plt.bar(labels,values)
plt.savefig("Context_Analysis_BarGraph.png")
plt.show()
plt.clf()