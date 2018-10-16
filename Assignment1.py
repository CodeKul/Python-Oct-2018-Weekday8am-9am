def removeAllExceptStrings(list):
    i = len(list) - 1
    while i >= 0:
        if not isinstance(list[i], str):
            list.remove(list[i])
        i -= 1


list = [1,2,3,'Codekul', 'The Gurukul for Coders!', 23.90, 34, 'Python - Codekul', 65]
removeAllExceptStrings(list)
print(list)