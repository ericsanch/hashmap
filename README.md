# hashmap
This project implements a hash map data structure which is used to store a sequence of words received as input. The hash map is used as part of a concordance program written to count the frequency at which each word of an input file occurs. When executing the concordance program, the user may select the top # number of words in the file. Included with this repository is a text file containing Lewis Carroll's 'Alice in Wonderland' for demonstrating the functionality of the program.

To use this program, edit line 392 of word_count.py to refer to the desired text file and the number of top words to be returned. In default state, the program will return the number of empty buckets in the hash map and the 5 most frequently used words in the included copy of Alice in Wonderland. The results should be as follows
[('the', 1644), ('and', 872), ('to', 729), ('a', 632), ('she', 541)]

This program was written for the final project of CS 261 at Oregon State University. The solution of this program and program prompt are subject to all applicable Oregon State University academic policies. The solution of this program is provided for informative purposes only and should not be reproduced for submission in any academic setting.
