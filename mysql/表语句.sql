CREATE TABLE history (
	ds datetime NOT NULL COMMENT '日期',
	confirm int(11) COMMENT '累计确诊病例',
	confirm_add int(11) COMMENT '新增确诊病例',
	suspect int(11) COMMENT '疑似病例',
	suspect_add int(11) COMMENT '新增疑似病例',
	heal int(11) COMMENT '累计治愈人数',
	heal_add int(11) COMMENT '新增治愈人数',
	dead int(11) COMMENT '累计死亡人数',
	dead_add int(11) COMMENT '新增死亡人数',
	PRIMARY KEY (ds) USING BTREE
	)ENGINE=InnoDB DEFAULT CHARSET=UTF8mb4;

CREATE TABLE details (
	id int(11) NOT NULL AUTO_INCREMENT,
	update_time datetime COMMENT '数据最后更新时间',
	province varchar(50) COMMENT '省份',
	city varchar(50) COMMENT '市区县',
	confirm int(11) COMMENT '累计确诊病例',
	confirm_add int(11) COMMENT '新增确诊病例',
	heal int(11) COMMENT '累计治愈人数',
	dead int(11) COMMENT '累计死亡人数',
	PRIMARY KEY (id)
	)ENGINE=InnoDB DEFAULT CHARSET=UTF8mb4;


CREATE database cov2020 CHARSET=utf8;

CREATE TABLE hotspot (
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	ds datetime NOT NULL,
	content varchar(255),
	)





