SET GLOBAL FOREIGN_KEY_CHECKS=0;

CREATE SCHEMA db_lms;
use db_lms;

CREATE TABLE user (id_user INT AUTO_INCREMENT PRIMARY KEY, 
        u_name VARCHAR(255), 
        tgl_lahir DATE, 
        pekerjaan VARCHAR(255), 
        alamat VARCHAR(255));

CREATE TABLE book (id_buku INT AUTO_INCREMENT PRIMARY KEY, 
        nama_buku VARCHAR(255), 
        kategori VARCHAR(255), 
        stock INT);

INSERT INTO user VALUES(1000, 'Asraf', '1967-11-17', 'Petani', 'sukarajo');

INSERT INTO user VALUES(NOT NULL, 'Arief', '1967-12-17', 'Koki', 'sudirman');

INSERT INTO user VALUES(0 ,'Abay', '2000-12-11', 'Mahasiswa', 'Malang');

INSERT INTO book VALUES(1000, 'Python', 'Teknologi', 4);

CREATE TABLE peminjam (id_user INT PRIMARY KEY,
		id_buku INT,
        nama_user VARCHAR(255), 
        nama_buku VARCHAR(255), 
        tanggal_pinjam DATE,
        tanggal_pengembalian DATE);
	
select * from peminjam;