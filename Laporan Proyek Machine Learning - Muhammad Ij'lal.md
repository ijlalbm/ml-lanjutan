# Laporan Proyek _Machine Learning_ - Muhammad Ij'lal

## _Domain_ Proyek

Mobil saat ini merupakan kebutuhan pokok bagi sebagian masyarakat dalam menjalankan aktifitasnya. Mobil bekas salah satu pilihan yang tinggi peminatnya karena kondisi masih baik dan layak digunakan. 

Tingginya  minat  masyarakat  terhadap  mobil  bekas  membuat  bisnis  ini semakin  meningkat,  hal ini  ditandai  dengan  banyaknya _showroom_ mobil  bekas. Tak luput diantara _showroom_ sangat kompetitif bersaing agar tetap eksis dalam bisnis mobil bekas. Salah  satu  masalah  yang  dihadapi  semua  _showroom_ adalah  menentukan  harga secara cepat dan akurat sehingga bisa menjual mobil dan segera mendapatkan _revenue_ menurut [(Kriswantara, Kurniawati, Pardede, 2021)](https://jurnal.syntaxliterate.co.id/index.php/syntax-literate/article/view/2716).

Untuk mendapatkan solusi dari kendala tersebut, akan digunakan pendekatan _machine learning_ untuk mendapatkan harga mobil yang bisa dijadikan dasar penetapan harga. _Machine learning_ telah berhasil memprediksi harga mobil bekas, misal [(Gajera P.,Gondaliya A.,Jenish K.,2021)](https://www.irjmets.com/uploadedfiles/paper/volume3/issue_3_march_2021/6681/1628083284.pdf) menggunakan 7 algoritma _machine learning_ dan didapatkan _error_ yang paling kecil dalam memprediksi harga adalah menggunakan algoritma _random forest_.

## _Business Understanding_
Tujuan utama dari aplikasi ini adalah untuk memprediksi harga mobil bekas berdasarkan variabel-variabel yang mempengaruhi harga dari mobil bekas. Sehingga _showroom_ memungkinkan membuat keputusan penetapan harga lebih cepat dan terukur. Dengan penetapan harga yang lebih cepat memungkinkan penjualan lebih cepat dan mendapatkan keuntungan lebih cepat.

### _Problem Statements_
- _Showroom_ kesulitan menetapkan standar harga ketika ingin menjual mobil bekas
- Belum diketahui variabel-variabel yang mempengaruhi harga mobil bekas

### _Goals_
- Dengan adanya model yang dihasilkan memungkinkan untuk digunakan dalam memprediksi harga mobil yang bisa dijadikan landasan dalam proses tawar menawar, bisa digunakan _showroom_ ketika ingin membeli atau menjual kembali.
- Akan didapatkan variabel yang paling berpengaruh dalam penetapan harga mobil bekas.

    ### _Solution statements_
    - Akan digunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan.
    - Melakukan _improvement_ pada _baseline model_ dengan _hyperparameter_ tuning.

## _Data Understanding_
Data yang digunakan pada analisis ini adalah dataset mobil bekas inggris namun hanya pada merek Toyota, dapat diakses pada [100,000 UK Used Car Dataset](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes?select=toyota.csv).

### Variabel-variabel pada _UK Used Car_ adalah sebagai berikut:
- _Model_ = Merupakan varian model dari toyota, seperti yaris, camry, dll
- _Year_ = Merupakan tahun keluaran mobil tersebut
- _Price_ = harga dari mobil bekas tersebut
- _Transmission_ = jenis transmisi dari mobil tersebut
- _Mileage_ = total jarak tempuh dari mobil tersebut
- _FuelType_ = jenis bahan bakar yang digunakan
- _Tax_ = pajak mobil tersebut
- _Mpg_ = kapasitas bahan bakar
- _EngineSize_ = tipe mesin yang digunakan
 
Untuk lebih memahami dataset, maka ditampilkan ringkasan data dengan fungsi ```.describe()```, maka didapatkan informasi ada data yang _min_nya 0 pada variabel _tax_ dan _engineSize_. Maka diasumsikan bahwa itu merupakan kesalahan karena tidak ada mesin yang _size_nya 0 dan kendaraan yang pajaknya 0.

_Outliers_ adalah sampel yang nilainya sangat jauh dari cakupan umum data utama. Ia adalah hasil pengamatan yang kemunculannya sangat jarang dan berbeda dari data hasil pengamatan lainnya. Untuk menghilangkan _outliers_ pada data mobil bekas, kami menggunakan _boxplot_ untuk menampilkan data _outliers_ kemudian menghapus data tersebut menggunakan teknik IQR. IQR=Q3-Q2.

![iqryear](https://drive.google.com/uc?export=view&id=10yJYVhdZL1uPv64sCsN-InmqyeeezSBV)

Pada gambar diatas terlihat bahwa ada data _outliers_ pada variabel tahun (ditandai dengan titik hitam), menyimpang dari data lainnya yaitu dari _boxplot_.

![iqryear](https://drive.google.com/uc?export=view&id=1gmlWdH0N3JuC-4a9jVwxA41RSydkYtPZ)

Pada variabel _engineSize_ juga terdapat data _outliers_. Untuk mengatasi hal ini maka akan dilakukan penghapusan pada data _outliers_ tersebut.
Langkah selanjutnya adalah menampilkan ringkasan dari data kategori.
![iqryear](https://drive.google.com/uc?export=view&id=15Q2Lp4KePmD1RD8H-vddGRsBejidNJvK)

Pada Gambar diatas terlihat bahwa model Aygo dan yaris merupakan 60% dari total data.

![iqryear](https://drive.google.com/uc?export=view&id=1w1OlYib3o-2EFfofPbcxg-5vtwAQH4NA)

Rata-rata transmisi pada data adalah _manual_ dan _automatic_.

Selanjutnya adalah menampilkan ringkasan data numerik.
![iqryear](https://drive.google.com/uc?export=view&id=1OUKqNOWwqtyPnynwg2EeA4KvP7RQG0Se)

Pada variabel _price_ dapat dilihat bahwa mayoritas harga mobil di harga 7000-1300.

Untuk mengetahui hubungan data kategori dengan harga mobil maka akan ditampilkan visualisasi datanya.
![iqryear](https://drive.google.com/uc?export=view&id=1es5HN3UFV-sU4KOfu9AssooTQlwbCjb0)

Dari gambar diatas terlihat bahwa harga cenderung mirip pada semua jenis model, maka dianggap model berpengaruh kecil terhadap harga.

![iqryear](https://drive.google.com/uc?export=view&id=1bH6RThA4tQJDK23TQWVQ4qjoOw0ntd7G)

Dari gambar diatas terlihat bahwa harga cenderung mirip pada semua jenis bahan bakar, maka _fuelType_ dianggap memiliki pengaruh kecil terhadap harga.

![iqryear](https://drive.google.com/uc?export=view&id=1hctNpjBMXuRoxvtzVVXLOHAG-3e5kye2)

Dari gambar diatas terlihat bahwa harga cenderung mirip pada semua jenis _transmission_, maka dianggap memiliki pengaruh kecil terhadap harga.

Untuk mengetahui korelasi antara variabel harga dengan variabel lain, maka digunakan fungsi _pairplot_ pada _library seaborns_.
![iqryear](https://drive.google.com/uc?export=view&id=1tGJZiqOG_fbv0VbEL7ZvjO_MsuQnj2u1)

Terlihat bahwa variabel _year_ memiliki korelasi positif terhadap harga. Semakin baru mobil tersebut, maka harga juga semakin mahal. Variabel _mileage_ juga memiliki pola,dimana berkorelasi negatif, semakin besar jarak tempuhnya, maka harga juga semakin murah. Variabel _engineSize_ juga memiliki korelasi terhadap harga, semakin besar _engine size_ nya, maka harga juga semakin mahal. Selanjutnya akan ditampilkan nilai korelasi setiap variabel terhadap harga.

![iqryear](https://drive.google.com/uc?export=view&id=1d8ZX9j1vRrTJ5jqGTfSGzFONS5OtclsB)

Dapat dilihat pada gambar bahwa variabel _year_ dan _engineSize_ memiliki korelasi yang cukup tinggi terhadap price, maka variabel tersebut akan digunakan sebagai input pada model.

## _Data Preparation_
Sebelum data diproses, maka dilakukan terkebih dahulu persiapan agar keluaran yang dihasilkan dapat konsisten hasilnya.

- Langkah pertama adalah mengubah data kategori menjadi data numerik karena algoritma hanya bisa memproses data numerik. Data yang diubah adalah _transmission_ dan _fuel type_. Disini kami menggunakan fungsi _OneHotEncoder_ yang disediakan oleh _library scikit-learn_.
- Langkah kedua adalah membagi data menjadi data latih dan data uji. Persentasenya adalah 90% data latih dan 10% data uji.
- Langkah _preprocessing_ selanjutnya adalah mengubah skala data agar memiliki performa yang lebih baik menggunakan fungsi _StandarScaler_ pada _library scikit-learn_.
  
|       | year      | engineSize |
|-------|-----------|------------|
| count | 3090.0000 | 3090.0000  |
| mean  | -0.0000   | 0.0000     |
| std   | 1.0002    | 1.0002     |
| min   | -3.7084   | -1.0746    |
| 25%   | -0.9065   | -1.0746    |
| 50%   | 0.0275    | 0.3024     |
| 75%   | 0.9615    | 0.5778     |
| max   | 1.8955    | 3.0563     |

Dapat dilihat pada tabel diatas bahwa _mean_ menjadi 0 dan _std_ menjadi 1.

## _Modeling_
Setelah mendapatkan variabel yang mempengaruhi harga mobil bekas. Selanjutnya untuk mengetahui prediksi harga mobil, maka digunakan 3 algoritma berbeda yang akurasinya akan diukur menggunakan mse, lalu akan dipilih model terbaik dengan mse terkecil pada data latih dan data uji.

### _Model Development_ dengan _K-Nearest Neighbor_
KNN adalah algoritma yang relatif sederhana dibandingkan dengan algoritma lain. Algoritma KNN menggunakan kesamaan fitur untuk memprediksi nilai dari setiap data yang baru. Dengan kata lain, setiap data baru diberi nilai berdasarkan seberapa mirip titik tersebut dalam set pelatihan.

KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat (dengan k adalah sebuah angka positif). Nah, itulah mengapa algoritma ini dinamakan K-nearest neighbor (sejumlah k tetangga terdekat). KNN bisa digunakan untuk kasus klasifikasi dan regresi. 

KNN bekerja pada data mobil bekas dengan menentukan terlebih dahulu secara acak banyak titik _neighbor_(k) pada sumbu x yaitu input model. Kemudian berdasarkan titik tersebut akan dihitung jarak pada titik-titik di sekitarnya. Jarak terdekat yang memiliki kesalahan terkecil yang akan ditentukan sebagai titik dalam model yang akan memprediksi data _input_ yang baru.

Pada algoritma KNN di percobaan ini menggunakan banyak _input(n neighbors)_ = 100.

### _Model Development_ dengan _Random Forest_
_Random forest_ merupakan salah satu model _machine learning_ yang termasuk ke dalam kategori _ensemble (group) learning_. Apa itu model _ensemble_? Sederhananya, ia merupakan model prediksi yang terdiri dari beberapa model dan bekerja secara bersama-sama. Ide dibalik model _ensemble_ adalah sekelompok model yang bekerja bersama menyelesaikan masalah. Sehingga, tingkat keberhasilan akan lebih tinggi dibanding model yang bekerja sendirian. Pada model _ensemble_, setiap model harus membuat prediksi secara independen. Kemudian, prediksi dari setiap model _ensemble_ ini digabungkan untuk membuat prediksi akhir.

 _Random forest_ pada dasarnya adalah versi _bagging_ dari algoritma _decision tree_. Bayangkan Anda memiliki satu _bag_ (tas) _random forest_ yang berisi beberapa _model decision tree_. _Model decision tree_ masing-masing memiliki _hyperparameter_ yang berbeda dan dilatih pada beberapa bagian (_subset_) data yang berbeda juga. Teknik pembagian data pada algoritma _decision tree_ adalah memilih sejumlah fitur dan sejumlah sampel secara acak dari dataset yang terdiri dari n fitur dan m sampel. 
 
 _Random forest_ bekerja pada data mobil bekas dengan membagi secara acak dan fitur berdasarkan banyak pohon yang ditentukan. Hasil prediksi setiap pohon _decision tree_ akan dicari rata-ratanya kemudian itulah yang menjadi hasil prediksi _random forest_.
 
 Pada algoritma _Random Forest_ di percobaan ini menggunakan parameter _n estimators_=55,_max depth_=16, dan _random state_=55.
 
 ### _Model Development_ dengan _Boosting Algorithm_
 Algoritma yang menggunakan teknik _boosting_ bekerja dengan membangun model dari data latih. Kemudian ia membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama. Model ditambahkan sampai data latih terprediksi dengan baik atau telah mencapai jumlah maksimum model untuk ditambahkan. 
 
 Seperti namanya, _boosting_, algoritma ini bertujuan untuk meningkatkan performa atau akurasi prediksi. Caranya adalah dengan menggabungkan beberapa model sederhana dan dianggap lemah (_weak learners_) sehingga membentuk suatu model yang kuat (_strong ensemble learner_). Algoritma _boosting_ muncul dari gagasan mengenai apakah algoritma yang sederhana seperti _linear regression_ dan _decision tree_ dapat dimodifikasi untuk dapat meningkatkan performa. 
 
 _Boosting_ akan bekerja pada data mobil bekas berdasarkan _learning rate_ dan _random state_ yang ditetapkan. _Boosting_ pada percobaan ini menggunakan parameter _learning rate_=0.02 dan _random state_=30.

## _Evaluation_
Metrik yang akan digunakan pada prediksi ini adalah MSE atau _Mean Squared Error_ yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi.

### MSE pada KNN
| _n estimators_ | _MSE train_ | MSE _test_ |
|--------------|-----------|----------|
|         120     |     5427      |     5478     |
|      100        |     4895      |     4852     |
|         150     |     6174      |      6184    |

### MSE pada _Random Forest_
| n _estimators_ | _max depth_ | _random state_ | _MSE train_ | _MSE test_ |
|--------------|-----------|--------------|-----------|----------|
|       30       |      16     |        55      |    2018       |     1824     |
|      55        |      16     |      55        |     2018      |      1817    |
|      100        |      16     |       55       |     2020      |     1809     |

### MSE pada _Boosting_
| _learning rate_ | _random state_ | MSE _train_ | MSE _test_ |
|---------------|--------------|-----------|----------|
|        0.02       |         30     |       3881    |    3382      |
|       0.02        |       55       |      3758     |     3398     |
|         0.02      |        100      |      3896     |     3407     |

Dari tabel diatas didapatkan kesimpulan bahwa nilai MSE terkecil ada pada algoritma _Random Forest_. Selanjutnya parameter dengan nilai _MSE_ terkecil  pada semua model diujikan dengan data acak, maka didapatkan kesalahan terkecil dengan menggunakan algoritma _random forest_.

| Nilai Target | Prediksi KNN | Prediksi RF | Prediksi _Boosting_ |
|--------------|--------------|-------------|-------------------|
| 9450         | 9782         | 9732        | 9946              |

# Kesimpulan
Variabel numerik yang paling berpengaruh terhadap harga mobil bekas adalah tahun pembelian mobil dan _engine size_ dari mobil tersebut.
Didapatkan juga kesimpulan bahwa model yang paling memiliki _mse_ terkecil menggunakan algoritma _random forest_.
Untuk menambah akurasi, dapat menambahkan data dari berbagai macam merek agar model lebih banyak belajar dari data dan menghasilkan _mse_ yang lebih kecil.

# Daftar Pustaka
[1] Kriswantara B.,Kurniawati,Pardede H.F., "PREDIKSI HARGA MOBIL BEKAS DENGAN _MACHINE LEARNING_", Jurnal Ilmiah Indonesia p–ISSN: 2541-0849, 2021.
[2] Gajera P.,Gondaliya A.,Jenish K.,"_OLD CAR PRICE PREDICTION WITH MACHINE LEARNING_",_International Research Journal of Modernization in Engineering Technology and Science Volume:03/Issue:03/March-2021_, 2021.
