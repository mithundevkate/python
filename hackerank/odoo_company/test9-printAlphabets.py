'''Write a function that, when called, returns an array for which each element is a letter of the alphabet, from "A" to "Z" (exactly once, in order and upper case). Your code cannot contain the character ' (quote), " (double quote) or ` (back quote)'''

def AlphaBets():
    import string
    print (list(string.ascii_uppercase))

AlphaBets()
