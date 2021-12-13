CREATE TABLE movie (
    movie_id serial PRIMARY KEY,
    title varchar(200) NOT NULL,
    imdbid char(10) NOT NULL,
    release_year int,
    runtime varchar(10),
    main_photo char(200),
    description char(300)
);

CREATE TABLE review (
    review_id serial PRIMARY KEY,
    username varchar(30) NOT NULL,
    movie_id int NOT NULL,
    rating float NOT NULL,
    description varchar(500),
    review_date date NOT NULL,
    constraint fk_movie
        foreign key(movie_id) references movie(movie_id)
);

insert into movie(title, imdbid, release_year, runtime, main_photo, description)
values ('Thor: The Dark World', 'tt1981115', 2013, '1h 52min', 'https://m.media-amazon.com/images/M/MV5BMTQyNzAwOTUxOF5BMl5BanBnXkFtZTcwMTE0OTc5OQ@@.jpg', 'When the Dark Elves attempt to plunge the universe into darkness, Thor must embark on a perilous and personal journey that will reunite him with doctor Jane Foster.');

insert into review(username, movie_id, rating, description, review_date)
values ( 'testUser', 1, 3.2, 'This is a test description', current_timestamp);