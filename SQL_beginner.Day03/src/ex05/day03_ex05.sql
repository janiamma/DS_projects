WITH Visited AS (
    SELECT 
        pizzeria.id AS v_pizzeria,
  		pizzeria.name as pizzeria_name, 
        person.id
    FROM pizzeria
    JOIN person_visits pv ON pv.pizzeria_id = pizzeria.id
    JOIN person ON pv.person_id = person.id
    WHERE person.name = 'Andrey'
)
SELECT 
     vd.pizzeria_name 
FROM 
    Visited vd
WHERE
    vd.v_pizzeria not IN (
    SELECT menu.pizzeria_id
	FROM menu
	WHERE menu.id IN (
    SELECT DISTINCT po.menu_id
    FROM person_order po
    WHERE po.person_id = vd.id
))
ORDER BY 1;