CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Contact (
    contact_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL DEFAULT '',
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL DEFAULT '',
    phone_number VARCHAR(20) NOT NULL DEFAULT '',
    company_name VARCHAR(50) NOT NULL DEFAULT '',
    company_position VARCHAR(50) NOT NULL DEFAULT '',
    memo VARCHAR(255) NOT NULL DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);


CREATE TABLE Label (
    label_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    label_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);


CREATE TABLE ContactLabel (
    contact_id INT NOT NULL,
    label_id INT NOT NULL,
    PRIMARY KEY (contact_id, label_id),
    FOREIGN KEY (contact_id) REFERENCES Contact(contact_id),
    FOREIGN KEY (label_id) REFERENCES Label(label_id)
);


CREATE TABLE ContactDetail (
    contact_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    contact_id INT NOT NULL,
    type VARCHAR(50) NOT NULL,
    value VARCHAR(255) NOT NULL DEFAULT '',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (contact_id) REFERENCES Contact(contact_id)
);