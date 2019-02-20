positive = ["ok","good"]
negative=["bad",'ugly']
positive_p = ["well"]
negative_n = ["not"]

text = input("Type: ")

if any(word in text.split() for word in positive and positive_p):
    print("POSITIVE+P")
elif any(word in text.split() for word in positive):
    if any(word in text.split() for word in positive and negative_n):
        print("NEGATIVE+N")
    else:
        print("POSITIVE")
elif any(word in text.split() for word in negative ):
    print("NEGATIVE")

else:
    print("Nuetral")
