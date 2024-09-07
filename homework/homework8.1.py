string='find the letter z'

for i in range(len(string)):
	if(string[i]=='z'):
		print(i)
		break
else:
	print("command not found")		
