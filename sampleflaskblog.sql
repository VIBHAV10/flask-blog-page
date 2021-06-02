-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2021 at 11:03 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sampleflaskblog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(10) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'vibhav10', '54546656', '6231', '2021-05-28 22:15:03', 'bvb@uefa.com'),
(2, 'vibhav10', '54546656', 'wsqs', '2021-05-29 10:35:36', 'bvb@uefa.com'),
(3, 'vibhav10', '54546656', 'wsqs', '2021-05-29 10:35:37', 'bvb@uefa.com'),
(4, 'vibhav10', '54546656', 'fwfwf', '2021-05-29 10:37:40', 'bvb@uefa.com'),
(5, 'vibhav10', '54546656', 'rtgrg', '2021-05-31 11:22:21', 'bvb@uefa.com'),
(6, 'vibhav10', '54546656', 'gtxm', '2021-05-31 11:58:34', 'bvb@uefa.com'),
(7, 'vibhav10', '23215135', 'hi', '2021-05-31 11:58:57', 'bvb@uefa.com'),
(8, 'suprit', '69696969', 'kat gaya', '2021-06-01 00:38:33', 'suprit'),
(9, 'vibhav10', '54546656', 'seghjyu.ukjheffghjl/kgf', '2021-06-01 20:10:05', 'bvb@uefa.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'First Post', 'Man must explore, and this is exploration at its greatest', 'parallel-clipper', 'frtlgnjgkrttrblgrfwbnngmgn ', 'clipper-bg.j', '2021-06-01 01:44:00'),
(2, 'Science and Prophecy ', 'We predict too much for the next year and yet far too little for the next ten.', 'science-prophecy', 'Many say exploration is part of our destiny, but it’s actually our duty to future generations', 'about-bg.jpg', '2021-05-29 18:39:03'),
(3, 'Android Studio', 'Full support for kotlin!', 'android-studio-support-fo', 'Android Studio provides full support for Kotlin, enabing you to add Kotlin files to your existing project and convert Java language code to Kotlin. You can then use all of Android Studio\'s existing tools with your Kotlin code, including autocomplete, lint checking, refactoring, debugging, and more.', '', '2021-05-29 20:40:02'),
(4, 'Variable', 'There are three main variables: independent variable, dependent variable and controlled variables.', 'variables', 'A variable is any factor, trait, or condition that can exist in differing amounts or types. An experiment usually has three kinds of variables: independent, dependent, and controlled. The independent variable is the one that is changed by the scientist.', 'home-bg.jpg', '2021-06-02 13:23:30'),
(5, 'positive parallel clipper', 'electronics', 'parallel-clipper', 'xcdsagjkl;kjf', 'clipper-bg.j', '2021-06-02 14:14:48');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
