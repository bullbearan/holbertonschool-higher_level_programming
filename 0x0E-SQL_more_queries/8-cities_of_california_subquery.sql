-- This sql script lists all privileges of the MySQL users
SELECT id, name FROM cities
WHERE states.name = 'California'
ORDER BY id
