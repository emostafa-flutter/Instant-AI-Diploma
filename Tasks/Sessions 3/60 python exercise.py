#!/usr/bin/env python
# coding: utf-8

# **1-Write a Python program to calculate the length of a string using 2 ways

# In[5]:


name = "eesa hamdy"
len(name)


# In[10]:


def Getlength(str):
    count = 0;
    for i in str:
        count +=1
    return count
name = "eesa hamdy"
print(Getlength(name))


# **2-Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead ("##Sample String : 'w3resource'
# Expected Result : 'w3ce'
# ##Sample String : 'w3'
# Expected Result : 'w3w3'
# ##Sample String : ' w'
# Expected Result : Empty String)

# In[ ]:


name = input("Enter String")
def getString(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]
print(getString(name))


# **3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. (Sample String : 'abc'
# Expected Result : 'abcing')

# In[36]:


name = input('Enter Name ')
def add_ing(str):
    if len(str)<2:
        return str
    if str[-3:] == 'ing':
        str += 'ly'
    else:
        str += "ing"
    return str
print(adding(name))


# **4-Write a Python function that takes a list of words and return the longest word and the length of the longest one
# (Longest word: Exercises
# Length of the longest word: 9)

# In[35]:


countList = int(input("Enter Count of List"))
words = []
for i in range(countList):
    word = input (f"Enter Word {i+1}: ")
    words.append(word)
def get_longest(words):
    longest_word = ""
    length = 0

    for word in words:
        if len(word) > length:
            longest_word = word
            length = len(word)

    return longest_word, length
longest_word, length = get_longest(words)
print(f"longest word : {longest_word} , Length : {length}")


# 

# In[ ]:





# In[ ]:





# **6-Write a Python program to remove characters that have odd index values in a given string (Sample String:abca Expected Result:ac)

# In[37]:


name = input("Enter Name")
def remove_odd(str):
    result = ""
    for i in range(len(str)):
        if i% 2 ==0:
            result += str[i]
    return result
print(remove_odd(name))


# **7-Write a Python program to count the occurrences of each word in a given sentence (Sample String:amr and ahmed are frindes but amr is the tallest Expected Result:2)

# In[2]:


sentence = input("Enter Sentence : ")
def count_words(str):
    words = str.split()
    count = {}
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count
print(count_words(sentence))


# **8-Write a Python script that takes input from the user and displays that input back in upper and lower cases

# In[3]:


name = input("Enter Name :")
print("Upper: ", name.upper())
print("Lower: ", name.lower())


# **9-Write a Python function to reverse a string if its length is a multiple of 4

# In[4]:


name = input('Enter Name')
def reverse_string(str):
    if len(str)%4==0:
        return ''.join(reversed(str))
    return str
print(reverse_string(name))


# **10- Write a Python program to remove a newline in Python

# In[21]:


def remove_newline(str):
    return str.replace("\n", "")
name = input('Enter Name: ')
s =remove_newline(name)
print(s)
print(remove_newline(name))
print(name.replace("\n",""))
print(name.rstrip())


# **11-Write a Python program to check whether a string starts with specified characters

# In[25]:


name = input('Enter Name : ')
prefix = input('Enter specified character ')
def starts_with(str, prefix):
    return str.startswith(prefix)
if starts_with(name, prefix):
    print(f"The string '{name}' starts with '{prefix}'.")
else:
    print(f"The string '{name}' does not start with '{prefix}'.")


# **12- Write a Python program to add prefix text to all of the lines in a string

# In[6]:


import textwrap
text = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries,
but also the leap into electronic typesetting, remaining essentially unchanged
    '''
text2 = textwrap.dedent(text)

txt = textwrap.fill(text2, width=70)
res = textwrap.indent(txt, '* ')
print(res)


# **13-Write a Python program to print the following numbers up to 2 decimal places

# In[12]:


print("{:.2f}".format(12.559995))


# **14-Write a Python program to print the following numbers up to 2 decimal places with a sign

# In[14]:


print("{:+.2f}".format(12.2132))
print("{:+.2f}".format(-12.231))


# **15-Write a Python program to display a number with a comma separator

# In[17]:


number = 1234567890
number = f"{number:,}"
print(number)


# **16-Write a Python program to reverse a string using 2 ways

# In[27]:


print("eesa"[::-1])
name = "eesa"
print("".join(reversed("eesa")))


#  **17-Write a Python program to count repeated characters in a string (hint:use dictionary)

# In[44]:


name = "eesa hamdy abdeltawab"
count_charachters = {ch: name.count(ch) for ch in name}
print("count:", count_charachters)


# **18-Write a Python program to find the first non-repeating character in a given string

# In[60]:


def get_non_repeating(str1):
    non_repeats_chars = []
    chs = {}
    for c in str1:
        if c in chs:
            chs[c] += 1
        else:
            chs[c] = 1
            non_repeats_chars.append(c)
    for c in non_repeats_chars:
        if chs[c] == 1:
            return c
    return None
name = "adasda"
print(get_non_repeating(name))


# **19-Write a Python program to remove spaces from a given string

# In[61]:


print("fsa fdsa fdas".replace(" ",""))


# **20-Write a Python program to count the number of non-empty substrings of a given string

# In[69]:


print( (len("eesa") * (len("eesa") + 1) // 2))


# **21-write a Python program to swap first and last element of any list.

# In[73]:


def swap(list1):
    if len(list1) > 1:
        list1[0], list1[-1] = list1[-1], list1[0]
    return list1
any_list = ["e", "h", "s", "w", "a"]
print(swap(any_list))


# **22-Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. (Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90])

# In[75]:


def swap(list1, pos1, pos2):
    pos1, pos2 = pos1 - 1, pos2 - 1
    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    return list1
print(swap([1,2,3,4,5],1,2))


# **23- search for the all ways to know the length of the list

# In[ ]:


**24-write a Python code to find the Maximum number of list of numbers.


# In[77]:


def max_Num(lst):
    return max(lst)
print("Maximum :", max_Num([1,2,3,4,5]))


# In[ ]:


**25-write a Python code to find the Minimum number of list of numbers.


# In[79]:


def min_Num(lst):
    return min(lst)
print("Minimum :", min_Num([1,2,3,4,5]))


# **26-search for if an elem is existing in list

# In[81]:


def elem_exiting(list1, elem):
    return elem in list1
print(elem_exiting([1,2,3,4,5],3))
print(elem_exiting([1,2,3,4,5],6))


# **27- clear python list using different ways

# In[ ]:


list = [1,2,3,4]
list.clearl()
list = []
del list[:]


# **28-remove duplicated elements from a list

# In[84]:


print(list(set([1,2,2,3,4,4,5])))


# **29-Given list values and keys list, convert these values to key value pairs in form of list of dictionaries. (Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
# Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}])

# In[90]:


print([dict(zip(["name", "id"], ["Gfg", 3, "is", 8][i:i + len(["name", "id"])])) for i in range(0, len(["Gfg", 3, "is", 8]), len(["name", "id"]))])


# **30-write a python program to count unique values inside a list using different ways

# In[97]:


print("count unique values inside a list : ", len(set([1, 2, 2, 5, 8, 7, 4, 4, 8])))
from collections import Counter
print("Count unique values inside a list:", len(Counter([1, 2, 2, 5, 8, 7, 4, 4, 8])))


# **31-write a python program Extract all elements with Frequency greater than K (Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
# Output : [4, 3] )

# In[31]:


test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
Output = [key for key, count in Counter(test_list).items() if count > K]
print(Output)


# **32-write a python program to find the Strongest Neighbour (Input: 1 2 2 3 4 5
# Output: 2 2 3 4 5)

# In[99]:


def strongest_neighbour(nums):
    return [max(nums[i], nums[i+1]) for i in range(len(nums) - 1)]
print("Strongest Neighbours : ", strongest_neighbour([2, 5, 5, 4, 3, 1]))


# **33-write a Python Program to print all Possible Combinations from the three Digits (Input: [1, 2, 3]
# Output:
# 1 2 3 ##
# 1 3 2 ##
# 2 1 3 ##
# 2 3 1 ##
# 3 1 2 ##
# 3 2 1)

# In[105]:


from itertools import permutations
perms = permutations([1, 2, 3])
for perm in perms:
    print(' '.join(map(str, perm)), end='\n')


# **34-write a Python program to find all the Combinations in the list with the given condition (Input: test_list = [1,2,3] 
# Output: 
#  [1], [1, 2], [1, 2, 3], [1, 3]
#  [2], [2, 3], [3])

# In[106]:


from itertools import combinations
print([list(c) for i in range(1, len([1, 2, 3]) + 1) for c in combinations([1, 2, 3], i)])


# **35-write a Python program to get all unique combinations of two Lists (List_1 = ["a","b"]
# List_2 = [1,2]
# Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] )

# In[107]:


from itertools import combinations
print([list(zip(["a", "b"], perm)) for perm in permutations([1, 2])])


# **36-Remove all the occurrences of an element from a list in Python (Input : 1 1 2 3 4 5 1 2 1 
# 
# **Output : 2 3 4 5 2)

# In[113]:


print(' '.join(map(str, [element for element in [1, 1, 2, 3, 4, 5, 1, 2, 1] if element != 2])))


# **37-write a python program to Replace index elements with elements in Other List (The original list 1 is : [‘Gfg’, ‘is’, ‘best’] The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0] The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’])

# In[117]:


print("The lists after index elements replacements is:", [(['Gfg', 'is', 'best'][i]) for i in [2, 2, 1, 0, 1, 2, 1, 0, 2, 2, 1, 0]])


# **38- write python program to Retain records with N occurrences of K(Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 2 
# Output : [(4, 5, 5, 4)]
# Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3 
# Output : [] )

# In[48]:


print("Output:", [tup for tup in [(4, 5, 5, 4), (5, 4, 3)] if tup.count(5) == 2])
print("Output:", [tup for tup in [(4, 5, 5, 4), (5, 4, 3)] if tup.count(5) == 3])


# **39-write a Python Program to Sort the list according to the column using lambda
# array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Output :
# Sorted array specific to column 0, [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Sorted array specific to column 1, [[2, 1, 2], [3, 2, 1], [1, 3, 3]]
# Sorted array specific to column 2, [[3, 2, 1], [2, 1, 2], [1, 3, 3]]

# In[47]:


array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
print(sorted(array, key=lambda x: x[0]))
print(sorted(array, key=lambda x: x[1]))
print(sorted(array, key=lambda x: x[2]))


# In[ ]:


**40- write a program to Sort Python Dictionaries by Key or Value
Input:
{'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

Output: 
{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}


# In[42]:


dict1 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
print({key: dict1[key] for key in sorted(dict1)})
print({key: value for key, value in sorted(dict1.items(), key=lambda item: item[1])})


# **41-write python program to Remove keys with Values Greater than K ( Including mixed values )
# nput : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’},
# K = 7 
# Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’}

# In[49]:





# **42-Write a Python program to concatenate the following dictionaries to create a new one
# 
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# In[37]:


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print( result)


# **43-Write a Python program to iterate over dictionaries using for loops

# In[118]:


dic = {'Eesa': 0, 'Hamdy': 1, 'Abdeltawab': 2}
for name, value in dic.items():
    print(name, ' : ', dic[name]) 


# **44- Write a Python script to merge two Python dictionaries

# In[120]:


dic1 = {'Eesa': 0, 'Hamdy': 1, 'Abdeltawab': 2}
dic2 = {'Ahmed': 3, 'Khaled': 4, 'Sayed': 5}
print({**dic1, **dic2})


# **45-Write a Python program to get the maximum and minimum values of a dictionary values

# In[122]:


print(max({'Eesa': 0, 'Hamdy': 1, 'Abdeltawab': 2, 'Ahmed': 3, 'Khaled': 4, 'Sayed': 5}.values()))
print(min({'Eesa': 0, 'Hamdy': 1, 'Abdeltawab': 2, 'Ahmed': 3, 'Khaled': 4, 'Sayed': 5}.values()))


# **46- Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# In[124]:


print({key: value for key, value in {'Eesa': 0, 'Hamdy': 1, 'Abdeltawab': 2, 'Ahmed': 3, 'Khaled': 4, 'Sayed': None}.items() if value is not None})


# **47-Write a Python program to create a tuple of numbers and print one item

# In[1]:


tuble = (1,2,3,4,5)
print(tuble[0])


# **48-Write a Python program to unpack a tuple into several variables

# In[54]:


tuple = ("Eesa", "Hamdy")
firstName , LastName = tuple
print(firstName , LastName)


# **49-Write a Python program to add an item to a tuple

# In[3]:


print("add an item to a tuple:", (1, 2, 3)+(4,))


# **50-Write a Python program to convert a tuple to a string

# In[13]:


tuple1 = ('a','b','c')
str = ''.join(tuple1)
print("convert a tuple to a string:", str)


# **51-Write a Python program to convert a list to a tuple

# In[14]:


print(tuple([1,2,3,4,5]))


# **52-Write a Python program to reverse a tuple

# In[15]:


tuple1= (1,2,3,4,5)
print(tuple1[::-1])


# **53-Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# In[22]:


sample_list= [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(" ",[(t[:-1] + (100,)) for t in sample_list])


# **54-Write a Python program to convert a given string list to a tuple
# Original string: python 3.0
# <class 'str'>
# Convert the said string to a tuple:
# ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')

# In[23]:


str= "python 3.0"
print(tuple(str))


# **55-Write a Python program to calculate the average value of the numbers in a given tuple of tuples

# In[26]:


tuple1 = ((1, 2, 3), (4, 5, 6))
average = sum(num for tup in tuple1 for num in tup) / sum(len(tup) for tup in tuple1)
print(average)


# **56-Write a Python program to add member(s) to a set.

# In[33]:


set1 = {1, 2, 3}
set1.add(4)
print(set1)


# **57-Write a Python program to remove an item from a set if it is present in the set.

# In[34]:


set1 = {1, 2, 3}
set1.discard(2)
print(set1)


# **58-Write a Python program to create an intersection,union,difference and symmetric difference of sets

# In[35]:


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))


# **59-Write a Python program to find the maximum and minimum values in a set

# In[36]:


print(max({5, 10, 3, 15, 2, 20}))
print(min({5, 10, 3, 15, 2, 20}))


# **60- Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

# In[50]:


sum1 = 10
seen = set()
pairs = []
for element in [1, 2, 3, 4, 5, 6]:
    complement = sum1 - element
    if complement in seen:
      pairs.append((complement, element))
    seen.add(element)
print(pairs)


# In[ ]:




