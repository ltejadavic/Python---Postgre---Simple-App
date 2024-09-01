CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE activities (
    activity_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    date DATE NOT NULL,
    steps INT,
    calories INT,
    active_minutes INT,
    water_ml INT
);