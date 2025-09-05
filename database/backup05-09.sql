/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.13-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: teste
-- ------------------------------------------------------
-- Server version	10.11.13-MariaDB-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contadores_mensais`
--

DROP TABLE IF EXISTS `contadores_mensais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `contadores_mensais` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num_serie` varchar(50) NOT NULL,
  `filial_id` int(11) NOT NULL,
  `contador` float DEFAULT NULL,
  `data` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `num_serie` (`num_serie`),
  KEY `filial_id` (`filial_id`),
  CONSTRAINT `contadores_mensais_ibfk_1` FOREIGN KEY (`num_serie`) REFERENCES `impressoras` (`num_serie`),
  CONSTRAINT `contadores_mensais_ibfk_2` FOREIGN KEY (`filial_id`) REFERENCES `filiais` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contadores_mensais`
--

LOCK TABLES `contadores_mensais` WRITE;
/*!40000 ALTER TABLE `contadores_mensais` DISABLE KEYS */;
INSERT INTO `contadores_mensais` VALUES
(1,'5BT795377',3,45984,'2025-09-03 15:11:10'),
(2,'BRB7MB824Z',23,50661,'2025-09-03 15:11:10'),
(3,'BRBSQ9906Z',25,19535,'2025-09-03 15:11:10'),
(4,'BRBSQ99085',38,9359,'2025-09-03 15:11:10'),
(5,'BRBSQ9908P',25,23667,'2025-09-03 15:11:10'),
(6,'BRBSQ990K7',38,23291,'2025-09-03 15:11:10'),
(7,'BRBSQ990M5',25,12395,'2025-09-03 15:11:10'),
(8,'BRBSQ990MZ',35,1115,'2025-09-03 15:11:10'),
(9,'BRBSQ9H0B1',50,12615,'2025-09-03 15:11:10'),
(10,'BRBSQ9P06Q',51,29138,'2025-09-03 15:11:10'),
(11,'BRBSQC00ZR',51,6967,'2025-09-03 15:11:10'),
(12,'BRBSS7S029',12,861,'2025-09-03 15:11:10'),
(13,'BRBSS9L0HT',35,4783,'2025-09-03 15:11:10'),
(14,'BRDSQB20CJ',50,4303,'2025-09-03 15:11:10'),
(15,'BRDSQB3003',26,4277,'2025-09-03 15:11:10'),
(16,'BRDSQB303W',12,15779,'2025-09-03 15:11:10'),
(17,'BRDSQB3040',53,12490,'2025-09-03 15:11:10'),
(18,'BRDSQB309C',53,8594,'2025-09-03 15:11:10'),
(19,'BRDSQB603X',12,9740,'2025-09-03 15:11:10'),
(20,'ZDDPB07M515Q8SL',45,56802,'2025-09-03 15:11:10'),
(21,'ZDDPB07M515QTJL',20,90364,'2025-09-03 15:11:10'),
(22,'ZDDPB07M6168QDK',45,76253,'2025-09-03 15:11:10'),
(23,'ZDDPB07M6168RVA',11,168793,'2025-09-03 15:11:10'),
(24,'ZDDPB07M616B4FE',29,73311,'2025-09-03 15:11:10'),
(25,'ZDDPB07M616B50H',28,67421,'2025-09-03 15:11:10'),
(26,'ZDDPB07M616B5DH',26,132266,'2025-09-03 15:11:10'),
(27,'ZDDPB07M616B5PH',27,145133,'2025-09-03 15:11:10'),
(28,'ZDDPB07M616B6PW',39,94131,'2025-09-03 15:11:10'),
(29,'ZDDPB07M616B6VW',35,53951,'2025-09-03 15:11:10'),
(30,'ZDDPB07M616B6WW',19,144429,'2025-09-03 15:11:10'),
(31,'ZDDPB07M616B8MZ',37,37248,'2025-09-03 15:11:10'),
(32,'ZDDPB07M616B9YP',35,89877,'2025-09-03 15:11:10'),
(33,'ZDDPB07M616BC7M',34,13915,'2025-09-03 15:11:10'),
(34,'ZDDPB07M616BCFM',19,132827,'2025-09-03 15:11:10'),
(35,'ZDDPB07M616BCGM',15,132947,'2025-09-03 15:11:10'),
(36,'ZDDPB07M716CNLX',6,95479,'2025-09-03 15:11:10'),
(37,'ZDDPB07M716CNNX',2,147732,'2025-09-03 15:11:10'),
(38,'ZDDPB07M716CP5F',20,21405,'2025-09-03 15:11:10'),
(39,'ZDDPB07M716CQDJ',39,156232,'2025-09-03 15:11:10'),
(40,'ZDDPB07M716CREV',19,263484,'2025-09-03 15:11:10'),
(41,'ZDDPB07M716CT2Y',23,141597,'2025-09-03 15:11:10'),
(42,'ZDDPB07M716CTQY',37,29764,'2025-09-03 15:11:10'),
(43,'ZDDPB07M716CTZY',4,131596,'2025-09-03 15:11:10'),
(44,'ZDDPB07M716CVKDX',4,36053,'2025-09-03 15:11:10'),
(45,'ZDDPB07M716CVPD',29,107456,'2025-09-03 15:11:11'),
(46,'ZDDPB07M716CVXD',9,115885,'2025-09-03 15:11:11'),
(47,'ZDDPB07M716CW1E',21,128181,'2025-09-03 15:11:11'),
(48,'ZDDPB07M716CX1H',2,130650,'2025-09-03 15:11:11'),
(49,'ZDDPB07M716CYWW',30,59066,'2025-09-03 15:11:11'),
(50,'ZDDPB07M716CZET',9,63620,'2025-09-03 15:11:11'),
(51,'ZDDPB07M716CZHTX',13,23957,'2025-09-03 15:11:11'),
(52,'ZDDPB07M716CZST',30,71360,'2025-09-03 15:11:11'),
(53,'ZDDPB07M716D00N',26,46893,'2025-09-03 15:11:11'),
(54,'ZDDPB07M716D2GM',28,190839,'2025-09-03 15:11:11'),
(55,'ZDDPB07M716D2RM',10,199673,'2025-09-03 15:11:11'),
(56,'ZDDPB07M716D2WM',27,91906,'2025-09-03 15:11:11'),
(57,'ZDDPB07M716D3BL',8,236656,'2025-09-03 15:11:11'),
(58,'ZDDPB07M716DERH',19,161239,'2025-09-03 15:11:11'),
(59,'ZDDPB07M716DETH',21,128113,'2025-09-03 15:11:11'),
(60,'ZDDPB07M716DF0W',23,35590,'2025-09-03 15:11:11'),
(61,'ZDDPB07M716DF2W',3,84669,'2025-09-03 15:11:11'),
(62,'ZDDPB07M716DN0L',8,119214,'2025-09-03 15:11:11'),
(63,'ZDDPB07M716DP0K',11,66912,'2025-09-03 15:11:11'),
(64,'ZDDPB07M716DQNA',5,172685,'2025-09-03 15:11:11');
/*!40000 ALTER TABLE `contadores_mensais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filiais`
--

DROP TABLE IF EXISTS `filiais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `filiais` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `nome` (`nome`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filiais`
--

LOCK TABLES `filiais` WRITE;
/*!40000 ALTER TABLE `filiais` DISABLE KEYS */;
INSERT INTO `filiais` VALUES
(28,'Araçatuba'),
(15,'Araraquara'),
(2,'Araras'),
(11,'Assis'),
(24,'Avare'),
(38,'Bandeirantes'),
(10,'Barra Bonita'),
(55,'Bragancia'),
(35,'Catanduva'),
(3,'Cerquilho'),
(52,'Cerquilho Central E'),
(5,'Charqueada'),
(9,'Chavantes'),
(4,'Cosmopolis'),
(41,'Costa Rica'),
(25,'Dourados'),
(34,'Goiatuba'),
(21,'Igarapava'),
(6,'Iracemapolis'),
(27,'Itapetininga'),
(45,'Itapeva'),
(20,'Jatai'),
(1,'Matriz'),
(16,'Matriz Implementos'),
(7,'Nova Odessa'),
(13,'Penapolis'),
(19,'Piracicaba UDG'),
(37,'Pirajuba'),
(26,'Quirinopolis'),
(22,'Ribeirão Preto'),
(12,'Rio Claro'),
(8,'Santa Cruz'),
(29,'São José do Rio Preto'),
(39,'Taquarituba'),
(50,'Taquarituba Khun'),
(30,'Tiete'),
(51,'Tupaciguara'),
(23,'Uberaba'),
(53,'Uberaba UDG');
/*!40000 ALTER TABLE `filiais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `impressora_filial`
--

DROP TABLE IF EXISTS `impressora_filial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `impressora_filial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num_serie` varchar(50) NOT NULL,
  `filial_id` int(11) NOT NULL,
  `posicao` varchar(20) DEFAULT NULL,
  `data_vinculo` datetime NOT NULL DEFAULT current_timestamp(),
  `status` varchar(20) DEFAULT 'Ativo',
  `observacoes` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `impressora_filial_ibfk_2` (`filial_id`),
  KEY `impressora_filial_ibfk_1` (`num_serie`),
  CONSTRAINT `impressora_filial_ibfk_1` FOREIGN KEY (`num_serie`) REFERENCES `impressoras` (`num_serie`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `impressora_filial_ibfk_2` FOREIGN KEY (`filial_id`) REFERENCES `filiais` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `impressora_filial`
--

LOCK TABLES `impressora_filial` WRITE;
/*!40000 ALTER TABLE `impressora_filial` DISABLE KEYS */;
INSERT INTO `impressora_filial` VALUES
(1,'5BT795377',3,NULL,'2025-08-11 16:28:02','Ativo',NULL),
(2,'BRB7MB824Z',23,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(3,'BRBSQ9906Z',25,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(4,'BRBSQ99085',38,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(5,'BRBSQ9908P',25,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(6,'BRBSQ990K7',38,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(7,'BRBSQ990M5',25,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(8,'BRBSQ990MZ',35,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(9,'BRBSQ9H0B1',50,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(10,'BRBSQ9P06Q',51,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(11,'BRBSQC00ZR',51,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(12,'BRBSS7S029',12,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(13,'BRBSS9L0HT',35,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(14,'BRDSQB20CJ',50,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(15,'BRDSQB3003',26,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(16,'BRDSQB303W',12,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(17,'BRDSQB3040',53,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(18,'BRDSQB309C',53,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(19,'BRDSQB603X',12,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(20,'ZDDPB07M515Q8SL',45,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(21,'ZDDPB07M515QTJL',20,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(22,'ZDDPB07M6168QDK',45,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(23,'ZDDPB07M6168RVA',11,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(24,'ZDDPB07M616B4FE',29,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(25,'ZDDPB07M616B50H',28,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(26,'ZDDPB07M616B5DH',26,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(27,'ZDDPB07M616B5PH',27,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(28,'ZDDPB07M616B6PW',39,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(29,'ZDDPB07M616B6VW',35,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(30,'ZDDPB07M616B8MZ',37,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(31,'ZDDPB07M616B8PZ',41,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(32,'ZDDPB07M616BC7M',34,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(33,'ZDDPB07M616BCFM',19,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(34,'ZDDPB07M616BCGM',15,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(35,'ZDDPB07M716CNLX',6,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(36,'ZDDPB07M716CNNX',2,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(37,'ZDDPB07M716CP5F',20,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(38,'ZDDPB07M716CQDJ',39,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(39,'ZDDPB07M716CREV',19,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(40,'ZDDPB07M716CT2Y',23,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(41,'ZDDPB07M716CTQY',37,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(42,'ZDDPB07M716CTZY',4,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(43,'ZDDPB07M716CVKDX',4,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(44,'ZDDPB07M716CVPD',29,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(45,'ZDDPB07M716CVXD',9,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(46,'ZDDPB07M716CW1E',21,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(47,'ZDDPB07M716CYWW',30,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(48,'ZDDPB07M716CZ1T',13,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(49,'ZDDPB07M716CZET',9,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(50,'ZDDPB07M716CZHTX',13,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(51,'ZDDPB07M716CZST',30,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(52,'ZDDPB07M716D00N',26,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(53,'ZDDPB07M716D2GM',28,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(54,'ZDDPB07M716D2RM',10,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(55,'ZDDPB07M716D2WM',27,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(56,'ZDDPB07M716D3BL',8,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(57,'ZDDPB07M716DERH',19,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(58,'ZDDPB07M716DETH',21,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(59,'ZDDPB07M716DF0W',23,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(60,'ZDDPB07M716DF2W',3,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(61,'ZDDPB07M716DN0L',8,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(62,'ZDDPB07M716DP0K',11,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(63,'ZDDPB07M716DQNA',5,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(64,'ZDDPB07M716HGFK',7,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(65,'ZDDPB07M716HGMK',45,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(66,'ZDEJB07M545T3BD',24,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(67,'ZDEJB07M545T5QH',15,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(68,'ZDEJB07M926YQPD',45,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(69,'ZDEJB07MA1740AV',4,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(70,'ZEQYBQAD800465L',5,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(71,'ZEQYBQAD801381X',3,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(72,'ZEQYBQAFA002ZLW',10,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(73,'ZER4BQADA01350E',5,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(74,'ZER4BQADA01355M',39,NULL,'2025-08-11 16:28:03','Ativo',NULL),
(75,'ZER4BQADA01355MX',3,NULL,'2025-08-11 16:28:03','Ativo',NULL);
/*!40000 ALTER TABLE `impressora_filial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `impressoras`
--

DROP TABLE IF EXISTS `impressoras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `impressoras` (
  `num_serie` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `tipo` varchar(7) DEFAULT NULL,
  `ip` varchar(18) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'Ativo',
  `conexao` enum('USB','IP') NOT NULL,
  PRIMARY KEY (`num_serie`),
  UNIQUE KEY `num_serie` (`num_serie`),
  UNIQUE KEY `ip` (`ip`),
  UNIQUE KEY `ip_2` (`ip`),
  CONSTRAINT `chk_usb_ip` CHECK (`conexao` = 'USB' and `ip` is null or `conexao` <> 'USB')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `impressoras`
--

LOCK TABLES `impressoras` WRITE;
/*!40000 ALTER TABLE `impressoras` DISABLE KEYS */;
INSERT INTO `impressoras` VALUES
('5BT795377','Xerox WorkCentre 3335','Térmica','10.0.3.51','Ativo','IP'),
('BRB7MB824Z','Samsung M332x 382x 402x Series','Térmica','10.0.23.52','Ativo','IP'),
('BRBSP4613F','HP LaserJet MFP E42540','Laser','192.168.50.89','Ativo','IP'),
('BRBSQ9906Z','HP LaserJet Pro MFP 4103fdw','Térmica','10.0.25.50','Ativo','IP'),
('BRBSQ99085','HP LaserJet Pro MFP 4103fdw','Térmica','10.0.38.52','Ativo','IP'),
('BRBSQ9908P','HP LaserJet Pro MFP 4103fdw','Térmica','10.0.25.51','Ativo','IP'),
('BRBSQ990K7','HP LaserJet Pro MFP 4103fdw','Térmica','10.0.38.50','Ativo','IP'),
('BRBSQ990M5','HP LaserJet Pro MFP 4103fdw','Térmica','10.0.25.53','Ativo','IP'),
('BRBSQ990MZ','HP LaserJet Pro MFP 4103fdw','Térmica','10.0.35.53','Ativo','IP'),
('BRBSQ9D0M4','nan','Laser',NULL,'Ativo','USB'),
('BRBSQ9H0B1','HP LaserJet Pro MFP 4103fdw','Térmica','10.0.50.50','Ativo','IP'),
('BRBSQ9P06Q','HP LaserJet Pro MFP 4103fdw','Térmica','10.0.51.50','Ativo','IP'),
('BRBSQC00NM','HP LaserJet Pro 4003dw','Laser','192.168.50.38','Ativo','IP'),
('BRBSQC00ZR','HP LaserJet Pro 4003dw','Térmica','10.0.51.52','Ativo','IP'),
('BRBSS440D2','nan','Laser','192.168.50.41','Ativo','IP'),
('BRBSS7S029','HP LaserJet MFP E42540','Térmica','10.0.12.52','Ativo','IP'),
('BRBSS9L0HT','HP LaserJet MFP E42540','Térmica','10.0.35.52','Ativo','IP'),
('BRDSQB20CJ','HP LaserJet Pro MFP M428fdw','Térmica','10.0.50.51','Ativo','IP'),
('BRDSQB3003','HP LaserJet Pro MFP M428fdw','Térmica','10.0.26.53','Ativo','IP'),
('BRDSQB303W','HP LaserJet Pro MFP M428fdw','Térmica','10.0.12.53','Ativo','IP'),
('BRDSQB3040','HP LaserJet Pro MFP M428fdw','Térmica','10.0.53.50','Ativo','IP'),
('BRDSQB309C','HP LaserJet Pro MFP M428fdw','Térmica','10.0.53.51','Ativo','IP'),
('BRDSQB30GH','HP LaserJet Pro MFP M428fdw','Térmica','10.0.16.59','Ativo','IP'),
('BRDSQB603X','HP LaserJet Pro MFP M428fdw','Térmica','10.0.12.54','Ativo','IP'),
('BRDSQB606S','HP LaserJet Pro MFP M428fdw','Laser','192.168.50.96','Ativo','IP'),
('CNCRQ6D04M','HP Color LaserJet Pro MFP M479fdw','Laser','192.168.50.46','Ativo','IP'),
('D5J224900896','ZD230','Térmica','192.168.50.62','Ativo','IP'),
('D5N213800657','ZD230','Térmica','10.0.21.55','Ativo','IP'),
('D5N213800711','ZD230','Térmica','10.0.44.55','Ativo','IP'),
('D5N213800715','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N213800720','ZD230','Térmica','192.168.50.54','Ativo','IP'),
('D5N213800728','ZD230','Térmica','10.0.7.55','Ativo','IP'),
('D5N213800779','ZD230','Térmica','10.0.8.56','Ativo','IP'),
('D5N213800788','ZD230','Térmica','10.0.37.55','Ativo','IP'),
('D5N213800880','ZD230','Térmica','10.0.39.56','Ativo','IP'),
('D5N213800957','ZD230','Térmica','10.0.29.55','Ativo','IP'),
('D5N213800985','ZD230','Térmica','10.0.15.55','Ativo','IP'),
('D5N213801090','ZD230','Térmica','10.0.23.55','Ativo','IP'),
('D5N213801092','ZD230','Térmica','10.0.4.53','Ativo','IP'),
('D5N213801098','ZD230','Térmica','10.0.6.56','Ativo','IP'),
('D5N213801102','ZD230','Térmica','10.0.9.55','Ativo','IP'),
('D5N213801117','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N213801119','ZD230','Térmica','10.0.41.55','Ativo','IP'),
('D5N213801123','ZD230','Térmica','10.0.5.55','Ativo','IP'),
('D5N213801127','ZD230','Térmica','10.0.2.56','Ativo','IP'),
('D5N213801133','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N213801136','ZD230','Térmica','10.0.20.55','Ativo','IP'),
('D5N213801139','ZD230','Térmica','10.0.10.55','Ativo','IP'),
('D5N213801150','ZD230','Térmica','10.0.36.55','Ativo','IP'),
('D5N213801151','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N213801152','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N213801272','ZD230','Térmica','10.0.24.55','Ativo','IP'),
('D5N213801292','ZD230','Térmica','10.0.3.52','Ativo','IP'),
('D5N213801332','ZD230','Térmica','10.0.12.55','Ativo','IP'),
('D5N214900226','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N220300498','ZD230','Térmica','192.168.50.68','Ativo','IP'),
('D5N220300710','ZD230','Térmica','10.0.45.55','Ativo','IP'),
('D5N220300724','ZD230','Térmica','192.168.50.101','Ativo','IP'),
('D5N220300735','ZD230','Térmica','192.168.50.55','Ativo','IP'),
('D5N223901690','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N224802168','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N224802314','ZD230','Térmica','192.168.50.56','Ativo','IP'),
('D5N224802511','ZD230','Térmica','10.0.35.55','Ativo','IP'),
('D5N230302027','ZD230','Térmica',NULL,'Ativo','USB'),
('D5N231901472','ZD230','Térmica','192.168.0.86','Ativo','IP'),
('D5N232201109','ZD230','Térmica',NULL,'Ativo','USB'),
('E173M860473','RICOH MP C4503','Laser','192.168.50.26','Ativo','IP'),
('G174RB30035','RICOH MP C4503','Laser','192.168.50.66','Ativo','IP'),
('G175R630307','RICOH MP C4503','Laser','192.168.50.65','Ativo','IP'),
('G176R930228 ','RICOH MP C4503','Laser','10.18.0.250','Ativo','IP'),
('KNDX04137','nan','Laser',NULL,'Ativo','USB'),
('T885Q111369','nan','Laser','10.18.31.23','Ativo','IP'),
('T885QB11297','nan','Laser','10.18.19.108','Ativo','IP'),
('ZDDPB07K7137EMY','SL-M4070FR','Laser','192.168.50.60','Ativo','IP'),
('ZDDPB07K7137ENY','nan','Laser','10.0.44.53','Offline','IP'),
('ZDDPB07M515Q8SL','Samsung M337x 387x 407x Series','Térmica','10.0.45.51','Offline','IP'),
('ZDDPB07M515QTJL','Samsung M337x 387x 407x Series','Térmica','10.0.20.50','Ativo','IP'),
('ZDDPB07M515RSMP','nan','Laser',NULL,'Ativo','USB'),
('ZDDPB07M6168QDK','Samsung M337x 387x 407x Series','Térmica','10.0.45.50','Ativo','IP'),
('ZDDPB07M6168QXK','SL-M4070FR','Laser','10.0.41.51','Offline','IP'),
('ZDDPB07M6168RNA','SL-M4070FR','Laser','192.168.50.53','Ativo','IP'),
('ZDDPB07M6168RVA','Samsung M337x 387x 407x Series','Térmica','10.0.11.50','Ativo','IP'),
('ZDDPB07M616B45E','SL-M4070FR','Laser','10.0.22.50','Offline','IP'),
('ZDDPB07M616B4FE','Samsung M337x 387x 407x Series','Térmica','10.0.29.50','Ativo','IP'),
('ZDDPB07M616B4VE','nan','Laser','10.0.36.51','Offline','IP'),
('ZDDPB07M616B50H','Samsung M337x 387x 407x Series','Térmica','10.0.28.50','Ativo','IP'),
('ZDDPB07M616B54H','SL-M4070FR','Laser','10.0.34.50','Offline','IP'),
('ZDDPB07M616B55H','SL-M4070FR','Laser','192.168.50.63','Ativo','IP'),
('ZDDPB07M616B5DH','Samsung M337x 387x 407x Series','Térmica','10.0.26.50','Ativo','IP'),
('ZDDPB07M616B5LH','SL-M4070FR','Laser','192.168.50.58','Ativo','IP'),
('ZDDPB07M616B5PH','Samsung M337x 387x 407x Series','Térmica','10.0.27.50','Ativo','IP'),
('ZDDPB07M616B6EW','nan','Laser','10.18.0.100','Ativo','IP'),
('ZDDPB07M616B6PW','Samsung M337x 387x 407x Series','Térmica','10.0.39.51','Ativo','IP'),
('ZDDPB07M616B6VW','Samsung M337x 387x 407x Series','Térmica','10.0.35.50','Ativo','IP'),
('ZDDPB07M616B6WW','Samsung M337x 387x 407x Series','Térmica','10.0.19.51','Ativo','IP'),
('ZDDPB07M616B6XW','nan','Laser','10.0.36.53','Offline','IP'),
('ZDDPB07M616B76T','SL-M4070FR','Laser','10.0.6.50','Erro no SNMP','IP'),
('ZDDPB07M616B8MZ','Samsung M337x 387x 407x Series','Térmica','10.0.37.50','Ativo','IP'),
('ZDDPB07M616B8PZ','Samsung M337x 387x 407x Series','Laser','10.0.41.50','Erro no SNMP','IP'),
('ZDDPB07M616B9YP','Samsung M337x 387x 407x Series','Térmica','10.0.35.51','Ativo','IP'),
('ZDDPB07M616BBXR','nan','Laser','10.0.44.50','Offline','IP'),
('ZDDPB07M616BC4M','SL-M4070FR','Laser','192.168.50.57','Ativo','IP'),
('ZDDPB07M616BC7M','Samsung M337x 387x 407x Series','Térmica','10.0.34.51','Ativo','IP'),
('ZDDPB07M616BCEM','SL-M4070FR','Laser','192.168.50.51','Ativo','IP'),
('ZDDPB07M616BCFM','Samsung M337x 387x 407x Series','Térmica','10.0.19.50','Ativo','IP'),
('ZDDPB07M616BCGM','Samsung M337x 387x 407x Series','Térmica','10.0.15.50','Ativo','IP'),
('ZDDPB07M616BCHM','nan','Laser','10.0.32.52','Offline','IP'),
('ZDDPB07M716CNLX','Samsung M337x 387x 407x Series','Térmica','10.0.6.51','Ativo','IP'),
('ZDDPB07M716CNNX','Samsung M337x 387x 407x Series','Térmica','10.0.2.50','Ativo','IP'),
('ZDDPB07M716CP5F','Samsung M337x 387x 407x Series','Térmica','10.0.20.51','Ativo','IP'),
('ZDDPB07M716CQDJ','Samsung M337x 387x 407x Series','Térmica','10.0.39.53','Ativo','IP'),
('ZDDPB07M716CREV','Samsung M337x 387x 407x Series','Térmica','10.0.19.56','Ativo','IP'),
('ZDDPB07M716CRWV','SL-M4070FR','Laser','192.168.50.73','Ativo','IP'),
('ZDDPB07M716CT2Y','Samsung M337x 387x 407x Series','Térmica','10.0.23.50','Ativo','IP'),
('ZDDPB07M716CTGY','SL-M4070FR','Laser','10.0.52.50','Offline','IP'),
('ZDDPB07M716CTQY','Samsung M337x 387x 407x Series','Térmica','10.0.37.51','Ativo','IP'),
('ZDDPB07M716CTZY','Samsung M337x 387x 407x Series','Térmica','10.0.4.52','Ativo','IP'),
('ZDDPB07M716CVFD','SL-M4070FR','Laser','192.168.50.27','Ativo','IP'),
('ZDDPB07M716CVKDX','Samsung M337x 387x 407x Series','Térmica','10.0.4.51','Ativo','IP'),
('ZDDPB07M716CVPD','Samsung M337x 387x 407x Series','Térmica','10.0.29.51','Ativo','IP'),
('ZDDPB07M716CVXD','Samsung M337x 387x 407x Series','Térmica','10.0.9.50','Ativo','IP'),
('ZDDPB07M716CW1E','Samsung M337x 387x 407x Series','Térmica','10.0.21.51','Ativo','IP'),
('ZDDPB07M716CX1H','Samsung M337x 387x 407x Series','Térmica','10.0.2.51','Ativo','IP'),
('ZDDPB07M716CXRH','Samsung M337x 387x 407x Series','Térmica','10.0.7.51','Ativo','IP'),
('ZDDPB07M716CYWW','Samsung M337x 387x 407x Series','Térmica','10.0.30.51','Ativo','IP'),
('ZDDPB07M716CZ1T','Samsung M337x 387x 407x Series','Térmica','10.0.13.51','Ativo','IP'),
('ZDDPB07M716CZBT','SL-M4070FR','Laser','10.0.7.50','Erro no SNMP','IP'),
('ZDDPB07M716CZDT','SL-M4070FR','Laser','192.168.50.49','Ativo','IP'),
('ZDDPB07M716CZET','Samsung M337x 387x 407x Series','Térmica','10.0.9.51','Ativo','IP'),
('ZDDPB07M716CZHTX','Samsung M337x 387x 407x Series','Térmica','10.0.13.50','Ativo','IP'),
('ZDDPB07M716CZLT','SL-M4070FR','Laser','192.168.50.78','Ativo','IP'),
('ZDDPB07M716CZST','Samsung M337x 387x 407x Series','Térmica','10.0.30.50','Ativo','IP'),
('ZDDPB07M716D00N','Samsung M337x 387x 407x Series','Térmica','10.0.26.54','Ativo','IP'),
('ZDDPB07M716D2GM','Samsung M337x 387x 407x Series','Térmica','10.0.28.51','Ativo','IP'),
('ZDDPB07M716D2JM','SL-M4070FR','Laser','10.0.24.51','Erro no SNMP','IP'),
('ZDDPB07M716D2RM','Samsung M337x 387x 407x Series','Térmica','10.0.10.51','Ativo','IP'),
('ZDDPB07M716D2WM','Samsung M337x 387x 407x Series','Térmica','10.0.27.51','Ativo','IP'),
('ZDDPB07M716D2XM','SL-M4070FR','Laser','192.168.50.34','Ativo','IP'),
('ZDDPB07M716D33L','nan','Laser','10.0.32.51','Offline','IP'),
('ZDDPB07M716D39L','SL-M4070FR','Laser','192.168.50.52','Ativo','IP'),
('ZDDPB07M716D3BL','Samsung M337x 387x 407x Series','Térmica','10.0.8.51','Ativo','IP'),
('ZDDPB07M716DEJH','SL-M4070FR','Laser','192.168.50.50','Ativo','IP'),
('ZDDPB07M716DEQH','SL-M4070FR','Laser','192.168.50.30','Ativo','IP'),
('ZDDPB07M716DERH','Samsung M337x 387x 407x Series','Térmica','10.0.19.52','Ativo','IP'),
('ZDDPB07M716DETH','Samsung M337x 387x 407x Series','Térmica','10.0.21.50','Ativo','IP'),
('ZDDPB07M716DF0W','Samsung M337x 387x 407x Series','Térmica','10.0.23.53','Ativo','IP'),
('ZDDPB07M716DF2W','Samsung M337x 387x 407x Series','Térmica','10.0.3.56','Ativo','IP'),
('ZDDPB07M716DN0L','Samsung M337x 387x 407x Series','Térmica','10.0.8.50','Ativo','IP'),
('ZDDPB07M716DP0K','Samsung M337x 387x 407x Series','Térmica','10.0.11.51','Ativo','IP'),
('ZDDPB07M716DQNA','Samsung M337x 387x 407x Series','Térmica','10.0.5.52','Offline','IP'),
('ZDDPB07M716DQVA','nan','Laser','10.0.32.50','Offline','IP'),
('ZDDPB07M716HGFK','Samsung M337x 387x 407x Series','Térmica',NULL,'Ativo','IP'),
('ZDDPB07M716HGHK','SL-M4070FR','Laser','192.168.50.31','Ativo','IP'),
('ZDDPB07M716HGKK','nan','Laser','10.0.36.50','Offline','IP'),
('ZDDPB07M716HGMK','Samsung M337x 387x 407x Series','Térmica','10.0.45.52','Ativo','IP'),
('ZDDPB07M716HGQK','nan','Laser',NULL,'Ativo','IP'),
('ZDEJB07M2253FPT','SL-M4020ND','Laser','192.168.50.48','Ativo','IP'),
('ZDEJB07M2253VHB','SL-M4020ND','Laser','192.168.50.70','Ativo','IP'),
('ZDEJB07M22542FN','SL-M4020ND','Laser','10.0.23.54','Erro no SNMP','IP'),
('ZDEJB07M545SSSN','SL-M4020ND','Laser','10.0.39.52','Erro no SNMP','IP'),
('ZDEJB07M545T2XY','nan','Laser','192.168.50.92','Ativo','IP'),
('ZDEJB07M545T3BD','Samsung M332x 382x 402x Series','Laser','10.0.24.50','Ativo','IP'),
('ZDEJB07M545T53H','SL-M4020ND','Laser','192.168.50.71','Ativo','IP'),
('ZDEJB07M545T5JH','nan','Laser','10.0.32.53','Offline','IP'),
('ZDEJB07M545T5QH','Samsung M332x 382x 402x Series','Térmica','10.0.15.51','Ativo','IP'),
('ZDEJB07M545T5SH','SL-M4020ND','Laser','10.0.12.50','Offline','IP'),
('ZDEJB07M545TG7X','Samsung M332x 382x 402x Series','Laser',NULL,'Ativo','IP'),
('ZDEJB07M926YQPD','Samsung M332x 382x 402x Series','Térmica','10.0.45.53','Ativo','IP'),
('ZDEJB07MA1740AV','Samsung M332x 382x 402x Series','Térmica','10.0.4.50','Ativo','IP'),
('ZEQYBQAD800465L','Samsung M332x 382x 402x Series','Térmica','10.0.5.50','Ativo','IP'),
('ZEQYBQAD801369Z','SL-M4020ND','Laser','192.168.50.43','Ativo','IP'),
('ZEQYBQAD801381X','Samsung M332x 382x 402x Series','Térmica','10.0.3.50','Ativo','IP'),
('ZEQYBQAFA002ZLW','Samsung M332x 382x 402x Series','Térmica','10.0.10.50','Ativo','IP'),
('ZER4BQADA01350E','Samsung M337x 387x 407x Series','Térmica','10.0.5.51','Ativo','IP'),
('ZER4BQADA01355M','Samsung M337x 387x 407x Series','Térmica','10.0.39.50','Ativo','IP'),
('ZER4BQADA01355MX','Samsung M337x 387x 407x Series','Térmica','10.0.3.53','Ativo','IP');
/*!40000 ALTER TABLE `impressoras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_movimentacoes`
--

DROP TABLE IF EXISTS `log_movimentacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `log_movimentacoes` (
  `id_log` int(11) NOT NULL AUTO_INCREMENT,
  `num_serie` varchar(50) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `evento` text NOT NULL,
  `ip_anterior` varchar(18) DEFAULT NULL,
  `ip_novo` varchar(18) DEFAULT NULL,
  `filial_anterior` int(11) DEFAULT NULL,
  `filial_nova` int(11) DEFAULT NULL,
  `usuario_resposavel` varchar(100) DEFAULT NULL,
  `data_evento` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id_log`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_movimentacoes`
--

LOCK TABLES `log_movimentacoes` WRITE;
/*!40000 ALTER TABLE `log_movimentacoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_movimentacoes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manutencao`
--

DROP TABLE IF EXISTS `manutencao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `manutencao` (
  `id_manu` int(11) NOT NULL,
  `num_serie` varchar(50) NOT NULL,
  `modelo` varchar(50) NOT NULL,
  `filial_id` int(11) NOT NULL,
  `filial_nome` varchar(50) NOT NULL,
  `ip` varchar(18) NOT NULL,
  `data_entrada` date NOT NULL,
  `data_saida` date NOT NULL,
  PRIMARY KEY (`id_manu`),
  UNIQUE KEY `id_manu` (`id_manu`),
  KEY `num_serie` (`num_serie`),
  KEY `filial_id` (`filial_id`),
  CONSTRAINT `manutencao_ibfk_1` FOREIGN KEY (`num_serie`) REFERENCES `impressoras` (`num_serie`),
  CONSTRAINT `manutencao_ibfk_2` FOREIGN KEY (`filial_id`) REFERENCES `filiais` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manutencao`
--

LOCK TABLES `manutencao` WRITE;
/*!40000 ALTER TABLE `manutencao` DISABLE KEYS */;
/*!40000 ALTER TABLE `manutencao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-05 16:18:21
