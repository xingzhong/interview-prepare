Player (name CHAR(20), number INT(4))
INSERT INTO Player VALUES ('Bill Henry', 50)
SELECT * FROM Player
SELECT name FROM Player WHERE number < 10 or number > 40
SELECT year, AVG(totalPoints) FROM Stats GROUP BY year
