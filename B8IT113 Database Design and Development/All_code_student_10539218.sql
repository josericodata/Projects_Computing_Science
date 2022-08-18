/*
Name: Table creation.
Written By: Jose Maria Rico Leal.
Function: We are creating 11 tables for this project.
Tables: Member, Trainer, TrainerArchive, MembershipCard, Login, MemberArchive, Payment, PaymentArchive, Marketing, Program and ProgramArchive.
Creation: Date                 
              30/11/2020           
*/

CREATE TABLE [Member](
 [MembershipNo] Varchar(10),
 [MFirstName] Varchar(40) Not Null,
 [MSurname] Varchar(40) Not Null,
 [AddressLine1] varchar(40) Not Null, 
 [AddressLine2] varchar(40) Null,
 [City] varchar(40) Not Null,
 [County] varchar(40) Null,
 [PostCode] char(8) Not Null,
 [PhoneNo] varchar(15) Not Null,
 [GDPR] Char (4) Null,
 [Email] varchar(40) Not Null,
 [JoinDate] date Not Null,
 [Active] char (1) Not Null,
 PRIMARY KEY ([MembershipNo])
);

CREATE TABLE [Trainer](
 [PPSNo] varchar(10),
 [TFirstName] varchar(40) Not Null,
 [TSurname] varchar(40) Not Null,
 [AddressLine1] varchar(40) Not Null,
 [City] varchar(40) Not Null,
 [County] varchar(40) Null,
 [PostCode] char(8) Not Null,
 [MobileNo] varchar(15) Not Null,
 [Email] varchar(40) Not Null,
 [JoinDate] date Not Null,
 [Active] char (1) Not Null,
 PRIMARY KEY ([PPSNo])
);

CREATE TABLE [TrainerArchive](
 [PPSNo] varchar(10),
 [AddressLine1] varchar(40) Not Null,
 [City] varchar(40) Not Null,
 [County] varchar(40) Null,
 [PostCode] char(8) Not Null,
 [MobileNo] varchar(15) Not Null,
 [Email] varchar(40) Not Null,
 [DateArchived] Date Not Null,
 FOREIGN KEY ([PPSNo]) REFERENCES [Trainer] ([PPSNo]) on delete set Null on update cascade
);

CREATE TABLE [MembershipCard](
 [MembershipNo] Varchar(10) Not Null,
 [IssueDate] Date Not Null,
 [Photo] Image Not Null,
 [LostCard] Char(5) Null,
 FOREIGN KEY([MembershipNo]) REFERENCES [Member]([MembershipNo]),
 PRIMARY KEY (MembershipNo,IssueDate)
);

CREATE TABLE [Login](
 [MembershipNo] Varchar(10) Not Null,
 [IssueDate] Date Not Null,
 [LoginDate] Datetime Not Null,
 FOREIGN KEY(MembershipNo,IssueDate) REFERENCES [MembershipCard](MembershipNo,IssueDate)
);

CREATE TABLE [MemberArchive](
 [MembershipNo] Varchar(10) Null,
 [AddressLine1] varchar(40) Not Null, 
 [AddressLine2] varchar(40) Null,
 [City] varchar(40) Not Null,
 [County] varchar(40) Null,
 [PostCode] char(8) Not Null,
 [PhoneNo] varchar(15) Not Null,
 [Email] varchar(40) Not Null,
 [DateArchived] date Not Null,
 FOREIGN KEY([MembershipNo]) REFERENCES [Member]([MembershipNo])on delete set Null on update cascade
);

CREATE TABLE [Payment](
 [MembershipNo] Varchar(10) Not Null,
 [StartDate] Date Not Null,
 [Method] varchar(20) Not Null,
 [Frequency] varchar(25) Not Null,
 FOREIGN KEY([MembershipNo]) REFERENCES [Member]([MembershipNo]),
 PRIMARY KEY (MembershipNo,StartDate)
);

CREATE TABLE [PaymentArchive](
 [MembershipNo] Varchar(10) Not Null,
 [StartDate] Date Not Null,
 [Method] varchar(25) Not Null,
 [Frequency] varchar(30) Not Null,
 [DateArchived] Date Not Null,
 FOREIGN KEY (MembershipNo,StartDate) REFERENCES [Payment](MembershipNo,StartDate))
 
CREATE TABLE [Marketing](
 [MembershipNo] Varchar(10) Null,
 [GDPR] Char (1) Not Null,
 [SendOutDate] Date Not Null,
 FOREIGN KEY([MembershipNo]) REFERENCES [Member]([MembershipNo]) on delete set Null on update cascade
);

CREATE TABLE [Program](
 [MembershipNo] Varchar(10) Not Null,
 [ProgStartDate] Date Not Null,
 [PPSNo] varchar(10) Null,
 [ProgDetails] varchar(50) Not Null,
 [ProgEndDate] Date Null,
 FOREIGN KEY([MembershipNo]) REFERENCES [Member]([MembershipNo]),
 FOREIGN KEY([PPSNo]) REFERENCES [Trainer]([PPSNo]) on delete set null on update cascade,
 PRIMARY KEY (MembershipNo,ProgStartDate)
);

CREATE TABLE [ProgramArchive](
 [MembershipNo] Varchar(10) Not Null,
 [ProgStartDate] Date Not Null,
 [PPSNo] varchar(10) Null,
 [ProgDetails] varchar(50) Not Null,
 [DateArchived] Date  Not Null,
 FOREIGN KEY(MembershipNo,ProgStartDate) REFERENCES [Program](MembershipNo,ProgStartDate)
 
 );

/*
Name: Data insertion.
Written By: Jose Maria Rico Leal.
Function: We are inserting data into the tables.
Creation: Date                 
              30/11/2020           
*/

Insert into Member
Values ('1000','Alberto','Azul','Heaven','N/A','Dublin','Dublin','D01 K710','+353894520767','A','alberto@gmail.com','2020-01-01','Y'),
		('1001','Rosa','Ruiz','Rock','Empty','Dublin','Dublin','D02 K711','+353894520768','B','rosa@gmail.com','2020-02-01','Y'),
('1002','Tomas','Roche','Forty Foot','N/A','Dublin','Dublin','D03 K712','+353899520767','Null','tomas@gmail.com','2020-03-01','N'),
('1003','Soledad','McFlurry','Cross East','Empty','Dublin','Dublin','D04 K713','+353894520710','A','soledad@gmail.com','2020-04-01','Y'),
('1004','Avril','Month','Noth Avenue','N/A','Dublin','Dublin','D05 K714','+353894520750','B','avril@gmail.com','2020-04-01','Y'),
('1005','Leon','Van Varle','Fifth Bulevard','Empty','Dublin','Dublin','D06 K715','+353894520799','Null','leon@gmail.com','2020-05-01','N'),
('1006','Vincent','Armstrong','Wall Street','N/A','Dublin','Dublin','D07 K716','+353894520759','A','vincent@gmail.com','2020-06-01','N'),
('1007','Camila','keane','Spanish Armada','Empty','Dublin','Dublin','D08 K717','+353894520745','Null','camila@gmail.com','2020-07-01','N'),
('1008','Diana','O Really','Celtic Tiger','N/A','Dublin','Dublin','D09 K718','+353894520750','B','diana@gmail.com','2020-07-01','Y'),
('1009','Charles','Williams','Phoenix Park','Empty','Dublin','Dublin','D10 K719','+353894520111','B','charles@gmail.com','2020-07-01','Y'),
('1010','Jacques','De Boer','All the way up','N/A','Dublin','Dublin','D11 K720','+353894522222','A','jacques@gmail.com','2020-07-01','Y'),                                             
('1011','Pedro','Sanchez','Above & beyond','Empty','Dublin','Dublin','D12 K755','+353894522555','A','Pedro@gmail.com','2020-07-02','Y'),
('1012','Pablo','Escobar','Halloween','N/A','Dublin','Dublin','D15 KH07','+353895555511','Null','Pablo@gmail.com','2020-07-03','N'),
('1013','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','+353812121222','B','Moises@gmail.com','2020-07-04','N'),
('1014','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','+353894520750','B','Paco@gmail.com','2020-09-06','N'),
('1015','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','+353894520111','B','Silvia@gmail.com','2020-09-07','N'),
('1016','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','+353894522222','B','Sofia@gmail.com','2020-09-08','N'),
('1017','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','+353894522555','B','Candela@gmail.com','2020-09-09','N'),
('1018','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','+353895555511','B','Charlie@gmail.com','2020-10-02','N'),
('1019','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','GDPR','+353812121222','B','Dominique@gmail.com','2020-10-03','N')

Insert into Trainer
 Values('2009375UA','Robby','Keane','Mount Anville','Dublin','Dublin','D14 KW12','+353894520761','Robbyletsgetfit@gmail.com','2020-01-01','Y'),
('2009375BB','Stephen','Roche','Mount Rock','Dublin','Dublin','D24 KX13','+353894520762','Stephenletsgetfit@gmail.com','2020-01-01','N'),
('2009375CC','Lance', 'Armstrong','Parnell','Dublin','Dublin','D08 MN11','+353894520763','Lanceletsgetfit@gmail.com','2020-01-01','N'),
('2009375AA','Elena','Isinbayeva','Camden','Dublin','Dublin','D01 LL13','+353894520764','Elenaletsgetfit@gmail.com','2020-01-01','Y'),
('2009375DD','Arantxa','Sanchez Vicario','Black Rock','Dublin','Dublin','D20 NA01','+353894520765','Arantxaletsgetfit@gmail.com','2020-01-01','Y'),
('2009375XX','Sara','Win','Tallaght','Dublin','Dublin','D15 PA13','+353894520766','Saraletsgetfit@gmail.com','2020-01-01','Y'),
('2009375ZZ','Jeyne','Wellness','BlueBell','Dublin','Dublin','D20 KA10','+353894520767','Jeyneletsgetfit@gmail.com','2020-02-01','N'),
('2009375MZ','Clare','O Really','Sea Point','Dublin','Dublin','D19 AP14','+353894520768','Clareletsgetfit@gmail.com','2020-02-01','N'),
('2009375QP','Molly','Phalan','Sandyford','Dublin','Dublin','D14 EW19','+353894550798','Mollyletsgetfit@gmail.com','2020-04-01','Y'),
('2009375AL','Alex','Ferguson','Blanchardstown','Dublin','Dublin','D02 XX99','+353894520333','Alexletsgetfit@gmail.com','2020-05-01','Y'),
('2009375MN','Domingo','Diaz','Goatstown','Dublin','Dublin','D14 AA11','+353894520111','Domingoletsgetfit@gmail.com','2020-06-01','Y'),
('2009375LK','Pep','Guardiola','Irishtown','Dublin','Dublin','D20 QQ11','+353894520555','Pepletsgetfit@gmail.com','2020-06-01','N')

Insert into MembershipCard
Values('1000','2020-01-01','C:\images\Photo1.jpg','Null'),
('1001','2020-02-01','C:\images\Photo2.jpg','Null'),
('1002','2020-03-01','C:\images\Photo3.jpg','Null'),
('1003','2020-04-01','C:\images\Photo4.jpg','Null'),
('1004','2020-04-01','C:\images\Photo5.jpg','Null'),
('1005','2020-05-01','C:\images\Photo6.jpg','Null'),
('1006','2020-06-01','C:\images\Photo7.jpg', 'Null'),
('1007','2020-07-01','C:\images\Photo8.jpg','Null'),
('1008','2020-07-01','C:\images\Photo9.jpg','Null'),
('1009','2020-07-01','C:\images\Photo10.jpg','Null'),
('1010','2020-07-01','C:\images\Photo11.jpg','Null'),
('1011','2020-07-02','C:\images\Photo12.jpg','Null'),
('1012','2020-07-03','C:\images\Photo13.jpg','Null'),
('1013','2020-07-04','C:\images\Photo14.jpg','Null'),
('1000','2020-03-15','C:\images\Photo1.jpg','Lost'),
('1002','2020-03-16','C:\images\Photo1.jpg','Lost')

Insert into Payment
Values('1000','2020-02-01','PayPal','Quarterly'),
('1001','2020-02-15','Cash','Quarterly'),
('1002','2020-03-15','Cash','Monthly'),
('1003','2020-05-01','Revolut','Monthly'),
('1004','2020-05-02','Direct Debit','Quarterly'),
('1005','2020-05-03','PayPal','Quarterly'),
('1006','2020-06-10','PayPal','Monthly'),
('1007','2020-07-02','Direct Debit','Monthly'),
('1008','2020-07-02','Credit Card','Monthly'),
('1009','2020-07-02','PayPal','Annually'),
('1010','2020-07-02','Direct Debit','Monthly'),
('1011','2020-07-03','PayPal','Quarterly'),
('1012','2020-07-04','Credit Card','Monthly'),
('1013','2020-07-05','Credit Card','Monthly'),
('1014','2020-09-06','PayPal','Monthly'),
('1015','2020-09-07','Direct Debit','Monthly'),
('1016','2020-09-08','Credit Card','Monthly'),
('1017','2020-09-09','PayPal','Annually'),
('1018','2020-10-01','Direct Debit','Monthly'),
('1019','2020-10-02','PayPal','Quarterly')

Insert into Program
Values('1000','2020-10-15','2009375AA','Zumba','2020-12-10'),
('1000','2020-10-16','2009375AA','Hit','2020-12-11'),
('1001','2020-10-16','2009375AL','Intensive program to gain muscle','2020-12-11'),
('1003','2020-10-17','2009375AL','Upper Body strengthen','2020-12-12'),
('1004','2020-10-17','2009375DD','Lower Body strengthen','2020-12-12'),
('1008','2020-10-18','2009375DD','Muscle flexibility program','2020-12-13'),
('1009','2020-10-19','2009375MN','Indoor cycling','2020-12-14'),
('1010','2020-10-20','2009375MN','Indoor cycling','2020-12-14'),
('1003','2020-10-20','2009375QP','Upper Body strengthen','2020-12-15'),
('1011','2020-10-21','2009375QP','Salsa dancing','2020-12-15'),
('1001','2020-10-21','2009375UA','Tango dancing','2020-12-16'),
('1003','2020-10-22','2009375UA','Flamenco dancing','2020-12-17'),
('1011','2020-10-23','2009375XX','Karate','2020-12-18'),
('1010','2020-10-24','2009375XX','Body Pump','2020-12-19'),
('1003','2020-10-25','2009375AA','Yoga','2020-12-20'),
('1004','2020-10-26','2009375AL','Pilates','2020-12-21'),
('1008','2020-10-27','2009375QP','Classic Dancing','2020-12-22'),
('1013','2020-10-22','2009375UA','Flamenco dancing','2020-12-17'),
('1014','2020-10-23','2009375XX','Karate','2020-12-18'),
('1015','2020-10-24','2009375XX','Body Pump','2020-12-19'),
('1016','2020-10-25','2009375AA','Yoga','2020-12-20'),
('1017','2020-10-26','2009375AL','Pilates','2020-12-21'),
('1018','2020-10-27','2009375QP','Classic Dancing','2020-12-22'),
('1019','2020-10-27','2009375QP','Classic Dancing','2020-12-22')

Insert into Login
Values('1000','2020-01-01','2020-01-01 17:53:11'),
('1001','2020-02-01','2020-02-01 16:33:35'),
('1002','2020-03-01','2020-03-01 15:11:55'),
('1003','2020-04-01','2020-04-01 19:03:54'),
('1004','2020-04-01','2020-04-01 12:33:00'),
('1005','2020-05-01','2020-05-01 00:00:09'),
('1006','2020-06-01','2020-06-01 15:44:12'),
('1007','2020-07-01','2020-07-01 20:24:03'),
('1008','2020-07-01','2020-07-01 02:54:33'),
('1009','2020-07-01','2020-07-01 13:15:11'),
('1010','2020-07-01','2020-07-01 12:35:00'),
('1011','2020-07-02','2020-01-02 15:49:59'),
('1012','2020-07-03','2020-01-03 18:30:40'),
('1013','2020-07-04','2020-01-04 20:41:41'),
('1000','2020-03-15','2020-10-01 18:44:33'),
('1013','2020-07-04','2020-10-16 00:35:00'),
('1001','2020-02-01','2020-10-15 19:55:11'),
('1004','2020-04-01','2020-10-17 04:49:59'),
('1008','2020-07-01','2020-10-18 16:40:40'),
('1009','2020-07-01','2020-10-18 20:55:41'),
('1010','2020-07-01','2020-10-20 12:35:59'),
('1011','2020-07-02','2020-10-21 10:22:40'),
('1011','2020-07-02','2020-10-22 11:34:41')

Insert into PaymentArchive
Values('1000','2020-02-01','Cash','Monthly','2020-02-01'),
('1001','2020-02-15','Direct Debit','Monthly','2020-02-15'),
('1002','2020-03-15','Credit Card','Quarterly','2020-03-15'),
('1003','2020-05-01','Revolut','Monthly','2020-05-01'),
('1004','2020-05-02','Direct Debit','Quarterly','2020-05-02'),
('1005','2020-05-03','Cash','Annually','2020-05-03'),
('1006','2020-06-10','PayPal','Monthly','2020-06-10'),
('1007','2020-07-02','Direct Debit','Annually','2020-07-02'),
('1008','2020-07-02','Credit Card','Monthly','2020-07-02'),
('1009','2020-07-02','PayPal','Quarterly','2020-07-02'),
('1010','2020-07-02','Direct Debit','Annually','2020-07-02'),
('1011','2020-07-03','Credit Card','Monthly','2020-07-03'),
('1012','2020-07-04','PayPal','Quarterly','2020-07-04'),
('1013','2020-07-05','Cash','Annually','2020-07-05'),
('1014','2020-09-06','Cash',' Annually ','2020-09-06'),
('1015','2020-09-07','Paypal',' Annually ','2020-09-07'),
('1016','2020-09-08','Paypal','Quarterly','2020-09-08'),
('1017','2020-09-09','Cash','Monthly','2020-09-09'),
('1018','2020-10-01','Credit Card',' Annually ','2020-10-01'),
('1019','2020-10-02','Debit Card','Monthly','2020-10-02')

Insert into ProgramArchive
Values('1000','2020-10-15','2009375BB','Yoga','2020-06-10'),
('1000','2020-10-16','2009375BB','Pilates','2020-06-11'),
('1001','2020-10-16','2009375CC','Zumba','2020-06-12'),
('1003','2020-10-17','2009375CC','Classic Dancing','2020-06-13'),
('1004','2020-10-17','2009375LK','Intensive program to gain muscle','2020-06-14'),
('1008','2020-10-18','2009375LK','Yoga','2020-06-15'),
('1009','2020-10-19','2009375MZ','Intensive program to lose weight','2020-06-16'),
('1010','2020-10-20','2009375MZ','Indoor jumping','2020-06-17'),
('1003','2020-10-20','2009375XX','Salsa dancing','2020-08-11'),
('1011','2020-10-21','2009375AA','Tango dancing','2020-08-09'),
('1001','2020-10-21','2009375DD','Flamenco dancing','2020-08-10'),
('1003','2020-10-22','2009375ZZ','Lower Body strengthen','2020-08-08'),
('1011','2020-10-23','2009375ZZ','Indoor cycling','2020-09-01'),
('1010','2020-10-24','2009375MZ','Yoga','2020-09-02'),
('1003','2020-10-25','2009375LK','Flamenco Dancing','2020-09-03'),
('1004','2020-10-26','2009375CC','Salsa','2020-09-04'),
('1008','2020-10-27','2009375BB','Body Pump','2020-09-08'),
('1013','2020-10-22','2009375BB','Pilates','2020-06-18'),
('1014','2020-10-23','2009375CC','Zumba','2020-06-18'),
('1015','2020-10-24','2009375CC','Classic Dancing','2020-06-19'),
('1016','2020-10-25','2009375LK','Intensive program to gain muscle','2020-06-20'),
('1017','2020-10-26','2009375LK','Yoga','2020-06-21'),
('1018','2020-10-27','2009375MZ','Intensive program to lose weight','2020-06-21'),
('1019','2020-10-27','2009375MZ','Indoor jumping','2020-06-22')

Insert into MemberArchive
Values ('1000','Hell','N/A','Cork','Cork','C01 K710','+353894520767','alberto@gmail.com','2020-01-15'),
		('1001','Stone','Empty','Dublin','Dublin','D14 K711','+353894520768','rosa@gmail.com','2020-02-15'),
('1002','Forty Feet','N/A','Dublin','Dublin','D17 K712','+353899520767','tomas@gmail.com','2020-03-15'),
('1003','Cross West','Empty','Cavan','Cavan','D04 K713','+353894520710','soledad@gmail.com','2020-04-15'),
('1004','Noth State','N/A','Dublin','Dublin','D15 K714','+353894520750','avril@gmail.com','2020-04-16'),
('1005','Fifth town','Empty','Galway','Galway','D15 K715','+353894520799','leon@gmail.com','2020-05-29'),
('1006','Wall & Fence','N/A','New York','New York','NY7 K716','+353894520759','vincent@gmail.com','2020-06-15'),
('1007','English Armada','Empty','London','London','L08 K717','+353894520745','camila@gmail.com','2020-07-15'),
('1008','Celtic Lyon','N/A','Boston','Boston','B09 K718','+353894520750','diana@gmail.com','2020-07-16'),
('1009','Phoenix road','Empty','Berlin','Berlin','B10 K719','+353894520111','charles@gmail.com','2020-07-08'),
('1010','All the way down','N/A','Bilbao','Bilbao','B15 K720','+353894522222','jacques@gmail.com','2020-07-10'),
('1011','So far so good','Empty','Madrid','Madrid','M12 K755','+353894522555','Pedro@gmail.com','2020-07-11'),
('1012','Pumpkin','N/A','Barcelona','Barcelona','B15 KH07','+353895555511','Pablo@gmail.com','2020-07-12'),
('1013','Computer Laptop','Empty','Alicante','Alicante','A24 KJ30','+353812121222','Donald@gmail.com','2020-07-30')

Insert into TrainerArchive
 Values('2009375UA','Wood Flood','Dublin','Dublin','D11 KH07','+353894520761','Robbyletsgetfit@gmail.com','2020-01-03'),
('2009375BB','Granadella','Xabia','Spain','X24 KX13','+353894520762','Stephenletsgetfit@gmail.com','2020-02-28'),
('2009375CC','Positive Test','Austin','Texas','A08 MN11','+353894520763','Lanceletsgetfit@gmail.com','2020-02-15'),
('2009375AA','George Street','Dublin','Dublin','D03 XX99','+353894520764','Elenaletsgetfit@gmail.com','2020-02-15'),
('2009375DD','Formigal','Andorra','Andorra','A20 NA01','+353894520765','Arantxaletsgetfit@gmail.com','2020-01-29'),
('2009375XX','Lucan','Dublin','Dublin','D18 LO99','+353894520766','Saraletsgetfit@gmail.com','2020-01-30'),
('2009375ZZ','BlueRing','Dublin','Dublin','D70 99KA','+353894520767','Jeyneletsgetfit@gmail.com','2020-04-14'),
('2009375MZ','Sea Line','Dublin','Dublin','D40 AK47','+353894520768','Clareletsgetfit@gmail.com','2020-02-11'),
('2009375QP','NorthStrand','Dublin','Dublin','D03 IIXX','+353894550798','Mollyletsgetfit@gmail.com','2020-04-15'),
('2009375AL','Old Goat','Glasgow','Glasgow','G02 XX99','+353894520333','Alexletsgetfit@gmail.com','2020-05-15'),
('2009375MN','Bushy Park','Dublin','Dublin','D99 X1A5','+353894520111','Domingoletsgetfit@gmail.com','2020-06-29'),
('2009375LK','Man City','Barcelona','Spain','B20 QQ11','+353894520555','Pepletsgetfit@gmail.com','2020-07-30')

Insert into Marketing
Values('1000','A','2020-04-01'),
('1001','B','2020-04-15'),
('1003','A','2020-04-01'),
('1004','B','2020-04-15'),
('1006','A','2020-04-01'),
('1008','B','2020-04-15'),
('1009','B','2020-04-15'),
('1010','A','2020-04-01'),
('1011','A','2020-04-01'),
('1013','B','2020-04-15'),
('1000','A','2020-05-01'),
('1001','B','2020-05-15'),
('1003','A','2020-05-01'),
('1004','B','2020-05-15'),
('1006','A','2020-05-01'),
('1008','B','2020-05-15'),
('1009','B','2020-05-15'),
('1010','A','2020-05-01'),
('1011','A','2020-05-01'),
('1013','B','2020-05-15')

/*
Name: usp_InsertProgram.
Written By: Jose Maria Rico Leal.
Function: This Stored Procedure will insert into Program Table and it will be needed in the SP usp_New_Member_and_Program when it be called there.
Parameters:@MembershipNo,@ProgStartDate,@PPSNo,@ProgDetails,@ProgEndDate.
Modification: Date                 Reason
              30/11/2020           This procedure will insert a row into Program Table.
*/

Create Proc usp_InsertProgram
@MembershipNo varchar(10),
@ProgStartDate date,
@PPSNo varchar(10),
@ProgDetails varchar(255),
@ProgEndDate date

As
IF @MembershipNo IS NULL 
	Return -1
ELSE
	BEGIN 
		Insert into Program
		Values (@MembershipNo,@ProgStartDate,@PPSNo,@ProgDetails,@ProgEndDate)
	
		If @@Rowcount <> 1 
			Return -1  
		Else
			Return 0 
	END
	
/*
Name: usp_New_Member_and_Program
Written By: Jose Maria Rico Leal.
Function: This Stored Procedure will insert into Member and Program table.
Parameters:@MembershipNo,@MFirstName,@MSurname,@AddressLine1,@AddressLine2,@City,@County,@PostCode,@PhoneNo,@GDPR,@Email,@JoinDate,@Active,@ProgStartDate,@PPSNo,@ProgDetails,@ProgEndDate.



Modification: Date                 Reason
              30/11/2020           This procedure will insert a row into Member and Program Table.
*/

Create proc usp_New_Member_and_Program
@MembershipNo varchar(10),
@MFirstName varchar(40),
@MSurname varchar(40),
@AddressLine1 varchar(40),
@AddressLine2 varchar(40),
@City varchar(40),
@County varchar(40),
@PostCode char(8),
@PhoneNo varchar(15),
@GDPR char(4),
@Email varchar(40),
@JoinDate date,
@Active char(1),
@ProgStartDate date,
@PPSNo varchar(10),
@ProgDetails varchar(50),
@ProgEndDate date

as
declare @identity int 

	Insert into Member
		    Values ( @MembershipNo,@MFirstName,@MSurname,@AddressLine1,@AddressLine2,@City,@County,@PostCode,@PhoneNo,@GDPR,@Email,@JoinDate,@Active)

	--negative point 

	if @@ERROR <> 0 OR @@ROWCOUNT <> 1
	begin
		print 'PROBLEM!!'
		return -1
	 END

	else
	begin 
		set @identity =  scope_identity()

		exec usp_InsertProgram @MembershipNo,@ProgStartDate,@PPSNo,@ProgDetails,@ProgEndDate

		if @@error <>0
			return -1

	end
	print 'ALL GOOD'
	return 0

/*
Name: usp_InsertTrainer.
Written By: Jose Maria Rico Leal.
Function: This Stored Procedure will insert into Trainer Table.
Parameters:@PPSNo,@TFirstName,@TSurdName,@AddressLine1,@City,@County,@PostCode,@MobileNo,@Email,@JoinDate,@Active
Modification: Date                 Reason
              30/11/2020           This procedure will insert a row into Program Table.
*/

Create Proc usp_InsertTrainer
@PPSNo varchar(10),
@TFirstName varchar(40),
@TSurdName varchar(40),
@AddressLine1 varchar (40),
@City varchar (40),
@County varchar (40),
@PostCode char (8),
@MobileNo varchar(15),
@Email varchar(60),
@JoinDate date,
@Active char (1)

As
IF @PPSNo IS NULL 
	Return -1
ELSE
	BEGIN 
		Insert into Trainer
		Values (@PPSNo,@TFirstName,@TSurdName,@AddressLine1,@City,@County,@PostCode,@MobileNo,@Email,@JoinDate,@Active)
	
		If @@Rowcount <> 1 
			Return -1  
				Else
			Return 0 
	END
 
/*

Name: usp_DeleteMember.
Written By: Jose Maria Rico Leal.
Function: This Stored Procedure will delete from Member Table.
Parameters:@MembershipNo.
Modification: Date                 Reason
              30/11/2020           This procedure will remove a row from Member Table and all its foreign keys associated.
*/

Create Proc usp_DeleteMember
@MembershipNo varchar(10)
As
IF @MembershipNo IS NULL 
	Return -1
ELSE
	BEGIN 

		delete from Login
		where MembershipNo = @MembershipNo 
		delete from MembershipCard
		where MembershipNo = @MembershipNo 
		delete from PaymentArchive
		where MembershipNo = @MembershipNo 
		delete from Payment
		where MembershipNo = @MembershipNo 
		delete from ProgramArchive
		where MembershipNo = @MembershipNo 
		delete from Program
		where MembershipNo = @MembershipNo 
		delete from Member
		where MembershipNo = @MembershipNo 
		

		If @@Rowcount <> 1  or @@ERROR <>0 
			Return -1  
		Else
			Return 0 
	END

/*
Name: usp_DeleteMemberArchiveGDPR.
Written By: Jose Maria Rico Leal.
Function: This Stored Procedure will update a row from MemberArchive Table, the members who leave the gym and have ticked the GDPR option ‘B’ will be affected.
Parameters:@MembershipNo.
Modification: Date                 Reason
              30/11/2020           We have to set up first this SP to name it in the following SP usp_DeleteMemberGDPR we will be updating two tables.
*/

Create Proc usp_DeleteMemberArchiveGDPR
@MembershipNo varchar(10)

As
IF @MembershipNo IS NULL 
	Return -1
ELSE
	BEGIN 
		Update MemberArchive
		set [AddressLine1] = 'GDPR',
			[AddressLine2] ='GDPR',
			[City] = 'GDPR',
			[County] = 'GDPR',
			[PostCode] = 'GDPR',
			[PhoneNo] = 'GDPR',
			[Email] ='GDPR',
			[DateArchived] = '9999-12-31'
			

		where [MembershipNo] = @MembershipNo
	
		If @@Rowcount <> 1 or @@ERROR <> 0
			print 'PROBLEM!!'
		Else
			print 'SUCCESFUL DELETION!!'
	END
 
/*

Name: usp_DeleteMemberGDPR.
Written By: Jose Maria Rico Leal.
Function: This Stored Procedure will update a row from Member Table and Member Archive, the members who leave the gym and have ticked the GDPR option ‘B’ will be affected.
Parameters:@MembershipNo.
Modification: Date                 Reason
              30/11/2020           This procedure will perform a soft deleted following GDPR guidelines.
*/

Create proc usp_DeleteMemberGDPR
@MembershipNo varchar(10),
@PhoneNo varchar(15),
@Email varchar(40),
@JoinDate date
As
declare @identity int 

		Update Member
		set [MFirstName] = 'GDPR',
			[MSurname] ='GDPR',
			[AddressLine1] = 'GDPR',
			[AddressLine2] = 'GDPR',
			[City] = 'GDPR',
			[County] = 'GDPR',
			[PostCode] = 'GDPR',
			[PhoneNo] = @PhoneNo,
			[GDPR] = 'B',
			[Email] =@Email,
			[JoinDate] = @JoinDate,
			[Active] = 'N'

		where [MembershipNo] = @MembershipNo 

	--negative point 

	if @@ERROR <> 0 OR @@ROWCOUNT <> 1
	begin
		print 'PROBLEM!!'
		return -1
	 END

	else
	begin 
		 set @identity =  scope_identity()

		exec usp_DeleteMemberArchiveGDPR @MembershipNo

		if @@error <>0
			return -1

	end
	print 'SUCCESFUL DELETION!!'
	return 0
 
/*
Name: ActiveMember_Book.
Written By: Jose Maria Rico Leal.
Function: This view will return all active Members, their Program details and Trainer details.
Modification: Date                 Reason
              30/11/2020           This view will return all active Members, their Program details and Trainer details.
*/

Create view ActiveMember_Book
As
Select p.ProgStartDate,
       p.ProgDetails,
	   p.ProgEndDate,
	   t.TFirstName as 'Trainer_Name',
	   t.Tsurname as 'Trainer_Surname',
	   t.AddressLine1 as 'Trainer_Address',
	   t.City as 'Trainer_City',
	   t.County as 'Trainer_County',
	   t.PostCode as 'Trainer_PostCode',
	   t.MobileNo as 'Trainer_MobileNo',
	   t.Email as 'Trainer_Email',
	   t.JoinDate as 'Trainer_JoinDate',
	   t.Active as 'Trainer_Active',
	   m.MFirstName as 'Member_First_Name',
	   m.MSurname as'Member_Surname',
	   m.AddressLine1 as 'Member_AddressLine1',
	   m.AddressLine2 as 'Member_AddressLine2',
	   m.City as 'Member_City',
	   m.County as 'Member_County',
	   m.PostCode as 'Member_PostCode',
	   m.PhoneNo as 'Member_PhoneNo',
	   m.GDPR,
	   m.Email as 'Member_Email',
	   m.JoinDate as 'Member_JoinDate',
	   m.Active as 'Member_Active'
	   	   
From Program p
Inner join Trainer t
On p.[PPSNo]= t.[PPSNo]
Inner join Member m
On m.[MembershipNo]=p.[MembershipNo]
Where M.Active = 'Y'
 
/*
Name: Non_ActiveMember_Marketing_Book.
Written By: Jose Maria Rico Leal.
Function: This view will return all non-active Members who have ticked GDPR option B, for marketing purposes.
Modification: Date                 Reason
              30/11/2020           We want to get business critical information to send emails and encourage them to get back to the gym.
*/

Create view Non_ActiveMember_Marketing_Book
As

Select 
	   m.MembershipNo,
	   m.MFirstName as 'Member_First_Name',
	   m.MSurname as'Member_Surname',
	   m.AddressLine1 as 'Member_AddressLine1',
	   m.AddressLine2 as 'Member_AddressLine2',
	   m.City as 'Member_City',
	   m.County as 'Member_County',
	   m.PostCode as 'Member_PostCode',
	   m.PhoneNo as 'Member_PhoneNo',
	   m.GDPR,
	   m.Email as 'Member_Email',
	   m.JoinDate as 'Member_JoinDate',
	   m.Active as 'Member_Active',
	   p.ProgDetails as 'Last_Program_On',
	   t.TFirstName as 'Last_Trainer_Name',
	   t.TSurname as 'Last_Trainer_Surname',
	   pa.ProgDetails as 'Previous_Program',
	   py.Frequency as 'Last_Frecuency_Payment_On',
	   py.Method as 'Last_Method_Payment_On',
	   pya.Frequency as 'Previous_Frequency_Payment',
	   pya.Method as 'Previous_Method_Payment'
	   
From PaymentArchive pya
inner join payment py
on pya.MembershipNo=py.MembershipNo


inner join program p
on py.MembershipNo=p.MembershipNo

inner join Trainer t
on t.PPSNo =p.PPSNo 

Inner JOIN ProgramArchive pa
on pa.MembershipNo=p.MembershipNo	   	   

INNER JOIN member m
On p.[MembershipNo]=m.[MembershipNo]
Where m.Active = 'N'
and m.GDPR ='B'

/*
Name: Selects & Tests for all the tables, SP & views.
Written By: Jose Maria Rico Leal.
Function: These functions will return all the data from the tables and view.
Modification: Date                 Reason
              30/11/2020           To double check if everything works fine.
*/
Select * from MemberArchive
Select * from Member
Select * from Trainer
Select * from TrainerArchive
Select * from MembershipCard
Select * from Login
Select * from MemberArchive
Select * from Payment
Select * from PaymentArchive
Select * from Marketing
Select * from Program
Select * from ProgramArchive

Exec usp_InsertProgram '1000','2020-11-11','2009375XX','Dance, Jump & Sing','2021-01-15'

Exec usp_New_Member_and_Program '1020','Roberto','Dark','Hell','N/A','Dublin','Dublin','D12 XXXX','+3538945307040','B','Roberto@gmail.com','2020-11-11','Y','2020-11-13','2009375QP','Modern Dancing','2020-12-31'

Exec usp_InsertTrainer '2009374AA','Domingo','Garcia','Englishhtown','Dublin','Dublin','D20 QQ11','+353894520555','Domingoletsgetfit@gmail.com','2020-06-01','Y'

Exec usp_DeleteMember '1000'

Exec usp_DeleteMemberArchiveGDPR '1004'

Exec usp_DeleteMemberGDPR '1001','+353894520768','rosa@gmail.com','2020-02-01'

Select * from ActiveMember_Book

Select * from Non_ActiveMember_Marketing_Book


