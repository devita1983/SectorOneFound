from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
import astropy.units as u

# Definir as coordenadas do objeto a ser observado
ra = 79.4806  # em graus
dec = -66.8150  # em graus
coords = SkyCoord(ra, dec, unit=u.deg)

# Usar a função Tesscut.get_sectors() para encontrar o setor que cobre as coordenadas do objeto
sector_table = Tesscut.get_sectors(coordinates=coords)
sector = sector_table[0]['sector']

print(f"Objeto observado no setor {sector} do TESS")

# Baixar a imagem do setor usando Tesscut
hdus = Tesscut.get_cutouts(coordinates=coords, size=10, sector=sector)

# Salvar a imagem em um arquivo fits
hdus[0].writeto("tess_image.fits", overwrite=True)

print("Imagem baixada com sucesso!")