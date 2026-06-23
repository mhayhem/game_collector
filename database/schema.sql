CREATE TABLE IF NOT EXIST users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXIST games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
    genre TEXT NOT NULL,
    platform TEXT NOT NULL,
    game_format TEXT NOT NULL,
    status TEXT NOT NULL,
    img_url TEXT NOT NULL DEFAULT "No image",
    user_id INTEGER NOT NULL,
);