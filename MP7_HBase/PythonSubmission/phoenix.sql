DROP VIEW IF EXISTS "powers";

CREATE VIEW "powers" (
    pk VARCHAR PRIMARY KEY,
    "professional"."name" VARCHAR,
    "personal"."power" VARCHAR,
    "personal"."hero" VARCHAR
);

SELECT
    p."professional"."name" as "Name1",
    p1."professional"."name" as "Name2",
    p."personal"."power" as "Power"
FROM
    "powers" AS p
JOIN
    "powers" as p1
ON
    p."personal"."power" = p1."personal"."power"
WHERE
    p."personal"."hero" = 'yes' AND p1."personal"."hero" = 'yes';
