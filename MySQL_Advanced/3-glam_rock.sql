-- listing all bands with glam rock and ranked by lonngevity
SELECT band_name,
    COALESCE(split, 2020) - formed as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
