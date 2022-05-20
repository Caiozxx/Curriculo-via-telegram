import requests
import time
import json
import os

class TelegramBot:
    def __init__(self):
        token = '5255695583:AAGLT4xCXy7MZdLkGWAlRyIC6kwcRk0CBuQ'
        self.url_base = f'https://api.telegram.org/bot{token}/'
    #inciar o bot
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            mensagens = atualizacao ['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    eh_primeira_mensagem = mensagem['message']['message_id'] == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta,chat_id)
    #receber mensagens
    def obter_mensagens(self,update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
    #criar respostas
    def criar_resposta(self,mensagem,eh_primeira_mensagem):
        if eh_primeira_mensagem == True:
            return f'''Ola bem vindo ao nosso HoroscupBot
        {os.linesep}'''
    #responder
    def responder(self,resposta,chat_id):
        #enviar
        link_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_envio)

bot = TelegramBot()
bot.Iniciar()