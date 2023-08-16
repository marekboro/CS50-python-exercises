#1
# def main():
#     yell("this is CS50!")
    
# def yell(phrase):
#     print(phrase.upper())
    
# if __name__ == "__main__":
#     main()


#2
# def main():
#     yell("this is CS50!", "you kicked my dog", "no you shadap")
    
# def yell(*words):
#     uppercased = list()
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)
    
# if __name__ == "__main__":
#     main()
    
#3
# def main():
#     yell("this is CS50!", "you kicked my dog", "no you shadap")
    
# def yell(*words):
#     uppercased = map(str.upper,words)
#     print(*uppercased)
    
# if __name__ == "__main__":
#     main()
    
#4
def main():
    yell("this is CS50!", "you kicked my dog", "no you shadap")
    
def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    
if __name__ == "__main__":
    main()