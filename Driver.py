from Job import Job
from Person import Person

# membuat class
class Driver(Job, Person):

	# deklarasi atribut private
	__licenseID = 0
	__activeUntil = ""
	__vehicleType = ""
	__j_obj = Job()
	__p_obj = Person()
	
	# constructor 
	def __init__(self):
		self.__licenseID = 0
		self.__activeUntil = ""
		self.__vehicleType = ""

	# setter dan getter untuk atribut licenseID
	def setLicenseID(self, licenseID):
		self.__licenseID = licenseID

	def getLicenseID(self):
		return self.__licenseID

	# setter dan getter untuk atribut activeUntil
	def setActiveUntil(self, activeUntil):
		self.__activeUntil = activeUntil

	def getActiveUntil(self):
		return self.__activeUntil

	# setter dan getter untuk atribut vehicleType
	def setVehicleType(self, vehicleType):
		self.__vehicleType = vehicleType

	def getVehicleType(self):
		return self.__vehicleType

	# method untuk mencetak output atribut dari class 
	def printDriver(self):
		print("ID Lisensi      : {}".format(self.__licenseID))
		print("Masa Aktif      : " + format(self.__activeUntil))
		print("Jenis Kendaraan : " + format(self.__vehicleType))
		print("----------------------------------------")