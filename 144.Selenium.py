# Automatização de tarefas
from selenium import webdriver
from time import sleep
from pathlib import Path

ROOT_FOLDER = Path(__file__)


class ChomeAuto:
    def __init__(self):
        self.driver_path = '/Users/es19237/Desktop/Python/Pycharm/CursoPython3/Seção5_Modulos-Pyhton/chromedriver'
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(self.driver_path, options=self.options)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except:
            pass

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password = self.chrome.find_element_by_id('password')
            btn_login = self.chrome.find_element_by_name('commit')
            input_login.send_keys('email@gmail.com')
            input_password.send_keys('aaaaa')
            btn_login.click()
        except Exception as e:
            pass


if __name__ == '__main__':
    chome = ChomeAuto()
    chome.acessa('https://github.com/')
    chome.clica_sign_in()
    chome.faz_login()
    sleep(3)
    chome.sair()
