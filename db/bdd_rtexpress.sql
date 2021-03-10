/*==============================================================*/
/* Nom de SGBD :  PostgreSQL 8                                  */
/* Date de cr�ation :  19/02/2021 20:42:34                      */
/*==============================================================*/

drop index HABITER_FK;

drop index CLIENT_PK;

drop table CLIENT;

drop index COLIS_PK;

drop table COLIS;

drop index DEPOSER_FK;

drop index DEPOSER3_FK;

drop index DEPOSER2_FK;

drop index DEPOSER_PK;

drop table DEPOSER;

drop index ENVOYER_FK;

drop index ENVOYER3_FK;

drop index ENVOYER2_FK;

drop index ENVOYER_PK;

drop table ENVOYER;

drop index INSTALLER_FK;

drop index FOURNISSEUR_PK;

drop table FOURNISSEUR;

drop index EMPLOYER_FK;

drop index PERSONNEL_PK;

drop table PERSONNEL;

drop index DEPENDRE_FK;

drop index PLD_PK;

drop table PLD;

drop index PLR_PK;

drop table PLR;

drop index RETIRER_FK;

drop index RETIRER3_FK;

drop index RETIRER2_FK;

drop index RETIRER_PK;

drop table RETIRER;

drop index TRANSMETTRE_FK;

drop index TRANSMETTRE3_FK;

drop index TRANSMETTRE2_FK;

drop index TRANSMETTRE_PK;

drop table TRANSMETTRE;

drop index ATTACHER_FK;

drop index VILLE_PK;

drop table VILLE;

/*==============================================================*/
/* Table : CLIENT                                               */
/*==============================================================*/
create table CLIENT (
   ID_CLIENT            SERIAL               not null,
   ID_VILLE             INT4                 not null,
   REF_CLIENT           VARCHAR(15)          not null,
   NOM_CLIENT           VARCHAR(50)          not null,
   PRENOM_CLIENT        VARCHAR(50)          not null,
   ADRESSE_CLIENT       VARCHAR(100)         not null,
   LOGIN_CLIENT         VARCHAR(15)          null,
   MDP_CLIENT           VARCHAR(15)          null,
   constraint PK_CLIENT primary key (ID_CLIENT)
);

/*==============================================================*/
/* Index : CLIENT_PK                                            */
/*==============================================================*/
create unique index CLIENT_PK on CLIENT (
ID_CLIENT
);

/*==============================================================*/
/* Index : HABITER_FK                                           */
/*==============================================================*/
create  index HABITER_FK on CLIENT (
ID_VILLE
);

/*==============================================================*/
/* Table : COLIS                                                */
/*==============================================================*/
create table COLIS (
   ID_COLIS             SERIAL               not null,
   REF_COLIS            VARCHAR(30)          not null,
   TYPE_COLIS           VARCHAR(20)          not null,
   constraint PK_COLIS primary key (ID_COLIS)
);

/*==============================================================*/
/* Index : COLIS_PK                                             */
/*==============================================================*/
create unique index COLIS_PK on COLIS (
ID_COLIS
);

/*==============================================================*/
/* Table : DEPOSER                                              */
/*==============================================================*/
create table DEPOSER (
   ID_PLD               INT4           not null,
   ID_COLIS             INT4                 not null,
   ID_FOURNISSEUR       INT4                 not null,
   DATE_DEPOT           DATE                 not null,
   constraint PK_DEPOSER primary key (ID_PLD, ID_COLIS, ID_FOURNISSEUR)
);

/*==============================================================*/
/* Index : DEPOSER_PK                                           */
/*==============================================================*/
create unique index DEPOSER_PK on DEPOSER (
ID_PLD,
ID_COLIS,
ID_FOURNISSEUR
);

/*==============================================================*/
/* Index : DEPOSER2_FK                                          */
/*==============================================================*/
create  index DEPOSER2_FK on DEPOSER (
ID_PLD
);

/*==============================================================*/
/* Index : DEPOSER3_FK                                          */
/*==============================================================*/
create  index DEPOSER3_FK on DEPOSER (
ID_COLIS
);

/*==============================================================*/
/* Index : DEPOSER_FK                                           */
/*==============================================================*/
create  index DEPOSER_FK on DEPOSER (
ID_FOURNISSEUR
);

/*==============================================================*/
/* Table : ENVOYER                                              */
/*==============================================================*/
create table ENVOYER (
   ID_PLD               INT4                 not null,
   ID_PLR               INT4                 not null,
   ID_COLIS             INT4                 not null,
   DATE_ENVOI           DATE                 not null,
   DATE_RECEPTION       DATE                 null,
   PLD_TO_PLR           BOOL                 null,
   constraint PK_ENVOYER primary key (ID_PLD, ID_PLR, ID_COLIS)
);

/*==============================================================*/
/* Index : ENVOYER_PK                                           */
/*==============================================================*/
create unique index ENVOYER_PK on ENVOYER (
ID_PLD,
ID_PLR,
ID_COLIS
);

/*==============================================================*/
/* Index : ENVOYER2_FK                                          */
/*==============================================================*/
create  index ENVOYER2_FK on ENVOYER (
ID_PLD
);

/*==============================================================*/
/* Index : ENVOYER3_FK                                          */
/*==============================================================*/
create  index ENVOYER3_FK on ENVOYER (
ID_PLR
);

/*==============================================================*/
/* Index : ENVOYER_FK                                           */
/*==============================================================*/
create  index ENVOYER_FK on ENVOYER (
ID_COLIS
);

/*==============================================================*/
/* Table : FOURNISSEUR                                          */
/*==============================================================*/
create table FOURNISSEUR (
   ID_FOURNISSEUR       SERIAL               not null,
   ID_VILLE             INT4                 not null,
   REF_FOURNISSEUR      VARCHAR(15)          not null,
   NOM_FOURNISSEUR      VARCHAR(100)         not null,
   ADRESSE_FOURNISSEUR  VARCHAR(100)         not null,
   ACTIVITE             VARCHAR(50)          null,
   LOGIN_FOURNISSEUR    VARCHAR(15)          null,
   MDP_FOURNISSEUR      VARCHAR(15)          null,
   constraint PK_FOURNISSEUR primary key (ID_FOURNISSEUR)
);

/*==============================================================*/
/* Index : FOURNISSEUR_PK                                       */
/*==============================================================*/
create unique index FOURNISSEUR_PK on FOURNISSEUR (
ID_FOURNISSEUR
);

/*==============================================================*/
/* Index : INSTALLER_FK                                         */
/*==============================================================*/
create  index INSTALLER_FK on FOURNISSEUR (
ID_VILLE
);

/*==============================================================*/
/* Table : PERSONNEL                                            */
/*==============================================================*/
create table PERSONNEL (
   ID_PERSONNEL         SERIAL               not null,
   ID_PLD               INT4           not null,
   NOM_PERSONNEL        VARCHAR(50)          not null,
   PRENOM_PERSONNEL     VARCHAR(50)          not null,
   LOGIN_PERSONNEL      VARCHAR(15)          not null,
   MDP_PERSONNEL        VARCHAR(15)          not null,
   constraint PK_PERSONNEL primary key (ID_PERSONNEL)
);

/*==============================================================*/
/* Index : PERSONNEL_PK                                         */
/*==============================================================*/
create unique index PERSONNEL_PK on PERSONNEL (
ID_PERSONNEL
);

/*==============================================================*/
/* Index : EMPLOYER_FK                                          */
/*==============================================================*/
create  index EMPLOYER_FK on PERSONNEL (
ID_PLD
);

/*==============================================================*/
/* Table : PLD                                                  */
/*==============================================================*/
create table PLD (
   ID_PLD               INT4                 not null,
   ID_PLR               INT4                 not null,
   REF_PLD              VARCHAR(6)           not null,
   NOM_PLD              VARCHAR(50)          not null,
   constraint PK_PLD primary key (ID_PLD)
);

/*==============================================================*/
/* Index : PLD_PK                                               */
/*==============================================================*/
create unique index PLD_PK on PLD (
ID_PLD
);

/*==============================================================*/
/* Index : DEPENDRE_FK                                          */
/*==============================================================*/
create  index DEPENDRE_FK on PLD (
ID_PLR
);

/*==============================================================*/
/* Table : PLR                                                  */
/*==============================================================*/
create table PLR (
   ID_PLR               INT4                 not null,
   REF_PLR              VARCHAR(6)           not null,
   NOM_PLR              VARCHAR(50)          not null,
   constraint PK_PLR primary key (ID_PLR)
);

/*==============================================================*/
/* Index : PLR_PK                                               */
/*==============================================================*/
create unique index PLR_PK on PLR (
ID_PLR
);

/*==============================================================*/
/* Table : RETIRER                                              */
/*==============================================================*/
create table RETIRER (
   ID_COLIS             INT4                 not null,
   ID_PLD               INT4                 not null,
   ID_CLIENT            INT4                 not null,
   DATE_RETRAIT         DATE                 not null,
   constraint PK_RETIRER primary key (ID_COLIS, ID_PLD, ID_CLIENT)
);

/*==============================================================*/
/* Index : RETIRER_PK                                           */
/*==============================================================*/
create unique index RETIRER_PK on RETIRER (
ID_COLIS,
ID_PLD,
ID_CLIENT
);

/*==============================================================*/
/* Index : RETIRER2_FK                                          */
/*==============================================================*/
create  index RETIRER2_FK on RETIRER (
ID_COLIS
);

/*==============================================================*/
/* Index : RETIRER3_FK                                          */
/*==============================================================*/
create  index RETIRER3_FK on RETIRER (
ID_PLD
);

/*==============================================================*/
/* Index : RETIRER_FK                                           */
/*==============================================================*/
create  index RETIRER_FK on RETIRER (
ID_CLIENT
);

/*==============================================================*/
/* Table : TRANSMETTRE                                          */
/*==============================================================*/
create table TRANSMETTRE (
   ID_PLR               INT4                 not null,
   PLR_ID_PLR           INT4                 not null,
   ID_COLIS             INT4                 not null,
   PLR_DATE_ENVOI       DATE                 not null,
   PLR_DATE_RECEPTION   DATE                 null,
   constraint PK_TRANSMETTRE primary key (ID_PLR, PLR_ID_PLR, ID_COLIS)
);

/*==============================================================*/
/* Index : TRANSMETTRE_PK                                       */
/*==============================================================*/
create unique index TRANSMETTRE_PK on TRANSMETTRE (
ID_PLR,
PLR_ID_PLR,
ID_COLIS
);

/*==============================================================*/
/* Index : TRANSMETTRE2_FK                                      */
/*==============================================================*/
create  index TRANSMETTRE2_FK on TRANSMETTRE (
ID_PLR
);

/*==============================================================*/
/* Index : TRANSMETTRE3_FK                                      */
/*==============================================================*/
create  index TRANSMETTRE3_FK on TRANSMETTRE (
PLR_ID_PLR
);

/*==============================================================*/
/* Index : TRANSMETTRE_FK                                       */
/*==============================================================*/
create  index TRANSMETTRE_FK on TRANSMETTRE (
ID_COLIS
);

/*==============================================================*/
/* Table : VILLE                                                */
/*==============================================================*/
create table VILLE (
   ID_VILLE             INT4                 not null,
   ID_PLD               INT4           not null,
   NOM_VILLE            VARCHAR(100)          not null,
   CP                   CHAR(5)              null,
   INSEE_CODE           VARCHAR(5)           null,
   GPS_LAT              FLOAT8               null,
   GPS_LNG              FLOAT8               null,
   constraint PK_VILLE primary key (ID_VILLE)
);

/*==============================================================*/
/* Index : VILLE_PK                                             */
/*==============================================================*/
create unique index VILLE_PK on VILLE (
ID_VILLE
);

/*==============================================================*/
/* Index : ATTACHER_FK                                          */
/*==============================================================*/
create  index ATTACHER_FK on VILLE (
ID_PLD
);

alter table CLIENT
   add constraint FK_CLIENT_HABITER_VILLE foreign key (ID_VILLE)
      references VILLE (ID_VILLE)
      on delete restrict on update restrict;

alter table DEPOSER
   add constraint FK_DEPOSER_DEPOSER_FOURNISS foreign key (ID_FOURNISSEUR)
      references FOURNISSEUR (ID_FOURNISSEUR)
      on delete restrict on update restrict;

alter table DEPOSER
   add constraint FK_DEPOSER_DEPOSER2_PLD foreign key (ID_PLD)
      references PLD (ID_PLD)
      on delete restrict on update restrict;

alter table DEPOSER
   add constraint FK_DEPOSER_DEPOSER3_COLIS foreign key (ID_COLIS)
      references COLIS (ID_COLIS)
      on delete restrict on update restrict;

alter table ENVOYER
   add constraint FK_ENVOYER_ENVOYER_COLIS foreign key (ID_COLIS)
      references COLIS (ID_COLIS)
      on delete restrict on update restrict;

alter table ENVOYER
   add constraint FK_ENVOYER_ENVOYER2_PLD foreign key (ID_PLD)
      references PLD (ID_PLD)
      on delete restrict on update restrict;

alter table ENVOYER
   add constraint FK_ENVOYER_ENVOYER3_PLR foreign key (ID_PLR)
      references PLR (ID_PLR)
      on delete restrict on update restrict;

alter table FOURNISSEUR
   add constraint FK_FOURNISS_INSTALLER_VILLE foreign key (ID_VILLE)
      references VILLE (ID_VILLE)
      on delete restrict on update restrict;

alter table PERSONNEL
   add constraint FK_PERSONNE_EMPLOYER_PLD foreign key (ID_PLD)
      references PLD (ID_PLD)
      on delete restrict on update restrict;

alter table PLD
   add constraint FK_PLD_DEPENDRE_PLR foreign key (ID_PLR)
      references PLR (ID_PLR)
      on delete restrict on update restrict;

alter table RETIRER
   add constraint FK_RETIRER_RETIRER_CLIENT foreign key (ID_CLIENT)
      references CLIENT (ID_CLIENT)
      on delete restrict on update restrict;

alter table RETIRER
   add constraint FK_RETIRER_RETIRER2_COLIS foreign key (ID_COLIS)
      references COLIS (ID_COLIS)
      on delete restrict on update restrict;

alter table RETIRER
   add constraint FK_RETIRER_RETIRER3_PLD foreign key (ID_PLD)
      references PLD (ID_PLD)
      on delete restrict on update restrict;

alter table TRANSMETTRE
   add constraint FK_TRANSMET_TRANSMETT_COLIS foreign key (ID_COLIS)
      references COLIS (ID_COLIS)
      on delete restrict on update restrict;

alter table TRANSMETTRE
   add constraint FK_TRANSMET_PLR_TRANSMETT foreign key (ID_PLR)
      references PLR (ID_PLR)
      on delete restrict on update restrict;

alter table TRANSMETTRE
   add constraint FK_TRANSMET_TRANSMETT_PLR foreign key (PLR_ID_PLR)
      references PLR (ID_PLR)
      on delete restrict on update restrict;

alter table VILLE
   add constraint FK_VILLE_ATTACHER_PLD foreign key (ID_PLD)
      references PLD (ID_PLD)
      on delete restrict on update restrict;

