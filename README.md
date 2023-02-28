# SectorOneFound!



## Sector 1 of TESS found! Finally

* Finalmente encontrei o Setor 6 do Satelite TESS.

* No artigo passado, tentei encontrar algum setor que pudesse baixar a imagem para analisar no Jupyter Notebook. 

Consegui as coordenadas com as seguintes importações

* - import requests
* - from astropy.coordinates import skyCoord
* - import astropy.unity as u

* - ra = 128.96
* - dec = -45.22
* - radius = 0.02
* - product = "SPOC"

* - url = f"https://mast.stsci.edu/tesscut/api/v0.1/sector?ra={ra}&dec={dec}&radius={radius}&product={product}"
* - reseponse = requests.get(url)

* - print(response.text)

#### E foi retornado:

![image](https://user-images.githubusercontent.com/117879893/221717251-e502325a-3273-4085-b4a1-4a140a0d805c.png)

* Com essas coordenadas tentei encontrar algum setor disponivel. Mas não consegui o corte na imagem para obter o objeto. Ao invés disso, retornava um belo de um "O objeto não está no setor desejado " :( 

* Em uma nova tentativa tentei importar  uma coordenada do SkyCoord mas definindo as coordenadas do objeto de interesse. Dessa vez defini as coordenadas do objeto a ser observado, convertendo em graus, e também adicionei a função Tesscut.get_sectors, assim consegui sabeer achar qual setor esta o Objeto do TESS e também baixar com arquivo fits. 

![image](https://user-images.githubusercontent.com/117879893/221718556-3cbe962d-1f63-498f-afae-312eac345cd6.png)

* Realizei algumas analises da imagem mas não o suficiente para dizer o que é. Não esta muito preciso! Preciso de mais tempo para aprender bibliotecas novas para analises e também de mais plotagem dessa imagem de diferentes maneiras para diferentes tipos de analises. 

#### The libraries used in this project were sourced from https://mast.stsci.edu/tesscut/
