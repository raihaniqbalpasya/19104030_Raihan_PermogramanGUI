-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2021 at 05:36 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_diagnosispenyakit`
--

-- --------------------------------------------------------

--
-- Table structure for table `detailpenyakit`
--

CREATE TABLE `detailpenyakit` (
  `namaPenyakit` varchar(50) NOT NULL,
  `gejala` varchar(50) NOT NULL,
  `obat` varchar(50) NOT NULL,
  `metodePenyembuhan` varchar(500) NOT NULL,
  `keterangan` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `detailpenyakit`
--

INSERT INTO `detailpenyakit` (`namaPenyakit`, `gejala`, `obat`, `metodePenyembuhan`, `keterangan`) VALUES
('Covid-19', 'Demam', 'Vaksin Covid-19', 'Isolasi mandiri, Kondumsi obat-obatan yang disarankan dokter, Mengurangi aktifitas diluar rumah, Rajin mencuci tangan, dan Istirahat secukupnya.', 'Sejauh ini terapi untuk pasien yang mengalami virus korona hanya sebatas simptomatik. Artinya, terapi diberikan berdasarkan gejala. Jika panas diberikan antipiretik, jika pasien mengalami sesak nafas diberikan alat bantu nafas dan lain sebagainya.'),
('Covid-19', 'Batuk Kering', '', '', ''),
('Covid-19', 'Kelelahan', '', '', ''),
('Covid-19', 'Nyeri Tenggorokan', '', '', ''),
('Covid-19', 'Sakit Kepala', '', '', ''),
('Covid-19', 'Hilangnya indera perasa atau penciuman', '', '', ''),
('Covid-19', 'Kesulitan bernapas atau sesak napas', '', '', ''),
('Covid-19', 'Hilangnya kemampuan berbicara atau bergerak', '', '', ''),
('Tifus', 'Demam', 'Antibiotik dalam bentuk suntikan', 'Istirahat yang cukup, Makan teratur dengan porsi sedikit, Perbanyak minum air putih, Rajin mencuci tangan', 'Penyakit tifus merupakan penyakit kambuhan yang dapat kembali muncul dengan gejala yang sama. Umumnya, setelah perawatan medis dengan penggunaan antibiotik selesai, gejala dapat kembali muncul. Jangan khawatir, umumnya penyakit tifus kambuhan menyebabkan gejala yang lebih ringan dibandingkan dengan penyakit tifus yang pertama kali dialami.'),
('Tifus', 'Nyeri Otot', 'Infus cairan dan nutrisi', '', ''),
('Tifus', 'Sakit Kepala', '', '', ''),
('Tifus', 'Kelelahan', '', '', ''),
('Tifus', 'Batuk Kering', '', '', ''),
('Tifus', 'Sakit Perut', '', '', ''),
('Asam Lambung', 'Heartburn', 'Antasida', 'Makan dengan teratur, Hindari makanan tertentu, Perhatikan porsi makan, Berhenti merokok, Kunyah makanan dengan benar.', 'Asam lambung memiliki tingkat keasaman yang sangat kuat antara 1-3 pH. Pada tingkat keasaaman tersebut hampir kebanyakan benda yang masuk ke dalam perut dapat hancur termasuk misalnya saja benda yang terbuat dari metal.'),
('Asam Lambung', 'Mulut terasa asam atau pahit', 'H-2 receptor blockers', '', ''),
('Asam Lambung', 'Sakit tenggorokan', 'Proton pump inhibitors (PPI)', '', ''),
('Asam Lambung', 'Dispepsia', 'Amoxicillin', '', ''),
('Asam Lambung', 'Batuk kering', '', '', ''),
('Asam Lambung', 'Nyeri dada', '', '', ''),
('Asma', 'Batuk', 'Agonis reseptor beta-adrenergik dalam bentuk Inhal', 'Terapi pernafasan, Terapi obat-obatan herbal, Terapi yoga, Terapi renang, Akupuntur.', 'Faktor paling kuat yang menyebabkan serangan asma terjadi pada penderita asma adalah, tungau, debu, polusi, bulu hewan, serbuk sari, asap tembakau, dan jamur.'),
('Asma', 'Dada terasa sesak', 'Suntikan epinephrine', '', ''),
('Asma', 'Sesak nafas', 'Aminophylline melalui Infus Intravena', '', ''),
('Asma', 'Bengek', '', '', ''),
('Asma', 'Berkeringat', '', '', ''),
('Asma', 'Kesadaran menurun', '', '', ''),
('Asma', 'Sianosis (kulit tampak kebiruan)', '', '', ''),
('Bronkitis', 'Batuk berdahak', 'Aspirin atau Acetaminophen', 'Minum banyak cairan, Perbanyak istirahat, Hindari merokok atau Lingkungan dengan banyak perokok.', 'Sama-sama menyerang paru-paru, tapi bronkitis akut dan bronkitis kronis disebabkan oleh hal yang berbeda. Bronkitis akut biasanya disebabkan oleh virus penyebab pilek dan flu (influenza). Sedangkan penyebab paling umum dari bronkitis kronis adalah kebiasaan merokok, polusi udara, debu, atau gas beracun yang ada di lingkungan atau tempat kerja'),
('Bronkitis', 'Sesak nafas', 'Trimetoprim-sulfametoksazol', '', ''),
('Bronkitis', 'Infeksi pernafasan seperti flu', 'Tetracyclin atau Ampisilin', '', ''),
('Bronkitis', 'Bengek', 'Antibiotik', '', ''),
('Bronkitis', 'Kelelahan', '', '', ''),
('Bronkitis', 'Pembengkakan kaki', '', '', ''),
('Bronkitis', 'Pergelangan kaki dan tungkai', '', '', ''),
('Bronkitis', 'Pipi tampak kemerahan', '', '', ''),
('Bronkitis', 'Sakit kepala', '', '', ''),
('Bronkitis', 'Gangguan penglihatan', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `historiuser`
--

CREATE TABLE `historiuser` (
  `histori_cariGejala` varchar(50) NOT NULL,
  `histori_cekDetailPenyakit` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `penyakit`
--

CREATE TABLE `penyakit` (
  `namaPenyakit` varchar(50) NOT NULL,
  `IDPenyakit` char(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `penyakit`
--

INSERT INTO `penyakit` (`namaPenyakit`, `IDPenyakit`) VALUES
('Asam Lambung', 'AL002'),
('Asma', 'ASM003'),
('Bronkitis', 'BRNKTS004'),
('Covid-19', 'CVD19'),
('Tifus', 'TFS001');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `detailpenyakit`
--
ALTER TABLE `detailpenyakit`
  ADD KEY `detailPenyakit_fk0` (`namaPenyakit`);

--
-- Indexes for table `penyakit`
--
ALTER TABLE `penyakit`
  ADD PRIMARY KEY (`namaPenyakit`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `detailpenyakit`
--
ALTER TABLE `detailpenyakit`
  ADD CONSTRAINT `detailPenyakit_fk0` FOREIGN KEY (`namaPenyakit`) REFERENCES `penyakit` (`namaPenyakit`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
