import time
import telepot
from telepot.loop import MessageLoop
import random
import logging
import sys
import urllib.request

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
            bot.sendMessage(chat_id,'Hoşgeldiniz '+ whois + '\n Robotu kullanmak için aşağıdaki komutları kullanabilirsiniz \n/senkimsin\n/dogancanozcankim\n/salla\n/selam\n/?')
        if command == 'otopark':
                otopark=urllib.request.urlopen("http://91.92.136.227/counter/get")
                bot.sendMessage(chat_id, 'Merkez otopark boş yer sayısı: ' + (otopark.read().decode("UTF-8")))
        if command == '/senkimsin':
            bot.sendMessage(chat_id,'Benim adım konksoft_bot ben belirli komutlara programlanmış çıktılar veren bir robotum')
        if command == '/dogancanozcankim':
            bot.sendMessage(chat_id,'Doğancan Özcan Benim Yaratıcımdır,Beni o programladı ve ben ona hizmet etmek için varım')
        if command == '/salla':
            bot.sendMessage(chat_id,random.randint(1,100))
        if command == '/selam':
                bot.sendMessage(chat_id,'Selam '+whois+' '+whoissurname)
        if command == '/?':
                bot.sendMessage(chat_id, '\n Robotu kullanmak için aşağıdaki komutları kullanabilirsiniz \n/senkimsin\notopark\n/dogancanozcankim\n/salla\n/selam\n/?\n')
        if command == '/ring':
		i==int(0)	
		z==int(1)
		kalanlar=[]
                while i < z:#Döngümüz
                        dakikalar=(425,445,455,465,475,500,510,515,525,530,550,570,600,660,720,780,840,900,960,1020,1065,1080,1095,1110,1125,1155,1170)#Servis Saatlerinin dakika olarak tutan liste.
                        z=len(dakikalar)#while döngüsü için z değişkenini while döngüsü içerisindeki dakikalar listesinin sayısına eşitleyen değişken
                        saat = time.localtime(time.time())#Şuanki Time verisini tutan değişken.
                        g=(saat.tm_hour,saat.tm_min)#Şuanki saati ve dakikayı tutan değişken.
                        fark=(((23-saat.tm_hour)*60)+(59-saat.tm_min))# 23:59 a kadar olan dakika değerimizi bu değişkende tutuyoruz.
                        kalansaat=((dakikalar[i]+fark)//60)
                        kalandakika=((dakikalar[i]+fark)-(kalansaat*60))
                        if kalansaat > 23:
                                kalansaat=kalansaat-24
                        kalan=(kalandakika+(kalansaat*60))
                        kalanlar.insert(i,kalan)
                        i=i+1
                kalanim=(min(kalanlar))
                kalansaat=(kalanim//60)
                kalandakika=kalanim-(kalansaat*60)
                bot.sendMessage(chat_id,"Bir Sonraki Teknokent Ringinin \nBilkent Metrodan Kalkışına ",kalansaat,"Saat",",",kalandakika,"dakika kalmıştır")


MessageLoop(bot, handle).run_as_thread()
print ('Grup Dinleniyor')

while 1:
        time.sleep(10)