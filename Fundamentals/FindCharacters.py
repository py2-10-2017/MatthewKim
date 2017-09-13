# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list=[]
for i in word_list:
    if i.find(char)>=0:
        new_list.append(i)
print new_list
