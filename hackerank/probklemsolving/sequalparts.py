import textwrap
string = 'jdskljdlsjdla'
max_width = 4
l = textwrap.wrap(string, max_width)
print(type(l))
for i in range(len(l)-1):
        print(l[i])
