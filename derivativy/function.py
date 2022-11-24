class Function:
	def __init__(self, fnstring) -> None:
		self.signs = ["*", "/", "+", "-", "^"]
		self.derivatives = []
		self.parts = self.lexfn(fnstring)
		print(self.parts)
		self.equation = self.parsefn(self.parts)
		        
	def derive():
		pass
		
	def lexfn(self, fnstring):
		parts = []
		tmp = ""
		for i in fnstring:
			if i.isdigit(): # multi digits, with floating point
				if tmp: # prevent out of range error
					if tmp[-1].isdigit() or tmp[-1] == ".":
						tmp += i
					else:
						parts.append(tmp)
						tmp = i
				else:
					tmp += i
				
			elif i.isalpha() or i in self.signs: # for one char things only append
				if tmp == "":
					parts.append(i)
				else:
					parts.append(tmp)
					tmp = ""
					parts.append(i)

			else: # " "
				pass
		
		# last part
		if tmp:
			parts.append(tmp)

		return parts
	
	def parsefn(parts):
		equation = []
		tmp = []
		for i in range(len(parts)):
			if i == "-" or i == "+": # sum and diff rule
				if any(c.isalpha() for c in tmp): # if it contains a letter

				else: # calculate
					
				tmp = ""
			else:
				tmp += i
			