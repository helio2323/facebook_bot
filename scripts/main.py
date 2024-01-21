from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from api_call import supabase_read
from api_call import imputar_dados
from api_call import ler_postagens



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
        
def salvar_grupos():
    
    login = facebook_login("https://www.facebook.com/?locale=pt_BR")
    
    func_click(10, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/a/div[1]/div[2]')
    
    func_send_keys(10, '','Itapeva empregos' ,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/label/input', True)
    
    time.sleep(2)
    
    #elemen = navegador.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/label/input')
    #elemen.send_keys(Keys.ENTER)

    #func_click(10, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[9]/div/a/div[1]')

    xpath = '//*[contains(@class, "x1i10hfl") and contains(@class, "xjbqb8w") and contains(@class, "x6umtig") and contains(@class, "x1b1mbwd") and contains(@class, "xaqea5y") and contains(@class, "xav7gou") and contains(@class, "x9f619") and contains(@class, "x1ypdohk") and contains(@class, "xt0psk2") and contains(@class, "xe8uvvx") and contains(@class, "xdj266r") and contains(@class, "x11i5rnm") and contains(@class, "xat24cr") and contains(@class, "x1mh8g0r") and contains(@class, "xexx8yu") and contains(@class, "x4uap5") and contains(@class, "x18d9i69") and contains(@class, "xkhd6sd") and contains(@class, "x16tdsg8") and contains(@class, "x1hl2dhg") and contains(@class, "xggy1nq") and contains(@class, "x1a2a7pz") and contains(@class, "xt0b8zv") and contains(@class, "xzsf02u") and contains(@class, "x1s688f")]'
    xpath_image = '//*[contains(@class, "x193iq5w") and contains(@class, "xeuugli") and contains(@class, "x13faqbe") and contains(@class, "x1vvkbs") and contains(@class, "x1xmvt09") and contains(@class, "x1lliihq") and contains(@class, "x1s928wv") and contains(@class, "xhkezso") and contains(@class, "x1gmr53x") and contains(@class, "x1cpjm7i") and contains(@class, "x1fgarty") and contains(@class, "x1943h6x") and contains(@class, "xudqn12") and contains(@class, "x3x7a5m") and contains(@class, "x6prxxf") and contains(@class, "xvq8zen") and contains(@class, "xo1l8bm") and contains(@class, "xi81zsa") and contains(@class, "x1yc453h")]'
    xpath_participando = "//*[contains(@class, 'x193iq5w') and contains(@class, 'xeuugli') and contains(@class, 'x13faqbe') and contains(@class, 'x1vvkbs') and contains(@class, 'x1xmvt09') and contains(@class, 'x1lliihq') and contains(@class, 'x1s928wv') and contains(@class, 'xhkezso') and contains(@class, 'x1gmr53x') and contains(@class, 'x1cpjm7i') and contains(@class, 'x1fgarty') and contains(@class, 'x1943h6x') and contains(@class, 'xudqn12') and contains(@class, 'x3x7a5m') and contains(@class, 'x6prxxf') and contains(@class, 'xvq8zen') and contains(@class, 'x1s688f') and contains(@class, 'x1mvi0mv')]"
    
        
    elementos = navegador.find_elements(By.XPATH, xpath)
    elementos_xpath = navegador.find_elements(By.XPATH, xpath_image)
    elementos_participando = navegador.find_elements(By.XPATH, xpath_participando)
    
    print(len(elementos))
    
    grupos_ = ler_postagens("https://consium.com.br/version-test/api/1.1/obj/recruit-grupos")
    
        
    
    
    

grupos = listar_salvar_grupos()