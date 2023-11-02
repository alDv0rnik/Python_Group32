text = input("Enter your string: ")
spacesCount = text.count(" ")
nonSpacesCount = len(text) - spacesCount
print("Count of spaces is", spacesCount)
print("Count of other symbols is", nonSpacesCount)