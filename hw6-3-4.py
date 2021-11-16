# Ryan Lugo: 11/15/21

list_prompt = str(input("List numbers/letters: "))
question_prompt = str(input("Do you want middle or ends? M / E : "))

split_list = list_prompt.split()

sorted_version = list(split_list)

end = len(sorted_version)-1
start = sorted_version[:1]
middle = sorted_version[1:end]

if question_prompt.lower() == "m":
    print("Here is the middle of the list",middle)
else:
    print("Here is the start:",start,"\nHere is the end:",sorted_version[end:])
