-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER `decrease_item_quantity`
BEFORE INSERT ON `orders`
FOR EACH ROW
UPDATE `items`
SET `quantity` = `quantity` - NEW.`number`
WHERE NEW.`item_name` = `name`;
