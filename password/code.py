
from random import *
import itertools


guess = ""
password = input("Password: ")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


while (guess != password):
    guess = ""
    perm = ""
    for letter in password:
        guessletter = letters[randint(0, 25)]
        guess = str(guessletter) + str(guess)

        perm = itertools.permutations(guess)
        
    for p in perm:                    
        guess = "".join(p)
        print(" ",guess,end="\r")
            
            
print(f"Password guessed! ==> {guess}")
input("")
