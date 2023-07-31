# #1
# name = input("What name you have?").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"

# print(f"Welcome back {name}")

# #2
# import re
# name = input("What name you have?").strip()

# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last,first = matches.groups()
#     name = f"{first} {last}"
# print(f"Welcome back {name}")

# #3
# import re
# name = input("What name you have?").strip()

# matches = re.search(r"^(.+), ?(.+)$", name)
# if matches:
#     name = f"{matches.group(2)} {matches.group(1)}"
# print(f"Welcome back {name}")

#4
import re
name = input("What name you have?").strip()

if matches := re.search(r"^(.+), ?(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"
print(f"Welcome back {name}")