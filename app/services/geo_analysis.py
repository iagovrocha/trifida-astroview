import rasterio
import geopandas as gpd
from shapely.geometry import Point
from rasterio.mask import mask

# NOTA: Você precisa baixar este arquivo de dados de população antes!
POPULATION_DATA_PATH = "data/population/data.tif"
ECONOMIC_VALUE_PER_CAPITA_USD = 15000

def get_population_in_radius(lat: float, lng: float, radius_km: float) -> int:
    """
    Calcula a população estimada dentro de um raio a partir de um ponto central.
    """
    try:
        # 1. Cria um círculo geográfico (buffer) ao redor do ponto de impacto
        point = Point(lng, lat)
        gdf_point = gpd.GeoDataFrame([1], geometry=[point], crs="EPSG:4326")
        radius_degrees = radius_km / 111.32 # Aproximação de km para graus
        gdf_circle = gdf_point.buffer(radius_degrees)

        # 2. Abre o mapa de população e recorta apenas a área do círculo
        with rasterio.open(POPULATION_DATA_PATH) as src:
            out_image, _ = mask(src, gdf_circle, crop=True)
            # 3. Soma os valores de todos os pixels (a população) dentro do círculo
            population_sum = out_image[out_image > 0].sum()
            
        return int(population_sum)
    except Exception as e:
        print(f"Erro ao calcular população: {e}")
        return 0


def get_economic_impact(population_in_risk: int) -> float:
    """
    Estima o impacto económico com base na população afetada.
    """
    economic_impact = population_in_risk * ECONOMIC_VALUE_PER_CAPITA_USD
    return economic_impact