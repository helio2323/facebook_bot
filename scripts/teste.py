import requests

url = "https://consium.com.br/version-test/api/1.1/wf/salvargrupo"
dados = {"grupo": "testenumero2"}

# Faz a requisição POST
resposta = requests.post(url, data=dados)

# Verifica o código de status da resposta
if resposta.status_code == 200:
    print("Requisição bem-sucedida!")
    print("Resposta:", resposta.text)
else:
    print(f"A requisição falhou com o código de status {resposta.status_code}")
    print("Resposta:", resposta.text)

