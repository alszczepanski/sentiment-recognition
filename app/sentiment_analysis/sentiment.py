from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:

    analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text: str):
        sentiment_dict = self.analyzer.polarity_scores(text)

        if sentiment_dict['compound'] >= 0.05:
            overall_sentiment = "Positive"
        elif sentiment_dict['compound'] <= - 0.05:
            overall_sentiment = "Negative"
        else:
            overall_sentiment = "Neutral"

        return overall_sentiment


analyzer = SentimentAnalyzer()
