def remove_useless_words(query):
    stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he']
    querywords = query.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)

    return result