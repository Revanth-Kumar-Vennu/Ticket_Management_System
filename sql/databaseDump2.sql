CREATE DATABASE  IF NOT EXISTS `ticketmanagementsystem` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ticketmanagementsystem`;
-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (x86_64)
--
-- Host: localhost    Database: ticketmanagementsystem
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `change_ticket`
--

DROP TABLE IF EXISTS `change_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `change_ticket` (
  `ticket_id` varchar(20) NOT NULL,
  `description` varchar(20) NOT NULL,
  `start_date` date NOT NULL,
  `status` enum('Open','In Progress','Closed') DEFAULT NULL,
  `priority` enum('P1','P2','P3','P4') DEFAULT NULL,
  `sprint_id` int NOT NULL,
  `created_by` int NOT NULL,
  `acceptor` int NOT NULL,
  `implementor` int NOT NULL,
  PRIMARY KEY (`ticket_id`),
  KEY `fk_change_sprint` (`sprint_id`),
  KEY `fk_change_emp` (`created_by`),
  KEY `fk_change_emp_accept` (`acceptor`),
  KEY `fk_change_emp_implement` (`implementor`),
  CONSTRAINT `fk_change_emp` FOREIGN KEY (`created_by`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_change_emp_accept` FOREIGN KEY (`acceptor`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_change_emp_implement` FOREIGN KEY (`implementor`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_change_sprint` FOREIGN KEY (`sprint_id`) REFERENCES `sprint` (`sprint_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `change_ticket`
--

LOCK TABLES `change_ticket` WRITE;
/*!40000 ALTER TABLE `change_ticket` DISABLE KEYS */;
INSERT INTO `change_ticket` VALUES ('CHG12348','Database change','2022-01-10','Open','P1',7,1,5,5),('CHG12349','DS change','2021-01-09','Closed','P1',6,2,4,4),('CHG134','ABC','2022-11-05','Open','P1',1,1,1,1),('CHG22345','AWS change','2020-05-10','Open','P1',1,2,1,1),('CHG22346','Azure change','2020-04-09','In Progress','P2',2,1,2,2),('CHG22347','Oracle change table','2019-01-10','Closed','P3',5,4,3,3);
/*!40000 ALTER TABLE `change_ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `emp_id` int NOT NULL,
  `team_id` int NOT NULL,
  `emp_name` varchar(20) NOT NULL,
  `date_of_birth` date NOT NULL,
  `sex` enum('Male','Female','Other') DEFAULT NULL,
  `address_street_name` varchar(20) DEFAULT NULL,
  `address_street_number` varchar(20) DEFAULT NULL,
  `address_zipcode` varchar(20) DEFAULT NULL,
  `address_city` varchar(20) DEFAULT NULL,
  `address_state` varchar(20) DEFAULT NULL,
  `phone_number` varchar(15) DEFAULT NULL,
  `joining_date` date DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
  KEY `fk_employee_team` (`team_id`),
  CONSTRAINT `fk_employee_team` FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,1,'Adam Heath','1994-05-04','Male','Mark Street','2','02130','Boston','Massachusetts','8576451235','2020-10-11'),(2,1,'Ben Foakes','1999-03-08','Male','Day Street','3','02130','Boston','Massachusetts','8576451548','2021-12-11'),(3,2,'Alisha','2000-05-09','Female','Hitech City','8','500045','Hyderabad','Telangana','8523003092','2021-09-11'),(4,3,'Christy Jones','1988-05-02','Female','Hogward Street','2','03140','New York City','New York','7569821310','2008-10-11'),(5,4,'Sam Harper','1990-04-04','Male','Dunk Street','5','21304','Dallas','Texas','8574123452','2012-10-11'),(123,1,'Deril','2022-11-11','Male','1','2','2','2','3','9999999999','2022-11-24');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incident_ticket`
--

DROP TABLE IF EXISTS `incident_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incident_ticket` (
  `ticket_id` varchar(50) NOT NULL,
  `description` varchar(20) NOT NULL,
  `start_date` date NOT NULL,
  `status` enum('Open','In Progress','Closed') DEFAULT NULL,
  `priority` enum('P1','P2','P3','P4') DEFAULT NULL,
  `sprint_id` int NOT NULL,
  `created_by` int NOT NULL,
  PRIMARY KEY (`ticket_id`),
  KEY `fk_incident_sprint` (`sprint_id`),
  KEY `fk_incident_emp` (`created_by`),
  CONSTRAINT `fk_incident_emp` FOREIGN KEY (`created_by`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_incident_sprint` FOREIGN KEY (`sprint_id`) REFERENCES `sprint` (`sprint_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incident_ticket`
--

LOCK TABLES `incident_ticket` WRITE;
/*!40000 ALTER TABLE `incident_ticket` DISABLE KEYS */;
INSERT INTO `incident_ticket` VALUES ('INC12345','AWS Login Error','2020-05-09','Open','P1',1,1),('INC12346','Azure Login Error','2020-04-09','In Progress','P2',2,2),('INC12347','Oracle Tables Error','2019-01-09','Closed','P3',5,3),('INC12348','Database Error','2022-01-09','Open','P1',7,5),('INC12349','DS values Error','2021-01-09','Closed','P2',6,4);
/*!40000 ALTER TABLE `incident_ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager` (
  `emp_id` int NOT NULL,
  `team_id` int NOT NULL,
  PRIMARY KEY (`emp_id`,`team_id`),
  KEY `fk_manager_team` (`team_id`),
  CONSTRAINT `fk_manager_employee` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_manager_team` FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
INSERT INTO `manager` VALUES (1,1),(2,1),(3,2),(4,3),(123,4);
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request_ticket`
--

DROP TABLE IF EXISTS `request_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request_ticket` (
  `ticket_id` varchar(50) NOT NULL,
  `description` varchar(20) NOT NULL,
  `start_date` date NOT NULL,
  `status` enum('Open','In Progress','Closed') DEFAULT NULL,
  `priority` enum('P1','P2','P3','P4') DEFAULT NULL,
  `sprint_id` int NOT NULL,
  `created_by` int NOT NULL,
  PRIMARY KEY (`ticket_id`),
  KEY `fk_request_sprint` (`sprint_id`),
  KEY `fk_request_emp` (`created_by`),
  CONSTRAINT `fk_request_emp` FOREIGN KEY (`created_by`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_request_sprint` FOREIGN KEY (`sprint_id`) REFERENCES `sprint` (`sprint_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_ticket`
--

LOCK TABLES `request_ticket` WRITE;
/*!40000 ALTER TABLE `request_ticket` DISABLE KEYS */;
INSERT INTO `request_ticket` VALUES ('REQ12348','Database Create','2022-01-09','Open','P1',7,5),('REQ12349','DS new usecase','2021-01-09','Closed','P2',6,4),('REQ22345','AWS Access','2020-05-09','Open','P1',1,1),('REQ22346','Azure Access','2020-04-09','In Progress','P2',2,2),('REQ22347','Oracle Tables Create','2019-01-09','Closed','P3',5,3);
/*!40000 ALTER TABLE `request_ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sprint`
--

DROP TABLE IF EXISTS `sprint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sprint` (
  `sprint_id` int NOT NULL,
  `sprint_name` varchar(20) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`sprint_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sprint`
--

LOCK TABLES `sprint` WRITE;
/*!40000 ALTER TABLE `sprint` DISABLE KEYS */;
INSERT INTO `sprint` VALUES (1,'AWS Sprint 1','2020-05-05','2020-05-30'),(2,'Azure Sprint 1','2020-04-05','2020-04-30'),(3,'AWS Sprint 2','2020-06-05','2020-06-30'),(4,'Azure Sprint 2','2020-07-05','2020-07-30'),(5,'Oracle Sprint 1','2019-01-01','2019-01-02'),(6,'Data Science S1','2021-01-05','2021-02-10'),(7,'DB S1','2022-01-05','2022-02-05'),(90,'','2022-11-18','2022-11-16'),(123,'ABC','2022-11-10','2022-11-25'),(999,'','2022-11-17','2022-11-09');
/*!40000 ALTER TABLE `sprint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sprint_team`
--

DROP TABLE IF EXISTS `sprint_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sprint_team` (
  `sprint_id` int NOT NULL,
  `team_id` int NOT NULL,
  PRIMARY KEY (`sprint_id`,`team_id`),
  KEY `fk_team` (`team_id`),
  CONSTRAINT `fk_sprint` FOREIGN KEY (`sprint_id`) REFERENCES `sprint` (`sprint_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_team` FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sprint_team`
--

LOCK TABLES `sprint_team` WRITE;
/*!40000 ALTER TABLE `sprint_team` DISABLE KEYS */;
INSERT INTO `sprint_team` VALUES (1,1),(3,1),(90,1),(123,1),(999,1),(2,2),(4,2),(5,3),(6,4),(7,5);
/*!40000 ALTER TABLE `sprint_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `team_id` int NOT NULL,
  `team_name` varchar(20) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (1,'AWS','This team works on AWS projects','Boston'),(2,'Azure','This team works on Microsoft Azure Projects','Hyderabad'),(3,'Oracle','This teams works on projects related to Oracle','New York'),(4,'Data Science','This team works on all the projects that are related to Data Science','Los Angeles'),(5,'Database Admin','This team takes care of all the database related projects','Dallas');
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'ticketmanagementsystem'
--

--
-- Dumping routines for database 'ticketmanagementsystem'
--
/*!50003 DROP PROCEDURE IF EXISTS `deleteChange` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteChange`(in chg_id VARCHAR(20))
BEGIN
DELETE FROM change_ticket WHERE change_ticket.ticket_id = chg_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `deleteIncident` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteIncident`(in inc_id VARCHAR(20))
BEGIN
DELETE FROM incident_ticket WHERE incident_ticket.ticket_id = inc_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `deleteRequest` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteRequest`(in req_id VARCHAR(20))
BEGIN
DELETE FROM request_ticket WHERE request_ticket.ticket_id = req_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-23 11:17:45
