import requests
import time
import json

class TelegramBot:
    def __init__(self):
        token = '5255695583:AAGLT4xCXy7MZdLkGWAlRyIC6kwcRk0CBuQ'
        url_base = f'api.telegram.org/bot{token}/'
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
                    resposta = self.criar_resposta()
                    self.responder(resposta,chat_id)
    #receber mensagens
    def obter_mensagens(self,update_id):
        link_requisicao = f'{self.url_base}/getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
    #criar respostas
    def criar_resposta(self):
        return 'Ola! Seja bem vindo ao Horoscupbot, seu novo jeito de ler seu Horoscup.'
    #responder
    def responder(self,resposta,chat_id):
        #enviar
        link_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_envio)

bot = TelegramBot()
bot.Iniciar()