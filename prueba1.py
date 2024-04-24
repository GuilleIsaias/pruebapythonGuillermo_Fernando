#R1: Importación de Librerias
import requests
import json
from string import Template
#R2: Función
def request_get(url):
    return json.loads(requests.get(url).text)
#R3: Obtencion de data
jsondata = request_get('https://aves.ninjas.cl/api/birds')
#R4: Obtención de dato de estudio
datos = [{"name_sp": bird["name"]["spanish"], "name_en": bird["name"]["english"], "image": bird["images"]["main"]} for bird in jsondata]
#R5: Creación de Template HTML
img_template = Template('<div class="card" style="width: 18rem;"><img src="$url"class="card-img-top" width="182" height="200" ><div class="card-body"></div><ul class="list-group list-group-flush"><li class="list-group-item"><p>$name_sp</p></li><li class="list-group-item"><p>$name_en</p></td></li></ul></div>')
html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <title>Aves de chile</title>
                            </head>
                            <body>
                            <h1>Aves de chile</h1>
                            <div style="display:flex; flex-wrap:wrap;"> $body </div>
                            </body>
                            </html>
                        ''')
#R6: Iteracion Template
lista_img = [img_template.substitute(url = elemento['image'], name_sp = elemento['name_sp'], name_en = elemento['name_en']) for elemento in datos]
#R7: HTML final
lista_img = ', '.join(lista_img)
html = html_template.substitute(body = lista_img)
print(html)
#R8: Creacion archivo HTML
with open('index.html', 'w') as f:
    f.write(html)
