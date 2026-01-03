
# * join : .join()
#               ? .join() is a string method that combines many strings into one single string.

#               ^ Eg: "separator".join(iterable_of_strings)

#               ! .join() works only on an iterable where every element is a string.

#               ? Nothing else is allowed.


#               ?  Think like this (very simple):
#               ?  
#               ?  You have many small strings:
#               ?  
#               ^  ["A", "B", "C"]
#               ?  
#               ?  
#               ?  You want:
#               ?  
#               ^  A-B-C
#               ?  
#               ?  
#               ?  You do:
#               ?  
#               ^  "-".join(["A", "B", "C"])




words = ["I", "love", "Python"]
sentence = " ".join(words)
print(sentence) # ^ I love Python


# ? Joining numbers (must convert to strings)

nums = [1, 2, 3]
result = ",".join(str(n) for n in nums)
print(result) # ^ 1,2,3

# ! Why .join() is used instead of +
words = ("234","234","234","2345","56")

s = " "
for word in words:
    s += word
print(s) # ^ 234234234234556

s = " ".join(words)
print(s) # ^ 234 234 234 2345 56

s = "-".join(words)
print(s) # ^ 234-234-234-2345-56



#    ! |  Iterable Type  |  Works?           |  Example                               |
#    ? |  -------------  |  ---------------  |  ------------------------------------- |
#    & |  list           |  Yes              |  `",".join(["a","b"])`                 |
#    & |  tuple          |  Yes              |  `",".join(("a","b"))`                 |
#    & |  set            |  Yes              |  `",".join({"a","b"})`                 |
#    & |  generator      |  Yes              |  `"".join(x for x in ["a","b"])`       |
#    & |  dict keys      |  Yes              |  `"".join({"a":1,"b":2})`              |
#    & |  dict values    |  Only if strings  |  `"".join({"a":"x","b":"y"}.values())` |


#    ! | Data              | Why                 |
#    ? | ----------------- | ------------------- |
#    & | Numbers           | Not strings         |
#    & | Lists inside list | Not strings         |
#    & | Objects           | Not strings         |
#    & | Mixed types       | Must be all strings |
#    & 