'''Write a program to download the contents of http://www.sap.com/belgique/index.html (the SAP homepage for Belgium), and then save the contents of the page to a new local file, with all occurrences of "SAP" replaced by "Odoo".'''
import requests

filedata = requests.get('http://www.sap.com/belgique/index.html')

with open("C:\Personal\my_file.text" ,'w') as f:

    for line in filedata:
        if 'SAP' in str(line):
            print(str(line).replace('SAP','Odoo'))
            f.write('%s \n' % (str(line).replace('SAP','Odoo')))
        else:
            f.write('%s \n' % (str(line).replace('SAP','Odoo')))


f.close()
