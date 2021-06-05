-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 23, 2021 at 05:59 AM
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
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `id` int(11) NOT NULL,
  `jenis` varchar(255) NOT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `varian` varchar(255) DEFAULT NULL,
  `warna` varchar(255) DEFAULT NULL,
  `harga` int(11) NOT NULL,
  `modal` int(11) NOT NULL,
  `stok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`id`, `jenis`, `brand`, `varian`, `warna`, `harga`, `modal`, `stok`) VALUES
(1, 'Joran', 'Charm', 'Black Bass', 'Hijau', 290000, 210000, 2),
(2, 'Joran', 'Kaizen', 'Chery', 'Hijau', 175000, 100000, 1),
(3, 'Joran', 'Kaizen', 'Isamu', 'Ungu', 135000, 70000, 2),
(4, 'Joran', 'Ouster', 'Power Solid', 'Ungu', 135000, 70000, 0),
(6, 'Joran', 'Swan', 'Super Prawn', 'Putih', 90000, 50000, 2),
(7, 'Joran', 'Maguro', 'Blue River', 'Biru', 135000, 70000, 1),
(15, 'Joran', 'Koinobori', 'NIKKI', 'Merah', 70000, 35000, 1),
(17, 'Joran', 'Golden', 'Surf', 'Hitam', 115000, 45000, 5),
(18, 'Joran', 'Power Rod', 'NEW', 'Hitam', 115000, 60000, 3),
(20, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 123),
(21, 'Hook', 'Owner', 'Carbon', 'Putih', 30000, 21000, 41),
(25, 'Hook', 'Kaizen', 'Carbon', 'Silver', 9000, 5100, 100),
(27, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 4000, 1900, 38),
(28, 'Hook', 'Carbon', 'Plus', 'Biru', 7000, 4600, 25),
(30, 'Reel', 'Daido', 'Plastik', 'Putih', 40000, 23000, 8),
(31, 'Joran', 'Bamboo', 'Katana', 'Gold', 85000, 45000, 2),
(32, 'Joran', 'Ouster', 'Rocket', 'Biru', 80000, 40000, 3),
(33, 'Bundle', 'Pioneer', 'Paket 1', 'Merah', 190000, 125000, 3),
(34, 'Bundle', 'Pioneer', 'Paket 2', 'Biru', 135000, 70000, 2),
(35, 'Hook', 'Charm', 'Carbon', 'Hitam', 9000, 4100, 213),
(36, 'Hook', 'Carbon', 'Mix', 'Hitam', 9000, 4100, 136),
(37, 'Snap', 'Daido', 'Fastlock', 'Hitam', 10000, 5000, 21),
(38, 'Snap', 'Pioneer', 'Hooks-Snap', 'Hitam', 10000, 5000, 18),
(39, 'Kili-Kili', 'Pro - Katsu', '3 Mata', 'Putih', 4000, 4000, 16),
(40, 'Kili-Kili', 'Pro - katsu', '2 Mata', 'Hitam', 4000, 4000, 40),
(41, 'Stopper', 'Pioneer', 'M (2)', 'Kuning', 8000, 4000, 40),
(42, 'Kili-Kili', 'Golden Glake', '2 Mata', 'Silver', 4000, 4000, 39),
(43, 'Senar', 'Penyu', 'Nylon', 'Putih', 20000, 12000, 1),
(44, 'Senar', 'Trumph', 'PE', 'Biru', 35000, 20000, 15),
(45, 'Senar', 'Penyu', 'Nylon', 'Biru', 20000, 12000, 5),
(46, 'Senar', 'Trumph', 'PE', 'Pink', 35000, 20000, 13),
(47, 'Reel', 'Kaizen', 'Gin 4000', 'Silver', 180000, 120000, 1),
(48, 'Reel', 'Pioneer', 'Sky Hawk 4000', 'Silver', 165000, 120000, 3);

-- --------------------------------------------------------

--
-- Table structure for table `costumers`
--

CREATE TABLE `costumers` (
  `id` int(11) NOT NULL,
  `first_name` varchar(128) NOT NULL,
  `last_name` varchar(128) NOT NULL,
  `address` varchar(255) NOT NULL,
  `email` varchar(128) NOT NULL,
  `phone_number` varchar(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `costumers`
--

INSERT INTO `costumers` (`id`, `first_name`, `last_name`, `address`, `email`, `phone_number`) VALUES
(16, 'Yanuar', 'Satria', 'Samarinda', 'yanuarsatria88@gmail.com', '+62 812-4074-1502'),
(18, 'Daffa', 'Putra', 'Samarinda', 'daffapm.21@gmail.com', '+62 812-4074-1502'),
(19, 'Risky', 'Kurniawan', 'Kutai Kartanegara', 'riskykurniawan945@gmail.com', '+62 821 5831-7722');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `order_number` int(11) NOT NULL,
  `costumer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `order_number`, `costumer_id`, `product_id`) VALUES
(1, 4362, 1, 1),
(2, 4223, 2, 21);

-- --------------------------------------------------------

--
-- Table structure for table `terjual`
--

CREATE TABLE `terjual` (
  `id` int(11) NOT NULL,
  `jenis` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `varian` varchar(255) NOT NULL,
  `warna` varchar(255) NOT NULL,
  `harga` int(11) NOT NULL,
  `modal` int(11) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `date` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `terjual`
--

INSERT INTO `terjual` (`id`, `jenis`, `brand`, `varian`, `warna`, `harga`, `modal`, `jumlah`, `date`) VALUES
(1, 'Joran', 'Kaizen', 'Chery', 'Hijau', 175000, 100000, 1, '2021-01-21-23:39:54'),
(2, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 6000, 3800, 2, '2021-01-21-23:24:54'),
(3, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-02-21-23:39:54'),
(4, 'Joran', 'Kaizen', 'Isamu', 'Ungu', 270000, 140000, 2, '2021-02-21-23:45:21'),
(5, 'Joran', 'Koinobori', 'NIKKI', 'Merah', 140000, 70000, 2, '2021-02-21-23:46:14'),
(6, 'Hook', 'Owner', 'Carbon', 'Putih', 120000, 84000, 4, '2021-03-22-00:09:20'),
(7, 'Reel', 'Daido', 'Plastik', 'Putih', 46000, 80000, 2, '2021-03-22-00:18:59'),
(8, 'Reel', 'Daido', 'Plastik', 'Putih', 160000, 92000, 4, '2021-03-22-00:21:04'),
(9, 'Reel', 'Pioneer', 'Sky Hawk 4000', 'Silver', 165000, 120000, 1, '2021-04-22-11:14:03'),
(10, 'Reel', 'Kaizen', 'Gin 4000', 'Silver', 180000, 120000, 1, '2021-04-22-11:14:03'),
(11, 'Bundle', 'Pioneer', 'Paket 1', 'Merah', 190000, 125000, 1, '2021-04-22-11:14:03'),
(12, 'Kili-Kili', 'Pro - Katsu', '3 Mata', 'Putih', 160000, 80000, 20, '2021-04-22-11:15:34'),
(13, 'Snap', 'Daido', 'Fastlock', 'Hitam', 40000, 20000, 4, '2021-04-22-11:16:10'),
(14, 'Senar', 'Penyu', 'Nylon', 'Putih', 80000, 48000, 4, '2021-04-22-11:16:10'),
(15, 'Senar', 'Trumph', 'PE', 'Pink', 70000, 40000, 2, '2021-04-22-11:16:10'),
(16, 'Reel', 'Daido', 'Plastik', 'Putih', 120000, 69000, 3, '2021-04-22-11:16:48'),
(17, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-04-23-13:44:03'),
(18, 'Hook', 'Carbon', 'Mix', 'Hitam', 16000, 8200, 2, '2021-04-23-15:21:59'),
(19, 'Hook', 'Carbon', 'Mix', 'Hitam', 16000, 8200, 2, '2021-04-23-15:21:59'),
(20, 'Hook', 'Carbon', 'Mix', 'Hitam', 16000, 8200, 2, '2021-04-23-15:21:59'),
(21, 'Hook', 'Carbon', 'Mix', 'Hitam', 16000, 8200, 2, '2021-04-23-15:21:59'),
(22, 'Hook', 'Carbon', 'Mix', 'Hitam', 16000, 8200, 2, '2021-04-23-15:23:16'),
(23, 'Hook', 'Carbon', 'Plus', 'Biru', 7000, 4600, 1, '2021-04-23-15:23:16'),
(24, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-23-15:24:56'),
(25, 'Hook', 'Charm', 'Carbon', 'Hitam', 8000, 4100, 1, '2021-04-23-15:26:01'),
(26, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-23-15:29:52'),
(27, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-23-15:29:52'),
(28, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-23-15:29:52'),
(29, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-23-15:29:52'),
(30, 'Hook', 'Charm', 'Carbon', 'Hitam', 8000, 4100, 1, '2021-04-23-15:30:09'),
(31, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-15:30:09'),
(32, 'Kili-Kili', 'Pro - Katsu', '3 Mata', 'Putih', 8000, 4000, 1, '2021-04-23-15:30:09'),
(33, 'Hook', 'Charm', 'Carbon', 'Hitam', 8000, 4100, 1, '2021-04-23-15:30:34'),
(34, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-15:30:34'),
(35, 'Kili-Kili', 'Pro - Katsu', '3 Mata', 'Putih', 8000, 4000, 1, '2021-04-23-15:30:34'),
(36, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-15:35:06'),
(37, 'Hook', 'Charm', 'Carbon', 'Hitam', 8000, 4100, 1, '2021-04-23-15:35:06'),
(38, 'Kili-Kili', 'Pro - Katsu', '3 Mata', 'Putih', 8000, 4000, 1, '2021-04-23-15:35:06'),
(39, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-23-17:21:01'),
(40, 'Hook', 'Charm', 'Carbon', 'Hitam', 8000, 4100, 1, '2021-04-23-17:23:01'),
(41, 'Hook', 'Carbon', 'Mix', 'Hitam', 40000, 20500, 5, '2021-04-23-17:43:22'),
(42, 'Joran', 'Charm', 'Black Bass', 'Hijau', 290000, 210000, 1, '2021-04-23-17:44:20'),
(43, 'Hook', 'Carbon', 'Mix', 'Hitam', 88000, 45100, 11, '2021-04-23-17:44:51'),
(44, 'Hook', 'Carbon', 'Mix', 'Hitam', 72000, 36900, 9, '2021-04-23-17:46:40'),
(45, 'Hook', 'Sigma', 'Carbon', 'Kuning', 76000, 38000, 19, '2021-04-23-17:50:40'),
(46, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-23-17:51:00'),
(47, 'Hook', 'Charm', 'Carbon', 'Hitam', 8000, 4100, 1, '2021-04-23-17:51:22'),
(48, 'Hook', 'Charm', 'Carbon', 'Hitam', 16000, 8200, 2, '2021-04-23-20:51:41'),
(49, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-20:56:34'),
(50, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-21:00:17'),
(51, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-21:11:50'),
(52, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-21:12:50'),
(53, 'Hook', 'Sigma', 'Carbon', 'Kuning', 20000, 10000, 5, '2021-04-23-21:12:50'),
(54, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-04-23-21:14:00'),
(55, 'Hook', 'Carbon', 'Mix', 'Hitam', 32000, 16400, 4, '2021-04-23-21:14:00'),
(56, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-04-23-21:37:42'),
(57, 'Hook', 'Carbon', 'Mix', 'Hitam', 32000, 16400, 4, '2021-04-23-21:39:46'),
(58, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-21:40:11'),
(59, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-23-21:40:49'),
(60, 'Hook', 'Charm', 'Carbon', 'Hitam', 16000, 8200, 2, '2021-04-23-21:43:43'),
(61, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-23-21:53:41'),
(62, 'Kili-Kili', 'Pro - Katsu', '3 Mata', 'Putih', 8000, 4000, 1, '2021-04-23-21:54:44'),
(63, 'Joran', 'Ouster', 'Power Solid', 'Ungu', 135000, 70000, 1, '2021-04-23-22:05:46'),
(64, 'Hook', 'Sigma', 'Carbon', 'Kuning', 20000, 10000, 5, '2021-04-23-22:05:46'),
(65, 'Hook', 'Carbon', 'Mix', 'Hitam', 16000, 8200, 2, '2021-04-23-22:05:46'),
(66, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 12000, 7600, 4, '2021-04-25-19:25:12'),
(67, 'Hook', 'Charm', 'Carbon', 'Hitam', 40000, 20500, 5, '2021-04-25-19:25:12'),
(68, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-04-25-19:25:12'),
(69, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-19:26:46'),
(70, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 9000, 5700, 3, '2021-04-25-19:27:46'),
(71, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 6000, 3800, 2, '2021-04-25-19:27:46'),
(72, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 9000, 5700, 3, '2021-04-25-19:27:46'),
(73, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-19:30:18'),
(74, 'Hook', 'Carbon', 'Plus', 'Biru', 14000, 9200, 2, '2021-04-25-19:30:18'),
(75, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-25-20:38:18'),
(76, 'Hook', 'Charm', 'Carbon', 'Hitam', 40000, 20500, 5, '2021-04-25-20:38:18'),
(77, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:48:20'),
(78, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:49:59'),
(79, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:51:29'),
(80, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:52:57'),
(81, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:54:39'),
(82, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-20:55:09'),
(83, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-20:55:09'),
(84, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:55:55'),
(85, 'Hook', 'Sigma', 'Carbon', 'Kuning', 20000, 10000, 5, '2021-04-25-20:55:55'),
(86, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:57:55'),
(87, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-04-25-20:57:55'),
(88, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:59:14'),
(89, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-25-20:59:14'),
(90, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-20:59:57'),
(91, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-21:08:50'),
(92, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 75000, 47500, 25, '2021-04-25-21:09:05'),
(93, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-21:11:48'),
(94, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-21:16:17'),
(95, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-21:18:12'),
(96, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-04-25-21:18:12'),
(97, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-21:22:58'),
(98, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-21:24:02'),
(99, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-21:28:33'),
(100, 'Hook', 'Sigma', 'Carbon', 'Kuning', 20000, 10000, 5, '2021-04-25-21:28:33'),
(101, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-25-21:29:20'),
(102, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 6000, 3800, 2, '2021-04-25-21:29:20'),
(103, 'Hook', 'Carbon', 'Plus', 'Biru', 7000, 4600, 1, '2021-04-25-21:29:20'),
(104, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-21:30:28'),
(105, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-21:34:46'),
(106, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-04-25-21:34:46'),
(107, 'Hook', 'Carbon', 'Plus', 'Biru', 7000, 4600, 1, '2021-04-25-21:34:46'),
(108, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-25-21:42:07'),
(109, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-25-21:42:07'),
(110, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-21:43:58'),
(111, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 3000, 1900, 1, '2021-04-25-21:44:39'),
(112, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 9000, 5700, 3, '2021-04-25-21:45:00'),
(113, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-25-21:45:25'),
(114, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 15000, 9500, 5, '2021-04-26-00:23:36'),
(115, 'Hook', 'Carbon', 'Plus', 'Biru', 14000, 9200, 2, '2021-04-26-00:23:36'),
(116, 'Hook', 'Carbon', 'Mix', 'Hitam', 80000, 41000, 10, '2021-04-26-00:23:36'),
(117, 'Hook', 'Carbon', 'Plus', 'Biru', 14000, 9200, 2, '2021-04-26-00:27:13'),
(118, 'Hook', 'Charm', 'Carbon', 'Hitam', 40000, 20500, 5, '2021-04-26-00:27:13'),
(119, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-04-26-00:27:13'),
(120, 'Hook', 'Carbon', 'Mix', 'Hitam', 8000, 4100, 1, '2021-04-26-00:27:13'),
(121, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 9000, 5700, 3, '2021-04-26-20:57:39'),
(122, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 12000, 7600, 4, '2021-04-26-20:57:39'),
(123, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 9000, 5700, 3, '2021-04-28-13:54:50'),
(124, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 6000, 3800, 2, '2021-04-30-10:15:07'),
(125, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 6000, 3800, 2, '2021-04-30-10:15:07'),
(126, 'Hook', 'Sigma', 'Carbon', 'Kuning', 20000, 10000, 5, '2021-04-30-11:06:51'),
(127, 'Hook', 'Charm', 'Carbon', 'Hitam', 20000, 20500, 5, '2021-04-30-11:06:51'),
(128, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 20000, 9500, 5, '2021-05-05-16:59:37'),
(129, 'Kili-Kili', 'Golden Glake', '2 Mata', 'Silver', 4000, 4000, 1, '2021-05-05-16:59:37'),
(130, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-05-08-23:24:46'),
(131, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-05-08-23:26:09'),
(132, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 12000, 5700, 3, '2021-05-08-23:26:09'),
(133, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-05-08-23:27:15'),
(134, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 12000, 5700, 3, '2021-05-08-23:27:15'),
(135, 'Hook', 'Charm', 'Carbon', 'Hitam', 8000, 8200, 2, '2021-05-08-23:28:02'),
(136, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 12000, 5700, 3, '2021-05-08-23:28:02'),
(137, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-05-08-23:28:02'),
(138, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-05-08-23:28:50'),
(139, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-05-08-23:28:50'),
(140, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-05-08-23:28:50'),
(141, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-05-08-23:28:50'),
(142, 'Hook', 'Sigma', 'Carbon', 'Kuning', 128000, 64000, 32, '2021-05-08-23:42:04'),
(143, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 4000, 1900, 1, '2021-05-08-23:44:18'),
(144, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-05-08-23:46:43'),
(145, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-05-08-23:47:34'),
(146, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-05-08-23:47:34'),
(147, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-05-08-23:48:01'),
(148, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 12000, 5700, 3, '2021-05-08-23:48:01'),
(149, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-05-08-23:50:37'),
(150, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-05-08-23:50:37'),
(151, 'Hook', 'Charm', 'Carbon', 'Hitam', 4000, 4100, 1, '2021-05-08-23:50:37'),
(152, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-05-08-23:55:43'),
(153, 'Hook', 'Audrey', 'Carbon', 'Darkgrey', 4000, 1900, 1, '2021-05-08-23:55:43'),
(154, 'Hook', 'Charm', 'Carbon', 'Hitam', 16000, 16400, 4, '2021-05-08-23:55:43'),
(155, 'Hook', 'Sigma', 'Carbon', 'Kuning', 12000, 6000, 3, '2021-05-11-13:32:47'),
(156, 'Hook', 'Sigma', 'Carbon', 'Kuning', 8000, 4000, 2, '2021-05-11-13:32:47'),
(157, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-05-11-13:32:47'),
(158, 'Hook', 'Sigma', 'Carbon', 'Kuning', 20000, 10000, 5, '2021-05-11-14:33:12'),
(159, 'Hook', 'Sigma', 'Carbon', 'Kuning', 20000, 10000, 5, '2021-05-11-14:34:07'),
(160, 'Hook', 'Sigma', 'Carbon', 'Kuning', 4000, 2000, 1, '2021-05-23-11:02:05');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `costumers`
--
ALTER TABLE `costumers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD KEY `costumer_id` (`costumer_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `terjual`
--
ALTER TABLE `terjual`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `barang`
--
ALTER TABLE `barang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `costumers`
--
ALTER TABLE `costumers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `terjual`
--
ALTER TABLE `terjual`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=161;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`costumer_id`) REFERENCES `costumers` (`id`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `barang` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
