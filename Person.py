# membuat class
class Person():

	# deklarasi atribut private
	__NIK = 0
	__name = ""
	__gender = ""
	
	# constructor 
	def __init__(self):
		self.__NIK = 0
		self.__name = ""
		self.__gender = 0

	# setter dan getter untuk atribut NIK
	def setNIK(self, NIK):
		self.__NIK = NIK

	def getNIK(self):
		return self.__NIK

	# setter dan getter untuk atribut name
	def setName(self, name):
		self.__name = name

	def getName(self):
		return self.__name

	# setter dan getter untuk atribut gender
	def setGender(self, gender):
		self.__gender = gender

	def getGender(self):
		return self.__gender

	def isSleep(self):
		print("{} is sleeping...".format(self.__name))

	# method untuk mencetak output atribut dari class 
	def printPerson(self):
		print("----------------------------------------")
		print("NIK             : {}".format(self.__NIK))
		print("Nama            : " + format(self.__name))
		print("Jenis Kelamin   : " + format(self.__gender))
		self.isSleep()
		print("----------------------------------------")