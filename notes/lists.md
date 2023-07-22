A list is like an array

eg: 
exampleList: list[str] = ["one","two","three","four"]
to slice a list we can use the 

exampleList[1:] will return ["two","three","four"] , give this list from index 1 to end

exampleList[1:-1] will return ["two","three"] , give this list from index 1 to -1 where -1 is the last entry index
exampleList[2:-2] will return [] 