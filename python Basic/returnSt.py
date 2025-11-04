#  wap to count vouwel in given string
'''
def count_char(string):
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count = count + 1
    return count

print(count_char('hello helllo hello Aa'))
'''

# WAP
def reverce_string(string):
    st = ""
    for char in string:
        st = char + st
    return st

print(reverce_string("hello"))
