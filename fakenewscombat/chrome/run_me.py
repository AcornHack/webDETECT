"""
welcome to James Dixon's code!

purpose:
        opens up a webpage and tests sentiemnt of text!

code to be used for demonstasion purposes for acorn hack
can also be eddited for the purposes for acorn hack

any questions , ask me on slack (user : A3457)
"""

import sentiment
import website_scrape

def sentimentOfArticle(url):
    return (sentiment.VADER_sentiment_score.sentiment_analyzer_scores(website_scrape.DataScrape().findArticle(website_scrape.DataScrape().runJavaScriptGetPage(url))))

def resultAnalyse(result):
    stats= []
    if float(result["neg"]) > 0.25:
        stats.append("slightly negative")
    if float(result["neg"]) > 0.5:
        stats.append("moderatly negative")
    if float(result["neg"]) > 0.75:
        stats.append("quite negative")
    if float(result["neg"]) > 0.95:
        stats.append("very negative")

    if float(result["pos"]) > 0.25:
        stats.append("slightly positive")
    if float(result["pos"]) > 0.5:
        stats.append("moderatly positive")
    if float(result["pos"]) > 0.75:
        stats.append("quite positive")
    if float(result["pos"]) > 0.95:
        stats.append("very positive")

    if float(result["compound"]) > 0.25:
        stats.append(" overall slightly positive")
    if float(result["compound"]) > 0.5:
        stats.append(" overall moderatly positive")
    if float(result["compound"]) > 0.75:
        stats.append(" overall quite positive")
    if float(result["compound"]) > 0.95:
        stats.append(" overall very positive")

    if float(result["compound"]) < 0.1 and float(result["compound"]) > -0.1 :
        stats.append(" overall neautral")

    return stats

def __main__():
    link = str(input("enter the news article link here:"))
    result = sentimentOfArticle(link)
    print(result)
    print(resultAnalyse(result))


__main__()
