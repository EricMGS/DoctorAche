CREATE DATABASE `symptbotdb`
DEFAULT CHARACTER SET UTF8
DEFAULT COLLATE UTF8_GENERAL_CI;



USE `symptbotdb`;



CREATE TABLE IF NOT EXISTS `doencas` (

	`id_doenca` INT 			NOT NULL AUTO_INCREMENT,
    `nome` 		VARCHAR(250)  	NOT NULL,
    
    CONSTRAINT `pk_doenca` PRIMARY KEY (`id_doenca`)
    
)DEFAULT CHARSET = utf8;



CREATE TABLE IF NOT EXISTS `sintomas` (

	`id_sintoma` 	INT				NOT NULL AUTO_INCREMENT,
    `nome` 			VARCHAR(250)  	NOT NULL,
    
    CONSTRAINT `pk_sintoma` PRIMARY KEY (`id_sintoma`)
    
)DEFAULT CHARSET = utf8;



CREATE TABLE `doenca_sintoma` (
  `id_doenca`    INT		NOT NULL,
  `id_sintoma`   INT		NOT NULL,
  
  CONSTRAINT `id_doenca_sintoma`	PRIMARY KEY (`id_doenca`,`id_sintoma`),
  CONSTRAINT `fk_doenca`          	FOREIGN KEY (`id_doenca`)           		REFERENCES `doencas` (`id_doenca`),
  CONSTRAINT `fk_sintoma`      		FOREIGN KEY (`id_sintoma`)           		REFERENCES `sintomas` (`id_sintoma`)
  );
