WITH tb_stats AS (
    SELECT MIN(qtdPontos) AS Mínimo,
           AVG(qtdPontos) AS Média,
           MAX(qtdPontos) AS Máximo
    FROM points
), 

tb_subset_mediana AS (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (select count(*) % 2 == 0 from points)
    OFFSET (select count(*) / 2 from points)
),

tb_mediana AS (
    SELECT AVG(qtdPontos) AS Mediana
    FROM tb_subset_mediana
),

tb_subset_quartil_01 AS (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (select count(*) % 2 == 0 from points)
    OFFSET (select 1 * count(*) / 4 from points)
),

tb_quartil_01 AS (
    SELECT AVG(qtdPontos) AS Quartil_01
    FROM tb_subset_quartil_01
),

tb_subset_quartil_03 AS (
    SELECT qtdPontos
    FROM points
    ORDER BY qtdPontos
    LIMIT 1 + (select count(*) % 2 == 0 from points)
    OFFSET (select 3 * count(*) / 4 from points)
),

tb_quartil_03 AS (
    SELECT AVG(qtdPontos) AS Quartil_03
    FROM tb_subset_quartil_03
)

SELECT  a.Mínimo,
        a.Média,
        b.*,
        c.*,
        d.*,
        a.Máximo
FROM tb_stats a, tb_quartil_01 b, tb_mediana c, tb_quartil_03 d
