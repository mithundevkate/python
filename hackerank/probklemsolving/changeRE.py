n = int(input())
count = 0
l = []
for i in range(n):
    if count != 0 and count != -1:
        if ("&&".startswith(' ') and "&&".endswith(' ') and "||".startswith(' ') and "||".endswith(' ')):
            l.append(input().replace(" && ", " and ").replace(" || "," or "))
    else:
        l.append(input())
    count = count+1
print("\n".join(l))
