-- listing students with score less than 80 and no meetings
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE SCORE < 80
AND last_meeting IS NULL
or last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH);
