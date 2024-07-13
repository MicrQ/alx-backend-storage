-- sql script that create a users table

CREATE TABLE IF NOT EXISTS `users` (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255)
);
