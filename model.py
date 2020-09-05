from gensim.parsing.preprocessing import remove_stopwords
from removewords import remove_extrawords

string = str(input("Enter your notes::::: "))
string = string.lower()
filtered_sentence = remove_stopwords(string)
filtered_sentence = remove_extrawords(filtered_sentence)
with open('ok2.txt','r') as fh:
     all_lines = fh.readlines()

word_list = list(filtered_sentence.split())
for i in word_list:
    for j in all_lines:
        if i in j:
            print(i,j)