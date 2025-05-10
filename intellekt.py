#Sprint_3a_task
def kod1():
#1) x dəyişəni verilmişdir. Əgər x > 0 olarsa "müsbət", x < 0 olarsa "mənfi", bərabərdirsə "sıfır" çap etsin.
 x = int(input('x deyerini daxil edin: '))
if x > 0:
        print('müsbet')
elif x < 0:
    print('mənfi')
else:
    print('sıfır')
   
kod1()

def kod2():
 #2) n rəqəmi cütdürsə "cüt", təkdirsə "tək" çap etsin.
 n = int(input('n dəyərini daxil edin: '))
if n % 2 == 0:
         print('cüt')
else:
    print('tək')

def kod3():
#3) a, b, c rəqəmləri verilmişdir. Ən böyük rəqəmi çap etsin.
 a = int(input('a rəqəmini daxil edin: '))
b = int(input('b rəqəmini daxil edin: '))
c = int(input('c rəqəmini daxil edin: '))

if a >= b and a >= c:

    print('Ən böyük rəqəm:', a)
elif b >= a and b >= c:
    print('Ən böyük rəqəm:', b)
else:
    print('Ən böyük rəqəm:', c)

def kod4():
#4) day dəyişəni 1-7 arası rəqəmdir. Müvafiq həftə gününü (1 = "Bazar ertəsi", ..., 7 = "Bazar") çap etsin, əks halda "Yanlış gün" yazsın.
 day = int(input("Günün nömrəsini daxil et (1-7): "))
if  day == 1:
  print("Bazar ertəsi")
elif day == 2:
    print("Çərşənbə axşamı")
elif day == 3:
  print("Çərşənbə")
elif day == 4:
    print("Cümə axşamı")
elif day == 5:
    print("Cümə")
elif day == 6:
 print("Şənbə")
elif day == 7:
    print("Bazar")
else:
    print("Yanlış gün")

def kod5():
#5) temp dəyişəni temperaturdur. Əgər temp < 0 olarsa "soyuq", 0-20 arası olarsa "normal", 20-dən böyükdürsə "isti" çap etsin.
 temp = int(input('Temperaturu daxil edin: '))
if temp < 0:
        print('soyuq')
elif 0 <= temp <= 20:
        print('normal')
else:
         print('isti')

def kod6():
#6) password adlı string verilmişdir. Əgər uzunluğu 8-dən kiçikdirsə "qısa", 8-12 arasıdırsa "orta", 12-dən böyükdürsə "uzun" çap etsin.
 password = input('Şifrəni daxil edin: ')
if len(password) < 8:
         print('qısa')
elif len(password) <= 12:
    print('orta')
else:
    print('uzun')

def kod7():
#7) x rəqəmi həm 3-ə, həm də 5-ə bölünürsə "3 və 5", yalnız 3-ə bölünürsə "3", yalnız 5-ə bölünürsə "5", heç birinə bölünmürsə "heç biri" çap etsin.
 x = int(input("x dəyərini daxil edin: "))
if x % 3 == 0 and x % 5 == 0:
         print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

def kod8():
#8) 0-dan 20-yə qədər cüt rəqəmləri çap etsin.	
 for i in range(0, 21):
     if i % 2 == 0:
          print(i)

def kod9():
#9) "Bağda ərik var idi …" stringinin hər elementini for ilə ayrı-ayrılıqda çap edin.
 text = "Bağda ərik var idi …"
for char in text:
         print(char)

def kod10():
#10) 1-dən 10-a qədər rəqəmləri çap edin, amma 3 xaric.
 for i in range(1, 11):
    if i == 3:
        continue
    print(i)

def kod11():
#11) 1-dən başlayaraq ilk 5-ə bölünən rəqəmi tapın və while ilə çap edin (break istifadə edin).
 a = 1
while True:
         if a % 5 == 0:
                      print(a)
                      break
         a += 1

def kod12():
#12) (1, 3, 5, 7, 9) listində/vectorunda 5-i tapın və indeksini çap edin (break istifadə edin).
 numbers = [1, 3, 5, 7, 9]
for i in range(len(numbers)):
         if numbers[i] == 5:
                      print(f"5-in indeksi: {i}")
                      break

#Sprint_3b_task
def kod13():
#1) salam adlı funksiya yaradın ki, heç bir arqument almadan sadəcə "Salam, Dünya!" çap etsin.
 def salam():
          print('Salam, Dünya!')
          salam()

def kod14():
#2) kub_hesabla adlı funksiya yaradın ki, bir rəqəm (n) qəbul etsin və onun kubunu qaytarsın.
 def kub_hesabla(n):
          return n ** 3
kub_hesabla(3)

def kod15():
#3) birlesdir adlı funksiya yaradın ki, iki söz qəbul etsin və onları boşluqla birləşdirib qaytarsın.
 def birlesdir(a, b):
          return a + ' ' + b

def kod16():
#4) cap_et adlı funksiya yaradın ki, bir listi arqument olaraq alsın və listin hər elementini for ilə çap etsin.
 def cap_et(l):
      def cap_et(l):
                    print(i)
                    cap_et('jhhuxdsb')


def kod17():
#5) toplam adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların cəmini qaytarsın.
 def toplam(*args):
          return sum(args)
toplam(1,2,3,4,5,6)


def kod18():
#6) ortalama adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların ortalamasını qaytarsın (əgər heç bir rəqəm yoxdursa, "Rəqəm yoxdur" qaytarsın).
 def ortalama(*args):
          if not args:
                        return 'Rəqəm yoxdur'
                        return sum(args) / len(args)
ortalama(1,2,3,4,5,6)


def kod19():
#7) adlar_rəqəmlər adlı funksiya yaradın ki, istənilən sayda ad və rəqəm cütünü (**kwargs) qəbul edib hər cütü çap etsin (məsələn, "ad: bir, rəqəm: 1").
 def adlar_rəqəmlər(**kwargs):
           for ad, rəqəm in kwargs.items():
                          print(f'ad: {ad}, rəqəm: {rəqəm}')
                  

def kod20():
#8) tip_yoxla adlı funksiya yaradın ki, bir dəyər qəbul edib onun tipini yoxlasın: "mətn", "rəqəm", "başqa" çap etsin.
 def tip_yoxla(dəyər):
           if isinstance(dəyər, str):
                          print('mətn')
           elif isinstance(dəyər, (int, float)):
                        print('rəqəm')
           else:
                          print('başqa')


def kod21():
#9) yas_kateqoriya adlı funksiya yaradın ki, input()/readline() ilə yaş soruşsun, 18-dən aşağıysa "Gənc", yuxarıdrsa "Yetkin" çap etsin.
 def yas_kateqoriya():
           yas = int(input('Yaşınızı daxil edin: '))
if yas < 18:
               print('Gənc')
else:
                print('Yetkin')
                yas_kateqoriya()


def kod22():
#10) soz_uzunluq adlı funksiya yaradın ki, input()/readline() ilə istifadəçidən söz alsın və onun uzunluğunu çap etsin.
 def soz_uzunluq():
            soz = input('Söz daxil edin: ')
print(len(soz))
soz_uzunluq()
            
#Sprint_4a_task
def kod23():
#1) İstifadəçidən iki rəqəm və bir əməliyyat (toplama, çıxma, vurma, bölmə) daxil etməsini tələb edən funksiya yazın. Mümkün xətaları (ValueError, TypeError və s.) idarə edin və müvafiq mesajlar çıxarın. Sonda da "Hesablama bitdi" mesajı çap olunsun.
# Sonda da "Hesablama bitdi" mesajı çap olunsun.
 def hesabla():
       try:
             a = float(input('Birinci ədədi daxil edin: '))
             b = float(input('İkinci ədədi daxil edin: '))
             əməl = input('Əməliyyat seçin (+, -, *, /): ')
             if əməl == '+':
               print(a + b)
             elif əməl == '-':
                      print(a - b)
             elif əməl == '*':
                   print(a * b)
             elif əməl == '/':
                   print(a / b)
             else:
                              print('Yanlış əməliyyat!')
       except (ValueError, TypeError, ZeroDivisionError) as e:
               print('Xəta baş verdi:', e)
       finally:
              print('Hesablama bitdi')


#2) 1-dən 50-yə qədər olan rəqəmlərdən yalnız 11ə qalıqsız bölünənlərini list olaraq qaytarın.
 result = []
for i in range(1, 51):
            if i % 11 == 0:
                            result.append(i)
                            print(result)

def kod25():
#3) Verilmiş sözlər siyahısından (["kitab", "qələm", "defter", "silgi"]) hər sözün ilk hərfini list olaraq qaytarın.
 sozler = ["kitab", "qələm", "defter", "silgi"]
ilk= []
for soz in sozler:
            ilk.append(soz[0])
            print(ilk)


def kod26():
#4) Şəhər adları (["Bakı", "Gəncə", "Sumqayıt"]) və kodları ([12, 22, 18]) siyahılarından {şəhər: kod} dictionary olaraq qaytarın.
 seherler = ["Bakı", "Gəncə", "Sumqayıt"]
kodlar = [12, 22, 18]
seher_kod_dict = {}
for i in range(len(seherler)):
                 seher_kod_dict[seherler[i]] = kodlar[i]
                 print(seher_kod_dict)

def kod27():
#5) Kilometri milə çevirən (mil = km * 0.621371) lambda funksiyası yazın və 5 fərqli dəyər üçün yoxlayın.
 km_to_mil = lambda km: km * 0.621371
deyerler = [1, 5, 10, 20, 50]
mil_deyerler = []
for km in deyerler:
            mil_deyerler.append(km_to_mil(km))
            print(mil_deyerler)

def kod28():
#6) [100, 200, 300, 400] qiymətlərinə 18% vergi əlavə etmək üçün map() və lambda istifadə edin. 
 qiymetler = [100, 200, 300, 400]
vergi_elaveli = list(map(lambda x: x * 1.18, qiymetler))
print(vergi_elaveli)          

def kod29():
#7) [3, 7, 12] və [2, 4, 6] siyahılarının elementlərini ikiqat artırmaq və sonra cəmləmək üçün map() istifadə edin.
 a = [3, 7, 12]
b = [2, 4, 6]
cem = list(map(lambda x, y: (x * 2) + (y * 2), a, b))
print(cem)

def kod30():
#8) [150, 80, 220, 45] siyahısından ən kiçik qiyməti reduce() ilə tapın.
  from functools import reduce
qiymetler = [150, 80, 220, 45]
en_kicik = reduce(lambda x, y: x if x < y else y, qiymetler)
print(en_kicik)
        
