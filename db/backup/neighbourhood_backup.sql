--
-- PostgreSQL database dump
--

-- Dumped from database version 13.5 (Ubuntu 13.5-0ubuntu0.21.04.1)
-- Dumped by pg_dump version 13.5 (Ubuntu 13.5-0ubuntu0.21.04.1)

-- Started on 2022-03-06 16:13:49 EET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3068 (class 0 OID 49648)
-- Dependencies: 216
-- Data for Name: neighbourhood; Type: TABLE DATA; Schema: scoop; Owner: mdeline
--

INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (1, 'Röylä', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (2, 'Alppiharju', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (3, 'Herttoniemi', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (4, 'Westend', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (5, 'Mellunkylä', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (6, 'Ulkosaaret', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (7, 'Korso', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (8, 'Kaarela', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (9, 'Haaga', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (10, 'Kamppi', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (11, 'Pasila', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (12, 'Leppävaara', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (13, 'Vaarala', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (14, 'Lauttasaari', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (15, 'Nuuksio', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (16, 'Taka-Töölö', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (17, 'Otaniemi', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (18, 'Länsisatama', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (19, 'Käpylä', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (20, 'Kruununhaka', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (21, 'Laajasalo', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (22, 'Laakso', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (23, 'Myyrmäki', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (24, 'Kauklahti', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (25, 'Sörnäinen', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (26, 'Vartiokylä', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (27, 'Munkkiniemi', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (28, 'Etu-Töölö', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (29, 'Ullanlinna', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (30, 'Kluuvi', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (31, 'Mankkaa', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (32, 'Vallila', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (33, 'Tikkurila', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (34, 'Vuosaari', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (35, 'Karhusuo', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (36, 'Kallio', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (37, 'Viikki', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (38, 'Malmi', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (39, 'Punavuori', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (40, 'Kaivopuisto', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (41, 'Oulunkylä', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (42, 'Tuomarinkylä', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (43, 'Hermanni', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (44, 'Suomenlinna', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (45, 'Veromies', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (46, 'Pakkala', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (47, 'Kulosaari', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (48, 'Eira', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (49, 'Kaartinkaupunki', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (50, 'Tapiola', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (51, 'Viinikkala', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (52, 'Katajanokka', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (53, 'Meilahti', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (54, 'Pitäjänmäki', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (55, 'Tammisto', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (56, 'Olari', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (57, 'Suutarila', '2022-03-05 09:54:54.015104+02');
INSERT INTO scoop.neighbourhood (id, name, created_at) VALUES (58, 'Haukilahti', '2022-03-05 09:54:54.015104+02');


--
-- TOC entry 3074 (class 0 OID 0)
-- Dependencies: 215
-- Name: neighbourhood_id_seq; Type: SEQUENCE SET; Schema: scoop; Owner: mdeline
--

SELECT pg_catalog.setval('scoop.neighbourhood_id_seq', 58, true);
