import time

i=0
z=1 
kalanlar=[]
while i<z:#Döngümüz
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
print("Bir Sonraki Teknokent Ringinin \nBilkent Metrodan Kalkışına ",kalansaat,"Saat",",",kalandakika,"dakika kalmıştır")
		
