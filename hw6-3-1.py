# Ryan Lugo: RJL 11/15/21

word_one = str(input("What is the first word?: "))
word_two  = str(input("What is the second word?: "))

sort_one = list(word_one)
sort_two = list(word_two)

sort_one.sort()
sort_two.sort()

if sort_one == sort_two:
    print(word_one,"and",word_two,"are anagrams.")
else:
   print(word_one,"and",word_two,"are not anagrams.")