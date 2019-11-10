import csv

l = []
with open("C:\\Users\\mdevkate\\Desktop\\DeleteCompartment.CSV", "r") as f_obj:
    reader = csv.DictReader(f_obj, delimiter=',')
    for i in reader:
        print(i['compartment_name'])
        l.append(i['compartment_name'])

print (l)
