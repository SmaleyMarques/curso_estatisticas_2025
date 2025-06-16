/*
Rodar 03_tabela_frequencia.py antes
*/

WITH tb_freq_abs AS (

    SELECT  descProduto,
            count(idTransacao) AS 'FreqAbs'

    FROM points
    GROUP BY descProduto

),

tb_freq_acum AS (

    SELECT  *,
            SUM(FreqAbs) OVER (ORDER BY FreqAbs) AS FreqAbsAcum,
            1.0 * FreqAbs / (SELECT SUM(FreqAbs) FROM tb_freq_abs) AS FreqRelativa
    FROM tb_freq_abs

)

    SELECT  *,
            SUM(FreqRelativa) OVER (ORDER BY FreqAbs) AS 'FreqRelativaAcum' 
    
    FROM tb_freq_acum