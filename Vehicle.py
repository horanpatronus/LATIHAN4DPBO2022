# membuat class
class Vehicle():

	# deklarasi atribut private
	__fuelType = ""
	__maxPassenger = 0
	
	# constructor 
	def __init__(self):
		self.__fuelType = ""
		self.__maxPassenger = 0

	# setter dan getter untuk atribut fuelType
	def setFuelType(self, fuelType):
		self.__fuelType = fuelType

	def getFuelType(self):
		return self.__fuelType

	# setter dan getter untuk atribut maxPassenger
	def setMaxPassenger(self, maxPassenger):
		self.__maxPassenger = maxPassenger

	def getMaxPassenger(self):
		return self.__maxPassenger

	def Move(self, condition):
		if(condition == "airplane") :
			print("The {} is moving...".format(condition))
		elif(condition == "ship") :
			print("The {} is moving...".format(condition))
	
	# method untuk mencetak output atribut dari class 
	def printVehicle(self, condition):
		print("Bahan Bakar     : " + format(self.__fuelType))
		print("Penumpang       : {} orang".format(self.__maxPassenger))
		self.Move(condition)
		print("----------------------------------------")
		