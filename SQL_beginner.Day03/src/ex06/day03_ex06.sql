SELECT
    menu1.pizza_name,
    pz1.name AS pizzeria_name1,
    pz2.name AS pizzeria_name2,
    menu1.price
FROM menu AS menu1
JOIN menu AS menu2 ON menu1.price = menu2.price
JOIN pizzeria AS pz1 ON menu1.pizzeria_id = pz1.id
JOIN pizzeria AS pz2 ON menu2.pizzeria_id = pz2.id
    WHERE menu1.id > menu2.id
            AND menu1.pizza_name = menu2.pizza_name
ORDER BY pizza_name;