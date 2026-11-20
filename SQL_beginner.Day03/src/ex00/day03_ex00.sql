WITH v_dates AS (
    SELECT 
        pizzeria.name as pizzeria_name, 
        pizzeria.id AS v_pizzeria, 
        pv.visit_date
    FROM pizzeria
    JOIN person_visits pv ON pv.pizzeria_id = pizzeria.id
    JOIN person ON pv.person_id = person.id
    WHERE person.name = 'Kate'
)

SELECT 
    menu.pizza_name, 
    menu.price, 
    vd.pizzeria_name AS pizzeria_name, 
    vd.visit_date
FROM 
    v_dates vd
JOIN 
    menu ON menu.pizzeria_id = vd.v_pizzeria
WHERE 
    menu.price BETWEEN 800 AND 1000
ORDER BY 
    1 ASC, -- pizza_name
    2 DESC, -- price
    3 ASC; -- visit_date