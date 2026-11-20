WITH ADD_menu AS (
    SELECT MAX(menu.id) + 1 AS new_id, pizzeria.id AS p_id
    FROM pizzeria
    JOIN menu ON pizzeria.id = menu.pizzeria_id
    WHERE pizzeria.name = 'Dominos'
    GROUP BY pizzeria.id
)
INSERT INTO menu (id, pizzeria_id, pizza_name, price)
SELECT new_id, p_id, 'sicilian pizza', 900
FROM ADD_menu;