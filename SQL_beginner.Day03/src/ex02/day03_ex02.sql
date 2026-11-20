SELECT menu.pizza_name, menu.price, pizzeria.name AS pizzeria_name
FROM menu
JOIN pizzeria ON pizzeria.id = menu.pizzeria_id
WHERE menu.id NOT IN (
    SELECT DISTINCT po.menu_id
    FROM person_order po
)
ORDER BY 1, 2 ASC;