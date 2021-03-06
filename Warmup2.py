def string_times(str, n):
    if n >= 0:
        return str * n


print(string_times("ah", 3)) 

def front_times(str, n):
    if len(str) < 3:
        return n * str
    else:
        return str[0:3] * n

print(front_times("Ahmed", 2)) 
print(front_times("Shoulah", 3))
print(front_times("ah", 3))     


def string_bits(str):
    if len(str) == 1:
        return str
    else:
        result = ""
        i = 0
        while i < len(str):
            if i % 2 == 0:
                result += str[i]
            i += 1
        return result

print(string_bits("Shoulah"))            

 
def string_splosion(str):
    if len(str) > 0:
        result = ""
        i = 1
        while i <= len(str):
            result += str[0:i]
            i += 1
        return result

print(string_splosion("Code"))     
   

""" 
Given a string, return the count of the number of times that a substring length 2 appears in 
the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2 """


def last2(str):
    counter = 0 #initialize the counter 
    if len(str) > 2:
        subString = str[len(str) - 2 : len(str)]
        
        i = 0
        while i < len(str) - 2:
            if str[i:i + 2] == subString:
                counter +=1
            i +=1
    return counter

print(last2("axxxaaxx"))        
 

"""  Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3 """
 
def array_count9(nums):
    counter = 0
    for n in nums:
        if n == 9:
            counter += 1

    return counter

print(array_count9([1, 9,9]))
print(array_count9([1]))

 

"""  Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False """
 
def array_front9(nums):
    is4Exists = False
    if len(nums) < 4:
        for i in range(len(nums)):
            if nums[i]  == 9:
                is4Exists = True
                break
    else:
        for i in range(4):
            if nums[i] == 9:
                is4Exists = True
                break
    return is4Exists

print(array_front9([1, 2, 9]))            
 

 
""" Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True """
 
def array123(nums):
    is123Exists = False
    if len(nums) >= 3:
        i = 0
        while i < len(nums) - 2:
            if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
                is123Exists = True
                break
            i +=1
    return is123Exists


print(array123([1, 1, 2, 1, 2, 3]))

 

""" Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
 So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0 """

def string_match(a, b):
    counter = 0
    smallerLength = 0
    if len(a) <= len(b):
        smallerLength = len(a)
    else:
        smallerLength = len(b)

    i = 0
    while i < smallerLength - 1:
        if a[i:i+2] == b[i:i+2]:
            counter += 1
        i += 1
    return counter

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc')) 
print(string_match('abc', 'axcdddddddddddddddddd'))                   