CREATE DATABASE IF NOT EXISTS nonliteral;
CREATE USER IF NOT EXISTS 'nonliteral' IDENTIFIED BY 'celikpromet';
GRANT ALL PRIVILEGES ON nonliteral.* TO 'nonliteral'@'%';
FLUSH PRIVILEGES;
