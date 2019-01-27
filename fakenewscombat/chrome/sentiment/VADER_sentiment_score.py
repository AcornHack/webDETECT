from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()



def sentiment_analyzer_scores(sentence):
    """
    pass in a sentance to get the sentiment scores out
    :param sentence: the sting to analyse
    :return: a dictionary (ask a mentor) that contains the score of negative or positive words
    """
    score = analyser.polarity_scores(sentence)
    return score





# for example , if you wanted to find all scores for a string:

#print(sentiment_analyzer_scores("i can tbeleive you did that you idiot you ABSALUTE idiot! i hate you"))


#                                                                                                          I
# to find only negative score for a string                                                     change it here   V

#print(sentiment_analyzer_scores("i can tbeleive you did that you idiot you ABSALUTE idiot!! i hate you")["neg"])