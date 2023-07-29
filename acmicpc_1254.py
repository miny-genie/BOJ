txt = input()

if txt == txt[::-1]:
	print(len(txt))
	
else:
	min_len = 1e9
	
	for end in range(1, len(txt)):
		rev_txt = txt[:-end][::-1]
		
		isPalindrome = txt + rev_txt
		
		if isPalindrome == isPalindrome[::-1]:
			min_len = len(isPalindrome)
	
	print(min_len)