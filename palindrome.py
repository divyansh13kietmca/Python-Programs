
def is_palindrome(word):
	rev = [word[words] for words in range(len(word))]
	rev.reverse()
	res = 0
	for i in range(len(word)):
		for j in range(i,len(rev)):
			if i == j and word[i].lower() != rev[j].lower():
				res = 1
	if res == 0:
		return True
	else:
		return False
#Provide different values for word and test your program
result=is_palindrome("Madam")
if(result):
	print("The given word is a Palindrome")
else:
	print("The given word is not a Palindrome")
