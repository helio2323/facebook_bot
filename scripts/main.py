from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


import requests
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

#funcao para realizar login no facebook (necessario 2 fatores talvez)
#Loop para verificar se é necessário fazer algum post
#funcao para adicionar grupos do facebook no supabase
#funcao para procurar novos grupos  no facebook
#funcao para postar anuncios nos grupos do facebook

navegador.maximize_window()

def facebook_login(url_face):
    
    #url_face = "https://www.facebook.com/?locale=pt_BR"
    
    navegador.get(url_face)
    
    dados_login = supabase_read("https://qlisjdanugwnechsmeaj.supabase.co/rest/v1/usuario?select=*",
                            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsaXNqZGFudWd3bmVjaHNtZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyNTMyMTUsImV4cCI6MTk5NjgyOTIxNX0.8YR-DaH-nG4yQD-P6g1ioOWfkiJEAp1i4EOb3TIEclk",
                            "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsaXNqZGFudWd3bmVjaHNtZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyNTMyMTUsImV4cCI6MTk5NjgyOTIxNX0.8YR-DaH-nG4yQD-P6g1ioOWfkiJEAp1i4EOb3TIEclk")

    if dados_login:
        for itens in dados_login:
            email = itens['email']
            senha = itens['senha']
            
    navegador.find_element('id', 'email').send_keys(email)
    navegador.find_element('id', 'pass').send_keys(senha)

    time.sleep(3)
    
    btn_entrar = navegador.find_element('id', 'u_0_5_vB')
    btn_entrar.click() 
        
    time.sleep(10)

    
        
    return

def supabase_read(url, api, auth):
    
    url = url
    payload = {}

    headers = {
    'apikey': api,
    'Authorization': auth
}
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response.json()


login = facebook_login("https://www.facebook.com/?locale=pt_BR")


        
