-- script that computes and stores avg score for student
DELIMITER //

DROP PROCEDURE if EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT) BEGIN
UPDATE users
SET average_score = (
    SELECT AVG(score)
    FROM corrections AS C
    WHERE c.user_id = user_id
  )
WHERE id = user_id;
END //
DELIMITER;
