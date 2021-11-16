# Ryan Lugo: 11/15/21

list_prompt = str(input("List numbers: "))
split_list = list_prompt.split()

sorted_version = list(split_list)
sorted_version.sort()
print(sorted_version)

if list(split_list) == sorted_version:
    print(list_prompt,"is a sorted list!")
else:
    print(list_prompt,"is not a sorted list!")