-- script to reset the attribute valid_email if changed
DELIMITER //
CREATE TRIGGER reset_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END; //
DELIMITER;
