import time
import telepot
from telepot.loop import MessageLoop
import random
import logging
import sys
import urllib.request
from bs4 import BeautifulSoup
import requests

TOKEN=sys.argv[1]
bot=telepot.Bot(TOKEN)
logging.basicConfig(filename='konksoft.log',level=logging.DEBUG)
def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	whois = msg['from']['first_name']
	whoissurname = msg['from']['last_name']
	date = msg['date']
	print (chat_id,whois,whoissurname,time.ctime()+'\nGirilen Komut: %s' % command)
	if command == '/start':
            bot.sendMessage(chat_id,'Hoşgeldiniz '+ whois + '\n Robotu kullanmak için aşağıdaki komutları kullanabilirsiniz \n/senkimsin\n/dogancanozcankim\n/otopark\n/ring\n/altingram\n/altinceyrek\n/salla\n/selam\n/?')
	if command == '/otopark':
                otopark=urllib.request.urlopen("http://91.92.136.227/counter/get")
                bot.sendMessage(chat_id, 'Merkez otopark boş yer sayısı: ' + (otopark.read().decode("UTF-8")))
	if command == '/senkimsin':
            bot.sendMessage(chat_id,'Benim adım konksoft_bot ben belirli komutlara programlanmış çıktılar veren bir robotum')
	if command == '/altingram':
		deger = BeautifulSoup(requests.get('http://bigpara.hurriyet.com.tr/altin/').content, 'html.parser').find_all('span',{'class':'value'})
		bot.sendMessage(chat_id,'Gram Altının Anlık Alış Değeri '+str(deger)[56:62]+ ' Satış Değeri ' + str(deger)[91:97]+' dir')
	if command == '/altinceyrek':
		deger = BeautifulSoup(requests.get('http://bigpara.hurriyet.com.tr/altin/').content, 'html.parser').find_all('span',{'class':'value'})
		bot.sendMessage(chat_id, ' Çeyrek Altının Anlık Alış Değeri '+str(deger)[162:168]+ ' Satış Değeri '+ str(deger)[197:203])
	if command == '/dogancanozcankim':
            bot.sendMessage(chat_id,'Doğancan Özcan Benim Yaratıcımdır,Beni o programladı ve ben ona hizmet etmek için varım')
	if command == '/salla':
            bot.sendMessage(chat_id,random.randint(1,100))
	if command == '/selam':
                bot.sendMessage(chat_id,'Selam '+whois+' '+whoissurname)
	if command == '/?':
                bot.sendMessage(chat_id, '\n Robotu kullanmak için aşağıdaki komutları kullanabilirsiniz \n/senkimsin\n/dogancanozcankim\n/otopark\n/ring\n/altingram\n/altinceyrek\n/salla\n/selam\n/?\n')
	if command == '/ring':
		iss= 0
		zss = 1
		kalanlar=[]
		kalanim=0
		kalansaat=0
		kalandakika=0
		kalan=0
		while iss < zss:#Döngümüz
                        dakikalar=(425,445,455,465,475,500,510,515,525,530,550,570,600,660,720,780,840,900,960,1020,1065,1080,1095,1110,1125,1155,1170)#Servis Saatlerinin dakika olarak tutan liste.
                        zss=len(dakikalar)#while döngüsü için z değişkenini while döngüsü içerisindeki dakikalar listesinin sayısına eşitleyen değişken
                        saat = time.localtime(time.time())#Şuanki Time verisini tutan değişken.
                        g=(saat.tm_hour,saat.tm_min)#Şuanki saati ve dakikayı tutan değişken.
                        fark=(((23-saat.tm_hour)*60)+(59-saat.tm_min))# 23:59 a kadar olan dakika değerimizi bu değişkende tutuyoruz.
                        kalansaat=((dakikalar[iss]+fark)//60)
                        kalandakika=((dakikalar[iss]+fark)-(kalansaat*60))
                        if kalansaat > 23:
                                kalansaat=kalansaat-24
                       	kalan=(kalandakika+(kalansaat*60))
                        kalanlar.insert(iss,kalan)
                        iss=iss+1
		kalanim=(min(kalanlar))
		kalansaat=(kalanim//60)
		kalandakika=kalanim-(kalansaat*60)
		bot.sendMessage(chat_id,'Bir Sonraki Ringin Bilkent Metrodan Kalkışına '+str(kalansaat)+' saat '+str(kalandakika)+' dakika kalmıştır')
MessageLoop(bot, handle).run_as_thread()
print ('Grup Dinleniyor')

while 1:
        time.sleep(10)
