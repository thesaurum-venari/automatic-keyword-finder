from textblob import TextBlob


def find_keywords(text):
    """
    This method calculates a list of noun phrases as potential keywords (tags) for a text
    :param text: The text to analyze
    :return: A list of potential keywords
    """
    blob_text = TextBlob(text)
    phrases_list = list(set(blob_text.noun_phrases))
    return phrases_list