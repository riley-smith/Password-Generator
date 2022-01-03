import os
import random
import sys
import time
import string

alphabet = list(string.ascii_lowercase)
upper_alphabet = list(string.ascii_uppercase)
numbers = list(string.digits)
spec_characters = list(string.punctuation)

def sleep():
    time.sleep(1.5)
    print("Please try again")


def random_integer():
    x = random.randint(0, 25)
    y = random.randint(0, 8)
    z = random.randint(0, 9)
    return([x,y,z])


def random_list():
    q = random.randint(1, 2)
    e = random.randint(1, 4)  #### for strong password
    return([q,e])



def weak_pass(n):
    global alphabet
    password = []
    i = 0
    while i < n:
        x = random_integer()[0]
        password.append(alphabet[x])
        i += 1
    p = ("".join(password))
    return p



def med_pass(n):
    global alphabet
    global numbers
    password = []
    i = 0
    while i < n:
        [x,y,z] = random_integer()
        [q,e] = random_list()
        if q == 1:
            password.append(alphabet[x])
            i += 1
        else:
            password.append(numbers[y])
            i += 1
    p = ("".join(password))
    return p


def strong_pass(n):
    global alphabet
    global numbers
    global spec_characters
    password = []
    global upper_alphabet

    i = 0
    while i < n:
        [x,y,z] = random_integer()
        [q,e] = random_list()
        if e == 1:
            password.append(alphabet[x])
            i += 1
        elif e == 2:
            password.append(numbers[y])
            i += 1
        elif e == 3: 
            password.append(upper_alphabet[x])
        else:
            password.append((spec_characters[z]))
            i += 1    
    p = ("".join(password))
    return p



def password_level():
    print("Password Generator")
    print("Weak, Medium, Strong")
    print("Type 1 for weak, 2 for medium, 3 for strong")

    count = 0
    while count < 1:
        try:
            choice = int(input())
            if choice not in [1,2,3]:
                print("Input must be 1, 2, or 3")
                sleep()         #### Small delay so the user has time to reflect on their mistake ####
            else : 
                count += 1
                print("How many characters do you want your password to be? (Enter an integer, maximum 50)")
        except ValueError:
            print("Input must be an integer")
            sleep()

    c_count = 0
    while c_count < 1:
        try:
            n = int(input())
            if n > 50:
                print("Character limit exceeded")
                sleep()
            elif n not in range(1,50):
                print("Input must be an integer from 1 to 50")
                sleep()
            else : 
                c_count += 1
        except ValueError:
            print("Input must be an integer")
            sleep()
                

 

    if choice == 1:
        p = weak_pass(n)
    elif choice == 2:
        p = med_pass(n)
    elif choice == 3:
        p = strong_pass(n)
    return p


text_file = "Passwords.txt"
save_path = ""               #### Path where you want the text file to be stored ####
completeName = os.path.join(save_path, text_file)

def pass_save(pass_final):
    print("What is this password for?")
    source = input("")
    create = open(completeName, "a+")
    create.write(f"\n {source} \n {pass_final} \n")
    create.close()



random_integer()
p = password_level()
print("Your password is: " + p)
time.sleep(1.5)
pass_save(p)


print("Password saved!")

