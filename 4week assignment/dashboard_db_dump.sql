-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: dashboard_db
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `idx` int NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `content` text NOT NULL,
  `is_secret` tinyint(1) DEFAULT NULL,
  `post_password` varchar(30) DEFAULT NULL,
  `file_name` varchar(100) DEFAULT NULL,
  `user_name` varchar(30) NOT NULL,
  PRIMARY KEY (`idx`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'비밀글',' 비밀글',1,NULL,NULL,'1212'),(2,'ㄴㄴㄴ',' ㄴㄴㅇ',1,NULL,NULL,'1212'),(3,'ㅇ',' ㄹㅇ',1,NULL,NULL,'1212'),(4,'ㄹㄹㄹ',' ㅇㅇㅇㅇ',1,NULL,NULL,'1212'),(5,'이상',' ㅇㅇㅇㅇ',1,'1234',NULL,'1212'),(6,'장범준 노래 가',' ㅇㅇㄹㄹㄷㅇ',1,'1111','my_file.txt','1212'),(7,'ㅇㅇㄹ',' ㄷㄷㄹㄷㄷ',0,NULL,NULL,'1212'),(8,'fff',' fffddaafe',0,NULL,NULL,'3333'),(9,'ddf',' efdadsf',1,'1234','new_file.txt','3333'),(10,'비밀글 테스트',' 테스트 수정',1,'1234',NULL,'glider0'),(11,'ㅇㅇㅇㅇ',' ㅁㅁㅁㅁㅁㅁㅁ',0,NULL,NULL,'3333'),(12,'ㅇㄹㄹㄷ',' ㅇㅇㄹㄴㅇㅁ',1,'11111',NULL,'3333'),(13,'dd',' fff',0,NULL,NULL,'3333'),(14,'비밀글 씀',' 내용은 비밀',1,'1111',NULL,'3333'),(15,'ffe',' rgtgtg',1,'3333',NULL,'1212');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_info` (
  `user_id` varchar(30) NOT NULL,
  `user_pw` varchar(30) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `user_email` varchar(50) NOT NULL,
  `user_phonenum` varchar(30) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES ('1212','3434','5656','7878','9090'),('3333','4444','3456','12346','66iii'),('glider0','abc123','박병호','glider0@naver.com','01025675528');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-03 13:26:50
