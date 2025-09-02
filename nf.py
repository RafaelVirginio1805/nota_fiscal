import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lê a planilha com os números das NFs
df = pd.read_excel("")  
nfs = df["NF"].dropna().astype(str).tolist()  

driver = webdriver.Edge()
wait = WebDriverWait(driver, 15)
driver.get("https://nfse.recife.pe.gov.br/contribuinte/consultas.aspx")

#loop
for nf in nfs:
    #aguarda o input para colar
    input_nf = wait.until(EC.presence_of_element_located((By.NAME, "ctl00$cphCabMenu$tbNumeroEmitida")))
    input_nf.clear()
    input_nf.send_keys(nf)


    #clica em visualizar
    visualizar_botao = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "button150")))
    visualizar_botao.click()

    # clica em gerar
    gerar_pdf = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btnNFSeGerarPdf")))
    gerar_pdf.click()

    #clica em voltar
    voltar_botao = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btnNFSeVoltar")))
    voltar_botao.click()

    time.sleep(2)  

driver.quit()
