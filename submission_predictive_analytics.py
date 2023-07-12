# -*- coding: utf-8 -*-
"""submission_predictive_analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EmPQbM14E6OpHTvtxoVUcHruuNn3wNdE

Langkah pertama adalah mengimport semua library yang dibutuhkan, numpy untuk memproses data numerik, matplotlib untuk membuat plot, pandas
untuk memproses data berbentuk dataframe (table), seaborn untuk visualisasi.
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

"""Menggunakan pandas untuk membaca file csv lalu mengubah data menjadi dataframe"""

from pandas.core.internals.managers import T
used_cars = pd.read_csv('/content/toyota.csv')
used_cars

"""Menggunakan fungsi info untuk mengetahui jenis variable(kolom), jumlah baris dan tipe data pada kolom tersebut."""

used_cars.info()

"""Menjalankan fungsi describe untuk mendapatkan ringkasan dari data, dan didapatkan nilai minimum 0 pada variabel tax dan enginesize, dan ini tidak sesuai dengan fakta karena tidak ada kendaraan yang engine sizenya 0."""

used_cars.describe()

"""Mengetahui banyak baris data yang bernilai 0 pada kolom tax dan engine size."""

tax = (used_cars.tax == 0).sum()
engineSize = (used_cars.engineSize == 0).sum()

print("Nilai 0 di kolom tax ada: ", tax)
print("Nilai 0 di kolom engineSize ada: ", engineSize)

"""Mendapatkan ringkasan data yang taxnya bernilai 0"""

used_cars.loc[(used_cars['tax']==0)]

"""Menghapus baris data yang memiliki nilai 0 karena kita tidak tahu alasan mengapa pajak bisa 0. Kita juga menghapus engine size 0 karena tidak sesuai dengan fakta."""

# Drop baris dengan nilai 'x', 'y', dan 'z' = 0
used_cars = used_cars.loc[(used_cars[['engineSize','tax']]!=0).all(axis=1)]

# Cek ukuran data untuk memastikan baris sudah di-drop
used_cars.shape

"""Menampilkan ringkasan data setelah menghapus data yang tax dan engine sizenya 0. Tidak didapatkan lagi nilai minimum 0."""

used_cars.describe()

"""Menampilkan data outliers dengan menggunakan metode IQR pada variabel year."""

sns.boxplot(x=used_cars['year'])

"""Menampilkan data outliers dengan menggunakan metode IQR pada variabel engine size."""

sns.boxplot(x=used_cars['engineSize'])

"""Menghapus data yang keluar dari IQR"""

Q1 = used_cars.quantile(0.25)
Q3 = used_cars.quantile(0.75)
IQR=Q3-Q1
used_cars=used_cars[~((used_cars<(Q1-1.5*IQR))|(used_cars>(Q3+1.5*IQR))).any(axis=1)]

# Cek ukuran dataset setelah kita drop outliers
used_cars.shape

"""Membagi variabel numerik dan variabel kategori."""

numerical_features = ['year', 'price', 'mileage', 'tax', 'mpg', 'engineSize']
categorical_features = ['model', 'transmission', 'fuelType']

"""Menampilkan persentase dan diagram pada variabel model"""

feature = categorical_features[0]
count = used_cars[feature].value_counts()
percent = 100*used_cars[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Menampilkan persentase dan diagram pada variabel transmission."""

feature = categorical_features[1]
count = used_cars[feature].value_counts()
percent = 100*used_cars[feature].value_counts(normalize=True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

"""Menampilkan diagram pada variabel bertipe numerik."""

used_cars.hist(bins=50, figsize=(20,15))
plt.show()

"""Menampilkan rata-rata price pada variabel kategori"""

cat_features = used_cars.select_dtypes(include='object').columns.to_list()

for col in cat_features:
  sns.catplot(x=col, y="price", kind="bar", dodge=False, height = 4, aspect = 3,  data=used_cars, palette="Set3")
  plt.title("Rata-rata 'price' Relatif terhadap - {}".format(col))

"""Mengamati hubungan antar variabel numerik"""

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(used_cars, diag_kind = 'kde')

"""Menampilkan hubungan/korelasi pada setiap variabel"""

plt.figure(figsize=(10, 8))
correlation_matrix = used_cars.corr().round(2)

# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )

"""Menghapus variabel yang tidak memiliki hubungan yang tinggi dengan variabel pricel"""

used_cars.drop(['model','mileage','tax','mpg'], inplace=True, axis=1)
used_cars.head()

"""Mengubah variabel kategorikal menjadi variabel numerik agar bisa diproses oleh algoritma."""

from sklearn.preprocessing import  OneHotEncoder
used_cars = pd.concat([used_cars, pd.get_dummies(used_cars['transmission'], prefix='transmission')],axis=1)
used_cars = pd.concat([used_cars, pd.get_dummies(used_cars['fuelType'], prefix='fuelType')],axis=1)
used_cars.drop(['transmission', 'fuelType'], axis=1, inplace=True)
used_cars.head()

"""Membagi data menjadi 2 bagian, data latih dan data uji dengan persentase 90% data latih dan 10% data uji."""

from sklearn.model_selection import train_test_split

X = used_cars.drop(["price"],axis =1)
y = used_cars["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

"""Menampilkan banyak baris data setelah dibagi menajadi 2"""

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""Mengubah skala data agar memiliki performa lebih baik, dengan mengubah mean menjadi 0 dan standar deviasi 1."""

from sklearn.preprocessing import StandardScaler

numerical_features = ['year','engineSize']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

"""Menampilkan mean 0 dan standar deviasi 1."""

X_train[numerical_features].describe().round(4)

"""Menyiapkan data untuk dianalisis, menetapkan variabel model dan metrik evaluasi."""

# Siapkan dataframe untuk analisis model
models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['KNN', 'RandomForest', 'Boosting'])

"""Melatih data menggunakan algoritma KNN"""

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(n_neighbors=100)
knn.fit(X_train, y_train)

models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""Melatih data menggunakan random forest"""

# Impor library yang dibutuhkan
from sklearn.ensemble import RandomForestRegressor

# buat model prediksi
RF = RandomForestRegressor(n_estimators=55, max_depth=16, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""Melatih data menggunakan algoritma adaboost"""

from sklearn.ensemble import AdaBoostRegressor

boosting = AdaBoostRegressor(learning_rate=0.02, random_state=30)
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""Melakukan scaling pada data uji"""

# Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1
X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

"""Membuat variabel mse untuk masing-masing data latih dan data uji pada setiap algoritma"""

# Buat variabel mse yang isinya adalah dataframe nilai mse data train dan test pada masing-masing algoritma
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])

# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}

# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3

# Panggil mse
mse

"""Menampilkan visualisasi nilai mse pada data latih dan data uji pada setiap algoritma."""

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Menggunakan model terbaik untuk memprediksi harga."""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

pd.DataFrame(pred_dict)