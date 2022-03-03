# LATIHAN4DPBO2022
Repositori ini dibuat untuk memenuhi tugas praktikum mata kuliah Desain Pemrograman Berorientasi Objek materi Multiple and Hierarchical Inheritance.

*Saya Rahma Maulida 2003688 mengerjakan Latihan 3 dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.*


##### Desain Program
Program terdiri atas 6 class, yaitu Vehicle, Ship, Airplane, Person, Job, dan Driver.
Link Desain: https://drive.google.com/file/d/10eEplTjk5bYlP7ui-EhfKZA7B9lKPbWn/view?usp=sharing

##### Penjelasan Desain Program
Secara hierarkial, "Driver" merupakan (is a) "Person" dan juga merupakan (is a) "Job", sehingga hubungan antara ketiga class tersebut adalah class Person dan class Job menjadi parent dari class Driver. "Driver" tentu memiliki atau mengendarai kendaraan. Oleh karena itu, hubungan antara class Driver dengan class Vehicle merupakan Composition. "Airplane" dan "Ship" merupakan jenis-jenis dari Vehicle (Airplane and Ship is a Vehicle), maka Vehicle menjadi Parent class dari kedua class tersebut. Oleh karena itu, hierarchical inheritance diimplementasikan dalam program ini.

Vehicle terdiri atas atribut:
- fuelType
- maxPassengers

Ship terdiri atas atribut:
- age
- type
- - countryOfManufacture

Person terdiri atas atribut:
- NIK
- name
- gender

Job terdiri atas atribut:
- NIP
- companyName
- position

Driver terdiri atas atribut:
- licenseID
- activeUntil
- vehicleType
- composition dari class Vehicle

#### Deskripsi Program
Program dibuat ke dalam bahasa Python.
Seluruh atribut merupakan atribut private. Data dimasukkan ke dalam object menggunakan setter. Data yang terdapat di dalam object selanjutnya dicetak sebagai output menggunakan method.

#### Tampilan Program
