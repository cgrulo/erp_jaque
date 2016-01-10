create database erp_jaque;
use erp_jaque;

create table cliente(
id_cli int auto_increment,
nom_cli varchar(100),
apep_cli varchar(80),
apem_cli varchar(80),
fecha_cli datetime,
del_cli varchar(80),
cp_cli int,
dir_cli varchar(250),

constraint pk_cli primary key (id_cli)
);


create table d_fac(
rfc_dfac varchar(20),
nom_dfac varchar(100),
dir_dfac varchar (300),
lug_dfac varchar (300),
id_cli1 int,

constraint pk_dfac primary key (rfc_dfac),
constraint fk_dfac foreign key (id_cli1) references cliente(id_cli)
);

create table tipo_prod(
id_tipo smallint auto_increment,
nom_tipo varchar(150),
marca_tipo varchar (150),

constraint pk_tipo primary key (id_tipo)
);

create table proveedor(
id_prov smallint auto_increment,
nom_prov varchar(250),
dir_prov varchar(300),

constraint pk_prov primary key (id_prov)
);

create table producto(
id_prod int auto_increment,
mod_prod varchar (300),
precio_prod middleint,
descrip_prod varchar (1500),
id_tipo1 smallint,
id_prov1 smallint,

constraint pk_prod primary key (id_prod),
constraint fk_tprod foreign key (id_tipo1) references tipo_prod(id_tipo),
constraint fk_pprod foreign key (id_prov1) references proveedor(id_prov)
);

create table pedido(
id_ped int,
fecha_ped datetime,
stat_ped varchar(150),
id_cli1 int,

constraint pk_ped primary key (id_ped),
constraint fk_cped foreign key (id_cli1) references cliente(id_cli)

);

create table contrato(
id_cont middleint auto_increment,
ini_cont datetime,
fin_cont datetime,
tipo_cont varchar(250),
oblig_cont varchar(3000),
id_cli2 int,

constraint pk_cont primary key (id_cont),
constraint fk_ccont foreign key (id_cli2) references cliente(id_cli)

);

create table reporte(
id_rep int auto_increment,
fecha_rep datetime,
raz_rep varchar(3500),
stat_rep varchar(150),
id_cli3 int,

constraint pk_rep primary key (id_rep),
constraint fk_crep foreign key (id_cli3) references cliente(id_cli)

);


create table factura(
id_fac int auto_increment,
fecha_fac datetime,
shcp_folio varchar(300),
folio_fac varchar(300),
cad_fac datetime,
id_cli4 int,

constraint pk_fac primary key (id_fac),
constraint fk_cfac foreign key (id_cli4) references cliente(id_cli)
);

create table ped_prod(
id_ped1 int,
id_prod1 int,
cantidad_prod smallint,
constraint fk_peped foreign key (id_ped1) references pedido(id_ped),
constraint fk_prped foreign key (id_prod1) references producto(id_prod)
);