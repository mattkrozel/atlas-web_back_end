-- sql script creating a trigger that decreases items
CREATE TRIGGER operation
AFTER
INSERT ON orders FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
