# Fizz Buzz 
# Given a random number as an input to a function, return "FIZZ" if the number is even and "BUZZ" if the number is odd

def fizz_buzz(a):
    #Given an Intiger
    if a % 2 == 0:
        return 'FIZZ'
    else:
        return 'BUZZ'

print(fizz_buzz(21))