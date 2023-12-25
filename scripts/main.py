from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from api_call import supabase_read

# Configurar as opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, options=chrome_options)
#navegador = webdriver.Chrome(options=chrome_options)

#variaveis
postar_grupos = False


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
    
    func_send_keys(10, 'email', email, '')
    func_send_keys(10, 'pass', senha, '')        
    
    #time.sleep(2)
    
    func_click(10, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
    
    time.sleep(2)
    
    usuario_logado = True
        
    return usuario_logado


def func_send_keys(espera, id, texto, xpath, Click_Enter=False):

    tempo_espera = espera
    
    try:
        if id != '':
            elemento = WebDriverWait(navegador, tempo_espera).until(
            EC.visibility_of_element_located((By.ID, id))
            )
            print('Elemento encontrado', elemento.text)
        elif xpath != '':
            elemento = WebDriverWait(navegador, tempo_espera).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
            )
            print('Elemento encontrado', elemento.text)        
    finally:
        if id != '':
            navegador.find_element(By.ID, id).send_keys(texto)
            if Click_Enter == True:
                elemento = navegador.find_element(By.ID, id)
                elemento.send_keys(Keys.ENTER)
            
        elif xpath != '':
            navegador.find_element(By.XPATH, xpath).send_keys(texto)
            if Click_Enter == True:
                elemento = navegador.find_element(By.XPATH, xpath)
                elemento.send_keys(Keys.ENTER)
            
        #APERTA ENTER CASO SEJA TRUE

            
    return


def func_click(espera, xpath):
    tempo_espera = espera
    
    try:
        elemento = WebDriverWait(navegador, tempo_espera).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        
        print('Elemento encontrado', elemento.text)
    
    finally:
        navegador.find_element(By.XPATH, xpath).click()
    return



programacao_posts = supabase_read('https://qlisjdanugwnechsmeaj.supabase.co/rest/v1/programacao_postagens?select=*',
                                      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsaXNqZGFudWd3bmVjaHNtZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyNTMyMTUsImV4cCI6MTk5NjgyOTIxNX0.8YR-DaH-nG4yQD-P6g1ioOWfkiJEAp1i4EOb3TIEclk",
                                      "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFsaXNqZGFudWd3bmVjaHNtZWFqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODEyNTMyMTUsImV4cCI6MTk5NjgyOTIxNX0.8YR-DaH-nG4yQD-P6g1ioOWfkiJEAp1i4EOb3TIEclk")

#login = facebook_login("https://www.facebook.com/?locale=pt_BR")


#aqui vai ser o While true para busca     
for item in programacao_posts:
    if item['status'] == 'programado':
        ...
        #faz a postagem nos grupos
        
def listar_salvar_grupos():
    
    login = facebook_login("https://www.facebook.com/?locale=pt_BR")
    
    func_click(10, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a/div[1]/div[2]')
    
    func_send_keys(10, '','Itapeva empregos' ,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/label/input', True)
    
    time.sleep(2)
    
    #elemen = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/label/input')
    #elemen.send_keys(Keys.ENTER)

    time.sleep(5)
    
    #func_click(10, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[9]/div/a/div[1]')

    
    time.sleep(10)
    
    return

grupos = listar_salvar_grupos()