# Email validator using python
# import re library
# write constraint of email as a variable

import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' # constraint of email

def  check(email):  #declare a function called check
    if(re.search(regex,email)):
        print("Valid email")
    else:
        print("Invalid email")

if __name__ == '__main__':
    email = input("Enter Email Address\n")
    check(email)
