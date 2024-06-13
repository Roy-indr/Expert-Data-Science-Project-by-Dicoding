# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Terdapat perusahaan multinasional bernama Jaya Jaya Maju yang mengalami kesulitan dalam mengelola karyawan. Akibatnya, attrition rate karyawan dalam perusahaan tersebut tinggi. Untuk itu, diperlukan identifikasi faktor penyebab yang dapat menyebabkan tingginya attrition rate karyawan. Pada dataset yang telah disediakan terdapat 35 kolom atau atribut. Penjelasan masing-masing atribut adalah sebagai berikut :

* **EmployeeId** - Employee Identifier
* **Attrition** - Did the employee attrition? (0=no, 1=yes)
* **Age** - Age of the employee
* **BusinessTravel** - Travel commitments for the job
* **DailyRate** - Daily salary
* **Department** - Employee Department
* **DistanceFromHome** - Distance from work to home (in km)
* **Education** - 1-Below College, 2-College, 3-Bachelor, 4-Master,5-Doctor
* **EducationField** - Field of Education
* **EnvironmentSatisfaction** - 1-Low, 2-Medium, 3-High, 4-Very High
* **Gender** - Employee's gender
* **HourlyRate** - Hourly salary
* **JobInvolvement** - 1-Low, 2-Medium, 3-High, 4-Very High
* **JobLevel** - Level of job (1 to 5)
* **JobRole** - Job Roles
* **JobSatisfaction** - 1-Low, 2-Medium, 3-High, 4-Very High
* **MaritalStatus** - Marital Status
* **MonthlyIncome** - Monthly salary
* **MonthlyRate** - Mounthly rate
* **NumCompaniesWorked** - Number of companies worked at
* **Over18** - Over 18 years of age?
* **OverTime** - Overtime?
* **PercentSalaryHike** - The percentage increase in salary last year
* **PerformanceRating** - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
* **RelationshipSatisfaction** - 1-Low, 2-Medium, 3-High, 4-Very High
* **StandardHours** - Standard Hours
* **StockOptionLevel** - Stock Option Level
* **TotalWorkingYears** - Total years worked
* **TrainingTimesLastYear** - Number of training attended last year
* **WorkLifeBalance** - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
* **YearsAtCompany** - Years at Company
* **YearsInCurrentRole** - Years in the current role
* **YearsSinceLastPromotion** - Years since the last promotion
* **YearsWithCurrManager** - Years with the current manager

### Permasalahan Bisnis

Perusahaan Jaya Jaya Abadi memiliki permasalahan dalam attrition rate pegawainya dimana jumlah pegawai yang yang keluar lebih dari 10%. Untuk itu, diperlukan identifikasi mengenai faktor apa saja yang menyebabkan tingginya attrition rate di perusahaan tersebut

### Cakupan Proyek

Pada proyek ini, terdapat beberapa hal yang perlu dilakukan:
* Melakukan proses analisa data employee attrition rate perusahaan Jaya Jaya Abadi
* Melakukan proses pembersihan data
* Melakukan proses eksplorasi data
* Mencari penyebab mungkinnya faktor-faktor attrition rate pada perusahaan Jaya Jaya Abadi
* Membuat model machine learning yang mampu memprediksi attrition rate
* Membuat business dashboard untuk laporan dan monitoring faktor-faktor attrition rate

Sehingga, proyek kali ini hanya untuk menggali informasi mengenai penyebab attrition rate hingga pembuatan business dashboard dan model machine learning untuk memprediksi kemungkinan attrition rate. Selain itu, diperlukan adanya business dashboard yang bertujuan untuk proses monitoring faktor-faktor tersebut. Beberapa pertanyaan yang bisa diajukan adalah:
* Apakah umur menjadi salah satu faktor attrition rate?
* Apakah kepuasaan pegawai terhadap lingkungan dan pekerjaannya berpengaruh?
* Apakah pegawai yang resign tersebut mayoritas melakukan lembur?
* Apakah pendapatan yang dihasilkan menjadi salah satu faktor?
* Apakah lama kerja pegawai di perusahaan memengaruhi?
* Apakah ada hubungan attrition rate dengan manager yang baru?   

Pada proyek ini, diharapkan tercapainya tujuan yaitu mengidentifikasi faktor penyebab attrition rate pegawai. Selain itu, pada proyek ini akan dihasilkan business dashboard dan model machine learning yang dapat digunakan untuk memantau dan memprediksi kemungkinan attrition rate pada pegawai.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Setup environment:

```
pipenv install
pipenv shell
pip install -r requirements.txt

```

## Business Dashboard

link  : http://localhost:3000/public/dashboard/e6eaa1e8-4a51-4894-8fb4-6fb70c6130d3

Business dashboard yang dibuat bertujuan membantu memberikan insight pada setiap attribute yang dianggap menjadi faktor penting terjadinya attrition rate. Attribute-attribute tersebut didapatkan dengan bantuan fungsi .corr() pada python untuk mencari attribute mana yang memiliki pengaruh pada attrition rate. Terdapat dua macam grafik pada dashboard, yaitu grafik bar dan pie. Grafik bar untuk membandingkan dua value pada attribute yang sama sedangkan grafik pie untuk mengetahui komposisi penyusun suatu attribute. Grafik-grafik pada dashboard bisa dikategorikan sebagai berikut :
* Grafik pengaruh umur terhadap attrition rate
* Grafik pengaruh kepuasan pegawai terhadap attrition rate
* Grafik pengaruh ovgertime terhadap attrition rate
* Grafik pengaruh monthly income terhadap attrition rate
* Grafik pengaruh lama kerja pegawai dalam perusahaan dan lama kerja pegawai di bawah manager baru terhadap attrition rate

## Conclusion

Dari proses eksplorasi data dan analisi data, dapat ditarik beberapa kesimpulan sebagai berikut:
* Sebagian besar karyawan yang resign berusia di antara 30 - 38 tahun. Kemudian, pada urutan ke-2 pada usia 20 tahun an
* Mayoritas pegawai yang resign merasa tidak puas pada lingkungan kerja dan pekerjaannya. Namun, urutan ke-2 dan ke-3 menunjukkan pegawai tetap resign meskipun merasa puas dengan hal-hal tersebut
* Banyaknya pegawai yang keluar juga dipengaruhi oleh penghasilan per bulannya. Semakin kecil penghasilannya semakin banyak yang mengajukan resign
* Mayoritas pegawai yang keluar memiliki total pengalaman kerja selama 0 hingga 5 tahun. Selain itu, banyaknya pegawai yang keluar didominasi orang yang belum bekerja lama di perusahaan. Namun, masih ada pegawai yang keluar meskipun sudahy lama bekerja di perusahaan
* Orang yang bekerja lembur cenderung banyak yang resign dari perusahaan

### Rekomendasi Action Items (Optional)

Dari hasil eksplorasi dan analisis data, dapat ditarik kesimpulan mengenai rekomendasi langkah yang bisa dilakukan untuk mengurangi attrition rate, yaitu sebagai berikut :

- Meningkatkan rasa nyaman dan puas untuk setiap pegawai di tempat kerja. Hal tersebut dapat dimulai dari meningkatkan kualitas tempat kerja, fasilitas tempat kerja, atau bisa dengan bertanya langsung kepada setiap pegawai mengenai perihal yang membuatnya tidak nyaman dan tidak puas di tempat kerja 
- Mengurangi jadwal lembur untuk karyawan atau meningkatkan pendapatan yang diterima dari hasil lembur
- Merekrut orang yang memiliki total pengalaman kerja lebih banyak
- Meningkatkan hasil pendapatan yang didapat pegawai

### Melakukan Predicition Pada Machine Learning yang Telah Dibuat

Untuk melakukan proses machine learning yang telah dibuat pengguna dapat melakukan tahap-tahap sebagai berikut:
- Pastikan telah menjalankan file jupyter dan memastikan adanya dataset 'cleaned.csv' setelahnya
- Buka file 'python_ML_script.py'
- Membuat list dua dimensi yang berisikan value baru untuk diprediksi, list sudah disediakan dengan nama 'new_data_to_predict'
- Run file maka hasilnya akan tertampil dengan 1 = attriton, 0 = no attrition
