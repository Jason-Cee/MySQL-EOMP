-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: Lifechoices_Online
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Login`
--

DROP TABLE IF EXISTS `Login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Login` (
  `Name` varchar(50) NOT NULL,
  `Id_Number` varchar(13) NOT NULL,
  `Phone_Number` int DEFAULT NULL,
  `Email_Address` varchar(50) NOT NULL,
  `Time_in` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Time_out` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Id_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Login`
--

LOCK TABLES `Login` WRITE;
/*!40000 ALTER TABLE `Login` DISABLE KEYS */;
INSERT INTO `Login` VALUES ('Jason Calvert','9804075027081',762562346,'jasondoescoding@gmail.com','2021-07-10 14:37:25','2021-07-10 18:09:07'),('Jason Calvert','9804075027082',762562346,'jasondoescoding@gmail.com','2021-07-10 14:37:25','2021-07-10 18:09:07'),('Julian Jeffries','9865321234567',1234567891,'julian@gmail.com','2021-07-10 14:37:25','2021-07-10 18:09:07'),('Yamkela Effort','9912021234567',1234567890,'yamaklea@gmail.com','2021-07-10 14:37:25','2021-07-10 18:09:07'),('test','test',1234,'test','2021-07-10 14:37:25','2021-07-10 18:09:07'),('TEST1','TEST1',123456789,'TEST1','2021-07-10 14:37:25','2021-07-10 18:09:07');
/*!40000 ALTER TABLE `Login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Next_Of_Kin`
--

DROP TABLE IF EXISTS `Next_Of_Kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Next_Of_Kin` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Phone_Number` int NOT NULL,
  `Id_Number` varchar(13) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `Id_Number` (`Id_Number`),
  CONSTRAINT `Next_Of_Kin_ibfk_1` FOREIGN KEY (`Id_Number`) REFERENCES `Login` (`Id_Number`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Next_Of_Kin`
--

LOCK TABLES `Next_Of_Kin` WRITE;
/*!40000 ALTER TABLE `Next_Of_Kin` DISABLE KEYS */;
INSERT INTO `Next_Of_Kin` VALUES (1,'Mufasa Jardien',789632581,'9912021234567'),(2,'Jason Abrahams',670202665,'9912021234567'),(3,'test',123456,'test'),(4,'TEST1',123,'TEST1');
/*!40000 ALTER TABLE `Next_Of_Kin` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-11 11:31:51
