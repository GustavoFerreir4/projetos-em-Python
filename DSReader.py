class CSV:

	def __init__(self, fileName):
		self.filePath = "DataSets/"+fileName
		self.file = open(self.filePath)
		self.file.seek(0)
		self.lineCount = 0
		while True:
			if self.file.readline():
				self.lineCount += 1
			else:
				break

	#returns number of lines (registers)
	def __len__(self):
		return self.lineCount

	#prints formatted Data
	def printData(self):
		self.file.seek(0)

		header = self.file.readline()
		header = self.seperateContent(header, True)

		cursor = self.file.tell()	

		print(header[0], "\t|", header[1], "\t|",header[2], "|")
		for line in range(0, len(self)):
			if line == 0:
				self.file.seek(cursor)
			print(self.seperateContent(self.file.readline()))

	#Creates an array if 'asArray' (bool) param is specified
	def seperateContent(self, text, asArray=False):
		clearText = text.strip() 
		if asArray:
			arr = text.split(',')
			for item in range(len(arr)):
				arr[item] = self.treatInput(arr[item])
			return arr
		else:
			return text.replace(",", "\t - \t")
			

	def toNumber(self, field):
		pass

	#returns a dictionary with values from the CSV file
	# def parseDict(self):
	# 	dictionary = dict()
	# 	matrice = self.matrice()
	# 	headers = matrice[0]
	# 	data = matrice[1:]

	# 	dict_columns = {header: [] for header in headers}
    
	# 	for line in data:
	# 		for index, value in enumerate(line):
	# 			if index < len(headers):
	# 				headers[index].append(value)
                


	#returns matrice of the CSV file
	def matrice(self, limit=0):
	
		matrice = list()
		self.file.seek(0)
		if not limit:
			for line in range(len(self)):
				matrice.append(self.seperateContent(self.file.readline(), True))
		else:
			for line in range(limit):
				matrice.append(self.seperateContent(self.file.readline(), True))

		return matrice


	#makes string fields integers, floats or strings
	def treatInput(self, input):
		try:
			return int(input)
		except ValueError:
			pass

		try:
			return float(input)
		except ValueError:
			pass

		return input

	

		





