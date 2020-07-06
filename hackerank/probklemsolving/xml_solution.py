string2 = 'mithun'
position = 3
character = 'l'
string1 =list(string2)
print(string1)
string1[position] = character
print("".join(string1))

string = 'ThIsisCoNfUsInG'
sub_string = 'is'
print(string.find(sub_string))

x = string.find(sub_string)

if x == -1 :
    x = 0
    print(x)
else:
    print(x)

import re
d = len(re.findall(r'(?=%s)'% sub_string, string))
print(d)
#print (str(d[0]))
string = 'ABCDCDC'
sub_string = 'CDC'
print(string.find(sub_string))
triplets = zip(*[string[i:] for i in range(len(sub_string))])
print(triplets.count(tuple(sub_string)))


'''count = ''
for i in string.split():
    count = 0
    if i.__contains__(sub_string)==True:
        #print(count)
        count = count +1
#print(count)'''

