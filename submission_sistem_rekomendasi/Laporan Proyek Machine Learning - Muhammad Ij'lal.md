# Laporan Proyek _Machine Learning_ - Muhammad Ij'lal

## _Project Overview_

Salah satu akibat dari perkembangan teknologi yang semakin cepat adalah dihasilkannya berbagai macam data yang semakin hari semakin bertambah. Berbagai macam penelitian pun mencoba mendapatkan manfaat dan wawasan dari data tersebut.

Menghadapi berbagai macam data tersebut sistem rekomendasi pun diusulkan. Tujuan dari sistem rekomendasi adalah menghasilkan rekomendasi yang mungkin _user_ tertarik berdasarkan preferensi _user_ tersebut [1].

Menemukan buku yang relevan di internet merupakan tantangan besar bagi pengguna internet. Sistem rekomendasi telah hadir untuk melakukan pencarian yang efektif berdasarkan preferensi pengguna. Sebagian besar sistem rekomendasi yang ada menggunakan _content based filtering_ dan _collaborative filtering_ berdasarkan _rating_ dari _user_ [2].

## _Business Understanding_
Tujuan utama dari aplikasi ini adalah mendapatkan rekomendasi buku berdasarkan jenis kategori buku yang pernah dipilih. Sehingga memungkinkan pengguna bisa mendapatkan buku yang bervariasi dan penjual buku bisa menjual lebih cepat. Aplikasi ini bisa diaplikasikan pada toko buku _online_, ketika seseorang ingin membeli sebuah buku maka sebelum membayar, pembeli bisa disarankan menambah buku lain yang sudah direkomendasikan oleh sistem aplikasi berdasarkan kemiripan _genres_, sehingga memungkinkan pembeli membeli buku lebih banyak dan lebih bervariasi, dengan ini penjual buku bisa menjual lebih banyak dan lebih bervariasi. Dengan ini pula penjualan bisa meningkat dan mendapatkan keuntungan lebih banyak. Sistem rekomendasi juga akan mempermudah pembeli menemukan buku yang sesuai dengan minatnya sehingga penjualan buku bisa lebih cepat.

### _Problem Statements_
- Bagaimana cara mendapatkan rekomendasi buku berdasarkan genre buku?

### _Goals_
- Mengetahui bagaimana mendapatkan model yang bisa digunakan untuk merekomendasikan buku berdasarkan genre buku yang di _input_ kan.

## _Data Understanding_

Data yang digunakan pada aplikasi ini bersumber dari situs _kaggle_ dapat diakses di tautan ini [_Best Books (10k) Multi-Genre Data_](https://www.kaggle.com/datasets/ishikajohari/best-books-10k-multi-genre-data). Terdapat 10.000 data dengan 8 kolom.

Variabel-variabel _dataset_ buku adalah sebagai berikut:
- _Unnamed_: 0  merupakan penomoran baris pada data.
- _Book_ merupakan judul buku.
- _Author_ merupakan penulis dari buku.
- _Description_ merupakan deskripsi dari buku.
- _Genres_ merupakan genre/aliran buku.
- _Avg_Rating_ merupakan rata-rata _rating_.
- _Num_Ratings_ merupakan banyak yang memberikan _rating_ pada buku.
- URL merupakan _link_ buku.

Langkah pertama yang dilakukan untuk memahami data adalah menampilkan ringkasan 5 data teratas. Terlihat bahwa data pada _genres_ didahului dan diakhiri oleh kurung siku [''], maka terlebih dahulu dilakukan operasi untuk menghilangkan tanda tersebut agar data lebih bersih.

Langkah selanjutnya adalah mengetahui banyak buku berdasarkan judul buku dan mengetahui _genres_ dari buku tersebut. Didapatkan 9871 buku dengan banyak genre 8043. Olehnya itu diketahui bahwa ada buku yang sama judulnya namun tidak kami hapus karena bisa saja judulnya sama namun penulis dan genrenya berbeda. 

Berikut beberapa genre dari dataset berdasarkan _book_ pada _dataset_.

Tabel 1 Ringkasan genre buku pada _dataset_
| Book                  | Genres                                                                                          |
|-----------------------|-------------------------------------------------------------------------------------------------|
| To Kill a Mockingbird | Classics,Fiction,Historical Fiction,School, Literature, Young adult, Historical                 |
| Pride and Prejudice   | 'Classics', 'Fiction', 'Romance', 'Historical Fiction', 'Literature', 'Historical', 'Audiobook' |

Adapun _genres_ pada dataset ini memiliki 8043 macam genre. Diantara genre tersebut adalah
- _Classics_ adalah jenis buku yang terkenal dan dianggap memiliki sastra yang tinggi.
- _Fiction_ adalah jenis buku yang merupakan cerita/kejadian yang bersumber dari imajinasi, bukan dari fakta.
- _School_ adalah jenis buku yang digunakan oleh pelajar.
- _Historical_ adalah buku yang terkait dengan sejarah.
- _Romance_ adalah buku tentang kisah asmara tentang seseorang dengan yang lain.
- _Fantacy_ adalah buku tentang harapan-harapan yang diharapkan terjadi pada masa depan.

Setelah menampilkan info dari data, langkah selanjutnya adalah menampilkan ringkasan dari variabel _ratings_.

Tabel 2 Hasil analisis pada tabel _ratings_
| Ukuran | Nilai |
|--------|-------|
| count  | 1000  |
| mean   | 4.06  |
| std    | 0.33  |
| min    | 0.00  |
| 25%    | 3.88  |
| 50%    | 4.08  |
| 75%    | 4.26  |
| max    | 5.00  |

Pada tabel 2 diketahui bahwa rentang variabel _rating_ adalah 0 sampai 5 yang didapatkan dari nilai _min_ dan _max_.

## _Data Preparation_

Sebelum data diproses oleh model, penting untuk mengetahui apakah ada data kosong pada dataset, agar hasil keluaran yang dihasilkan benar representasi data seluruh data pada dataset, olehnya itu langkah selanjutnya adalah memeriksa data yang memiliki nilai _null_.

Tabel 3 Deteksi jumlah data _null_ pada tiap variabel
| Variabel    | Banyak data null |
|-------------|------------------|
| Unnamed:0   | 0                |
| Book        | 0                |
| Author      | 0                |
| Description | 77               |
| Genres      | 0                |
| Avg_Ratings | 0                |
| Num_Ratings | 0                |
| URL         | 0                |

Pada tabel 3 Terlihat bahwa data _null_ hanya terdapat pada variabel _Description_ yaitu sebanyak 77, namun hal itu dibiarkan karena pada aplikasi ini variabel _Description_ tidak digunakan.

Langkah selanjutnya adalah membuat variabel baru dengan mengambil variabel yang akan digunakan untuk membuat sistem rekomendasi yaitu variabel _Author_, _Book_, _Genres_, _Avg_Ratings_. Adapun variabel yang digunakan untuk mendapatkan rekomendasi adalah variabel _Genres_.

## _Modeling_

Variabel _Genres_ merupakan data teks, data teks memerlukan persiapan khusus sebelum digunakan untuk pemodelan. Teks harus diurai terlebih dahulu dengan teknik tokenisasi. Kemudian, ia perlu dikodekan menjadi bilangan numerik agar dapat digunakan sebagai masukan pada algoritma _machine learning_. Proses ini disebut ekstraksi atau rekayasa fitur(_feature engineering_).

Terdapat beberapa metode rekayasa fitur untuk representasi teks. Metode ini diklasifikasikan ke dalam empat kategori, antara lain:

- _Basic vectorization approaches_ (contoh: _One-Hot Encoding_, _Bag of Words_, _Bag of N-Grams_, dan _TF-IDF_).
- _Distributed representations_ (contoh: _Words Embeddings_).
- _Universal text representation_ (menggunakan _pre-trained embedding_).
- _Handcrafted features_ (mengandalkan _domain-specific knowledge_).

Metode rekayasa fitur untuk representasi teks yang digunakan pada aplikasi ini adalah TF-IDF.

### TF-IDF
Teknik penilaian TF-IDF merupakan kepanjangan dari _Term Frequency-Inverse Document Frequency_. Ia bertujuan untuk mengukur seberapa penting suatu kata terhadap kata-kata lain dalam dokumen. TF-IDF adalah skema representasi yang umum digunakan untuk sistem pengambilan informasi dan ekstraksi dokumen yang relevan dengan kueri tertentu. ini berdasarkan seberapa sering kata tersebut muncul pada teks dan seluruh dokumen.

Sedangkan IDF (_Inverse Document Frequency_) mengukur pentingnya istilah di seluruh korpus. Dalam komputasi TF, semua istilah diberikan bobot kepentingan (weight) yang sama. Meskipun sering muncul, _stop word_ seperti _is_, _are_, _am_, dsb, tidaklah penting. Untuk mengatasi kasus seperti ini, IDF mempertimbangkan _term_ yang sangat umum di seluruh dokumen dan menimbang istilah-istilah yang jarang.

Langkah awal proses TF akan bekerja pada dataset dengan memecahkan kata pada kolom _genres_. Setelah semua kata didapatkan, TF akan menghitung berapa kali kata tersebut muncul dalam kolom _genres_. Setelah itu TF akan membagi setiap jumlah kemunculan suatu kata kemudian membagi dengan banyak kata untuk mendapatkan frekuensi pada setiap kata. 

Langkah selanjutnya adalah melakukan proses IDF, proses IDF merupakan proses yang penting karena ingin didapatkan kata-kata yang jarang muncul, kemudian memberikannya dengan nilai yang tinggi, jika tidak dilakukan proses IDF, maka kata-kata yang sering muncul seperti imbuhan _the_ akan memiliki nilai yang tinggi pada kalimat.

Setelah dilakukan proses TF-IDF. Untuk mengetahui nilai setiap kata pada _genres_, selanjutnya dipasangkan dengan kolom _Book_

Tabel 4 Nilai TF-IDF masing-masing genre buku
| Book                              | research | nonfiction | spain | 16th | mythos | eugenics |
|-----------------------------------|---------:|-----------:|------:|-----:|-------:|---------:|
| Your Leadership Edge              |      0.0 |   0.202145 |   0.0 |  0.0 |    0.0 |      0.0 |
| There's No Such Place As Far Away |      0.0 |   0.000000 |   0.0 |  0.0 |    0.0 |      0.0 |

Tabel 4 merupakan ringkasan nilai TF-ID _genres_ pada setiap buku.

Untuk mendapatkan rekomendasi buku, akan digunakan metode _Content Based Filtering_ meskipun metode ini memiliki kekurangan yaitu sangat bergantung dengan preferensi pengguna sebelumnya.

### _Content Based Filtering_
Ide dari sistem rekomendasi berbasis konten (content-based filtering) adalah merekomendasikan item yang mirip dengan item yang disukai pengguna di masa lalu. Content-based filtering mempelajari profil minat pengguna berdasarkan data dari objek yang telah dinilai pengguna. Algoritma ini bekerja dengan menyarankan item serupa yang pernah disukai di masa lalu atau sedang dilihat di masa kini kepada pengguna. Semakin banyak informasi yang diberikan pengguna, semakin baik akurasi sistem rekomendasi. 

Metode ini akan digunakan pada rekomendasi buku ini dengan asumsi bahwa pengguna pernah menyukai atau melihat suatu buku. Untuk merekomendasikan buku lain maka diambil genre buku yang dipilih oleh _user_ kemudian mencocokkannya dengan buku lain yang genrenya mirip dengannya. Untuk mengetahui derajat kesamaan antar buku, maka akan digunakan metode _Cosine Similarity_. 

### _Cosine Similarity_
Metode cosine similarity merupakan metode untuk menghitung kesamaan antara dua buah objek yang dinyatakan dalam dua buah vector dengan menggunakan _keywords_ (kata kunci) dari sebuah dokumen sebagai ukuran. Semakin mirip kedua objek tersebut, maka nilai akan mendekati 1, jika berbeda akan mendekat 0. Lankah selanjutnya adalah mencari nilai _cosine similarity_ pada nilai TF-IDF yang didapatkan.

 Langkah selanjutnya adalah memasangkan buku dengan buku yang lain agar didapatkan buku yang mirip berdasarkan nilai _cosine similarity_ nya.

Tabel 5 Nilai _Cosine Similarity_ tiap buku dengan buku lainnya
|                                                       Book | Legends of  the Amazon | Essays and Poems | The Irresistible Revolution:  Living as an Ordinary Radical | Taras Bulba | The Seat of the Soul | Single-Minded |
|-----------------------------------------------------------:|-----------------------:|-----------------:|------------------------------------------------------------:|------------:|---------------------:|--------------:|
|                   Danny and the Dinosaur                   |                    0.0 |         0.048840 |                                                    0.000000 |    0.072881 |             0.000000 |      0.019394 |
| Those Pricey Thakur Girls  (Those Pricey Thakur Girls, #1) |                    0.0 |         0.064516 |                                                    0.000000 |    0.144701 |             0.000000 |      0.731162 |
|                    The Blood of Flowers                    |                    0.0 |         0.000000 |                                                    0.000000 |    0.155468 |             0.000000 |      0.100320 |

Tabel 5 merupakan contoh ringkasan nilai derajat kesamaan antar buku pada dataset, semakin mirip buku dengan buku lainnya nilai akan mendekati 1, semakin tidak mirip akan mendekati 0. 

Pada tahap sebelumnya telah didapatkan derajat kesamaan buku dengan buku lainnya. Pada tahap ini akan ditampilkan _top-10_ rekomendasi berdasarkan derajat kesamaan yang didapatkan pada proses _cosine similarity_.

Tabel 6 Hasil rekomendasi model yang relevan terhadap buku _input_
|    | Judul Buku                                       | _Genres_                                                                                                                 |
|----|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| 1  | _Love Medicine (Love Medicine, #1)_              | 'Fiction', 'Historical Fiction', 'Short Stories', 'Novels', 'Literary Fiction', 'Literature', 'Classics'                 |
| 2  | _All the Pretty Horses (The Border Trilogy, #1)_ | 'Fiction', 'Westerns', 'Historical Fiction', 'Classics', 'Literature', 'Novels', 'Literary Fiction'                      |
| 3  | _Angle of Repose_                                | 'Fiction', 'Historical Fiction', 'Classics', 'Westerns', 'Literature', 'Literary Fiction', 'Novels'                      |
| 4  | _Legends of the Fall_                            | 'Fiction', 'Historical Fiction', 'Westerns', 'Short Stories', 'Classics', 'Historical', 'American'                       |
| 5  | _Lost Nation_                                    | 'Historical Fiction', 'Fiction', 'Historical', 'Westerns', 'Novels', 'American', 'Literary Fiction'                      |
| 6  | _The Sense of Touch_                             | 'Short Stories', 'Literary Fiction', 'Fiction', 'Contemporary', 'Novels'                                                 |
| 7  | _Little Century_                                 | 'Historical Fiction', 'Fiction', 'Westerns', 'Historical', 'Romance', 'Adult Fiction', 'Literary Fiction'                |
| 8  | _The Nightingales of Troy: Connected Stories_    | 'Short Stories', 'Fiction', 'Historical Fiction', 'Literary Fiction', 'American', 'Historical'                           |
| 9  | _Point Omega_                                    | 'Fiction', 'Novels', 'American', 'Literature', 'Contemporary', 'Literary Fiction', 'Novella'                             |
| 10 | _Memory Wall_                                    | 'Short Stories', 'Fiction', 'Contemporary', 'Historical Fiction', 'Science Fiction', 'Literary Fiction', 'Adult Fiction' |

## Evaluation
Sistem rekomendasi dianggap sebagai jenis sistem pengambilan informasi tertentu oleh peneliti. Presisi telah digunakan oleh banyak peneliti untuk evaluasi sistem rekomendasi. Presisi diartikan sebagai rasio rekomendasi yang relevan dengan jumlah total item yang direkomendasikan.

Presisi = Rekomendasi buku yang relevan / Banyak buku yang direkomendasikan

Buku yang diujikan adalah buku dengan judul _Train Dreams_ dengan _genres_	_'Fiction', 'Historical Fiction', 'Novella', 'Westerns', 'Novels', 'Literary Fiction', 'Short Stories'_

Variabel _Genres_ pada _dataset_ ini memiliki lebih dari 2 genre, ketika genre buku pada hasil rekomendasi lebih banyak yang relevan dengan genre _input_ an, maka akan diberi nilai 1, jika genre yang relevan adalah sama atau lebih sedikit maka diberi nilai 0. Maka berdasarkan genre pada tabel 6 presisi yang didapatkan adalah $`\frac{1+0+1+1+1+1+1+1+1+1}{10} * 100 = 90\%`$

# Kesimpulan
Model yang dihasilkan mampu mendapatkan 10 rekomendasi buku yang dibuktikan dengan kemiripan genre pada buku _input_ an pada model dengan genre buku hasil rekomendasi. Presisi yang didapatkan adalah 90%.

Untuk mendapatkan hasil yang maksimal bisa membandingkan hasilnya menggunakan metode lain seperti _Collaborative Filtering_.

# Daftar Pustaka
[1] Chun-Mei Li, Yi-han Mai, Pi Wey, Qi yan, Jiang jie teng, Dong shuo,"_Personalized Recommendation Algorithm for books and its
implementation_", Journal of Physics: Conference Series : IOP Publishing, 2020.[Online serial].Available: https://iopscience.iop.org/article/10.1088/1742-6596/1738/1/012053/pdf. [Accessed July. 17, 2023].

[2] Sarma Dhiman,Mittra Tanni ,Hossain Mohammad Shahadat, "_Personalized Book Recommendation System using Machine Learning Algorithm_", _(IJACSA) International Journal of Advanced Computer Science and Applications,
Vol. 12,No.1_2021.[Online serial].Available: https://pdfs.semanticscholar.org/d53f/32726dd28cd19a7b583712d33198561b7e09.pdf. [Accessed July. 17, 2023].
