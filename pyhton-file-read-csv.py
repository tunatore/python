#Created on Jul 25, 2013

#@author: tuna

file = open('C:\\Users\\tunato\\Desktop\\pythontest.csv', 'r')

#printing file name
print (file.name)

#reading files in an array
#lines = file.readlines()
#print (lines)

#displaying file content line by line
for line in file:
    print (line.rstrip())
file.close()

print ('\n')

#writing to a file
try:
    fh = open('C:\\Users\\tunato\\Desktop\\pythontext.txt', 'w') #opening in write mode
    fh.write('Writing log content inside')
except IOError:
    print ('Error: I/O Error')
else:
    print ('Content is written')

print ('\n')

import csv
#reading file using csv module
with open('C:\\Users\\tunato\\Desktop\\pythontest.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        print (line)