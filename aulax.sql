create database if not exists venda;
use venda;

CREATE TABLE if not exists TIPO_VEICULO (
     COD_TIPO_VEICULO 	INT NOT NULL AUTO_INCREMENT,
     DSC_TIPO_VEICULO 	VARCHAR (45) NOT NULL,
     CONSTRAINT PK_TIPO_VEICULO 
     PRIMARY KEY (COD_TIPO_VEICULO)
  ) ENGINE = INNODB;

CREATE TABLE if not exists MARCA (
     COD_MARCA 		INT NOT NULL AUTO_INCREMENT,
     NOM_MARCA 		VARCHAR (45) NOT NULL,
     NOM_MARCA_FIPE 	VARCHAR (45) NOT NULL,
     KEY_MARCA   		VARCHAR (45) NOT NULL,
     ID_MARCA_FIPE 		VARCHAR (45) NOT NULL,
     CONSTRAINT PK_MARCA PRIMARY KEY (COD_MARCA)
  ) ENGINE = INNODB;

CREATE TABLE if not exists TABELA (
     COD_VEICULO 		INT NOT NULL AUTO_INCREMENT,
     NOM_VEICULO 		VARCHAR (45) NOT NULL,
     NOM_VEICULO_FIPE 		VARCHAR (45),
     KEY_VEICULO 		VARCHAR (45),
     ID_VEICULO 			VARCHAR (45),
     COD_MARCA 		INT	NOT NULL,
     COD_TIPO_VEICULO 		INT 	NOT NULL,
     CONSTRAINT PK_TABELA PRIMARY KEY (COD_VEICULO),
     CONSTRAINT FK_TABELA_MARCA 
     FOREIGN KEY (COD_MARCA)
     REFERENCES MARCA (COD_MARCA),
     CONSTRAINT FK_TABELA_TIPO_VEICULO 
     FOREIGN KEY (COD_TIPO_VEICULO)
     REFERENCES TIPO_VEICULO (COD_TIPO_VEICULO)        
  ) ENGINE = INNODB;

CREATE TABLE if not exists MODELO (
     SEQ_MODELO 		INT NOT NULL AUTO_INCREMENT,
     DESC_MODELO 		VARCHAR (100) NOT NULL,
     KEY_MODELO_FIPE	VARCHAR (20) NOT NULL,
     COD_MODELO_FIPE 	VARCHAR (20) NOT NULL,
     ID_MODELO_FIPE 	VARCHAR (20) NOT NULL,
     COD_VEICULO 		INT NOT NULL,
     CONSTRAINT PK_MODELO PRIMARY KEY (SEQ_MODELO),
     CONSTRAINT FK_MODELO_VEICULO 
     FOREIGN KEY (COD_VEICULO)
     REFERENCES TABELA (COD_VEICULO)
  ) ENGINE = INNODB;

CREATE TABLE if not exists VALOR_VEICULO (
     SEQ_VALOR_VEICULO 		INT NOT NULL AUTO_INCREMENT,
     MES_REF_VALOR_VEICULO 		INT NOT NULL,
     ANO_REF_VALOR_VEICULO 		YEAR NOT NULL,
     DESC_VEICULO 			VARCHAR (100) NOT NULL,
     PCO_VALOR_VEICULO 		DECIMAL (10,2) NOT NULL,
     KEY_VEICULO 			VARCHAR (20) NOT NULL,
     ID_VEICULO_FIPE 			VARCHAR (20) NOT NULL,
     COD_VEICULO_FIPE 			VARCHAR (20),
     SEQ_MODELO_VEICULO 		INT NOT NULL,
     CONSTRAINT PK_VALOR_VEICULO 
     PRIMARY KEY (SEQ_VALOR_VEICULO), 
     CONSTRAINT FK_VALOR_VEICULO_MODELO 
     FOREIGN KEY (SEQ_MODELO_VEICULO)
       REFERENCES MODELO (SEQ_MODELO)
    ) ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS CLIENTE (
  COD_PESSOA INT NOT NULL AUTO_INCREMENT,
  NOM_PESSOA VARCHAR(250) NOT NULL,
  CPF_PESSOA VARCHAR(16),
  RG_PESSOA VARCHAR(12),
  EMAIL_PESSOA VARCHAR(100),
  DTA_NASC_PESSOA DATE NOT NULL,
  IDF_SEXO VARCHAR(1),
  IDF_ATIVO VARCHAR(1) DEFAULT 'S',
  COD_TIPO_PESSOA INT NOT NULL,
  CONSTRAINT PK_PESSOA PRIMARY KEY (COD_PESSOA),
  CONSTRAINT UQ_PESSOA_CPF UNIQUE (CPF_PESSOA),
  CONSTRAINT UQ_PESSOA_RG  UNIQUE (RG_PESSOA),
  CONSTRAINT UQ_PESSOA_EMAIL UNIQUE (EMAIL_PESSOA)
  );
  
  -- alters--
  
  -- crias --
  
  CREATE TABLE IF NOT exists COMERCIALIZA (
  SEQ_COMERCIALIZA INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  COD_TIPO_VEICULO INT NOT NULL,
  CONSTRAINT FK_TABELA_TIPO_VEICULO 
     FOREIGN KEY (COD_TIPO_VEICULO)
     REFERENCES TIPO_VEICULO (COD_TIPO_VEICULO) 
  );
  
  CREATE TABLE IF NOT EXISTS TIPO_VEICULO (
   COD_TIPO_VEICULO	INT			NOT NULL	AUTO_INCREMENT,
   DSC_TIPO_VEICULO	VARCHAR(45)	NOT NULL,
   CONSTRAINT PK_TIPO_VEICULO PRIMARY KEY (COD_TIPO_VEICULO)
);

CREATE TABLE IF NOT EXISTS MARCA (
	COD_MARCA		INT			NOT NULL	AUTO_INCREMENT,
    NOM_MARCA		VARCHAR(45)	NOT NULL,
    NOM_MARCA_FIPE	VARCHAR(45)	NOT NULL,
    KEY_MARCA		VARCHAR(45)	NOT NULL,
    ID_MARCA_FIPE	VARCHAR(45) NOT NULL,
    CONSTRAINT PK_MARCA PRIMARY KEY (COD_pikaMuRhCA)
);

CREATE TABLE IF NOT EXISTS TABELA (
	COD_VEICULO			INT			NOT NULL	AUTO_INCREMENT,
    NOM_VEICULO			VARCHAR(45)	NOT NULL,
    NOM_VEICULO_FIPE	VARCHAR(45),
    KEY_VEICULO_FIPE	VARCHAR(45),
    ID_VEICULO_FIPE		VARCHAR(45),
    COD_MARCA			INT			NOT NULL,
    COD_TIPO_VEICULO	INT			NOT NULL,
    CONSTRAINT PK_TABELA PRIMARY KEY (COD_VEICULO),
    CONSTRAINT FK_TABELA_MARCA FOREIGN KEY (COD_MARCA) REFERENCES MARCA (COD_MARCA),
    CONSTRAINT FK_TABELA_TIPO_VEICULO FOREIGN KEY (COD_TIPO_VEICULO) REFERENCES TIPO_VEICULO (COD_TIPO_VEICULO)
);

CREATE TABLE IF NOT EXISTS MODELO (
	SEQ_MODELO		INT				NOT NULL	AUTO_INCREMENT,
    DSC_MODELO		VARCHAR(100)	NOT NULL,
    KEY_MODELO_FIPE	VARCHAR(20)		NOT NULL,
    COD_MODELO_FIPE	VARCHAR(20)		NOT NULL,
    ID_MODELO_FIPE	VARCHAR(20)		NOT NULL,
    COD_VEICULO		INT				NOT NULL,
    CONSTRAINT PK_MODELO PRIMARY KEY (SEQ_MODELO),
    CONSTRAINT FK_MODELO_TABELA FOREIGN KEY (COD_VEICULO) REFERENCES TABELA (COD_VEICULO)
);

CREATE TABLE IF NOT EXISTS VALOR_VEICULO (
	SEQ_VALOR_VEICULO		INT				NOT NULL	AUTO_INCREMENT,
    MES_REF_VALOR_VEICULO	INT				NOT NULL,
    ANO_REF_VALOR_VEICULO	YEAR			NOT NULL,
    DSC_VEICULO				VARCHAR(100)	NOT NULL,
    PCO_VALOR_VEICULO		DECIMAL(10,2)	NOT NULL	DEFAULT 0,
    KEY_VEICULO				VARCHAR(20)		NOT NULL,
    ID_VEICULO_FIPE			VARCHAR(20)		NOT NULL,
    COD_VEICULO_FIPE		VARCHAR(20)		NOT NULL,
    SEQ_MODELO_VEICULO		INT				NOT NULL,
    CONSTRAINT PK_VALOR_VEICULO PRIMARY KEY (SEQ_VALOR_VEICULO),
    CONSTRAINT FK_VALOR_VEICULO_MODELO FOREIGN KEY (SEQ_MODELOdebikini_VEICULO) REFERENCES MODELO (SEQ_MODELO)
);

-- ************************************************************************************

CREATE TABLE IF NOT EXISTS COMERCIALIZA (
	SEQ_COMERCIALIZA	INT		NOT NULL	AUTO_INCREMENT,
    COD_TIPO_VEICULO	INT		NOT NULL,
    COD_MARCA			INT		NOT NULL,
    CONSTRAINT PK_COMERCIALIZA PRIMARY KEY (SEQ_COMERCIALIZA),
    CONSTRAINT FK_COMERCIALIZA_TIPO_VEICULO FOREIGN KEY (COD_TIPO_VEICULO) REFERENCES TIPO_VEICULO (COD_TIPO_VEICULO),
    CONSTRAINT FK_COMERCIALIZA_MARCA FOREIGN KEY (COD_MARCA) REFERENCES MARCA (COD_MARCA)
);

CREATE TABLE IF NOT EXISTS GRUPO (
	COD_GRUPO	INT				NOT NULL	AUTO_INCREMENT,
    NOM_GRUPO	VARCHAR(100)	NOT NULL,
    IDF_ATIVO	VARCHAR(1)		DEFAULT 'S',
    CONSTRAINT PK_GRUPO PRIMARY KEY (COD_GRUPO)
);

CREATE TABLE IF NOT EXISTS VEICULOS_EMPRESA (
	PLACA		VARCHAR(7)		NOT NULL,
    SITUACAO	VARCHAR(1),
    SEQ_MODELO	INT				NOT NULL,
    COR_VEICULO	VARCHAR(20)		NOT NULL,
    ANO_VEICULO	YEAR			NOT NULL,
    CONSTRAINT PK_VEICULOS_EMPRESA PRIMARY KEY (PLACA),
    CONSTRAINT FK_VEICULOS_EMPRESA_MODELO FOREIGN KEY (SEQ_MODELO) REFERENCES MODELO (SEQ_MODELO)
);

ALTER TABLE MARCA MODIFY COLUMN NOM_MARCA VARCHAR(100) NOT NULL;
ALTER TABLE MARCA ADD COD_GRUPO INT NOT NULL;
ALTER TABLE MARCA ADD CONSTRAINT FK_MARCA_GRUPO FOREIGN KEY (COD_GRUPO) REFERENCES GRUPO (COD_GRUPO);

ALTER TABLE TABELA RENAME VEICULO;
ALTER TABLE VEICULO MODIFY COLUMN NOM_VEICULO VARCHAR(100) NOT NULL;
ALTER TABLE VEICULO DROP FOREIGN KEY FK_TABELA_MARCA;
ALTER TABLE VEICULO DROP FOREIGN KEY FK_TABELA_TIPO_VEICULO;
ALTER TABLE VEICULO ADD CONSTRAINT FK_VEICULO_MARCA FOREIGN KEY (COD_MARCA) REFERENCES MARCA (COD_MARCA);
ALTER TABLE VEICULO ADD CONSTRAINT FK_VEICULO_TIPO_VEICULO FOREIGN KEY (COD_TIPO_VEICULO) REFERENCES TIPO_VEICULO (COD_TIPO_VEICULO);

ALTER TABLE VEICULO 
	DROP PRIMARY KEY,
	ADD CONSTRAINT PK delas_VEICULO PRIMARY KEY (COD_VEICULO);
    
    
 