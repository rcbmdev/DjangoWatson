from subprocess import call
from gtts import gTTS
import speech_recognition as sr
from bs4 import BeautifulSoup
import webbrowser as browser
import json
from requests import get

hotword = 'rosa'
IBM_USERNAME = "165da149-f20b-4756-b580-9f5b67b63465"
IBM_PASSWORD = "10Y40zS2RbNu"

def monitora_audio_ibm():
    while True:
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            print("Aguardando o comando")
            audio = microfone.listen(source)
        try:
            trigger = microfone.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, language='pt-BR')
            trigger = trigger.lower()
            print(trigger)

            if hotword in trigger:
                print('Comando: ', trigger)
                responde('feedback')
                executa_comandos(trigger)
                break
                # executar demais comandos
        except sr.UnknownValueError:
            print("IBM Speech to Text could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from IBM Speech to Text service; {0}".format(e))
    return trigger

def responde(arquivo):
    call(['aplay','audios/' + arquivo +'.mp3']) #Linux

def executa_comandos(trigger):
    if 'notícias' in trigger:
        ultimas_noticias()
    else:
        mensagem = trigger.strip(hotword)
        cria_audio(mensagem)
        print('Comando Inválido: ', mensagem)
        responde('comando_invalido')

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save('audios/mensagem.mp3')
    call(['aplay','audios/mensagem.mp3'])
    #os.remove('audios/noticias.mp3')

def ultimas_noticias():
    dados_json = []
    site = get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:2]:
        #noticias = dict(titulo = item.title.text,
        #                link = item.link.text)
        mensagem = item.title.text
        cria_audio(mensagem)

def main():
    monitora_audio_ibm()

#main()
ultimas_noticias()