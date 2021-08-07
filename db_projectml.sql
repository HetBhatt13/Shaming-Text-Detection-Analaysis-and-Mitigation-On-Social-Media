-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.5.19


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema db_projectml
--

CREATE DATABASE IF NOT EXISTS db_projectml;
USE db_projectml;

--
-- Definition of table `tbl_records`
--

DROP TABLE IF EXISTS `tbl_records`;
CREATE TABLE `tbl_records` (
  `rec_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userid` int(10) unsigned DEFAULT NULL,
  `text` varchar(1000) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `label` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `religious` varchar(45) NOT NULL,
  `abusive` varchar(45) NOT NULL,
  `comparative` varchar(45) NOT NULL,
  `passingjudgement` varchar(45) NOT NULL,
  PRIMARY KEY (`rec_id`),
  KEY `FK_PersonOrder` (`userid`),
  CONSTRAINT `FK_PersonOrder` FOREIGN KEY (`userid`) REFERENCES `tbl_users` (`usr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_records`
--

/*!40000 ALTER TABLE `tbl_records` DISABLE KEYS */;
INSERT INTO `tbl_records` (`rec_id`,`userid`,`text`,`label`,`religious`,`abusive`,`comparative`,`passingjudgement`) VALUES 
 (1,7,'it s no more shiv sena now its muslim sena balasaheb used to pray for lord shiva n\r\n','1','yes','no','yes','yes'),
 (2,7,'greed of oligarchs enemyofthepeople send us the money asap feed us hemp cannabis marijuana our food god\r\n','1','yes','no','no','no');
/*!40000 ALTER TABLE `tbl_records` ENABLE KEYS */;


--
-- Definition of table `tbl_users`
--

DROP TABLE IF EXISTS `tbl_users`;
CREATE TABLE `tbl_users` (
  `usr_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `usr_dateadded` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `usr_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `usr_email` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `usr_pass` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `usr_mobile` varchar(20) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `usr_counter` varchar(5) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`usr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_users`
--

/*!40000 ALTER TABLE `tbl_users` DISABLE KEYS */;
INSERT INTO `tbl_users` (`usr_id`,`usr_dateadded`,`usr_name`,`usr_email`,`usr_pass`,`usr_mobile`,`usr_counter`) VALUES 
 (2,'2021-03-24 16:48:51','Balchandra Samleti','balsamleti@gmail.com','qwerty','9175416700','1'),
 (3,'2021-03-24 17:40:40','sheela jadhav','jadhavsheela144@gmail.com','qwerty','9518522312','1'),
 (5,'2021-04-07 11:06:51','pramod','p@gmail.com','12345','07350706868','1'),
 (6,'2021-05-07 11:14:22','karan tailor','karan@gmail.com','karan123@','9890430022','1'),
 (7,'2021-06-01 18:27:36','mauli','mili@gmail.com','12345','9890430022','1');
/*!40000 ALTER TABLE `tbl_users` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
