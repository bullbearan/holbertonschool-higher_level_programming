-- This script lists all databases of your MySQL server
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
