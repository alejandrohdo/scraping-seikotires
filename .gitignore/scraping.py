import requests
import json
from lxml import html
headers = {
    'authority': 'seikotires-mx.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'es-PE,es-US;q=0.9,es-419;q=0.8,es;q=0.7',
}

params = (
    ('id_c', '40'),
)

response = requests.get('https://seikotires-mx.com/cotizacion_p.php', 
    headers=headers, 
    params=params)

tree = html.fromstring(response.content)
list_data = []
for row in range(2,5):
    dict_data = {}
    for colum in range(1,10):
        name_colum = tree.xpath('//table[1]/tbody/tr[1]/td['+str(colum)+']/b/text()')[0]
        value_colum = tree.xpath("//table[1]/tbody/tr["+str(row)+"]/td["+str(colum)+"]/a/text()")
        value_colum = value_colum[0] if value_colum else ''
        dict_data[name_colum] = value_colum
        # print ('value>', value)
    list_data.append(dict_data)

print ('DATA >', json.dumps(list_data))