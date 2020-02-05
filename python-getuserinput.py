'''
Created on Aug 1, 2013
Python version > 3
@author: tunatore
'''
import time

# before python 3 please use raw_input() function instead
# refer to http://www.python.org/dev/peps/pep-3111/

# starting clock
startTime = time.clock()

stars = input('I will print stars tell me any number :')

# printing stars
for j in range(int(stars) + 1):
    print('*' * (j))

word = input('Tell me a word :')

# printing word
for j in range(int(len(word) + 1)):
    print(word[j - 1] * (j))

# stopping clock
stopTime = time.clock()

print("You have been using this program for {0} seconds".format(stopTime - startTime))
