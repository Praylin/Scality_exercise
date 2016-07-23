#!/usr/bin/python
'''Program accepts a text file as an argumet and prints the number of words in file,
the number of occurances of each word in the file and finally the sorted list of words
based on the number of occurrances in each line '''

import sys
from collections import Counter, OrderedDict

f = open(sys.argv[1])
data  = (f.read())
print data #prints the file data
data_list = (data.split())
print(data_list) #prints the file data as a list of words
print len(data_list) #prints the number of words
counted_data = Counter(data_list)
print  counted_data #Print the words sorted based on the number of occurrances as a list
sorted_x = OrderedDict(sorted(counted_data.items(), key=lambda x: (-x[1], x[0]))) #sort the list in descending order based on the number of occurrances
for key, value in sorted_x.items(): #prints the list line by line
    print (key, value)
