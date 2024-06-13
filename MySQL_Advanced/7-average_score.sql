-- script that computes and stores avg score for student
DELIMITER //

DROP PROCEDURE if EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT) BEGIN
BEGIN
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END //
DELIMITER;
