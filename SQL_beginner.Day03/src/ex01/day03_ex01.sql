SELECT menu.id as menu_id
FROM menu
WHERE menu.id NOT IN (
    SELECT DISTINCT po.menu_id
    FROM person_order po
)
ORDER BY 1 ASC;