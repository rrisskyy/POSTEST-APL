-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2021 at 09:57 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `toko-pancing`
--

-- --------------------------------------------------------

--
-- Table structure for table `tokopancing`
--

CREATE TABLE `tokopancing` (
  `id` int(11) NOT NULL,
  `jenis` varchar(255) NOT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `varian` varchar(255) DEFAULT NULL,
  `warna` varchar(255) DEFAULT NULL,
  `harga` int(11) NOT NULL,
  `stok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tokopancing`
--

INSERT INTO `tokopancing` (`id`, `jenis`, `brand`, `varian`, `warna`, `harga`, `stok`) VALUES
(1, 'Joran', 'Charm', 'Black Bass', 'Hijau', 290000, 3),
(2, 'Joran', 'Kaizen', 'Chery', 'Hijau', 175000, 1),
(3, 'Joran', 'Kaizen', 'Isamu', 'Ungu', 135000, 2),
(4, 'Joran', 'Ouster', 'Power Solid', 'Ungu', 135000, 1),
(5, 'Joran', 'Kaizen', 'Chiyo', 'Hijau', 100000, 3),
(6, 'Joran', 'Swan', 'Super Prawn', 'Putih', 85000, 5),
(7, 'Joran', 'Maguro', 'Blue River', 'Biru', 135000, 1),
(15, 'Joran', 'Koinobori', 'NIKKI', 'Merah', 70000, 3),
(17, 'Joran', 'Golden', 'Surf', 'Hitam', 115000, 5),
(18, 'Joran', 'Power Rod', 'NEW', 'Hitam', 115000, 3),
(20, 'Hook', 'Sigma', 'Carbon', 'Kuning', 3000, 34),
(21, 'Hook', 'Owner', 'Carbon', 'Putih', 30000, 45),
(22, 'Joran', 'Bamboo', 'Bamboo', 'Hitam', 85000, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tokopancing`
--
ALTER TABLE `tokopancing`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tokopancing`
--
ALTER TABLE `tokopancing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
