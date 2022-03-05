-- 1. Populoidaan taulu
do $$
	declare 
		row record;
	begin
		for row in (
			select distinct neighbourhood
			from scoop.venue
			where neighbourhood != ''
		)
		loop
			insert into scoop.neighbourhood(name) values(row.neighbourhood);
			raise notice '%', row.neighbourhood;
		end loop;
	end
$$;

-- 2. Lisätään viiteavain
alter table scoop.venue add column  neighbourhood_id int null;
alter table scoop.venue add constraint neighbourhood_fk 
foreign key (neighbourhood_id) references scoop.neighbourhood(id);

-- 3. Populoidaan viiteavain
do $$
	declare 
		row record;
	begin
		for row in (
			select 
				venue.id as venue_id, 
				venue.name as venue_name,
				venue.neighbourhood as venue_nh,
				
				nh.name as neighbourhood_name,
				nh.id as neighbourhood_id
			from scoop.venue
			left join scoop.neighbourhood nh on nh.name = venue.neighbourhood
		)
		loop
			update scoop.venue set neighbourhood_id = row.neighbourhood_id
			where id = row.venue_id;
		end loop;
	end
$$;

-- Tarkistusta 
select venue.neighbourhood, venue.neighbourhood_id, nh.id, nh.name
from scoop.venue left join scoop.neighbourhood nh on nh.id = venue.neighbourhood_id