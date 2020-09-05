from gensim.parsing.preprocessing import remove_stopwords


string = str(input("Enter your notes::::: "))
filtered_sentence = remove_stopwords(string)
with open('ok.txt','r') as fh:
     all_lines = fh.readlines()
print(all_lines)
word_list = list(filtered_sentence.split())
for i in word_list:
    for j in all_lines:
        if i in j:
            print(i,j)