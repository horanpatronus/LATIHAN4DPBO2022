# import class
from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane
from Person import Person
from Job import Job
from Driver import Driver

#------ Driver #1 ------#
# membuat array object untuk driver pertama
d1 = Driver()
d1.setNIP(12393004055593)
d1.setCompanyName("PT Maju Bersama")
d1.setPosition("Pilot")
d1.setNIK(31239300405559)
d1.setName("John Doe")
d1.setGender("Laki-laki")
d1.setLicenseID(23930040555931)
d1.setActiveUntil("22/02/2027")
d1.setVehicleType("Pesawat Terbang")

# membuat array object untuk vehicle dari driver pertama
a1 = Airplane()
a1.setFuelType("Kerosin")
a1.setMaxPassenger(539)
a1.setType("Boeing 747")
a1.setAirplaneAge(5)
a1.setWingsLength(64)

# mencetak driver pertama
print("\n==============")
print("Driver Pertama")
print("==============")
d1.printPerson()
d1.printJob()
d1.printDriver()
a1.printAirplane()
a1.printVehicle("airplane")

#------ Driver #2 ------#
# membuat array object untuk driver kedua
d2 = Driver()
d2.setNIP(96593684068503)
d2.setCompanyName("PT Karya Cipta")
d2.setPosition("Nahkoda")
d2.setNIK(39659368406850)
d2.setName("Frank Hasim")
d2.setGender("Laki-laki")
d2.setLicenseID(65936840685039)
d2.setActiveUntil("01/01/2023")
d2.setVehicleType("Kapal Ferry")

# membuat array object untuk vehicle dari driver kedua
s2 = Ship()
s2.setFuelType("Solar")
s2.setMaxPassenger(264)
s2.setShipAge(5)
s2.setType("Kapal Penumpang")
s2.setCountryOfManufacture("Indonesia")

# mencetak driver kedua
print("\n============")
print("Driver Kedua")
print("============")
d2.printPerson()
d2.printJob()
d2.printDriver()
s2.printShip()
s2.printVehicle("ship")

#------ Driver #3 ------#
# membuat array object untuk driver ketiga
d3 = Driver()
d3.setNIP(72393015355065)
d3.setCompanyName("TNI AD RI")
d3.setPosition("Pilot")
d3.setNIK(57239301535506)
d3.setName("Syamsudin")
d3.setGender("Laki-laki")
d3.setLicenseID(23930153550657)
d3.setActiveUntil("08/08/2022")
d3.setVehicleType("Pesawat Angkut Militer")

# membuat array object untuk vehicle dari driver ketiga
a3 = Airplane()
a3.setFuelType("Avtur")
a3.setMaxPassenger(92)
a3.setType("Hercules C-130")
a3.setAirplaneAge(12)
a3.setWingsLength(40.5)

# mencetak driver ketiga
print("\n=============")
print("Driver Ketiga")
print("=============")
d3.printPerson()
d3.printJob()
d3.printDriver()
a3.printAirplane()
a3.printVehicle("airplane")

#------ Driver #4 ------#
# membuat array object untuk driver keempat
d4 = Driver()
d4.setNIP(66083684284108)
d4.setCompanyName("TNI AL RI")
d4.setPosition("Nahkoda")
d4.setNIK(86608368428410)
d4.setName("George Hasan")
d4.setGender("Laki-laki")
d4.setLicenseID(60836842841086)
d4.setActiveUntil("29/11/2029")
d4.setVehicleType("Kapal Selam")

# membuat array object untuk vehicle dari driver keempat
s4 = Ship()
s4.setFuelType("Diesel Listrik")
s4.setMaxPassenger(32)
s4.setShipAge(4)
s4.setType("Scorpene")
s4.setCountryOfManufacture("Prancis")

# mencetak driver keempat
print("\n==============")
print("Driver Keempat")
print("==============")
d4.printPerson()
d4.printJob()
d4.printDriver()
s4.printShip()
s4.printVehicle("ship")

#------ Driver #5 ------#
# membuat array object untuk driver kelima
d5 = Driver()
d5.setNIP(12330559049305)
d5.setCompanyName("PT Antara")
d5.setPosition("Pilot")
d5.setNIK(51233055904930)
d5.setName("Ahmad Nugraha")
d5.setGender("Laki-laki")
d5.setLicenseID(23305590493051)
d5.setActiveUntil("16/12/2024")
d5.setVehicleType("Pesawat Business Jet")

# membuat array object untuk vehicle dari driver kelima
a5 = Airplane()
a5.setFuelType("Minyak Bumi")
a5.setMaxPassenger(19)
a5.setType("Gulfstream G550")
a5.setAirplaneAge(1)
a5.setWingsLength(28.5)

# mencetak driver kelima
print("\n=============")
print("Driver Kelima")	
print("=============")
d5.printPerson()
d5.printJob()
d5.printDriver()
a5.printAirplane()
a5.printVehicle("airplane")