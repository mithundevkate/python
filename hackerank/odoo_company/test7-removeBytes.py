'''You have a huge file named "data.bin" that does not fit in memory; code a program that deletes every 7th byte of it. truncate can be used to change its size.
'''


with open("C:\\data.bin") as f:
    filedata = f.read()
f.close()

with open("C:\\data.bin" ,'w') as f:
    del filedata[7::7]
    f.write(filedata)
f.close()
