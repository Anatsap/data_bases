USE iot_db;

INSERT INTO iot_db.movies (movie_id, title, release_year, duration, description, imdb_code, rating) 
VALUES
(1, 'Space Adventure', 2023, 120, 'Космічна пригода з екшн-сценами', 'IMDB001', 8.5),
(2, 'Love in Paris', 2021, 95, 'Романтична комедія у Парижі', 'IMDB002', 7.9),
(3, 'Mystery Mansion', 2022, 110, 'Детективна історія з несподіваним фіналом', 'IMDB003', 8.2),
(4, 'Superhero Chronicles', 2020, 140, 'Епічний супергеройський фільм', 'IMDB004', 8.8),
(5, 'The Last Samurai', 2003, 134, 'Історична драма', 'IMDB005', 9.0),
(6, 'Comedy Nights', 2019, 100, 'Легка комедія для всієї родини', 'IMDB006', 7.5),
(7, 'Ocean’s Secrets', 2024, 125, 'Пригодницький фільм про океан', 'IMDB007', 8.1),
(8, 'Horror House', 2018, 90, 'Жахи з несподіваними сюжетними поворотами', 'IMDB008', 6.9),
(9, 'Time Traveler', 2025, 115, 'Науково-фантастичний фільм', 'IMDB009', 8.3),
(10, 'Magical Forest', 2022, 105, 'Фентезі-пригода у чарівному лісі', 'IMDB010', 7.8);
INSERT INTO iot_db.movie_descriptions (description_id, movie_id, full_description, keyword) 
VALUES
(1, 1, 'In a world threatened by evil forces, a young hero discovers his true power...', 'hero'),
(2, 2, 'Two families have been enemies for generations. Their children fall in love...', 'romance'),
(3, 3, 'Astronauts travel to a distant planet to save humanity from extinction...', 'sci-fi'),
(4, 4, 'A brilliant detective must solve a series of mysterious murders in the city...', 'mystery'),
(5, 5, 'Young students learn magic and uncover a dark plot threatening their world...', 'fantasy'),
(6, 6,'During a great war, heroes rise and empires fall, changing history forever...', 'historical'),
(7, 7,'Two friends get caught in ridiculous situations while trying to impress...', 'comedy'),
(8, 8, 'A group of strangers must survive after a plane crash in the dangerous jungle...', 'adventure'),
(9, 9,'In a dystopian future, rebels fight against a corrupt government to reclaim...', 'dystopia'),
(10, 10,'A small-town musician travels the world to find inspiration and true love...', 'musical');
INSERT INTO iot_db.actors (actor_id, name, birth_date, nationality, bio, imdb_code, last_name) 
VALUES
(1, 'Robert', '1965-04-04', 'USA', 'American actor, famous for Iron Man', 'nm0000375', 'Downey'),
(2, 'Anna', '1984-11-22', 'USA', 'Actress known for Black Widow', 'nm0424060', 'Loise'),
(3, 'Chris ', '1981-06-13', 'USA', 'Played Captain America', 'nm0262635', 'Ewanse'),
(4, 'Chris ', '1983-08-11', 'USA', 'Known for Thor in MCU', 'nm1165110', 'Hemworth'),
(5, 'Mark', '1983-08-11', 'USA', 'Known for Hulk in Avengers', 'nm0749263', 'Ruffalo'),
(6, 'Jeremy', '1971-01-07', 'UK', 'Actor known for Hawkeye', 'nm0719637', 'Renner'),
(7, 'Tom', '1996-06-01', 'UK', 'Known for Spider-Man', 'nm4043618', 'Holland'),
(8, 'Zendaya', '1996-09-01', 'UK', 'Actress and singer', 'nm3918035', 'Holland'),
(9, 'Benedict', '1976-07-19', 'Australia', 'Known for Doctor Strange', 'nm1212722', 'Cunberbatch'),
(10, 'Elizabeth', '1989-02-16', 'Australia', 'Played Scarlet Witch', 'nm0646073', 'Olsen'),
(11, 'Anna', '1976-07-02', 'Australia', 'Known as superhero', 'nm0646042', 'Welyo');
INSERT INTO iot_db.movie_actors(movie_id, actor_id, character_name, billing_order) 
VALUES
(1, 1, 'Hero', 1),
(1, 2, 'Animated Hero', 2),
(1, 3, 'Sidekick', 3),
(1, 5, 'Villain', 3),
(2, 2, 'Lol', 1),
(2, 4, 'Romantic Lead', 2),
(2, 5, 'Friend', 3),
(3, 6, 'Comic Relief', 1),
(3, 5,'Captain', 2),
(3, 3, 'Alien', 3),
(4, 3, 'Scientist', 1),
(4, 4, 'Detective', 2),
(4, 5,'Suspect', 1),
(5, 7, 'OJOK', 1),
(5, 5,'King', 2),
(6, 5,'People', 3);
INSERT INTO iot_db.reviews(review_id, movie_id, user_name, rating, comment) 
VALUES
(1, 1, 'User1', 9.0, 'Amazing action scenes!'),
(2, 2, 'User2', 7.0, 'Funny and light'),
(3, 3, 'User3', 10.0, 'Loved the sci-fi plot'),
(4, 4, 'User4', 2.0, 'Too slow for me'),
(5, 5, 'User5', 5.0, 'Great for kids'),
(6, 6, 'User6', 8.0, 'Beautiful historical setting'),
(7, 7, 'User7', 9.0, 'Informative documentary'),
(8, 8, 'User8', 8.0, 'Epic fantasy adventure'),
(9, 9,'User9', 4.0, 'Very bad show'),
(10, 4, 'User10', 5.8, 'Just not for me'),
(11, 7, 'User8', 7.4, 'Not bad');
INSERT INTO iot_db.movie_facts(fact_id, movie_id, fact_text, source) 
VALUES
(1, 1, 'Filming lasted for 6 months.', 'Studio archive'),
(2, 2, 'More than 200 costumes were used.', 'Production notes'),
(3, 3, 'Part of the movie was filmed in space.', 'Behind-the-scenes'),
(4, 4, 'All props were handcrafted.', 'Interview'),
(5, 5, 'Actors performed all the stunts themselves.', 'Director’s commentary'),
(6, 1, 'The soundtrack won an award.', 'Award records'),
(7, 3, 'The premiere took place simultaneously in 50 countries.', 'Press release'),
(8, 2, 'The script was rewritten 3 times.', 'Screenwriter interview'),
(9, 3, 'The premiere took place simultaneously in 50 countries.', 'Press release'),
(10, 2, 'The script was rewritten 3 times.', 'Screenwriter interview');
INSERT INTO iot_db.country(country_id, country_name) 
VALUES
(6, 'Canada'),
(3, 'France'),
(4, 'Germany'),
(5, 'Japan'),
(2, 'UK'),
(10, 'Ukraine'),
(8, 'Italy'),
(7, 'Switzerland'),
(9, 'Colombia'),
(1, 'USA');
INSERT INTO iot_db.box_office(box_id, movie_id, country_id, amount) 
VALUES
(1, 1, 1, 250000000.00),
(2, 1, 2, 80000000.00),
(3, 2, 3, 120000000.00),
(4, 3, 3, 50000000.00),
(5, 3, 4, 180000000.00),
(6, 4, 5, 30000000.00),
(7, 5, 2, 90000000.00),
(8, 2, 6, 20000000.00),
(9, 6, 4, 80000000.00),
(10, 4, 1, 900000000.00);
INSERT INTO iot_db.genres(genre_id, name) 
VALUES
(1, 'Action'),
(2, 'Comedy'),
(3, 'Sci-Fi'),
(4, 'Thriller'),
(5, 'Animation'),
(6, 'Drama'),
(7, 'Documentary'),
(8, 'Drama'),
(9, 'Documentary'),
(10, 'Fantasy');
INSERT INTO iot_db.movie_genres( movie_id, genre_id) 
VALUES
(1, 1), (1, 2), (4, 2), (2, 3),
(1, 4), (5, 6), (2, 7), (2, 8),
(2, 1), (2, 5);
INSERT INTO iot_db.directors(director_id, first_name, last_name, nationality, imdb_code) 
VALUES
(1, 'Christopher', 'Nolan', 'British', 'nm0634240'),
(2, 'Greta', 'Gerwig', 'American', 'nm1950086'),
(3, 'Quentin', 'Tarantino', 'American', 'nm0000233'),
(4, 'Denis', 'Villeneuve', 'Canadian', 'nm0898288'),
(5, 'Sofia', 'Coppola', 'Mexican', 'nm0001068'),
(6, 'Bong', 'Joon-ho', 'South Korean', 'nm0097835'),
(7, 'Alfonso', 'Cuarón', 'Mexican', 'nm0190859'),
(8, 'Bong', 'Joon-ho', 'South Korean', 'nm0094435'),
(9, 'Alfonso', 'Cuarón', 'Mexican', 'nm0190853'),
(10, 'Alfonso', 'Cuarón', 'Mexican', 'nm0190959'),
(11, 'Alfonso', 'Cuarón', 'Mexican', 'nm0190439');
INSERT INTO iot_db.movie_directors( movie_id, director_id) 
VALUES
(1, 1), (1, 2), (2, 2), (3, 2),
(1, 3), (3, 3), (2, 4), (4, 4),
(2, 3), (4, 1);