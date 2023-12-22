from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    
    func_send_keys(10, 'email', email)
    func_send_keys(10, 'pass', senha)        
    
    #time.sleep(2)
    
    
    navegador.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
        
    time.sleep(5)

    navegador.find_element('xpath', '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[4]/div/a').click()
    
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



def func_send_keys(espera, id, texto):

    tempo_espera = espera
    
    try:     
        elemento = WebDriverWait(navegador, tempo_espera).until(
            EC.visibility_of_element_located((By.ID, id))
            )
            
        print('Elemento encontrado', elemento.text)
        
    finally:
        navegador.find_element(By.ID, id).send_keys(texto)
        print('----')
    
    return

login = facebook_login("https://www.facebook.com/?locale=pt_BR")
