listIterationWithIndex = ['Test1','Goose','Bison','Pelican']

#iterate over list with index
for i, withIndex in enumerate(listIterationWithIndex):
    print ("element -- ", i , withIndex)

'''
output
element --  0 Test1
element --  1 Goose
element --  2 Bison
element --  3 Pelican
'''

tuple_ =  ('Cat','Dog','Elephant','Bird','Tiger','Lion', \
           'Rabbit')

#iterate over tuple with index
for i, withIndex in enumerate(tuple_):
    print ("element -- ", i , withIndex)

'''
output
element --  0 Cat
element --  1 Dog
element --  2 Elephant
element --  3 Bird
element --  4 Tiger
element --  5 Lion
element --  6 Rabbit
'''

dictionaryAnimalSpeed = {'tiger': 65, 'monkey': 25 ,'bison': 35, 'cheetah': 113 }

#iterate over dictionary with index
for i, withIndex in enumerate(dictionaryAnimalSpeed.keys()):
    print ("element -- ", i , withIndex)

'''
output
element --  0 bison
element --  1 cheetah
element --  2 monkey
element --  3 tiger
'''   