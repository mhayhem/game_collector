CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    disabled BOOLEAN NOT NULL DEFAULT 0,
    is_admin BOOLEAN NOT NULL DEFAULT 0,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    developer TEXT DEFAULT 'Unknow',
    year_release DATETIME,
    img_url TEXT NOT NULL DEFAULT 'No image',
);

CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS platforms (
    platform_id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform_name TEXT NOT NULL UNIQUE,
    manufacturer_id INTEGER NOT NULL

    FOREIGN KEY (manufacturer_id)
        REFERENCES manufacturers(manufacturer_id)
);

CREATE TABLE IF NOT EXISTS user_games (
    user_game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    game_platform_id INTEGER NOT NULL,
    game_format TEXT NOT NULL,
    purchase_status TEXT NOT NULL,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)
    
    FOREIGN KEY (game_platform_id)
        REFERENCES game_platform(game_platform_id)
);

CREATE TABLE IF NOT EXISTS game_platform (
    game_platform_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL,
    platform_id INTEGER NOT NULL,

    UNIQUE(game_id, platform_id)

    FOREIGN KEY (game_id)
        REFERENCES games(game_id)
    
    FOREIGN KEY (platform_id)
        REFERENCES platforms(platform_id)
);

