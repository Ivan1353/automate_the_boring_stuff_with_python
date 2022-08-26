read_file = open(r".\text.txt", "r")
text = read_file.read()
text_list = text.split(' ')
read_file.close()

for word in text_list:
    if word[:9] == "ADJECTIVE":
        text_list[text_list.index(word)] = input(f"Enter an adjective: ")
    if word[:4] == "NOUN":
        text_list[text_list.index(word)] = input(f"Enter a noun: ")
    if word[:4] == "VERB":
        text_list[text_list.index(word)] = input(f"Enter a verb: ")
    if word[:6] == "ADVERB":
        text_list[text_list.index(word)] = input(f"Enter an adverb: ")


text = ' '.join(text_list)
print(text)
write_file = open(r".\text.txt", "w")
write_file.write(text)