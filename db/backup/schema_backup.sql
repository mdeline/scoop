create table scoop.role (
    id serial not null,
    name varchar(50) not null,
    constraint role_pk primary key (id),
    constraint role_name_uk unique(name)
);

insert into scoop.role(name) values ('user'), ('admin');

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

create table scoop.neighbourhood (
    id serial not null,
    name text not null,
	created_at timestamp with time zone not null default now(),
    constraint neighbourhood_pk primary key (id),
    constraint neighbourhood_name_uk unique(name)
);

create table scoop.venue (
    id serial not null,
    name text not null,
    description text null,
    info_url text null,
    img_url text null,
    street_address varchar(50) not null,
    postal_code varchar(5) not null,
    city varchar(50) not null,
    neighbourhood_id bigint null,
	created_at timestamp with time zone not null default now(),
    constraint restaurant_pk primary key (id),
    constraint neighbourhood_fk foreign key(neighbourhood_id) references scoop.neighbourhood(id)
);

create table scoop.review
(
    id serial not null,
    venue_id bigint not null,
    appuser_id bigint not null,
    review text not null, 
    stars int not null,
    created_at timestamptz not null default now(),
    modified_at timestamptz null,
    deleted boolean not null default false,
    constraint review_pk primary key (id),
    constraint venue_id_fk foreign key(venue_id) references scoop.venue(id),
    constraint appuser_id_fk foreign key(appuser_id) references scoop.appuser(id)
);