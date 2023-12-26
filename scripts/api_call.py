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


def imputar_dados():
    url = 'https://qlisjdanugwnechsmeaj.supabase.co/rest/v1/grupos_facebook'
    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsaXNqZGFudWd3bmVjaHNtZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyNTMyMTUsImV4cCI6MTk5NjgyOTIxNX0.8YR-DaH-nG4yQD-P6g1ioOWfkiJEAp1i4EOb3TIEclk',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsaXNqZGFudWd3bmVjaHNtZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyNTMyMTUsImV4cCI6MTk5NjgyOTIxNX0.8YR-DaH-nG4yQD-P6g1ioOWfkiJEAp1i4EOb3TIEclk',
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
    }
    data = {
        'link_grupo': 'someValue',
        'infos_1': 'otherValue'
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.status_code)
    print(response.json())  # Se quiser ver a resposta do servidor

