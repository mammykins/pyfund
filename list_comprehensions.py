from math import factorial

words = "Why sometimes I have believed as many as six impossible things \
before breakfast".split()

print("words = ", words)

print("This command, [len(word) for word in words] outputs:",\
 [len(word) for word in words])

print("The comprehension is enclosed in square brackets just like a literal list",
"but instead of literal elements it contains a fragment of declarative code,",
"which describes how to construct the elements fo the list. Here the new list is formed by binding word to each value in words in turn",
"and evaluating len (word) to create a new value.")


f = [len(str(factorial(x))) for x in range(20)]

print("The following, f = [len(str(factorial(x))) for x in range(20)], gets: ", f)
