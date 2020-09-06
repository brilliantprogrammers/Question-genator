from gensim.parsing.preprocessing import remove_stopwords
from removewords import remove_extrawords
from questionlist import unique_question

string = str(input("Enter your notes::::: "))
string = string.lower()
filtered_sentence = remove_stopwords(string)
filtered_sentence = remove_extrawords(filtered_sentence)
question_list = []
with open('ok2.txt','r') as fh:
     all_lines = fh.readlines()

word_list = list(filtered_sentence.split())
for i in word_list:
    for j in all_lines:
        if i in j:
            question_list.append(j)

final_question = unique_question(question_list)
for i in final_question:
    print(i)