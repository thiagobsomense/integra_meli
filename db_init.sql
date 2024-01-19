RENAME TABLE db_analize.loja_mercado_livre TO db_analize.ml_loja;
ALTER TABLE ml_loja ADD last_updated timestamp NULL DEFAULT CURRENT_TIMESTAMP;

DROP TABLE IF EXISTS db_analize.pedidos_pagamentos_mercado_livre;
DROP TABLE IF EXISTS db_analize.pedidos_itens_mercado_livre;
DROP TABLE IF EXISTS db_analize.pedidos_envios_mercado_livre;
DROP TABLE IF EXISTS db_analize.pedidos_mercado_livre;

DROP TABLE IF EXISTS db_analize.ml_pedidos_pagamentos;
DROP TABLE IF EXISTS db_analize.ml_pedidos_itens;
DROP TABLE IF EXISTS db_analize.ml_pedidos_envios;
DROP TABLE IF EXISTS db_analize.ml_pedidos_devolucao;
DROP TABLE IF EXISTS db_analize.ml_pedidos;
DROP TABLE IF EXISTS db_analize.ml_faturamento_periodos;
DROP TABLE IF EXISTS db_analize.ml_faturamento_documentos;
DROP TABLE IF EXISTS db_analize.ml_faturamento_resumo;
DROP TABLE IF EXISTS db_analize.ml_faturamento_detalhes;
DROP TABLE IF EXISTS db_analize.ml_faturamento_garantias;
DROP TABLE IF EXISTS db_analize.ml_faturamento_logistica_full;


CREATE TABLE IF NOT EXISTS `ml_loja` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `access_token` varchar(255) DEFAULT NULL,
  `token_type` varchar(255) DEFAULT NULL,
  `expires_in` varchar(255) DEFAULT NULL,
  `user_id` varchar(255) DEFAULT NULL,
  `refresh_token` varchar(255) DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `last_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_pedidos` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `ml_order_id` varchar(255) NOT NULL UNIQUE,
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
  `claim_id` varchar(255) NULL DEFAULT NULL,
  `claim_status` varchar(45) NULL DEFAULT NULL,
  `claim_try_number` int DEFAULT 0,
  `claim_last_updated` timestamp NULL DEFAULT NULL,
  `claim_resource_type` varchar(255) NULL DEFAULT NULL,
  `claim_date_closed` timestamp NULL DEFAULT NULL,
  `payment_id` varchar(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `user_id`, `ml_order_id`),
  UNIQUE INDEX `ml_order_id_UNIQUE` (`ml_order_id` ASC) VISIBLE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_pedidos_itens` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`, `user_id`, `ml_order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_pedidos_pagamentos` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`, `user_id`,`ml_order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_pedidos_envios` (
	`id` BIGINT NOT NULL AUTO_INCREMENT,
    `user_id` VARCHAR(255) NOT NULL,
	`ml_order_id` VARCHAR(255) NOT NULL,
    `substatus_history_json` TEXT NULL,
    `snapshot_packing_json` TEXT NULL,
    `receiver_id` VARCHAR(255) NULL,
    `base_cost` DECIMAL(10,2),
    `cost_components_json` TEXT NULL,
    `type` VARCHAR(45) NULL,
    `return_details_json` TEXT NULL,
    `sender_id` VARCHAR(255) NOT NULL,
    `mode` VARCHAR(45) NULL,
    `order_cost` DECIMAL(10,2),
    `priority_class_json` TEXT NULL,
    `service_id` VARCHAR(45) NULL,
    `tracking_number` VARCHAR(45) NULL,
    `shipping_id` VARCHAR(255) NOT NULL,
    `shipping_items_json` TEXT NULL,
    `tracking_method` VARCHAR(45) NULL,
    `last_updated` timestamp NULL DEFAULT NULL,
    `items_types_json` TEXT NULL,
    `comments` VARCHAR(255) NULL,
    `substatus` VARCHAR(255) NULL,
    `date_created` timestamp NULL DEFAULT NULL,
    `date_first_printed` timestamp NULL DEFAULT NULL,
    `created_by` VARCHAR(45) NULL,
    `application_id` VARCHAR(45) NULL,
    `return_tracking_number` VARCHAR(45) NULL,
    `site_id` VARCHAR(45) NULL,
    `carrier_info` VARCHAR(45) NULL,
    `market_place` VARCHAR(45) NULL,
    `customer_id` VARCHAR(45) NULL,
    `quotation` VARCHAR(255) NULL,
    `status` VARCHAR(45) NULL,
    `logistic_type` VARCHAR(255) null,
    `data_atualizacao` timestamp NULL DEFAULT NULL,
  	`data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`id`, `user_id`,`ml_order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_pedidos_devolucao` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(255) NOT NULL,
  `ml_order_id` VARCHAR(255) NOT NULL,
  `resource_id` VARCHAR(45) NULL,
  `resource` VARCHAR(45) NULL,
  `claim_id` VARCHAR(45) NULL,
  `status` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  `subtype` VARCHAR(45) NULL,
  `status_money` VARCHAR(45) NULL,
  `refund_at` VARCHAR(45) NULL,
  `shipping_json` TEXT NULL,
  `warehouse_review_json` TEXT NULL,
  `date_created` VARCHAR(45) NULL,
  `last_updated` VARCHAR(45) NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_nota_fiscal` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` VARCHAR(255) NOT NULL,
  `ml_order_id` VARCHAR(255) NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `transaction_status` VARCHAR(45) NOT NULL,
  `issuer_json` TEXT NULL,
  `recipient_json` TEXT NULL,
  `shipment_json` TEXT NULL,
  `items_json` TEXT NULL,
  `issued_date` VARCHAR(45) NULL,
  `invoice_series` INT NULL,
  `invoice_number` BIGINT NULL,
  `invoice_key` VARCHAR(255),
  `attributes_json` TEXT NULL,
  `fiscal_data_json` TEXT NULL,
  `amount` DECIMAL(20,2) NULL,
  `items_amount` DECIMAL(20,2) NULL,
  `errors_json` TEXT NULL,
  `items_quantity` INT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_faturamento_periodos` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `amount` DECIMAL(20,2) NOT NULL,
  `unpaid_amount` DECIMAL(20,2),
  `period_date_from` DATE NULL,
  `period_date_to` DATE NULL,
  `expiration_date` DATE NULL,
  `debt_expiration_date` DATE NULL,
  `debt_expiration_date_move_reason` DATE NULL,
  `debt_expiration_date_move_reason_description` DATE NULL,
  `period_status` varchar(100) NOT NULL,
  `is_documents` TINYINT(1) DEFAULT 0, 
  `is_summary` TINYINT(1) DEFAULT 0, 
  `is_details` TINYINT(1) DEFAULT 0, 
  `is_insurtech` TINYINT(1) DEFAULT 0, 
  `is_fulfillment` TINYINT(1) DEFAULT 0, 
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_faturamento_documentos` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `document_id` varchar(255) NULL,
  `associated_document_id` varchar(255) NULL,
  `expiration_date` DATE NULL,
  `amount` DECIMAL(20,2) NOT NULL,
  `unpaid_amount` DECIMAL(20,2),
  `document_status` varchar(20) NULL,
  `site_id` varchar(20) NULL,
  `period_date_from` DATE NULL,
  `period_date_to` DATE NULL,
  `currency_id` varchar(20) NULL,
  `count_details` varchar(20) NULL,
  `files_json` TEXT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_faturamento_resumo` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `period_date_from` DATE NULL,
  `period_date_to` DATE NULL,
  `expiration_date` DATE NULL,
  `amount` DECIMAL(20,2) NOT NULL,
  `credit_note` DECIMAL(20,2),
  `tax` DECIMAL(20,2),
  `bonuses_json` TEXT NULL,
  `charges_json` TEXT NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_faturamento_detalhes` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `legal_document_number` varchar(255) NULL,
  `legal_document_status` varchar(45) NULL,
  `legal_document_status_description` varchar(150) NULL,
  `creation_date_time` timestamp NULL DEFAULT NULL,
  `detail_id` varchar(255) NULL,
  `movement_id` varchar(255) NULL,
  `transaction_detail` varchar(255) NULL,
  `debited_from_operation` varchar(20) NULL,
  `debited_from_operation_description` varchar(20) NULL,
  `status` varchar(100) NULL,
  `status_description` varchar(255) NULL,
  `charge_bonified_id` varchar(255) NULL,
  `detail_amount` DECIMAL(20,2) NOT NULL,
  `detail_type` varchar(45) NULL,
  `detail_sub_type` varchar(45) NULL,
  `charge_amount_without_discount` DECIMAL(20,2) NOT NULL,
  `discount_amount` DECIMAL(20,2) NOT NULL,
  `discount_reason` varchar(255) NULL,
  `sales_info_json` TEXT NULL,
  `shipping_id` varchar(255) NULL,
  `pack_id` varchar(100) NULL,
  `receiver_shipping_cost` DECIMAL(20,2) DEFAULT '0.00',
  `items_info_json` TEXT NULL,
  `operation_info_json` TEXT NULL,
  `perception_info_json` TEXT NULL,
  `document_id` varchar(255) NULL,
  `marketplace` varchar(255) NULL,
  `currency_id` varchar(45) NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_faturamento_garantias` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `legal_document_number` varchar(255) NULL,
  `legal_document_status` varchar(45) NULL,
  `legal_document_status_description` varchar(150) NULL,
  `creation_date_time` timestamp NULL DEFAULT NULL,
  `detail_id` varchar(255) NULL,
  `transaction_detail` varchar(255) NULL,
  `status` varchar(100) NULL,
  `status_description` varchar(255) NULL,
  `charge_bonified_id` varchar(255) NULL,
  `detail_type` varchar(45) NULL,
  `detail_sub_type` varchar(45) NULL,
  `concept_type` varchar(100) NULL,
  `warranty_info_json` TEXT NULL,
  `prepaid_info_json` TEXT NULL,
  `document_id` varchar(255) NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_faturamento_logistica_full` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `key` varchar(20) NOT NULL,
  `group` varchar(20) NOT NULL,
  `document_type` varchar(45) NOT NULL,
  `legal_document_number` varchar(255) NULL,
  `legal_document_status` varchar(45) NULL,
  `legal_document_status_description` varchar(150) NULL,
  `creation_date_time` timestamp NULL DEFAULT NULL,
  `detail_id` varchar(255) NULL,
  `detail_amount` decimal(20,2) NULL,
  `transaction_detail` varchar(255) NULL,
  `charge_bonified_id` varchar(255) NULL,
  `detail_type` varchar(45) NULL,
  `detail_sub_type` varchar(45) NULL,
  `concept_type` varchar(100) NULL,
  `payment_id` varchar(255) NULL,
  `type` varchar(45) NOT NULL,
  `amount_per_unit` DECIMAL(20,2),
  `amount` DECIMAL(20,2),
  `sku` varchar(255) NULL,
  `ean` varchar(255) NULL,
  `item_id` varchar(255) NULL,
  `item_title` varchar(255) NULL,
  `variation` varchar(255) NULL,
  `quantity` INT NULL,
  `volume_type` varchar(255) NULL,
  `inventory_id` varchar(255) NULL,
  `inbound_id` varchar(255) NULL,
  `volume_unit` varchar(10) NULL,
  `amount_per_volume_unit` DECIMAL(20,2),
  `volume` DECIMAL(20,5) NULL,
  `volume_total` DECIMAL(20,5) NULL,
  `document_id` varchar(255) NULL,
  `data_atualizacao` timestamp NULL DEFAULT NULL,
  `data_insercao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE IF NOT EXISTS `ml_logs` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `step` VARCHAR(255) NOT NULL,
  `status` VARCHAR(255) NOT NULL,
  `init_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `end_at` DATETIME NULL,
  `message` VARCHAR(255) NULL,
  `body` TEXT NULL,
  `solved` TINYINT NULL,
  `solved_at` DATETIME NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;