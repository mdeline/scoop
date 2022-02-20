-- Connecting to the databse
create role dbconnect with
    nologin
    nosuperuser
    noinherit
    nocreatedb
    nocreaterole
    noreplication
;

-- Read privileges
create role dbreader with
    nologin
    nosuperuser
    noinherit
    nocreatedb
    nocreaterole
    noreplication
;

-- Write privileges
create role dbwriter with
    nologin
    nosuperuser
    noinherit
    nocreatedb
    nocreaterole
    noreplication
;

create role dbmanager with
    login
    nosuperuser
    noinherit
    nocreatedb
    nocreaterole
    noreplication
    password 'manager';

grant dbconnect, dbreader, dbwriter to dbmanager;

/* Create database */
create database scoop
    with owner = dbmanager
    encoding = 'UTF8'
    lc_collate = 'en_US.UTF-8'
    lc_ctype = 'en_US.UTF-8'
    tablespace = pg_default
    connection limit = -1;

grant connect on database scoop to dbconnect;
grant all on database scoop to dbmanager;

/* Schema */
create schema if not exists scoop authorization dbmanager;
alter role dbmanager set search_path to scoop;

-- Privileges
grant all on schema scoop to dbmanager;
alter default privileges in schema scoop grant all on sequences to dbmanager;
alter default privileges in schema scoop grant select, insert, delete, update, truncate on tables to dbmanager;
grant usage on schema scoop to dbreader, dbwriter;
grant select on all sequences in schema scoop to dbreader;
grant usage, select on all sequences in schema scoop to dbwriter;

alter default privileges in schema scoop grant select on tables to dbreader;
alter default privileges in schema scoop grant select on sequences to dbwriter;
alter default privileges in schema scoop grant usage, select on sequences to dbwriter;
alter default privileges in schema scoop grant select, insert, delete, update on tables to dbwriter;

/* Create Tables */

-- Role
drop table if exists scoop.role;
create table scoop.role (
    id serial not null,
    name varchar(50) not null,
    constraint role_pk primary key (id),
    constraint role_name_uk unique(name)
);

insert into scoop.role(name) values ('user'), ('admin');

-- App user
drop table if exists scoop.appuser;
create table scoop.appuser (
    id serial not null,
	fullname text not null,
    email varchar(50) not null,
    password text not null,
    role_id bigint not null,
    img_url text null,
    constraint appuser_pk primary key (id),
    constraint appuser_email_uk unique (email),
	constraint appuser_role_fk foreign key(role_id) references scoop.role(id)
);

-- Venue
drop table if exists scoop.restaurant, scoop.venue;
create table scoop.venue (
    id serial not null,
    name text not null,
    description text null,
    info_url text null,
    img_url text null,
    street_address varchar(50) not null,
    postal_code varchar(5) not null,
    city varchar(50) not null,
    neighbourhood varchar(50) null,
	created_at timestamp with time zone not null default now(),
    constraint restaurant_pk primary key (id)
    -- constraint venue_name_uk unique (name)
);

-- Review
drop table if exists scoop.review;
create table scoop.review
(
    id serial not null,
    venue_id bigint not null,
    appuser_id bigint not null,
    review text not null, 
    stars int not null,
    created_at timestamptz not null default now(),
    modified_at timestamptz null,
    constraint review_pk primary key (id),
    constraint venue_id_fk foreign key(venue_id) references scoop.venue(id),
    constraint appuser_id_fk foreign key(appuser_id) references scoop.appuser(id)
);

-- do later
-- Category
create table scoop.category
(
    id serial not null,
    name varchar(25) not null,
    constraint category_pk primary key (id),
    constraint category_name_uk unique(name)
);

insert into scoop.category(name) 
values ('Korean'), ('Mexican'), ('Italian'), ('Nepalese'), ('Salad'), ('Dessert'), ('Street Food'), ('Vegan'); 

-- Venue Category
create table scoop.venuecategory
(
    id serial not null,
    venue_id bigint not null, -- fk
    category_id bigint not null,
    constraint venuecategory_pk primary key(id),
    constraint venue_id_fk foreign key(venue_id) references scoop.venue(id),
    constraint category_id_fk foreign key(category_id) references scoop.category(id)
);

insert into scoop.restaurantcategory(restaurant_id, category_id) 
values (1, 1), (1, 6);