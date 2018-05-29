word = "coc"

def palindrome(x):
    y = x
    while True:
        x = x[::-1]
        if x == y:
            return 0
            #print 0
        else:
            return -1
            
print palindrome(word)