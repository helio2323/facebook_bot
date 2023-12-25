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
