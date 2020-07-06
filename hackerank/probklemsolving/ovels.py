vowels = "aeiouy"
str = "vuv tpikawrurtmtcrs ajhgby tbnvycfnc bdczzgqygrpvoploooab"

count = 0
L = []

for i in set(str.split()):
    L.append(len([i for i in list(i) if i in list(vowels)]))

print(L)
l1= []
for i in L:
    if i % 2 == 0:
        l1.append(2)
    else:
        l1.append(1)

print(sum(l1))
