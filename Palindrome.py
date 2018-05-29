a = "mom"
b = "Son"
c = "Dad"

def palindrome(x):     # Defining a procedure called "palindrome"
    y = x              # Defining a variable which will refer to value (string) passed in palindrome(x)
    while True:        # Initialising "While" Loop
        x = x[::-1]    # string[::-1] reverses the String
        if x == y:     # As y refers to value of x (y = x ,as stated), "If" statement intialises and checks if x (after x[::-1] is equal to y
            return 0   # if reverse of x is equals to y (i.e., Palindrome) then return 0    
        else:
            return -1  # Else it will return -1
            
print palindrome(a)    # a = "mom" and Palindrome of "mom" is "mom", Result will be 0
print palindrome(b)    # b = "Son" and Palindrome od "Son" is "noS", Result will be -1
print palindrome(c)    # c = "Dad" and Palindrome of "Dad" is "daD", Result will be -1 [Note: Python is CASE sensitive]

# GAURAV PADAWE
