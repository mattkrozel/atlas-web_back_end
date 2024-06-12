-- sql script ranking country origins of bands ordered by fans
SELECT origin,
    SUM(fans) AS nb_fans
from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
    