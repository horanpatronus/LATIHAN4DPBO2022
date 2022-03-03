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
- countryOfManufacture

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

![1](https://user-images.githubusercontent.com/91965618/156534368-c602306f-4b45-49c7-a87a-aece936b51d4.png)

![2](https://user-images.githubusercontent.com/91965618/156534383-2da6fa0d-5f70-41bf-b4eb-c0cd6f430667.png)

![3](https://user-images.githubusercontent.com/91965618/156534387-73c17222-65dc-48ff-ad1d-72b30ce9e6eb.png)

![4](https://user-images.githubusercontent.com/91965618/156534396-d0d20b3a-b189-4f9b-8fed-63508a95686b.png)
