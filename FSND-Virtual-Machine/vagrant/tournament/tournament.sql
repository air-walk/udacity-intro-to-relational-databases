-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
create table players (id serial, name text, num_matches integer, wins integer);

create table matches (id serial, p1 integer, p2 integer, winner integer);