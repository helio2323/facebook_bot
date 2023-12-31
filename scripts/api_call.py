import requests

def supabase_read(url, api, auth):
    
    url = url
    payload = {}

    headers = {
    'apikey': api,
    'Authorization': auth
}
    response = requests.request("GET", url, headers=headers, data=payload)
        
    return response.json()


def imputar_dados(nome_grupo, link_grupo, infos_1, participando):
    url = 'https://qlisjdanugwnechsmeaj.supabase.co/rest/v1/grupos_facebook'
    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsaXNqZGFudWd3bmVjaHNtZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyNTMyMTUsImV4cCI6MTk5NjgyOTIxNX0.8YR-DaH-nG4yQD-P6g1ioOWfkiJEAp1i4EOb3TIEclk',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsaXNqZGFudWd3bmVjaHNtZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyNTMyMTUsImV4cCI6MTk5NjgyOTIxNX0.8YR-DaH-nG4yQD-P6g1ioOWfkiJEAp1i4EOb3TIEclk',
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
    }
    data = {
        'nome_grupo': nome_grupo,
        'link_grupo': link_grupo,
        'infos_1': infos_1,
        'particip': participando
    }

    try:
        with requests.post(url, headers=headers, json=data) as response:
            print(response.status_code)
            if response.status_code == 201:  # Considera o status 201 como sucesso na criação
                if response.text:  # Verifica se há conteúdo na resposta
                    try:
                        print(response.json())  # Tenta imprimir o JSON se estiver presente
                    except ValueError as e:
                        print("Erro ao decodificar JSON:", e)
                else:
                    print("Resposta vazia")
            else:
                print("Falha ao enviar dados. Código de status:", response.status_code)
    except requests.RequestException as e:
        print("Erro de requisição:", e)
   