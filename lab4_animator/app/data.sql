CREATE DATABASE IF NOT EXISTS animator_booking_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE animator_booking_db;

CREATE TABLE IF NOT EXISTS city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS animator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    specialization VARCHAR(120) DEFAULT '',
    hourly_rate DECIMAL(10, 2) DEFAULT 0.00,
    city_id INT NULL,
    CONSTRAINT fk_animator_city FOREIGN KEY (city_id)
        REFERENCES city(id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS program (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    duration_minutes INT NOT NULL DEFAULT 60
);

CREATE TABLE IF NOT EXISTS animator_program (
    animator_id INT NOT NULL,
    program_id INT NOT NULL,
    PRIMARY KEY (animator_id, program_id),
    CONSTRAINT fk_ap_animator FOREIGN KEY (animator_id)
        REFERENCES animator(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_ap_program FOREIGN KEY (program_id)
        REFERENCES program(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT IGNORE INTO city (id, name) VALUES (1, 'Lviv'), (2, 'Kyiv');

INSERT IGNORE INTO animator (id, name, specialization, hourly_rate, city_id) VALUES
    (1, 'Olena Koval', 'Spider-Man & Quest', 1200.00, 1),
    (2, 'Maxym Bondar', 'Bubble Show', 1500.00, 1),
    (3, 'Sofiia Melnyk', 'Princess Party', 1100.00, 2);

INSERT IGNORE INTO program (id, title, duration_minutes) VALUES
    (1, 'Superhero Mission', 60),
    (2, 'Giant Bubbles', 45),
    (3, 'Royal Ball', 90);

INSERT IGNORE INTO animator_program (animator_id, program_id) VALUES
    (1, 1),
    (1, 3),
    (2, 2),
    (3, 3);