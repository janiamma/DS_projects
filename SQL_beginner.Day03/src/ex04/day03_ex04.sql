(SELECT pz.name AS pizzeria_name
FROM pizzeria pz
JOIN menu ON pz.id = menu.pizzeria_id
JOIN person_order po ON menu.id = po.menu_id
JOIN person ON po.person_id = person.id
WHERE person.gender = 'male'
EXCEPT
    SELECT pz.name AS pizzeria_name
    FROM pizzeria pz
    JOIN menu ON pz.id = menu.pizzeria_id
    JOIN person_order po ON menu.id = po.menu_id
    JOIN person ON po.person_id = person.id
    WHERE person.gender = 'female'
)

UNION
	
(SELECT pz.name AS pizzeria_name
FROM pizzeria pz
JOIN menu ON pz.id = menu.pizzeria_id
JOIN person_order po ON menu.id = po.menu_id
JOIN person ON po.person_id = person.id
WHERE person.gender = 'female'
EXCEPT
    SELECT pz.name AS pizzeria_name
    FROM pizzeria pz
    JOIN menu ON pz.id = menu.pizzeria_id
    JOIN person_order po ON menu.id = po.menu_id
    JOIN person ON po.person_id = person.id
    WHERE person.gender = 'male'
)
ORDER BY pizzeria_name;