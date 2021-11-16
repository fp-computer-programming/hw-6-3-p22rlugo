# Ryan Lugo: 11/15/21

list_prompt = str(input("List numbers: "))
split_list = list_prompt.split()

sorted_version = list(split_list)

print(int(sorted_version[0]) + int(sorted_version[1])  + int(sorted_version[2]) + int(sorted_version[3]) + int(sorted_version[4]))