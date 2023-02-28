from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
from astropy import units as u

# Defina as coordenadas do objeto de interesse
ra = 23.133381
dec = -52.322797
coords = SkyCoord(ra, dec, unit="deg")

# Use a função Tesscut.get_sectors para encontrar os setores que cobrem as coordenadas do objeto
sectors = Tesscut.get_sectors(coordinates=coords)
print(f"Sectores que cobrem as coordenadas do objeto: {sectors}")

# Definir o setor que queremos baixar
sector_table = sectors[0]
sector = sector_table['sectorName']

# Baixar a imagem do setor usando Tesscut
hdus = Tesscut.get_cutouts(coords, size=10, sector=sector)