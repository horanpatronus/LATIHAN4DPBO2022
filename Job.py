# membuat class
class Job():

	# deklarasi atribut private
	__NIP = 0
	__companyName = ""
	__position = ""
	
	# constructor 
	def __init__(self):
		self.__NIP = 0
		self.__companyName = ""
		self.__position = ""

	# setter dan getter untuk atribut NIP
	def setNIP(self, NIP):
		self.__NIP = NIP

	def getNIP(self):
		return self.__NIP

	# setter dan getter untuk atribut companyName
	def setCompanyName(self, companyName):
		self.__companyName = companyName

	def getCompanyName(self):
		return self.__companyName

	# setter dan getter untuk atribut position
	def setPosition(self, position):
		self.__position = position

	def getPosition(self):
		return self.__position

	# method untuk mencetak output atribut dari class 
	def printJob(self):
		print("NIP             : {}".format(self.__NIP))
		print("Nama Perusahaan : " + format(self.__companyName))
		print("Jabatan         : " + format(self.__position))
		print("----------------------------------------")