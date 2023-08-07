'''
python'da Dize Manipülasyonlari ve Formatlama	
çok çeşitli yöntemlerle gerçekleştirilebilir.
işte bazi temel dize manipülasyonlari ve formatlama yöntemleri.
'''


'''
1.)Dize Birleştirme
iki veya daha fazla dizeyi birleştirmek için
+ operatörünü kullanabilirsiniz
'''
kelime1="Merhaba"
kelime2="Python"
birlesik_cumle=kelime1 + " " + kelime2
print(birlesik_cumle)


'''
2.)Dize Uzunluğu
Bir dizenin uzunluğunu len()
fonksiyonu ile bulabilirsiniz.
'''
dize1="Egitim"
uzunluk=len(dize1)
print(uzunluk)


'''
3.)Dize Dilimleme
Dize içindeki belli bir araligi almak için
dilimleme işlemlerini kullanabilirsiniz.
'''
dize = "Selamlar, Python Ogrencileri"
alt_dize=dize[0:16] #Selamlar, Python


'''
4.)Dize Formatlama
Dizeleri belirli bir düzen içinde biçimlendirmek
için format() veya f-stringler kullanabilirsiniz.
'''
isim = "Ahmet"
yas = 30
formatli_dize = "Benim adim {}, ve {} yaşindayim.".format(isim, yas)
print(formatli_dize)  # "Benim adim Ahmet, ve 30 yaşindayim."

# veya f-string kullanarak:
formatli_dize = f"Benim adim {isim}, ve {yas} yaşindayim."


'''
5.)Dize Metodlari
Python'da birçok dize metodu bulunmaktadir.
'''
dize = "Merhaba Dünya"
buyuk_harfler = dize.upper()  # "MERHABA DÜNYA"
kucuk_harfler = dize.lower()  # "merhaba dünya"
kelime_listesi = dize.split()  # ['Merhaba', 'Dünya']


'''
6.)Dize Biçimlendirme (f-strings)
Python 3.6 ve sonraki sürümlerde,
f-stringler kullanarak dize biçimlendirmesi yapabilirsiniz.
'''
isim = "Ayşe"
yas = 25
formatli_dize = f"Benim adim {isim}, ve {yas} yaşindayim."


'''
7.)Dize Düzeltme
Boşluklari baştan veya sondan kaldirmak için
strip() metodunu kullanabilirsiniz.
'''
dize_duzeltme= "   Örnek Dize   "
duzeltilmis_dize = dize_duzeltme.strip()  # "Örnek Dize"


'''
8.)Dize Değiştirme
Belirli bir alt dizeyi başka bir dizeyle değiştirmek için replace()
metodunu kullanabilirsiniz.
'''
dize_degistirme= "Merhaba Dünya"
yeni_dize = dize_degistirme.replace("Merhaba", "Selam")  # "Selam Dünya"


'''
9.)Dize Kontrolü:
Dize içinde belli bir alt dizenin varliğini
kontrol etmek için in anahtar kelimesini kullanabilirsiniz:
'''
dize_kontrol = "Merhaba Dünya"
if "Merhaba" in dize_kontrol:
    print("Merhaba bulundu.")