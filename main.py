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

MessageLoop(bot, handle).run_as_thread()
print ('Grup Dinleniyor')

while 1:
    	time.sleep(10)
