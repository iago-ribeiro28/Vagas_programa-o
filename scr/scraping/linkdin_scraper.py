""" é possivel dar um scraping do linkedin usando a URL 

https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?
keywords=""&location=Brasil&f_WT=2&geoId=106057199&position=1&start=0

f_WT=2
significar que é uma vaga remota

Start é a página, então essa é a pagina 0.
"""
import logging
import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
from datetime import datetime


class Scraping():
    def __init__(self):
        # Dando inicio na classe que vai ser responsável por fazer o Scraping do linkedin
        # Chama a função _setup_logging que vai ser usado para deixar registrado os scraps feitos
        self.response = requests.session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'}

        self._setup_logging()
        
    def _setup_logging(self):
        # configura a mensagem que vai ser passadas nos logs
        data = datetime.now().strftime("%d-%m-%Y")
        nome_log = f"Scrap - {data}"
        
        log_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'log')
        os.makedirs(log_dir, exist_ok=True)

        # Caminho completo para o arquivo de log
        log_file = os.path.join(log_dir, f"{nome_log}.log")

        logging.basicConfig(
            level=logging.DEBUG, 
            filename=log_file, 
            filemode='w',
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        
        self.logger = logging.getLogger(self.__class__.__name__)
    
    
    
    def buscando_vagas(self):
        self.url = f'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=""&location=Brasil&f_WT=2&geoId=106057199&position=1&start=0'
        self.response = requests.get(self.url, headers= self.headers)
        self.page_html = self.response.text
        self.soup = BeautifulSoup(self.page_html, features='html.parser')
        self.logger.info(self.soup)
        
    def teste(self):
        self.logger.info('Teste executado com sucesso!')
        
        
        
teste = Scraping()
teste.buscando_vagas()
teste.teste()

