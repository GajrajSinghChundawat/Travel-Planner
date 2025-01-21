create database travel_planner;
create table travel_kb(id int, destination varchar(100), description varchar(250), details varchar(250), metadata json);
insert into travel_kb values
(1, 'Paris', 'City of Light', 'Eiffel Tower, Louvre Museum', '{"type":"city"}'),
(2, 'Rome', 'Eternal City', 'Colosseum, Vatican City', '{"type":"city"}'),
(3, 'New York', 'The Big Apple', 'Statue of Liberty, Central Park', '{"type":"city"}'),
(4, 'Tokyo', 'City of the Rising Sun', 'Mount Fuji, Shibuya Crossing', '{"type":"city"}'),
(5, 'Sydney', 'Harbour City', 'Sydney Opera House, Bondi Beach', '{"type":"city"}'),
(6, 'London', 'Capital of England', 'Big Ben, Buckingham Palace', '{"type":"city"}'),
(7, 'Dubai', 'City of Innovation', 'Burj Khalifa, Palm Jumeirah', '{"type":"city"}'),
(8, 'Cairo', 'City of Pyramids', 'Great Pyramid of Giza, Nile River', '{"type":"city"}'),
(9, 'Machu Picchu', 'Lost City of the Incas', 'Ancient Inca Ruins, Sacred Valley', '{"type":"landmark"}'),
(10, 'Kyoto', 'City of Temples', 'Kinkaku-ji, Fushimi Inari Shrine', '{"type":"city"}');

alter table travel_kb add column desc_vectors json;