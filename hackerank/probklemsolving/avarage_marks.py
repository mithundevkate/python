marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}

key = 'Malika'

for i , k in marks.items():
    print (i , sum(k)/len(k))
