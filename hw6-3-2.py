# Ryan Lugo: 11/15/21

list_prompt = str(input("List numbers: "))

sorted_version = list(list_prompt)
sorted_version.sort()
print(sorted_version.index(" "))

if list_prompt == sorted_version:
    print(list_prompt,"is a sorted list!")
else:
    print(list_prompt,"is not a sorted list!")