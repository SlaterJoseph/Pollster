CREATE TABLE if NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    hashed_password VARCHAR(1024) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    photo TEXT,
    description TEXT
);

CREATE TABLE if NOT EXISTS polls (
    id SERIAL PRIMARY KEY,
    question VARCHAR(1024) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ending_at TIMESTAMP,
    creator_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE if NOT EXISTS poll_options (
    id SERIAL PRIMARY KEY,
    poll_id INT NOT NULL REFERENCES polls(id) ON DELETE CASCADE,
    option_text VARCHAR(255) NOT NULL,
    option_order INT NOT NULL,
    UNIQUE (poll_id, option_order)
);

CREATE TABLE if NOT EXISTS responses (
    user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    poll_id INT NOT NULL REFERENCES polls(id) ON DELETE CASCADE,
    response INT NOT NULL REFERENCES poll_options(id),
    responded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, poll_id)
);

CREATE TABLE if NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    user_id INT NULL REFERENCES users(id) ON DELETE SET NULL,
    poll_id INT NOT NULL REFERENCES polls(id) ON DELETE CASCADE,
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    parent_comment_id INT NULL REFERENCES comments(id)
);