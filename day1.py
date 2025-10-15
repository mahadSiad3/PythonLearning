# # Introduction
# # Day 1 - 30DaysOfPython Challenge

# print(3 + 2)   # addition(+)
# print(3 - 2)   # subtraction(-)
# print(3 * 2)   # multiplication(*)
# print(3 / 2)   # division(/)
# print(3 ** 2)  # exponential(**)
# print(3 % 2)   # modulus(%)
# print(3 // 2)  # Floor division operator(//)

# # Checking data types



# print(type(10))                  # Int

        # an int is a whole number w/o any floating points, it can be positive,neg, or zero.
        #when an integer is created ex: x=5, the computer allocates some memory in ram to store that number, then puts it into binary for ex:101010
        # then its associated with a variable name x in a symbol table or object reference. 
        # in C or java : an int is a primitve type and is stored directly in memory as raw bits. an int uses 4 bytes which ==32 bit(1byte = 8 bits).

        # in python ints are objects and store not only the numeric value but its metadata(type info, reference count,ect.), so in x=5 the 5 is a full object in memory which take up more memory depending on the size.

        # 




# print(type(3.14))                # Float

# print(type(1 + 3j))              # Complex







# print(type('Asabeneh'))          # String

        #strings are a sequence of characters and can be anything like a letter, number or whitespace. Once strings are created they cannot be changed as they are immutable
        # unlike ints strings are more complex and need to store not only the object header but its reference count, type, length and the actual data. They can take anywhere fom 1-4 bytes per character
        # ex: s="hello" -> s = s + "world" == "hello world", since strings are immutable 'S' wasn't changed but a new string object was created and if not referenced again the old string will get garbage collected.
            # this concatination will take up more memory






# print(type([1, 2, 3]))           # List

            # a list is an ORDERED Collection of items of any types (strings, integers, objects, other lists) and lists are mutable meaning they can be changed, you can add, remove, or change the items in a list.
            # lists work for referencing the same as arrays. ex: myList = [1,"hello",3.14,[1,17,43]] , if you print(myList[2]) == 3.14 , print(myList[3][2]) == 43
            # unlike sets which use hash table, list are dynamic arrays. python pre-allocates a contiguos block of memory for the list. 
                                #In memory terms:
                                # All the elements are stored right next to each other in RAM
                                # There are no gaps between them
                                # The CPU can calculate the address of any element using simple math
            # each slot in the array stores a pointer to the python object as python stores the data types as objects, and the objects themselves live elsewhere in memory. each pointer is 8 bytes on a 64bit system.
            # it runs on O(n) which means its when a list is created and you are searching through it if you wanted to find x in mylist.
            # ex: mylist=[10,20,30,40] and you wanted to find x=40 it would go and check 10,20,30,then 40 and print 40.
                    # this is called a linear search is is O(n)



# print(type({'name':'Asabeneh'})) # Dictionary
        # like objects in javascript dictionaries are key value pairs so name is the key which is unique(like elements in a set) and the value is the string 'Asabeneh' 
        # they are stored also in hash tables which are created the same way as sets but now they store both the key and its value. so when searching through the hash table example
                    # person = {'name':'john', 'age':24}
                    #print(person[name]) == john | this is because the hash is going to the table finding the location of the key and retrieving its value. giving it a runtime on O(1).
                                # usage example key value pairs
                                        # person = {'name': 'Asabeneh', 'age': 25}
                                        # Access
                                        #   print(person['age']) == 25

                                        # Add new key-value
                                        #   person['country'] = 'Finland'

                                        # Check if key exists
                                        #   print('name' in person)  == True

                                        # Iterate
                                        #   for key, value in person.items():
                                        #      print(key, value)



# print(type({9.8, 3.14, 2.7}))    # Set

    # {...} is creating a set and not a list or diictionary , sets do not keep order unlike a list which does
    # , and can print in any order they want. internally sets use hashing
            #firstly sets are mutable and can be added to remove() or changed.
            #hashing is the process of converting a piece of data into a unique has value ex: 'hello world' would == 1234565
            # python builds a hash table in memory to store the information in a set. like a fast index card system so it doesn't have to check every element in the deck
            # just calculates the hash ('hello world') then goes to its memory location(runs in O(1) worset case is O(n): 
            # downside: uses more memory as it stores both the value its object "hello"(object) : 123(value)
            # also creates a larger than necessary array to fit to avoid collisions. 
'''
                  Best/Worst/Next Fit = how the OS allocates memory to processes.
                  Hashing = how a program organizes data within the memory it already owns
                  hashes are created by for ex: x=30 , h = hash(x). now x is some long number that is now its hash value, then to find its location the 
                  number of index is taken and modulo(%) is used to determine its location.
                                    Example: hash(30) = 2305843009213693951
                                    Suppose number_of_buckets = 8 → bucket_index = 2305843009213693951 % 8 = 7
                                    Python looks directly in bucket 7
'''

                                    #   Hash values (simplified) | Value   
                                    # | 129832            | "hello" |
                                    # | 12                | 12      |
                                    # | 5                 | 5       |
                                    # | 982739            | "world" |




# print(type((9.8, 3.14, 2.7)))    # Tuple
        # works exactly like a list but is immutable and cannot be changed in size or elements once created and is slightly more efficeint in memory as Python doesn’t need to allocate extra memory for potential growth, unlike lists.
        # if you wanted to add something to for example tuple T = (1,"hello",3) you would have to make another variable T2 = T + (4,): have to include the comma for it to be a value in the tuple and not just a number
        # to remove you have to again make a new variable and remove from the original by either filtering ex: T3 = (x for x in T if T != 3), T3 now equals (1,"hello")
                # or by slicing new_tuple = t[start:stop:step] ex: 

'''   
                        t = (1, "hello", 3) 
                        new_tuple = t[start:stop:step]
                        # Take everything before index 1, then everything after index 1
                        t2 = t[:1] + t[2:]
                        print(t2)  # (1, 3)
                        t[:1] → (1,) → elements before index 1
                        t[2:] → (3,) → elements from index 2 onward
                        Concatenate → (1, 3)
                        Notice we cannot do t2 = t[:- [2]] — that syntax isn’t valid in Python. 
'''
 

 
# print(type(3 == 3))              # Bool
        #a boolean is true or false: yes,or no: yes= 1 no= 2. they can control flow of the code and logic.
        #print(True +True+False+True) = print(1+1+0+1) = 3
        #All comparisons return a Boolean: x = 5 y = 10
        # print(x > y)   # False.   print(a and b)  # False
        # print(x < y)   # True.    print(a or b)   # True
        # print(x == 5)  # True.    print(not a)    # False
        # print(x != 5)  # False
        #a boolean is a singleton object and is only either true or false in memory. This leads to very little memory usage.
# print(type(3 >= 3))              # Bool

print(3+5)
print(10 // 5)
print('hello world')
print("hello world")
print({"hello", 5, 'world',12})
print({4,'its',"blue",44,9.8})
print({'red', "green", 14, 33})

print(1 + 3j) 
myList = [1,"hello",3.14,[1,2,3]] 
print(myList[2])

print(True +True+False+True)