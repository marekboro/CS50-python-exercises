# #1
# #url = input("give please your url :").strip()
# url = "https://twitter.com/someuserName"

# username = url.replace("https://twitter.com/","")
# print(f"username: {username}")

# #2

# userInput = " my username is https://twitter.com/someuserName ".strip()

# username = userInput.removeprefix("https://twitter.com/")
# print(f"username: {username}")

# #3
# import re
# userInput = " my username is https://www.twitter.com/someuserName ".strip()

# username = re.sub(r"^.+(https?://)?(www\.)?twitter\.com/","", userInput)

# print(f"Username: {username}")

#4
import re
userInput = " my username is https://www.twitter.com/someuserName "

if matches := re.search(r"^.+https?://(?:www\.)?twitter\.com/(\w)", userInput.strip(), re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
