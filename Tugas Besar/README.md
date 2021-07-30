# Diagnose.it
Aplikasi untuk diagnosis penyakit hanya dari rumah


## Kelompok NICE
1. Rafi Awang Bagaskoro  - 19104018
2. Raihan Iqbal Pasya    - 19104030
3. Nirmaya Dwi Utami     - 19104044
4. Rizki Delaga Prasetya - 19104074


## Latar Belakang
Di era yang modern seperti sekarang ini, semua orang menginginkan segala sesuatu yang simpel, mudah dan cepat. Baik dari segi transportasi, pembayaran, pendidikan, investasi bahkan sampai segi kesehatan. Apalagi dengan kondisi pandemi Covid-19 seperti sekarang ini, masyarakat sangat menghindari untuk keluar rumah jika tidak terlalu diperlukan, karena ketakutan akan tertular virus Covid-19 yang berbahaya. Maka dari itu banyak dari mereka hanya melakukan perawatan mandiri dirumah jika terkena penyakit yang kemungkinan dapat diobati dengan bahan-bahan alami (herbal) atau dengan obat-obatan yang biasa ditemui di apotek terdekat. Namun hal tersebut justru malah dapat berakibat fatal apabila kita mencoba untuk mendiagnosis sendiri penyakit yang kita alami tanpa bantuan ahli. Untuk itu, kami merancang sebuah aplikasi yang dapat digunakan untuk mendiagnosa penyakit yang anda alami dan dapat digunakan dengan mudah dan simpel, serta sudah mendapatkan persetujuan dari banyak dokter ternama di Indonesia, sehingga dapat digunakan secara bebas dan legal tanpa takut salah diagnosa atau salah obat.


## Deskripsi
Aplikasi **Diagnose.it** ini bertujuan untuk membantu masyarakat agar dapat mendiagnosa penyakit ringan yang mereka alami tanpa harus pergi ke rumah sakit dan mengeluarkan biaya yang cukup mahal hanya untuk memeriksa kondisi kesehatan mereka. Aplikasi ini memiliki fitur utama yang dapat membantu masyarakat dalam mendiagnosa sekaligus mengobati penyakit yang mereka alami, yaitu fitur diagnosa yang dapat digunakan untuk mendiagnosa penyakit yang mereka alami hanya dengan menginputkan gejala yang sedang dirasakan. Dan fitur tambahan yaitu fitur artikel yang dapat digunakan untuk melihat berbagai artikel atau berita terkini mengenai kesehatan sebagai referensi serta menambah pengetahuan dan informasi.

## Use Case Diagram
![UseCaseAplikasiDiagnose it](https://user-images.githubusercontent.com/72425333/127586180-92cb72ef-62f4-4b44-8e70-35f870c0b4ca.png)

## Desain Database
![image](https://user-images.githubusercontent.com/72425333/127528263-8a818fe2-da72-45bd-bb0b-c69c9a2f045c.png)

## Cara Penggunaan
* Saat membuka apliaksi, user akan langsung diarahkan ke Menu Utama
* Kemudian user dapat melakukan diagnosa dengan melihat petunjuk cara melakukan diagnosa pada Menu Utama, atau user dapat melakukan diagnosa sesuai dengan penjelasan berikut :
  * Pada Menu Utama, silahkan klik "**Diagnosis Sekarang**" untuk mulai melakukan diagnosa.
  * Setelah itu pengguna memilih gejala yang dialami, pada daftar gejala yang tersedia, kemudian klik "**Tambah Gejala**". 
  * **Pastikan gejala yang anda masukkan sesuai dengan gejala yang anda alami.**
  * Jika anda salah menginput gejala, anda dapat memilih gejala yang ingin anda hapus dan klik "**Hapus Gejala**" untuk menghapus gejala tersebut.
  * Jika gejala yang dialami sudah sesuai, silahkan klik "**Diagnosis Penyakit Sekarang**" untuk memulai mendiagnosis penyakit anda.
  * Setelah itu akan muncul Hasil Diagnosa atau daftar penyakit yang mungkin sedang anda alami.
  * **Penyakit teratas merupakan penyakit yang paling relevan dengan gejala yang anda alami**
  * User dapat melihat detail penyakit yang anda alami dengan memilih salah satu penyakit pada Hasil Diagnosis, lalu mengklik tombol "**Cek Detail**" untuk melihat Detail Penyakit.
  * Pada Detail Penyakit akan ditampilkan nama penyakit, gejala, obat, metode penyembuhan, dan keterangan dari penyakit yang anda pilih.
* User juga dapat melihat artikel seputar kesehatan pada Menu Utama dibagian Artikel Kesehatan Terbaru.

## Beberapa layout pada aplikasi Diagnose.it
#### 1. Menu Utama
![image](https://user-images.githubusercontent.com/72425333/127584682-3d93498d-c99c-4f36-a163-f2d8081a1523.png)

#### 2. Halaman Artikel
![image](https://user-images.githubusercontent.com/72425333/127525946-8da2770b-997b-4be5-97ab-42a593319350.png)

#### 3. Halaman Input Gejala
![image](https://user-images.githubusercontent.com/72425333/127526605-6afeed15-cb96-4cf5-a85f-0612ac069a61.png)

#### 4. Halaman Hasil Diagnosis
![image](https://user-images.githubusercontent.com/72425333/127527110-4ea75882-9944-4df2-811a-3dede1dd240f.png)

#### 5. Halaman Detail Penyakit
![image](https://user-images.githubusercontent.com/72425333/127527412-0a5e7cd5-6dfa-4667-8ecf-b228018c3f38.png)


## Beberapa Widget yang digunakan pada aplikasi Diagnose.it
* QMainWindow
* Qlabel       
* QPushButton 
* QComboBox    
* QListWidget 
* QTableWidget 
* QTabWidget   
* QFrame       
* QScrollArea
* QGroupBox

