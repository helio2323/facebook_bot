from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

#funcao para realizar login no facebook (necessario 2 fatores talvez)
#Loop para verificar se é necessário fazer algum post
#funcao para adicionar grupos do facebook no supabase
#funcao para procurar novos grupos  no facebook
#funcao para postar anuncios nos grupos do facebook

