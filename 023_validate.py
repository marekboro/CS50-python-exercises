#1:
# email = input("Give me email: ")
# if "@" in email:
#     print("This looks valid")
# else:
#     print("Wrong!")

#2:
# email = input("Give me email: ")
# if "@" in email and "." in email:
#     print("This looks valid")
# else:
#     print("Wrong!")

#3:
# email = input("Give me email: ").strip()
# username, domain = email.split("@")

# # if username and "." in domain:
# if username and domain.endswith(".com"):
#     print("Good good")
# else:
#     print("bad")

## 4:
# import re

# email = input("Do you have email for me? ").strip()
# # if re.search("@", email):
# #5 if re.search(r"^.+@.+\.com$", email):
# #6 if re.search(r"^[^@]+@[^@]+\.com$", email):
# #7 if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
# #8 if re.search(r"^\w+@\w+\.com$", email):
# if re.search(r"^\w+@\w+\.(com|org|net|gov|edu)$", email):
#     print("That's good")
# else:
#     print("you are a no good user!")

# #9:
# import re

# # email = input("Do you have email for me? ").strip().lower()
# email = input("Do you have email for me? ").strip().lower()
# # if re.search(r"^\w+@\w+\.(com|org|net|gov|edu)$", email.lower()):
# # if re.search(r"^\w+@\w+\.(com|org|net|gov|edu)$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)?\w+\.(com|org|net|gov|edu)$", email, re.IGNORECASE):
#     print("That's good")
# else:
#     print("you are a no good user!")

#10:
import re

# email = input("Do you have email for me? ").strip().lower()
email = input("Do you have email for me? ").strip().lower()
# if re.search(r"^\w+@\w+\.(com|org|net|gov|edu)$", email.lower()):
# if re.search(r"^\w+@\w+\.(com|org|net|gov|edu)$", email, re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?\w+\.(com|org|net|gov|edu)$", email, re.IGNORECASE):
    print("That's good")
else:
    print("you are a no good user!")


