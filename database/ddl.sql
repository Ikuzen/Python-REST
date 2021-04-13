CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	username varchar(255) NOT NULL,
	birthdate date,
	joined_at date DEFAULT CURRENT_DATE,
	password varchar(30) NOT NULL
);

CREATE TABLE tournaments (
    id SERIAL PRIMARY KEY,
	name varchar(15) unique NOT NULL,
	size INTEGER,
	tournament_type varchar(30),
    organizer_id BIGINT references users(id)
);

CREATE TABLE participations (
	user_id BIGINT references users(id),
	tournament_id BIGINT references tournaments(id)
);