import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '5255695583:AAGLT4xCXy7MZdLkGWAlRyIC6kwcRk0CBuQ'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'''Olá bem vindo ao meu curriculo! Oque gostaria de ver primeiro? 1 - Dados pessoais.{os.linesep}2 - Objeitvos{os.linesep}3 - Experiencias profissionais{os.linesep}4 - Formação academica{os.linesep}5 - Qualificações e atividades complementares{os.linesep}6 - Informações adicionais{os.linesep}7 - Negocios
		'''
        if mensagem == '1':
            return f'''Rua quitandinha N°161 | Carapicuiba-SP, 06365080 | Cel: 11983879195{os.linesep} Gmails: fcaio127@gmail.con- fcaio127@uni9.edu.br-codex@dnmx.org{os.linesep}Para retornar ao menu digite "menu" ou "Menu"
            '''
        elif mensagem == '2':
            return f'''Busco uma oportunidade nova de emprego nas areas de tecnologia ou areas correlatas. posso atuar como Estagiario, junior ou trainee.{os.linesep}Para retornar ao menu digite "menu" ou "Menu"
            '''
        elif mensagem == '3':
      	    return f'''Jamef encomendas urgentes | Ajudante de carga | 19/03/2019 ate agora{os.linesep} para retornar digite "menu" ou "Menu"
	        '''
	elif mensagem == '4':
            return f'''Uninove | Tecnologia em analise e desenvolvimento de sistemas (cursando 4° semestre){os.linesep} Centro senai de tecnologia educacionais | competencia transversal - Tecnologia da informação e computação | E.E Toufic joulian - ensino medio completo{os.linesep} para retornar digite "menu" ou "mneu".
            '''
        elif mensagem == '5':
            return f'''Ingles | nivel basico Espanhol | Nivel basico | Intesivo de python - lira hashtag | Chat bot - Telegram e Whatsapp | Automações para redes socias - Instagram | Sistemas operacionais | Kali, Unbuntu, Windows 7,8.1 e 10 | Dropzone - site para venda de serviços | A arte de vestir - Site baseado em um livro. 
            '''
        elif mensagem == '6':
            return f'''Disponibilidade para trabalhar em qualquer horario, CNH B e disponibilidade para viajar pela empresa.{os.linesep} Para retornar digite "menu" ou "Menu".
	        '''
        elif mensagem == '7':
            return f'''Gostaria de Enviar uma Proposta de negocio? Se a resposta for sim Digite "s" ou "sim" caso seja não digite "n" ou "não"
            '''

        elif mensagem.lower() in ('s', 'sim'):
            return ''' Obrigado por escolher esta opção. Estamos quase la, Para entrar em contato Digite "1". '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Desculpe por não atender suas necessidades agora, espero ver você aqui em breve para um futuro negocio. Tenha um Bom dia, tarde e noite! :) '''
        else:
            return 'Gostaria de acessar o menu? Digite "menu"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()
