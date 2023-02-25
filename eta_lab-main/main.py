from src.phonebook import Phonebook

phoneBook = Phonebook()

#Add
phoneBook.add("Will", "81987788778")
print(phoneBook.entries)

#lookup
phoneBook.lookup("Will")

#Get Names
print(phoneBook.get_names())

#Get Numbers
print(phoneBook.get_numbers())

#Search
print(phoneBook.search("Will"))

#get_phonebook_sorted
print(phoneBook.get_phonebook_sorted())

#get_phonebook_reverse
print(phoneBook.get_phonebook_reverse())

#Delete
print(phoneBook.delete("Will"))