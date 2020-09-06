def remove_extrawords(query):
    with open('ok.txt','r') as fh:
        all_lines = fh.read()
    stopwords = list(all_lines.split(' '))
    querywords = query.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)

    return result