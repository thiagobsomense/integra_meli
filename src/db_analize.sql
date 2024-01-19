-- MySQL dump 10.13  Distrib 8.1.0, for Win64 (x86_64)
--
-- Host: localhost    Database: db_analize
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `charge_info_mercado_livre`
--

DROP TABLE IF EXISTS `charge_info_mercado_livre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `charge_info_mercado_livre` (
  `document_id` varchar(255) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `legal_document_number` varchar(100) DEFAULT NULL,
  `legal_document_status` varchar(100) DEFAULT NULL,
  `legal_document_status_description` varchar(100) DEFAULT NULL,
  `creation_date_time` timestamp NULL DEFAULT NULL,
  `detail_id` bigint DEFAULT NULL,
  `transaction_detail` varchar(100) DEFAULT NULL,
  `debited_from_operation` varchar(100) DEFAULT NULL,
  `debited_from_operation_description` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `status_description` varchar(100) DEFAULT NULL,
  `charge_bonified_id` varchar(100) DEFAULT NULL,
  `detail_amount` decimal(10,2) DEFAULT NULL,
  `detail_type` varchar(100) DEFAULT NULL,
  `detail_sub_type` varchar(100) DEFAULT NULL,
  `charge_amount_without_discount` decimal(10,2) DEFAULT NULL,
  `discount_amount` decimal(10,2) DEFAULT NULL,
  `discount_reason` varchar(100) DEFAULT NULL,
  `shipping_id` varchar(100) DEFAULT NULL,
  `pack_id` varchar(100) DEFAULT NULL,
  `receiver_shipping_cost` decimal(10,2) DEFAULT NULL,
  `marketplace` varchar(100) DEFAULT NULL,
  `currency_id` varchar(100) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`document_id`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cliente_loja_mercado_livre`
--

DROP TABLE IF EXISTS `cliente_loja_mercado_livre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente_loja_mercado_livre` (
  `id_cliente` int NOT NULL,
  `id_loja` int NOT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_cliente`,`id_loja`),
  KEY `id_loja` (`id_loja`),
  CONSTRAINT `cliente_loja_mercado_livre_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`ID`),
  CONSTRAINT `cliente_loja_mercado_livre_ibfk_2` FOREIGN KEY (`id_loja`) REFERENCES `ml_loja` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cliente_loja_shopee`
--

DROP TABLE IF EXISTS `cliente_loja_shopee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente_loja_shopee` (
  `id_cliente` int NOT NULL,
  `id_loja` int NOT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_cliente`,`id_loja`),
  KEY `id_loja` (`id_loja`),
  CONSTRAINT `cliente_loja_shopee_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`ID`),
  CONSTRAINT `cliente_loja_shopee_ibfk_2` FOREIGN KEY (`id_loja`) REFERENCES `loja_shopee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `senha` varchar(255) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `data_vencimento` timestamp NOT NULL,
  `ativo` tinyint(1) DEFAULT '1',
  `root` tinyint(1) DEFAULT '0',
  `modulo_shopee` tinyint(1) DEFAULT '0',
  `modulo_bling` tinyint(1) DEFAULT '0',
  `modulo_ads` tinyint(1) DEFAULT '0',
  `modulo_api` tinyint(1) DEFAULT '0',
  `modulo_mercado_livre` tinyint(1) DEFAULT '0',
  `qtd_lojas` int DEFAULT '3',
  `qtd_lojas_mercadolivreint` int DEFAULT '3',
  `email` varchar(255) DEFAULT NULL,
  `telefone` varchar(255) DEFAULT NULL,
  `cnpj` varchar(255) DEFAULT NULL,
  `modulo_shein` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_nome_clientes` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `itens_shopee`
--

DROP TABLE IF EXISTS `itens_shopee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itens_shopee` (
  `shop_id` int NOT NULL,
  `item_id` varchar(255) NOT NULL,
  `item_sku` varchar(255) NOT NULL,
  `model_id` varchar(255) NOT NULL,
  `model_sku` varchar(255) NOT NULL,
  `preco_custo` decimal(10,2) DEFAULT '0.00',
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`shop_id`,`item_id`,`model_id`),
  KEY `ix_itens_shopee_shop_item` (`shop_id`,`item_id`),
  KEY `ix_itens_shopee_shop` (`shop_id`),
  CONSTRAINT `itens_shopee_ibfk_1` FOREIGN KEY (`shop_id`, `item_id`, `model_id`) REFERENCES `pedidos_itens` (`shop_id`, `item_id`, `model_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `loja_shopee`
--

DROP TABLE IF EXISTS `loja_shopee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loja_shopee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `acess_token` varchar(255) DEFAULT NULL,
  `refresh_token` varchar(255) DEFAULT NULL,
  `shop_id` int DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `ativo` tinyint(1) DEFAULT '1',
  `is_conected` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_shop_id_loja` (`shop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_faturamento_detalhes`
--

DROP TABLE IF EXISTS `ml_faturamento_detalhes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_faturamento_detalhes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `legal_document_number` varchar(255) DEFAULT NULL,
  `legal_document_status` varchar(45) DEFAULT NULL,
  `legal_document_status_description` varchar(150) DEFAULT NULL,
  `creation_date_time` timestamp NULL DEFAULT NULL,
  `detail_id` varchar(255) DEFAULT NULL,
  `transaction_detail` varchar(255) DEFAULT NULL,
  `debited_from_operation` varchar(20) DEFAULT NULL,
  `debited_from_operation_description` varchar(20) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `status_description` varchar(255) DEFAULT NULL,
  `charge_bonified_id` varchar(255) DEFAULT NULL,
  `detail_amount` decimal(20,2) NOT NULL,
  `detail_type` varchar(45) DEFAULT NULL,
  `detail_sub_type` varchar(45) DEFAULT NULL,
  `charge_amount_without_discount` decimal(20,2) NOT NULL,
  `discount_amount` decimal(20,2) NOT NULL,
  `discount_reason` varchar(255) DEFAULT NULL,
  `sales_info_json` text,
  `shipping_id` varchar(255) DEFAULT NULL,
  `pack_id` varchar(100) DEFAULT NULL,
  `receiver_shipping_cost` decimal(20,2) DEFAULT '0.00',
  `items_info_json` text,
  `document_id` varchar(255) DEFAULT NULL,
  `marketplace` varchar(255) DEFAULT NULL,
  `currency_id` varchar(45) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5602 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_faturamento_documentos`
--

DROP TABLE IF EXISTS `ml_faturamento_documentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_faturamento_documentos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `document_id` varchar(255) DEFAULT NULL,
  `associated_document_id` varchar(255) DEFAULT NULL,
  `expiration_date` date DEFAULT NULL,
  `amount` decimal(20,2) NOT NULL,
  `unpaid_amount` decimal(20,2) DEFAULT NULL,
  `document_status` varchar(20) DEFAULT NULL,
  `site_id` varchar(20) DEFAULT NULL,
  `period_date_from` date DEFAULT NULL,
  `period_date_to` date DEFAULT NULL,
  `currency_id` varchar(20) DEFAULT NULL,
  `count_details` varchar(20) DEFAULT NULL,
  `files_json` text,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1048 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_faturamento_garantias`
--

DROP TABLE IF EXISTS `ml_faturamento_garantias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_faturamento_garantias` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `legal_document_number` varchar(255) DEFAULT NULL,
  `legal_document_status` varchar(45) DEFAULT NULL,
  `legal_document_status_description` varchar(150) DEFAULT NULL,
  `creation_date_time` timestamp NULL DEFAULT NULL,
  `detail_id` varchar(255) DEFAULT NULL,
  `transaction_detail` varchar(255) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `status_description` varchar(255) DEFAULT NULL,
  `charge_bonified_id` varchar(255) DEFAULT NULL,
  `detail_type` varchar(45) DEFAULT NULL,
  `detail_sub_type` varchar(45) DEFAULT NULL,
  `concept_type` varchar(100) DEFAULT NULL,
  `warranty_info_json` text,
  `prepaid_info_json` text,
  `document_id` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_faturamento_logistica_full`
--

DROP TABLE IF EXISTS `ml_faturamento_logistica_full`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_faturamento_logistica_full` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `legal_document_number` varchar(255) DEFAULT NULL,
  `legal_document_status` varchar(45) DEFAULT NULL,
  `legal_document_status_description` varchar(150) DEFAULT NULL,
  `creation_date_time` timestamp NULL DEFAULT NULL,
  `detail_id` varchar(255) DEFAULT NULL,
  `detail_amount` decimal(20,2) DEFAULT NULL,
  `transaction_detail` varchar(255) DEFAULT NULL,
  `charge_bonified_id` varchar(255) DEFAULT NULL,
  `detail_type` varchar(45) DEFAULT NULL,
  `detail_sub_type` varchar(45) DEFAULT NULL,
  `concept_type` varchar(100) DEFAULT NULL,
  `payment_id` varchar(255) DEFAULT NULL,
  `type` varchar(45) NOT NULL,
  `amount_per_unit` decimal(20,2) DEFAULT NULL,
  `amount` decimal(20,2) DEFAULT NULL,
  `sku` varchar(255) DEFAULT NULL,
  `ean` varchar(255) DEFAULT NULL,
  `item_id` varchar(255) DEFAULT NULL,
  `item_title` varchar(255) DEFAULT NULL,
  `variation` varchar(255) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `volume_type` varchar(255) DEFAULT NULL,
  `inventory_id` varchar(255) DEFAULT NULL,
  `inbound_id` varchar(255) DEFAULT NULL,
  `volume_unit` varchar(10) DEFAULT NULL,
  `amount_per_volume_unit` decimal(20,2) DEFAULT NULL,
  `volume` decimal(20,5) DEFAULT NULL,
  `volume_total` decimal(20,5) DEFAULT NULL,
  `document_id` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_faturamento_periodos`
--

DROP TABLE IF EXISTS `ml_faturamento_periodos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_faturamento_periodos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `amount` decimal(20,2) NOT NULL,
  `unpaid_amount` decimal(20,2) DEFAULT NULL,
  `period_date_from` date DEFAULT NULL,
  `period_date_to` date DEFAULT NULL,
  `expiration_date` date DEFAULT NULL,
  `debt_expiration_date` date DEFAULT NULL,
  `debt_expiration_date_move_reason` date DEFAULT NULL,
  `debt_expiration_date_move_reason_description` date DEFAULT NULL,
  `period_status` varchar(100) NOT NULL,
  `is_documents` tinyint(1) DEFAULT '0',
  `is_summary` tinyint(1) DEFAULT '0',
  `is_details` tinyint(1) DEFAULT '0',
  `is_insurtech` tinyint(1) DEFAULT '0',
  `is_fulfillment` tinyint(1) DEFAULT '0',
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=584 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_faturamento_resumo`
--

DROP TABLE IF EXISTS `ml_faturamento_resumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_faturamento_resumo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `period_date_from` date DEFAULT NULL,
  `period_date_to` date DEFAULT NULL,
  `expiration_date` date DEFAULT NULL,
  `amount` decimal(20,2) NOT NULL,
  `credit_note` decimal(20,2) DEFAULT NULL,
  `tax` decimal(20,2) DEFAULT NULL,
  `bonuses_json` text,
  `charges_json` text,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=230 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_logs`
--

DROP TABLE IF EXISTS `ml_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_logs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `step` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `init_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `end_at` datetime DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `body` text,
  `solved` tinyint DEFAULT NULL,
  `solved_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1424 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_loja`
--

DROP TABLE IF EXISTS `ml_loja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_loja` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `access_token` varchar(255) DEFAULT NULL,
  `token_type` varchar(255) DEFAULT NULL,
  `expires_in` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `refresh_token` varchar(255) DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `last_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ix_user_id_loja` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_nota_fiscal`
--

DROP TABLE IF EXISTS `ml_nota_fiscal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_nota_fiscal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `ml_order_id` varchar(255) NOT NULL,
  `status` varchar(45) NOT NULL,
  `transaction_status` varchar(45) NOT NULL,
  `issuer_json` text,
  `recipient_json` text,
  `shipment_json` text,
  `items_json` text,
  `issued_date` varchar(45) DEFAULT NULL,
  `invoice_key` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `invoice_series` int DEFAULT NULL,
  `invoice_number` bigint DEFAULT NULL,
  `attributes_json` text,
  `fiscal_data_json` text,
  `amount` decimal(20,2) DEFAULT NULL,
  `items_amount` decimal(20,2) DEFAULT NULL,
  `errors_json` text,
  `items_quantity` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8020 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_pedidos`
--

DROP TABLE IF EXISTS `ml_pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_pedidos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `ml_order_id` varchar(255) NOT NULL,
  `fulfilled` tinyint(1) DEFAULT NULL,
  `expiration_date` timestamp NULL DEFAULT NULL,
  `date_closed` timestamp NULL DEFAULT NULL,
  `last_updated` timestamp NULL DEFAULT NULL,
  `date_created` timestamp NULL DEFAULT NULL,
  `manufacturing_ending_date` timestamp NULL DEFAULT NULL,
  `shipping_id` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `paid_amount` decimal(10,2) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `claim_id` varchar(255) DEFAULT NULL,
  `claim_status` varchar(45) DEFAULT NULL,
  `claim_try_number` int DEFAULT '0',
  `claim_last_updated` timestamp NULL DEFAULT NULL,
  `claim_resource_type` varchar(255) DEFAULT NULL,
  `claim_date_closed` timestamp NULL DEFAULT NULL,
  `payment_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`,`user_id`,`ml_order_id`),
  UNIQUE KEY `ml_order_id` (`ml_order_id`),
  UNIQUE KEY `ml_order_id_UNIQUE` (`ml_order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24131 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_pedidos_devolucao`
--

DROP TABLE IF EXISTS `ml_pedidos_devolucao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_pedidos_devolucao` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `ml_order_id` varchar(255) NOT NULL,
  `resource_id` varchar(45) DEFAULT NULL,
  `resource` varchar(45) DEFAULT NULL,
  `claim_id` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `subtype` varchar(45) DEFAULT NULL,
  `status_money` varchar(45) DEFAULT NULL,
  `refund_at` varchar(45) DEFAULT NULL,
  `shipping_json` text,
  `warehouse_review_json` text,
  `date_created` varchar(45) DEFAULT NULL,
  `last_updated` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_pedidos_envios`
--

DROP TABLE IF EXISTS `ml_pedidos_envios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_pedidos_envios` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `ml_order_id` varchar(255) NOT NULL,
  `substatus_history_json` text,
  `snapshot_packing_json` text,
  `receiver_id` varchar(255) DEFAULT NULL,
  `base_cost` decimal(10,2) DEFAULT NULL,
  `cost_components_json` text,
  `type` varchar(45) DEFAULT NULL,
  `return_details_json` text,
  `sender_id` varchar(255) NOT NULL,
  `mode` varchar(45) DEFAULT NULL,
  `order_cost` decimal(10,2) DEFAULT NULL,
  `priority_class_json` text,
  `service_id` varchar(45) DEFAULT NULL,
  `tracking_number` varchar(45) DEFAULT NULL,
  `shipping_id` varchar(255) NOT NULL,
  `shipping_items_json` text,
  `tracking_method` varchar(45) DEFAULT NULL,
  `last_updated` timestamp NULL DEFAULT NULL,
  `items_types_json` text,
  `comments` varchar(255) DEFAULT NULL,
  `substatus` varchar(255) DEFAULT NULL,
  `date_created` timestamp NULL DEFAULT NULL,
  `date_first_printed` timestamp NULL DEFAULT NULL,
  `created_by` varchar(45) DEFAULT NULL,
  `application_id` varchar(45) DEFAULT NULL,
  `return_tracking_number` varchar(45) DEFAULT NULL,
  `site_id` varchar(45) DEFAULT NULL,
  `carrier_info` varchar(45) DEFAULT NULL,
  `market_place` varchar(45) DEFAULT NULL,
  `customer_id` varchar(45) DEFAULT NULL,
  `quotation` varchar(255) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `logistic_type` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`user_id`,`ml_order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20444 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_pedidos_itens`
--

DROP TABLE IF EXISTS `ml_pedidos_itens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_pedidos_itens` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `ml_order_id` varchar(255) NOT NULL,
  `seq` int NOT NULL,
  `ml_item_id` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `category_id` varchar(255) NOT NULL,
  `variation_id` varchar(255) NOT NULL,
  `seller_custom_field` varchar(255) DEFAULT NULL,
  `global_price` decimal(10,2) DEFAULT '0.00',
  `net_weight` varchar(255) DEFAULT NULL,
  `warranty` varchar(255) DEFAULT NULL,
  `condition_item` varchar(255) DEFAULT NULL,
  `seller_sku` varchar(255) DEFAULT NULL,
  `quantity` decimal(10,0) DEFAULT NULL,
  `unit_price` decimal(10,2) DEFAULT '0.00',
  `full_unit_price` decimal(10,2) DEFAULT '0.00',
  `currency_id` varchar(255) DEFAULT NULL,
  `manufacturing_days` varchar(255) DEFAULT NULL,
  `picked_quantity` varchar(255) DEFAULT NULL,
  `listing_type_id` varchar(255) DEFAULT NULL,
  `base_exchange_rate` varchar(255) DEFAULT NULL,
  `base_currency_id` varchar(255) DEFAULT NULL,
  `bundle` varchar(255) DEFAULT NULL,
  `element_id` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`user_id`,`ml_order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24180 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ml_pedidos_pagamentos`
--

DROP TABLE IF EXISTS `ml_pedidos_pagamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ml_pedidos_pagamentos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `ml_order_id` varchar(255) NOT NULL,
  `payment_id` varchar(255) NOT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `status_code` varchar(255) DEFAULT NULL,
  `total_paid_amount` varchar(255) DEFAULT NULL,
  `operation_type` varchar(255) DEFAULT NULL,
  `transaction_amount` varchar(255) DEFAULT NULL,
  `transaction_amount_refunded` int DEFAULT NULL,
  `date_approved` varchar(255) DEFAULT NULL,
  `collector_id` varchar(255) DEFAULT NULL,
  `coupon_id` varchar(255) DEFAULT NULL,
  `installments` int DEFAULT NULL,
  `authorization_code` varchar(255) DEFAULT NULL,
  `taxes_amount` varchar(255) DEFAULT NULL,
  `date_last_modified` varchar(255) DEFAULT NULL,
  `coupon_amount` varchar(255) DEFAULT NULL,
  `shipping_cost` varchar(255) DEFAULT NULL,
  `installment_amount` varchar(255) DEFAULT NULL,
  `date_created` varchar(255) DEFAULT NULL,
  `activation_uri` varchar(255) DEFAULT NULL,
  `overpaid_amount` varchar(255) DEFAULT NULL,
  `card_id` varchar(255) DEFAULT NULL,
  `status_detail` varchar(255) DEFAULT NULL,
  `issuer_id` varchar(255) DEFAULT NULL,
  `payment_method_id` varchar(255) DEFAULT NULL,
  `payment_type` varchar(255) DEFAULT NULL,
  `deferred_period` varchar(255) DEFAULT NULL,
  `atm_transfer_reference_transaction_id` varchar(255) DEFAULT NULL,
  `atm_transfer_reference_company_id` varchar(255) DEFAULT NULL,
  `site_id` varchar(255) DEFAULT NULL,
  `payer_id` varchar(255) DEFAULT NULL,
  `order_id` varchar(255) DEFAULT NULL,
  `currency_id` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `transaction_order_id` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`,`user_id`,`ml_order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25149 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pagamentos_shopee`
--

DROP TABLE IF EXISTS `pagamentos_shopee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagamentos_shopee` (
  `shop_id` int NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  `wallet_type` varchar(255) DEFAULT NULL,
  `transaction_type` varchar(255) DEFAULT NULL,
  `amount` decimal(15,2) DEFAULT NULL,
  `current_balance` decimal(15,2) DEFAULT NULL,
  `create_time` varchar(255) DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `order_sn` varchar(255) DEFAULT NULL,
  `refund_sn` varchar(255) DEFAULT NULL,
  `withdrawal_type` varchar(255) DEFAULT NULL,
  `transaction_fee` decimal(15,2) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `withdrawal_id` varchar(255) DEFAULT NULL,
  `root_withdrawal_id` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`shop_id`,`transaction_id`),
  KEY `ix_dt_pgto` (`create_time`),
  KEY `ix_shop_id` (`shop_id`),
  KEY `ix_shop_id_order_sn` (`shop_id`,`order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedidos`
--

DROP TABLE IF EXISTS `pedidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `order_status` varchar(255) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`shop_id`,`order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedidos_dados`
--

DROP TABLE IF EXISTS `pedidos_dados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos_dados` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `cancel_by` varchar(255) DEFAULT NULL,
  `cancel_reason` varchar(255) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `days_to_ship` int DEFAULT NULL,
  `pay_time` timestamp NULL DEFAULT NULL,
  `payment_method` varchar(255) DEFAULT NULL,
  `prescription_check_status` varchar(255) DEFAULT NULL,
  `region` varchar(255) DEFAULT NULL,
  `reverse_shipping_fee` decimal(15,2) DEFAULT NULL,
  `ship_by_date` timestamp NULL DEFAULT NULL,
  `update_time` timestamp NULL DEFAULT NULL,
  `package_number` varchar(255) DEFAULT NULL,
  `logistics_status` varchar(255) DEFAULT NULL,
  `shipping_carrier` varchar(255) DEFAULT NULL,
  `parcel_chargeable_weight_gram` decimal(15,2) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`shop_id`,`order_sn`),
  KEY `ix_pd_shop_id_order_sn` (`shop_id`,`order_sn`),
  CONSTRAINT `pedidos_dados_ibfk_1` FOREIGN KEY (`shop_id`, `order_sn`) REFERENCES `pedidos` (`shop_id`, `order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedidos_entrega`
--

DROP TABLE IF EXISTS `pedidos_entrega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos_entrega` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `ra_name` varchar(255) DEFAULT NULL,
  `ra_phone` varchar(255) DEFAULT NULL,
  `ra_town` varchar(255) DEFAULT NULL,
  `ra_district` varchar(255) DEFAULT NULL,
  `ra_city` varchar(255) DEFAULT NULL,
  `ra_state` varchar(255) DEFAULT NULL,
  `ra_region` varchar(255) DEFAULT NULL,
  `ra_zipcode` varchar(255) DEFAULT NULL,
  `ra_full_address` varchar(255) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`shop_id`,`order_sn`),
  CONSTRAINT `pedidos_entrega_ibfk_1` FOREIGN KEY (`shop_id`, `order_sn`) REFERENCES `pedidos` (`shop_id`, `order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedidos_escrow`
--

DROP TABLE IF EXISTS `pedidos_escrow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos_escrow` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `actual_shipping_fee` decimal(15,2) DEFAULT NULL,
  `buyer_paid_shipping_fee` decimal(15,2) DEFAULT NULL,
  `buyer_total_amount` decimal(15,2) DEFAULT NULL,
  `buyer_transaction_fee` decimal(15,2) DEFAULT NULL,
  `campaign_fee` decimal(15,2) DEFAULT NULL,
  `coins` decimal(15,2) DEFAULT NULL,
  `commission_fee` decimal(15,2) DEFAULT NULL,
  `cost_of_goods_sold` decimal(15,2) DEFAULT NULL,
  `credit_card_promotion` decimal(15,2) DEFAULT NULL,
  `credit_card_transaction_fee` decimal(15,2) DEFAULT NULL,
  `cross_border_tax` decimal(15,2) DEFAULT NULL,
  `delivery_seller_protection_fee_premium_amount` decimal(15,2) DEFAULT NULL,
  `drc_adjustable_refund` decimal(15,2) DEFAULT NULL,
  `escrow_amount` decimal(15,2) DEFAULT NULL,
  `escrow_tax` decimal(15,2) DEFAULT NULL,
  `estimated_shipping_fee` decimal(15,2) DEFAULT NULL,
  `final_escrow_product_gst` decimal(15,2) DEFAULT NULL,
  `final_escrow_shipping_gst` decimal(15,2) DEFAULT NULL,
  `final_product_protection` decimal(15,2) DEFAULT NULL,
  `final_product_vat_tax` decimal(15,2) DEFAULT NULL,
  `final_return_to_seller_shipping_fee` decimal(15,2) DEFAULT NULL,
  `final_shipping_fee` decimal(15,2) DEFAULT NULL,
  `final_shipping_vat_tax` decimal(15,2) DEFAULT NULL,
  `order_chargeable_weight` decimal(15,2) DEFAULT NULL,
  `original_cost_of_goods_sold` decimal(15,2) DEFAULT NULL,
  `original_price` decimal(15,2) DEFAULT NULL,
  `original_shopee_discount` decimal(15,2) DEFAULT NULL,
  `payment_promotion` decimal(15,2) DEFAULT NULL,
  `reverse_shipping_fee` decimal(15,2) DEFAULT NULL,
  `rsf_seller_protection_fee_claim_amount` decimal(15,2) DEFAULT NULL,
  `rsf_seller_protection_fee_premium_amount` decimal(15,2) DEFAULT NULL,
  `seller_coin_cash_back` decimal(15,2) DEFAULT NULL,
  `seller_discount` decimal(15,2) DEFAULT NULL,
  `seller_lost_compensation` decimal(15,2) DEFAULT NULL,
  `seller_return_refund` decimal(15,2) DEFAULT NULL,
  `seller_shipping_discount` decimal(15,2) DEFAULT NULL,
  `seller_transaction_fee` decimal(15,2) DEFAULT NULL,
  `service_fee` decimal(15,2) DEFAULT NULL,
  `shipping_fee_discount_from_3pl` decimal(15,2) DEFAULT NULL,
  `shopee_discount` decimal(15,2) DEFAULT NULL,
  `shopee_shipping_rebate` decimal(15,2) DEFAULT NULL,
  `voucher_from_seller` decimal(15,2) DEFAULT NULL,
  `voucher_from_shopee` decimal(15,2) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`shop_id`,`order_sn`),
  CONSTRAINT `pedidos_escrow_ibfk_1` FOREIGN KEY (`shop_id`, `order_sn`) REFERENCES `pedidos` (`shop_id`, `order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedidos_itens`
--

DROP TABLE IF EXISTS `pedidos_itens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos_itens` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `seq` int NOT NULL,
  `activity_id` text,
  `activity_type` varchar(50) DEFAULT NULL,
  `discount_from_coin` decimal(10,2) DEFAULT NULL,
  `discount_from_voucher_seller` decimal(10,2) DEFAULT NULL,
  `discount_from_voucher_shopee` decimal(10,2) DEFAULT NULL,
  `discounted_price` decimal(10,2) DEFAULT NULL,
  `is_b2c_shop_item` tinyint(1) DEFAULT NULL,
  `is_main_item` tinyint(1) DEFAULT NULL,
  `item_id` varchar(255) DEFAULT NULL,
  `item_name` text,
  `item_sku` varchar(50) DEFAULT NULL,
  `model_id` varchar(255) DEFAULT NULL,
  `model_name` varchar(255) DEFAULT NULL,
  `model_sku` varchar(50) DEFAULT NULL,
  `original_price` decimal(10,2) DEFAULT NULL,
  `quantity_purchased` int DEFAULT NULL,
  `seller_discount` decimal(10,2) DEFAULT NULL,
  `shopee_discount` decimal(10,2) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`shop_id`,`order_sn`,`seq`),
  KEY `shop_id` (`shop_id`,`order_sn`),
  KEY `item_id` (`item_id`),
  KEY `item_sku` (`item_sku`),
  KEY `shop_id_2` (`shop_id`,`item_id`,`model_id`),
  CONSTRAINT `pedidos_itens_ibfk_1` FOREIGN KEY (`shop_id`, `order_sn`) REFERENCES `pedidos` (`shop_id`, `order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedidos_nota`
--

DROP TABLE IF EXISTS `pedidos_nota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos_nota` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `ia_number` varchar(255) DEFAULT NULL,
  `ia_series_number` varchar(255) DEFAULT NULL,
  `ia_access_key` varchar(255) DEFAULT NULL,
  `ia_issue_date` timestamp NULL DEFAULT NULL,
  `ia_total_value` decimal(15,2) DEFAULT NULL,
  `ia_products_total_value` decimal(15,2) DEFAULT NULL,
  `ia_tax_code` varchar(255) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`shop_id`,`order_sn`),
  CONSTRAINT `pedidos_nota_ibfk_1` FOREIGN KEY (`shop_id`, `order_sn`) REFERENCES `pedidos` (`shop_id`, `order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pedidos_tracking_number`
--

DROP TABLE IF EXISTS `pedidos_tracking_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos_tracking_number` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `tracking_number` varchar(255) DEFAULT NULL,
  `data_criacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`shop_id`,`order_sn`),
  CONSTRAINT `pedidos_tracking_number_ibfk_1` FOREIGN KEY (`shop_id`, `order_sn`) REFERENCES `pedidos` (`shop_id`, `order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `processamento_shopee`
--

DROP TABLE IF EXISTS `processamento_shopee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `processamento_shopee` (
  `seq_geral` bigint NOT NULL,
  `shop_id` int NOT NULL,
  `periodo_processo_ini` timestamp NOT NULL,
  `periodo_processo_fim` timestamp NOT NULL,
  `data_ini` timestamp NOT NULL,
  `data_fim` timestamp NULL DEFAULT NULL,
  `status_processo` varchar(25) NOT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`seq_geral`,`shop_id`),
  KEY `shop_id_idx` (`shop_id`),
  KEY `status_processo_idx` (`status_processo`),
  CONSTRAINT `processamento_shopee_ibfk_1` FOREIGN KEY (`seq_geral`) REFERENCES `processamento_shopee_geral` (`seq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `processamento_shopee_geral`
--

DROP TABLE IF EXISTS `processamento_shopee_geral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `processamento_shopee_geral` (
  `seq` bigint NOT NULL AUTO_INCREMENT,
  `qtd_lojas` int NOT NULL,
  `rotina` varchar(255) NOT NULL,
  `processo` varchar(255) NOT NULL,
  `periodo_processo_ini` timestamp NOT NULL,
  `periodo_processo_fim` timestamp NOT NULL,
  `data_ini` timestamp NOT NULL,
  `data_fim` timestamp NULL DEFAULT NULL,
  `status_processo` varchar(25) NOT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`seq`),
  KEY `status_processo_idx` (`status_processo`),
  KEY `rotina_processo_idx` (`rotina`),
  KEY `processo_processo_idx` (`processo`)
) ENGINE=InnoDB AUTO_INCREMENT=362 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `return_shopee`
--

DROP TABLE IF EXISTS `return_shopee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `return_shopee` (
  `shop_id` int NOT NULL,
  `return_sn` varchar(255) NOT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `text_reason` text,
  `refund_amount` decimal(15,2) DEFAULT NULL,
  `create_time` varchar(255) DEFAULT NULL,
  `update_time` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `due_date` varchar(255) DEFAULT NULL,
  `tracking_number` varchar(255) DEFAULT NULL,
  `amount_before_discount` decimal(15,2) DEFAULT NULL,
  `order_sn` varchar(255) DEFAULT NULL,
  `return_ship_due_date` varchar(255) DEFAULT NULL,
  `return_seller_due_date` varchar(255) DEFAULT NULL,
  `negotiation_status` varchar(255) DEFAULT NULL,
  `seller_proof_status` varchar(255) DEFAULT NULL,
  `seller_compensation_status` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`shop_id`,`return_sn`),
  KEY `shop_id` (`shop_id`,`return_sn`),
  KEY `order_sn` (`order_sn`),
  KEY `create_time` (`create_time`),
  KEY `tracking_number` (`tracking_number`),
  KEY `ix_return_shopee_order_shop2` (`shop_id`,`order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `return_shopee_itens`
--

DROP TABLE IF EXISTS `return_shopee_itens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `return_shopee_itens` (
  `cont` int NOT NULL,
  `shop_id` int NOT NULL,
  `return_sn` varchar(255) NOT NULL,
  `item_id` varchar(255) DEFAULT NULL,
  `model_id` text,
  `name` text,
  `amount` decimal(15,2) DEFAULT NULL,
  `item_price` decimal(15,2) DEFAULT NULL,
  `is_add_on_deal` tinyint(1) DEFAULT NULL,
  `is_main_item` tinyint(1) DEFAULT NULL,
  `item_sku` varchar(255) DEFAULT NULL,
  `variation_sku` varchar(255) DEFAULT NULL,
  `add_on_deal_id` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cont`,`shop_id`,`return_sn`),
  KEY `shop_id` (`shop_id`,`return_sn`),
  CONSTRAINT `return_shopee_itens_ibfk_1` FOREIGN KEY (`shop_id`, `return_sn`) REFERENCES `return_shopee` (`shop_id`, `return_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sales_info_mercado_livre`
--

DROP TABLE IF EXISTS `sales_info_mercado_livre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_info_mercado_livre` (
  `document_id` varchar(255) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `seq` int DEFAULT NULL,
  `order_id` varchar(255) DEFAULT NULL,
  `operation_id` bigint DEFAULT NULL,
  `sale_date_time` timestamp NULL DEFAULT NULL,
  `sales_channel` varchar(50) DEFAULT NULL,
  `payer_nickname` varchar(100) DEFAULT NULL,
  `state_name` varchar(50) DEFAULT NULL,
  `transaction_amount` decimal(10,2) DEFAULT NULL,
  `charge_info_id` int DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  KEY `document_id` (`document_id`,`user_id`),
  CONSTRAINT `sales_info_mercado_livre_ibfk_1` FOREIGN KEY (`document_id`, `user_id`) REFERENCES `charge_info_mercado_livre` (`document_id`, `user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tracking_info_itens`
--

DROP TABLE IF EXISTS `tracking_info_itens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tracking_info_itens` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `logistics_status` varchar(255) DEFAULT NULL,
  `update_time` timestamp NOT NULL,
  `description` text,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`shop_id`,`order_sn`,`update_time`),
  KEY `shop_id` (`shop_id`),
  KEY `order_sn` (`order_sn`),
  KEY `ix_update` (`update_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tracking_info_pai`
--

DROP TABLE IF EXISTS `tracking_info_pai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tracking_info_pai` (
  `shop_id` int NOT NULL,
  `order_sn` varchar(255) NOT NULL,
  `logistics_status` varchar(255) DEFAULT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`shop_id`,`order_sn`),
  KEY `shop_id` (`shop_id`),
  KEY `order_sn` (`order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-19  7:37:26
