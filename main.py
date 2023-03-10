
def input_text(text):
	
	word = text.split(" ")
	array = []
	for i in range(len(word)):
		array.append(len(word[i]))
	max_number = max(array)
	for i in range(len(word)):
		if len(word[i]) == max_number:
			print(word[i]," || [ total length of the word is : ",len(word[i]),"]")
	print("\n\n")

def from_file(name):
	
	with open(name) as f:
		file_read = f.read()
	word = file_read.split(" ")
	array = []
	for i in range(len(word)):
		array.append(len(word[i]))
	max_number = max(array)
	for i in range(len(word)):
		if len(word[i]) == max_number:
			print(word[i]," || [ total length of the word is : ",len(word[i]),"]")
	print("\n\n")		
def main():
	
	print("1 : check biggest word from input\n2 : check biggest word from file\n3 : exit")
	check = int(input("> "))
	
	if check == 1:
		input_text(input(" enter your text here :  "))
		main()
	elif check == 2:
		from_file(input("enter your file name [file.txt] or file path \n "))
		main()
	elif check == 3:
		exit()
	else:
		main()
main()


()