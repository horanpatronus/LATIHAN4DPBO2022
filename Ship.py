from Vehicle import Vehicle

# membuat class
class Ship(Vehicle):

	# deklarasi atribut private
	__shipAge = 0
	__Type = ""
	__countryOfManufacture = ""
	
	# constructor 
	def __init__(self):
		self.__shipAge = 0
		self.__Type = ""
		self.__countryOfManufacture = ""

	# setter dan getter untuk atribut age
	def setShipAge(self, shipAge):
		self.__shipAge = shipAge

	def getShipAge(self):
		return self.__shipAge

	# setter dan getter untuk atribut Type
	def setType(self, Type):
		self.__Type = Type

	def getType(self):
		return self.__Type

	# setter dan getter untuk atribut countryOfManufacture
	def setCountryOfManufacture(self, countryOfManufacture):
		self.__countryOfManufacture = countryOfManufacture

	def getCountryOfManufacture(self):
		return self.__countryOfManufacture

	# method untuk mencetak output atribut dari class 
	def printShip(self):
		print("Usia Kapal     : {} Tahun".format(self.__shipAge))
		print("Tipe           : " + self.__Type)
		print("Negara Pabrik  : " + self.__countryOfManufacture)
		print("----------------------------------------")