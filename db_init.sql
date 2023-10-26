RENAME TABLE db_analize.loja_mercado_livre TO db_analize.ml_loja;
--ALTER TABLE ml_loja ADD last_updated timestamp NULL DEFAULT CURRENT_TIMESTAMP;

DROP TABLE IF EXISTS db_analize.pedidos_pagamentos_mercado_livre;
DROP TABLE IF EXISTS db_analize.pedidos_itens_mercado_livre;
DROP TABLE IF EXISTS db_analize.pedidos_envios_mercado_livre;
DROP TABLE IF EXISTS db_analize.pedidos_mercado_livre;

DROP TABLE IF EXISTS db_analize.ml_pedidos_pagamentos;
DROP TABLE IF EXISTS db_analize.ml_pedidos_itens;
DROP TABLE IF EXISTS db_analize.ml_pedidos_envios;
DROP TABLE IF EXISTS db_analize.ml_pedidos;
DROP TABLE IF EXISTS db_analize.ml_pedidos_devolucao;

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
  `claim_last_updated` timestamp NULL DEFAULT NULL,
  `claim_resource_type` varchar(255) NULL DEFAULT NULL,
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