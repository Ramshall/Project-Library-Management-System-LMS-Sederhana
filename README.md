# Project-Library-Management-System-LMS-Sederhana

Dalam repositori ini, terdapat beberapa file python yang digunakan di antaranya:
* main.py
* add_user.py
* add_book.py
* issue_book.py
* return_book
* search_book

Note: program utama berjalan di main.py dengan mengimport 5 packages yang masing-masing memiliki connector to sql beserta cursor. Selain itu, table pun sudah saya buat terpisah dari program di atas dengan nama 'db_lms' pada workbench saya. Database tersebut memiliki table dengan namanya (user, book, dan peminjam).

## add_user
pada packages ini terdapat class yang memiliki tiga fungsi:
1. Fungsi inisiasi: connector yang menghubungkan ke database yang saya buat 'db_lms'
2. Fungsi add_user: Diperintahkan untuk mengambil data, seperti name, tanggal_lahir, pkj (pekerjaan), dan almt (alamat) dari input yang dimasukkan user. Pada fungsi ini juga terdapat insiasi mycursor untuk mengeksekusi query yang saya buat
3. Fungsi  view_issue: Diperintahkan untuk menampilkan data user dengan query select dari table user yang disimpan pada variabel 'sql_query'. Kemudian, variabel tersebut dirubah menjadi Dataframe

## search_book
pada packages ini terdapat class yang memiliki dua fungsi:
1. Fungsi inisiasi: connector yang menghubungkan ke database yang saya buat 'db_lms'
2. Fungsi search_book: Diperintahkan untuk menampilkan data buku dari variabel 'book_name' yang diinput user kemudian dimasukian ke dalam query yang akan diekseusi menggunakan select dari table book yang disimpan pada variabel 'sql_query'. Kemudian, variabel tersebut dirubah menjadi Dataframe 

## issue_book
pada packages ini terdapat class yang memiliki tiga fungsi:
1. Fungsi inisiasi: connector yang menghubungkan ke database yang saya buat 'db_lms'
2. Fungsi issue_book: Diperintahkan untuk mengambil data, seperti id_peminjam, id_buku, nama_peminjam, dan nama_buku dari input yang dimasukkan. Pada fungsi ini juga terdapat insiasi mycursor untuk mengeksekusi query yang saya buat, yaitu sql_inset_query untuk insert value dan sql_query_update untuk update

note: terdapat dua variabel untuk memasukkan ke dalam query, yaitu begin_date dan end_date.
* begin_date: Dengan bantuan datetime mengamnggil data hari input yang ter-record
* end_date: Dengan bantuan timedelta dari packages datetime juga, akan melakukan pertambahan hari pada variabel begin_date

3. Fungsi  view_book: Diperintahkan untuk menampilkan data peminjaman dengan query select dari table peminjam yang disimpan pada variabel 'sql_query'. Kemudian, variabel tersebut dirubah menjadi Dataframe

## add_book
pada packages ini terdapat class yang memiliki tiga fungsi:
1. Fungsi inisiasi: connector yang menghubungkan ke database yang saya buat 'db_lms'
2. Fungsi add_book: Diperintahkan untuk mengambil data, seperti kode_buku, book_name, category, dan stock dari input yang dimasukkan. Pada fungsi ini juga terdapat insiasi mycursor untuk mengeksekusi query yang saya buat
3. Fungsi  view_book: Diperintahkan untuk menampilkan data buku dengan query select dari table book yang disimpan pada variabel 'sql_query'. Kemudian, variabel tersebut dirubah menjadi Dataframe

## return book
pada packages ini terdapat class yang memiliki tiga fungsi:
1. Fungsi inisiasi: connector yang menghubungkan ke database yang saya buat 'db_lms'
2. Fungsi return_book: Diperintahkan untuk mengambil data, seperti id_peminjam dan id_buku (id_book) dari input yang dimasukkan. Pada fungsi ini juga terdapat insiasi mycursor untuk mengeksekusi query yang saya buat, yaitu sql_query_peminjam (untuk delete data dari table peminjam menggunakan kondisi user) dan sql_query_book untuk update stock pada table book

## Perbaikan yang Dapat Dilakukan
1. Memisah connector dan cursor menjadi packages sendiri (note: connection_database tidak digunakan karena belum selesai terhambat waktu deadline pengerjaan)
2. Menambahkan defensive pada issue_book jika stock pada database < 1 akan error.
