def duplicate(string):

    duplicateString = ""

    for x in string:

        if x not in duplicateString:

            duplicateString += x

    return duplicateString



string = input("Enter the string: ")

print("String after removing the duplicates is:", duplicate(string))

