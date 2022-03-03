from Vehicle import Vehicle

# membuat class
class Airplane(Vehicle):

	# deklarasi atribut private
	__Type = ""
	__airplaneAge = 0
	__wingsLength = 0
	
	# constructor 
	def __init__(self):
		self.__Type = ""
		self.__airplaneAge = 0
		self.__wingsLength = 0

	# setter dan getter untuk atribut Type
	def setType(self, Type):
		self.__Type = Type

	def getType(self):
		return self.__Type

	# setter dan getter untuk atribut age
	def setAirplaneAge(self, airplaneAge):
		self.__airplaneAge = airplaneAge

	def getAge(self):
		return self.__airplaneAge

	# setter dan getter untuk atribut wingsLength
	def setWingsLength(self, wingsLength):
		self.__wingsLength = wingsLength

	def getWingsLength(self):
		return self.__wingsLength

	# method untuk mencetak output atribut dari class 
	def printAirplane(self):
		print("Usia Pesawat    : {} Tahun".format(self.__airplaneAge))
		print("Tipe            : " + format(self.__Type))
		print("Panjang Sayap   : {} m".format(self.__wingsLength))
		print("----------------------------------------")