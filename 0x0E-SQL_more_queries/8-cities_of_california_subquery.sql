-- This sql script lists all privileges of the MySQL users
SELECT cities.id, cities.name
FROM cities, states
WHERE states.name = 'California' AND cities.state_id = states.id
ORDER BY cities.id
