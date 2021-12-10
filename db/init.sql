CREATE TABLE movie (
    movie_id serial PRIMARY KEY,
    title varchar(40) NOT NULL,
    imdbID char(10) NOT NULL,
    release_year int,
    runtime varchar(10),
    imdb_rating float,
    main_photo char(200),
    description char(300)
);

CREATE TABLE person (
    person_id serial PRIMARY KEY,
    username varchar(30) NOT NULL
);

CREATE TABLE review (
    review_id serial PRIMARY KEY,
    person_id int NOT NULL,
    movie_id int NOT NULL,
    rating float NOT NULL,
    description varchar(500),
    review_date date NOT NULL,
    constraint fk_person
        foreign key(person_id) references person(person_id),
    constraint fk_movie
        foreign key(movie_id) references movie(movie_id)
);

insert into movie(title, imdbID, release_year, runtime, imdb_rating, main_photo, description)
values ('Thor: The Dark World', 'tt1981115', 2013, '1h 52min',  6.9, 'https://m.media-amazon.com/images/M/MV5BMTQyNzAwOTUxOF5BMl5BanBnXkFtZTcwMTE0OTc5OQ@@.jpg', 'When the Dark Elves attempt to plunge the universe into darkness, Thor must embark on a perilous and personal journey that will reunite him with doctor Jane Foster.')

insert into person(username) values ('testuser')

insert into review(person_id, movie_id, rating, description, review_date)
values ( 1, 1, 3.2, 'This is a test description', current_timestamp)