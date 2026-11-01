

import re


email = input("Enter email address: ")

if re.match(r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$', email):
    print("Valid Email")
else:
    print("Invalid Email")


phone = input("Enter phone number: ")

if re.match(r'^[6-9][0-9]{9}$', phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

log = input("Enter log message: ")

ids = re.findall(r'TXN\d+', log)

print("Transaction IDs:", ids)