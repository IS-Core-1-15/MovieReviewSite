CREATE TABLE movies (
    id char(5) CONSTRAINT firstkey PRIMARY KEY,
    title varchar(40) NOT NULL,
    imdbID char(10) NOT NULL,
    release_year integer,
    runtime varchar(10),
    imdb_rating float,
    main_photo char(50),
    description char(300)
);

