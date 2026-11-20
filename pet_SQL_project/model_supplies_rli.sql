                       Список отношений
 Схема  |         Имя         |        Тип         | Владелец
--------+---------------------+--------------------+----------
 public | goods               | таблица            | postgres
 public | goods_type          | таблица            | postgres
 public | invoices            | таблица            | postgres
 public | invoices_id_seq     | последовательность | postgres
 public | req                 | таблица            | postgres
 public | req_id_seq          | последовательность | postgres
 public | req_item            | таблица            | postgres
 public | req_item_id_seq     | последовательность | postgres
 public | shipment            | таблица            | postgres
 public | shipment_id_seq     | последовательность | postgres
 public | stock               | таблица            | postgres
 public | stock_balance_today | представление      | postgres
 public | supplier            | таблица            | postgres


/* пример создания таблицы goods */
create table goods
( id bigint primary key ,
  name varchar not null,
  measure varchar default 'kg' not null ,
  goods_type bigint,
  constraint fk_goods_goods_type foreign key  (goods_type) references goods_type(type_id)
  );
alter table goods add constraint ch_measure check ( measure in ('kg','pcs') );


/* структура таблицы goods в postgresql*/

                                       Таблица "public.goods"
  Столбец   |        Тип        | Правило сортировки | Допустимость NULL |      По умолчанию
------------+-------------------+--------------------+-------------------+-------------------------
 id         | bigint            |                    | not null          |
 name       | character varying |                    | not null          |
 measure    | character varying |                    | not null          | 'kg'::character varying
 goods_type | bigint            |                    |                   |
Индексы:
    "goods_pkey" PRIMARY KEY, btree (id)
Ограничения внешнего ключа:
    "fk_goods_goods_type" FOREIGN KEY (goods_type) REFERENCES goods_type(type_id)
Ссылки извне:
    TABLE "shipment" CONSTRAINT "fk_shipment_goods_id" FOREIGN KEY (goods_id) REFERENCES goods(id)
    TABLE "req_item" CONSTRAINT "req_item_goods_id_fkey" FOREIGN KEY (goods_id) REFERENCES goods(id)


/* пример заполнения таблицы данными */
INSERT INTO goods (id, name, measure, goods_type) VALUES
(1, 'пирожное', 'kg', 2),
(3, 'вафли вес', 'kg', 4),
(4, 'геркулес - овсяные хлопья', 'kg', 4),
(5, 'горох шлифованный/колотый', 'kg', 4),
(6, 'горошек зелёный', 'pcs', 4),
(7, 'гречка', 'kg', 4);


/* вывод по запросу SELECT * FROM goods LIMIT 7 */
 id |           name            | measure | goods_type
----+---------------------------+---------+------------
  1 | пирожное                  | pcs     |          2
  2 | брусника                  | kg      |          3
  3 | вафли вес                 | kg      |          4
  4 | геркулес - овсяные хлопья | kg      |          4
  5 | горох шлифованный/колотый | kg      |          4
  6 | горошек зелёный           | pcs     |          4
  7 | гречка                    | kg      |          4


/* вывод всех строк таблицы goods_type */

 type_id |         type_name
---------+---------------------------
       1 | мясо рыба и полуфабрикаты
       2 | молочка
       3 | фрукты овощи
       4 | сухие продукты


/* пример структуры таблицы shipment (поставки) */

                                                     Таблица "public.shipment"
    Столбец    |          Тип           | Правило сортировки | Допустимость NULL |                  По умолчанию        
---------------+------------------------+--------------------+-------------------+-------------------------------------------------
 id            | integer                |                    | not null          | nextval('shipment_id_seq'::regclass)
 invoice_id    | bigint                 |                    |                   |
 goods_id      | bigint                 |                    | not null          |
 quantity      | numeric                |                    | not null          |
 price         | numeric(10,2)          |                    | not null          |
 amount        | numeric(10,2)          |                    |                   | generated always as ((price * quantity)) stored
 producer_name | character varying(100) |                    |                   |
 expire_date   | date                   |                    |                   |
Индексы:
    "shipment_pkey" PRIMARY KEY, btree (id)
Ограничения внешнего ключа:
    "fk_shipment_goods_id" FOREIGN KEY (goods_id) REFERENCES goods(id)
    "fk_shipment_invoice_id" FOREIGN KEY (invoice_id) REFERENCES invoices(id)


/* выборка накладных по дате с наименованием поставщика и сортировкой по складу, наименованию и номеру накладной */
SELECT
    i.delivery_date AS date,
    i.invoice_number AS invoice,
    s.name AS supplier,
    sk.stock_name AS sklad
FROM invoices i
JOIN supplier s ON i.shipper_id = s.id
JOIN stock sk ON i.sklad_id = sk.stock_id
WHERE delivery_date = '2025-09-11'
ORDER BY 4, 3, 2;

/* ответ на запрос */
    date    |   invoice   |   supplier   |   sklad
------------+-------------+--------------+-----------
 2025-09-11 | 3630        | ООО Готово   | бюджет
 2025-09-11 | 1325        | ООО Индюков  | бюджет
 2025-09-11 | 1326        | ООО Индюков  | бюджет
 2025-09-11 | 1508        | ООО Мясников | бюджет
 2025-09-11 | 1509        | ООО Мясников | бюджет
 2025-09-11 | 3627        | ООО Готово   | внебюджет
 2025-09-11 | 3628        | ООО Готово   | внебюджет
 2025-09-11 | 3629        | ООО Готово   | внебюджет
 2025-09-11 | 1327        | ООО Индюков  | внебюджет
 2025-09-11 | 1328        | ООО Индюков  | внебюджет
 2025-09-11 | 1510        | ООО Мясников | внебюджет
 2025-09-11 | 1511        | ООО Мясников | внебюджет
 2025-09-11 | б/н балык 1 | ООО Судаков  | внебюджет