# abra o terminal e execute o codigo pip install nome_biblioteca

import requests

url = 'https://www.exemplo.com'
response = requests.get(url)

print(f'A Solicitação HTTP para url {url} retornou o status {response.status_code}')
