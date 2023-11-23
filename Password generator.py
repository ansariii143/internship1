import random

import string

lowercase=string.ascii_lowercase
# print(lowercase)
uppercase=string.ascii_uppercase
digits=string.digits
specialCharecters="!@#$%^&*()"


length=int(input('Enter the length of the password'))

all= lowercase + uppercase + digits + specialCharecters

# print("all")

password=''.join(random.sample(all,length))

print(password)





