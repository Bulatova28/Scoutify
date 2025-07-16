CREATE DATABASE scoutify_gitdb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
use scoutify_gitdb;
SHOW TABLES;

create table country (
    id_country int auto_increment primary key,
    country_name varchar(15) unique not null
);

create table event_type (
    id_event_type int auto_increment primary key,
    event_type_name varchar(50) unique not null
);

create table role(
	id_role int auto_increment primary key,
    role_name varchar(15) unique not null
);

create table formation_org(
	id_form int auto_increment primary key,
    form_name varchar(160) not null
);

create table user(
	id_user int auto_increment primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(100) unique not null,
    user_password varchar(255) not null,
    phone int(9) not null,
    formation_id int null,
    foreign key (formation_id) references formation_org(id_form)
		ON DELETE SET NULL
);

create table user_roles (
	user_id int not null,
    role_id int not null,
    primary key (user_id, role_id),
    foreign key (user_id) references user(id_user)
		ON DELETE CASCADE,
    foreign key (role_id) references role(id_role)
    ON DELETE CASCADE
);

create table event(
	id_event int auto_increment primary key,
    title varchar(150) not null,
    start_date datetime not null,
    end_date datetime null,
    location varchar(100) not null,
    price decimal(6,2) not null check (price >= 0),
    currency varchar(3) not null,
    age_category varchar (15) not null,
    transportation varchar(200),
    application varchar(500) null,
    description text null,
    country_id int not null,
    foreign key (country_id) references country(id_country),
    event_type_id int not null,
    foreign key (event_type_id) references event_type(id_event_type),
    organizer_id int null,
    foreign key (organizer_id) references user(id_user),
    event_image varchar(255) null
);

insert into country
values (1, 'Україна'),
(2, 'Польща'),
(11, 'Латвія'),
(22, 'Португалія'),
(27, 'Угорщина'),
(29, 'Кувейт');

select * from country order by id_country asc;

insert into event_type
values (1, 'Акції та естафети'),
(2, 'Волонтерство'),
(3, 'Кемпінг'),
(4, 'Форуми та конференції'),
(5, 'Тренінги та сесії');

select * from event_type;

insert into role
values (1, 'Організатор'),
(2, 'Скаут');

select * from role;

insert into formation_org
values (1, 'Грифони'),
(2, 'Сарматівці');

select * from formation_org;

insert into user 
values (1, 'Анастасія', 'Кропивницька', 'examplekrop@gmail.com', '21212121', '987654321', 1),
(2, 'Оксана', 'Коротенко', 'examplekorot@gmail.com', '32323232', '123456789', 2);

select * from user;

insert into user_roles
values (1, 2),
(2, 1);

select * from user_roles;

DESCRIBE event;

insert into event
values (1, 'Світло миру з Віфлеєму', '2024-12-24', '2024-12-26', 'Краків, Польща', 100, 'USD', '11+', 'Трансфер автобусом зі Львова та Києва до Кракова', 'https://www.google.com', null, 2, 1, 1, 'img/смзв-президент.jpeg'),
(2, 'Табір у Латвії', '2023-05-21', '2023-05-26', 'Рига, Латвія', 250, 'EUR', '16+', 'Автобус зі Львова, Києва та Одеси до Риги', 'https://www.google.com', null, 11, 3, null, 'img/1-bg.jpg');

select * from event;

update event
set description = "Віфлеємський вогонь миру – це міжнародний скаутський захід, що відбувається щороку напередодні Різдва.
Основна мета – поширити символічний вогонь з місця народження Ісуса Христа до всіх, хто його потребує. Вогонь є символом доброї справи й підтримки.
Традицію передавати вогонь придумали австрійські скаути, щоб нагадати суспільству істинну суть Різдва. Про час, коли необхідно подумати про тих, хто потребує допомоги. Особливо про тих, хто не святкуватиме Різдво разом зі своєю родиною через хворобу, життєві обставини або захищаючи нашу країну на фронті.
Вогонь миру — це символ злагоди, спокою, любові до людей та світу."
where id_event = 1;

update event
set description = "Табір у Латвії – це унікальна можливість провести час на мальовничому узбережжі Балтійського моря. 
Учасники насолоджуватимуться захопливими пригодами серед піщаних пляжів, хвойних лісів та чистого повітря. Програма табору включає командні ігри, походи, майстер-класи з виживання та вечірні ватри зі скаутськими піснями. Це ідеальне місце для нових знайомств, розвитку лідерських навичок та зміцнення дружби. 
Табір стане незабутнім досвідом для кожного, хто прагне поєднати відпочинок з природою і дух скаутської спільноти."
where id_event = 2;

insert into event
values (3, 'World Scout Meet 2024', '2024-06-25', '2024-07-03', 'Овар, Португалія', 470, 'EUR', '18-25 років', 'Затверджується для кожного СО/СФ індивідуально через лідера', 'https://www.google.com', null, 22, 3, null, 'img/moot-2025.jpg');

update event 
set description = "World Scout Meet — це міжнародний захід що об'єднує понад 5000 Скаутів віком від 18 до 25 років з усього світу, які збираються разом, щоб обмінятись досвідом та поділитись культурою своєї країни, навчитися найкращого один у одного та здобути нові навички. 
Додаткова інформація: необхідно володіння англійською мовою (B1+); наявність форми, хустки та вишиванки; додаткові витрати (такі як проїзд, страхування, представницькі витрати) складатимуть орієнтовно 1100 євро для учасників та 980 євро для IST"
where id_event = 3;

insert into event
values (4, 'Міжнародний скаутський форум', '2025-03-11', '2025-03-25', 'Ель-Кувейт, Кувейт', 1000, 'USD', '18-26 років', 'Індивідуально', 'https://www.google.com', null, 29, 4, null, 'img/кувейт.jpg');

update event 
set description = "Для участі буде відібрано 1 хлопця (має змогу виїжджати за кордон) і 1 дівчину. 
Участь у Форумі безкоштовна, проте учасники мають покрити витрати на дорогу. Орієнтовна вартість — від 1000 доларів.  
Умови участі: стандартні критерії відбору учасників НОСУ на міжнародні заходи ВОСР згідно з додатком 3"
where id_event = 4;

insert into event
values (5, 'Частинки миру', '2025-04-04', '2025-04-08', 'Будапешт, Угорщина', 50, 'EUR', '18-30 років', 'Індивідуально, витрати покриваються організаторами', 'https://www.google.com', null, 27, 5, null, 'img/частинки-миру.jpg');

update event 
set description = "На учасників чекає міжнародна навчальна сесія, присвячена найбільш актуальним і чутливим темам, з якими стикається молодь в умовах конфлікту.  
Проживання, квитки, харчування покриваються організаторами. 
Критерії відбору: стандартні + бути у ролі Скаутського лідера. З більш детальними умовами участі можна ознайомитись на офіційному сайті."
where id_event = 5;