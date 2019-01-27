import re
import sentiment.VADER_sentiment_score



class DataScrape:
    def runJavaScriptGetPage(self, url):
        """
        connects though a driver to chrome browser to request link and run all javascript in the browser. NOTE, CHROME DRIVER IN DIRECTORY. DO NOT DELEITE. ALLLOWS PYTHON TO COMUNICATE WITH CHROME
        :param url: url to be input into chrome
        :return: html string of webpoage containg all run javascript results
        """
        from selenium import webdriver
        browser = webdriver.Chrome()  # replace with .Firefox(), or with the browser of your choice
        browser.get(url)  # navigate to the page

        data = browser.execute_script("return document.body.innerHTML")  # returns the inner HTML as a string
        browser.close()
        browser.quit()
        return data

    def findArticle(self, html: str):
            """
            finds date and price of record of house in string
            :param html: string of data of all html of a website
            :return: generates price for a specific date, and yeilds this date and price
            """
            return ' '.join(s[0] for s in re.findall(r'<p[^>]*>((.*?))</p>', str(html)))




#print (sentiment.VADER_sentiment_score.sentiment_analyzer_scores(DataScrape().findArticle(DataScrape().runJavaScriptGetPage("https://www.wired.co.uk/article/facebook-whatsapp-merger"))))