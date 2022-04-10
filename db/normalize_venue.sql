-- 1. Populate the table 'scoop.neighbourhood' with neighbourhood names
insert into scoop.neighbourhood(name, created_at)
select distinct neighbourhood, now() 
from scoop.venue where neighbourhood != ''
returning *; 

-- 2. Add a foreign key 'neighbourhood_id' to 'scoop.venue'
alter table scoop.venue add column neighbourhood_id int null;
alter table scoop.venue add constraint neighbourhood_fk foreign key (neighbourhood_id) references scoop.neighbourhood(id);

-- 3. Populate the foreign key 'neighbourhood_id'
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

-- Checking the data 
select venue.neighbourhood, venue.neighbourhood_id, nh.id, nh.name
from scoop.venue left join scoop.neighbourhood nh on nh.id = venue.neighbourhood_id