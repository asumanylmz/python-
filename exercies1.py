"""-------7'ye bölünebilen ancak 5'in katı olmayan tüm bu sayıları bulacak, 2000 ile 3200 arasında
(her ikisi de dahil) bir program yazınız. Elde edilen numaralar tek bir satıra virgülle ayrılmış bir sıra ile basılmalıdır.
"""


"""for i in range(2000,3200):
    if (i%7==0 and i%5!=0) :
        print (i,end=",")"""

"""------------Verilen sayıların faktöriyelini hesaplayabilen bir program yazın.Sonuçlar tek bir satıra virgülle ayrılmış
sırayla yazdırılmalıdır.Programa aşağıdaki girdinin sağlandığını varsayalım: 8 Sonra çıktı: 40320
"""
"""fak= int(input("sayıyı gırınız "))
def fact(x):
    if(x==0) :
        return 1
    else:
        return x*fact(x-1)
print(fact(fak))"""

"""-------------Belirli bir n integral numarasıyla, 1 ile n arasında bir tam sayı olan (her ikisi de dahil) (i, ixi) içeren bir sözlük
 oluşturmak için bir program yazın. ve sonra program sözlüğü yazdırmalıdır. Programa aşağıdaki girdinin sağlandığını : 8
Ardından çıktı şu şekilde olmalıdır:
1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""
"""
dict1={}
n=int(input("sayıyı gırınız "))

for i in range(1,n+1):
    dict1[i]=i*i
    
print(dict1)
"""

"""----------#Konsoldan virgülle ayrılmış sayılar dizisini kabul eden ve her sayıyı içeren bir liste ve tuple üreten bir program yazın
Programa aşağıdaki girdinin sağlandığını varsayalım:
"""
"""
input1=input("sayıları gırınız")
list1=input1.split(",")
tuple1=tuple(list1)
print(list1)
print(tuple1)
"""

"""-----------En az iki yöntemi olan bir sınıf tanımlayın:

getString: konsol girişinden bir dize almak için
printString: dizeyi büyük harflerle yazdırmak için.
Ayrıca, sınıf yöntemlerini test etmek için lütfen basit test işlevini ekleyin."""

"""
class deneme :
    def getString(self):
        self.x=input("giriş yapın")

    def printString(self):
        print(self.x.upper())

den=deneme()
den.getString()
den.printString()

"""

"""
---------Verilen formüle göre değeri hesaplayan ve yazdıran bir program yazın:

Q = [(2 _ C _ D) / H] 'nin karekökü

Aşağıda C ve H'nin sabit değerleri verilmiştir:

C 50'dir. H 30'dur.

D, değerleri programınıza virgülle ayrılmış bir sırayla girilmesi gereken değişkendir.Örneğin,
programa aşağıdaki virgülle ayrılmış giriş sırasının verildiğini varsayalım:

100,150,180
Programın çıktısı şöyle olmalıdır:

18,22,24
"""
"""
import math
c=50
h=30
list1=[]
d = [x for x in input("sayıyı gırınzı").split(',')]
for i in d:
    list1.append(str(int(round(math.sqrt(2*c*float(i)/h)))))
print(list1,end=(","))

"""
"""
 -----------Girdi olarak 2 hane, X, Y alan ve 2 boyutlu bir dizi oluşturan bir program yazın. Dizinin i'inci
satırındaki ve j'inci sütunundaki öğe değeri i _ j olmalıdır. *

Not: i = 0,1 .., X-1; j = 0,1, ¡Y-1. Programa aşağıdaki girdilerin verildiğini varsayalım: 3,5

Ardından, programın çıktısı şöyle olmalıdır:

[[0, 0, 0, 0, 0]
 [0, 1, 2, 3, 4]
 [0, 2, 4, 6, 8]]
"""
"""
d = [x for x in input("boyutları gırınzı").split(',')]
st=int(d[0])
su=int(d[1])
dizi=[[0 for col in range(su)] for row in range(st)]
for i in  range(0,st):
    for j in range(0,su):
        dizi[i][j]=i*j
print(dizi)
"""
"""
-------------Virgülle ayrılmış sözcük dizisini girdi olarak kabul eden ve sözcükleri alfabetik olarak sıraladıktan sonra virgülle ayrılmış bir sırayla yazdıran bir program yazın.

Programa aşağıdaki girdinin sağlandığını varsayalım:

without,hello,bag,world
Ardından çıktı şu şekilde olmalıdır:

bag,hello,without,world
"""
"""
x=[x for x in input("kelimeleri giriniz").split(",")]
x.sort()
print(x)
"""
"""
---------Satır sırasını girdi olarak kabul eden ve cümledeki tüm karakterleri büyük harf yaptıktan sonra satırları 
yazdıran bir program yazın.

Programa aşağıdaki girdinin sağlandığını varsayalım:

Hello world
Practice makes perfect
Ardından çıktı şu şekilde olmalıdır:

HELLO WORLD
PRACTICE MAKES PERFECT
"""
"""
lines = []
while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print (sentence)
"""
"""
---------Boşluklarla ayrılmış sözcük dizisini giriş olarak kabul eden ve tüm yinelenen sözcükleri çıkarıp 
alfanümerik olarak sıraladıktan sonra sözcükleri yazdıran bir program yazın.

Programa aşağıdaki girdinin sağlandığını varsayalım:
asu hela ela ela asu knsfd jaed 
hello world and practice makes perfect and hello world again
Ardından çıktı şu şekilde olmalıdır:

again and hello makes perfect practice world
"""
"""
y=[x for x in input("kelimleri giriniz").split(" ")]
y.sort()
print(" ".join(set(y)))
"""
"""

------Giriş olarak virgülle ayrılmış 4 basamaklı ikili sayılar dizisini kabul eden bir program yazın ve
 sonra bunların 5'e bölünüp bölünemeyeceğini kontrol edin. 5'e bölünebilen sayılar, virgülle ayrılmış
bir sırada basılacaktır.

Misal:

0100,0011,1010,1001
O zaman çıktı şöyle olmalıdır:

1010
"""
"""
flag=0
y=[x for x in input("sayıları gırınız").split(",")]
for i in y:
    if len(i) != 4:
        print(i +" sayı yanliş boyutta ")
        continue
    for j in i:

         if int(j)<2:
           pass
         else:
             print(i + " sayı ıkıklık degil")
             flag=1
         if flag==1:
                break

    if flag == 0:
        if int(i,2) % 5 == 0:
            print(i+"bese bolunebilir")
"""
"""
Sayının her basamağı çift sayı olacak şekilde 1000 ile 3000 (her ikisi de dahil) arasındaki tüm bu sayıları
bulacak bir program yazın. Elde edilen sayılar tek bir satıra virgülle ayrılmış sırayla basılmalıdır.
"""
"""
for i in range(1000,3001):
    s=str(i)
    flag = 0
    for j in s:
        if int(j)%2==0:
            pass
        else:
            flag=1
            break
    if flag==0:
        print(i,end=",")
"""
"""
Bir cümleyi kabul eden ve harflerin ve rakamların sayısını hesaplayan bir program yazın.

Programa aşağıdaki girdinin sağlandığını varsayalım:

hello world! 123
Ardından çıktı şu şekilde olmalıdır:

LETTERS 10
DIGITS 3
"""
"""
num=0
world=0
x=input("cümle giriniz")
for i in str(x):
        if i.isdigit(): #sayı mı?
            num=num+1
        elif i.isalpha(): # harf mı
            world=world+1
print("harf "+str(world)+"\nsayı "+str(num))
"""
"""
Bir cümleyi kabul eden ve büyük harflerin ve küçük harflerin sayısını hesaplayan bir program yazın.

Programa aşağıdaki girdinin sağlandığını varsayalım:

Hello world!
Ardından çıktı şu şekilde olmalıdır:

UPPER CASE 1
LOWER CASE 9
"""
"""
x=input("cumleyı gırınız")
dict1={'Upper case':0,'lower case':0}
for i in str(x):
    if i.islower():
        dict1['Upper case']+=1
    elif i.isupper():
        dict1['lower case']+=1

print(dict1)
"""
"""
-----A + aa + aaa + aaaa'nın değerini a'nın değeri olarak verilen bir basamakla hesaplayan bir program yazın.

Programa aşağıdaki girdinin sağlandığını varsayalım:

9
Ardından çıktı şu şekilde olmalıdır:

11106
"""
"""
x=int(input("sayıyı gırınız "))
solve=x*(1+11+111+1111)
print("sonuc: "+str(solve))
"""
"""

------Bir listedeki her bir tek sayının karesini almak için bir liste anlayışı kullanın. Liste,
 virgülle ayrılmış sayılar dizisi ile girilir. > Programa aşağıdaki girdinin sağlandığını varsayalım:

1,2,3,4,5,6,7,8,9
Ardından çıktı şu şekilde olmalıdır:

1,9,25,49,81
"""
"""
x=input("sayı gırınız").split(",")
for i in x:
    j= int(i)
    if j%2!=0:
        print(str(j*j),end=",")

"""
"""
-----------Konsol girişinden bir işlem günlüğüne göre bir banka hesabının net tutarını hesaplayan bir
 program yazın.İşlem günlüğü formatı aşağıdaki gibi gösterilir:

D 100
W 200
D, para yatırma, W ise para çekme anlamına gelir.
Programa aşağıdaki girdinin sağlandığını varsayalım:

D 300
D 300
W 200
D 100
Ardından çıktı şu şekilde olmalıdır:

500

"""
"""
solve=0
x= input("işlem ve degr gırınız \n").split(" ")
while True:
    x= input()
    if not x :
        break
    else:
        i=x.split(" ")
        islem=i[0]
        value=int(i[1])
        if islem == 'D':
            solve = solve + value
        elif islem == 'W':
            solve = solve + value
print(str(solve))
"""

"""
Bir web sitesi, kullanıcıların kaydolmak için kullanıcı adı ve şifre girmesini gerektirir.
Kullanıcılar tarafından girilen parola geçerliliğini kontrol etmek için bir program yazın.

Şifreyi kontrol etmek için kriterler şunlardır:

[Az] arasında en az 1 harf
[0-9] arasında en az 1 sayı
[AZ] arasında en az 1 harf
[$ # @] 'Den en az 1 karakter
Minimum işlem şifresi uzunluğu: 6
Maksimum işlem şifresi uzunluğu: 12
Programınız virgülle ayrılmış bir dizi parolayı kabul etmeli ve bunları yukarıdaki kriterlere göre kontrol
edecektir. Kriterlere uyan şifreler, her biri virgülle ayrılmış olarak yazdırılacaktır.

"""
"""
num,cha,low,up,=0,0,0,0
x=input("sifre griniz").split(",")
for i in x:
    if len(i)<=6:
        print(i+"şifre min 6 olmalıdır")
    elif len(i)>=12:
        print(i+"sifre max 12 olmalıdır")
    else:
        for j in i:
            if j.isdigit():
                num=1
            if  j=="$" or j=="#" or j=="@":
                cha=1
            if j.islower():
                low=1
            if j.isupper():
                up=1
        print(str(num)+"num"+str(cha)+"cha"+str(low)+"low"+str(up)+"up")
        if num==1 and cha==1 and low==1  and up==1:
            print(i+" şifre duzgundur ")
            num, cha, low, up, = 0, 0, 0, 0
        else:
            print("şifre duzgun degıl")
           # ABd1234@
"""
"""
-------(İsim, yaş, puan) tuplelarını, adın dize, yaş ve puanın sayı olduğu artan sıraya göre sıralamak için
bir program yazmanız gerekmektedir. Demetler konsol tarafından girilir. Sıralama ölçütü şöyledir:

1: Ada göre sırala
2: Ardından yaşa göre sıralayın
3: Ardından puana göre sıralayın
Öncelik bu ad> yaş> puandır.

Aşağıdaki demetler programa girdi olarak verilirse:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Ardından, programın çıktısı şöyle olmalıdır:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
-------------------------------------------bak-------------------------------------------------
"""
"""
from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))
"""

"""
Verilen bir 0 ve n aralığı arasında 7'ye bölünebilen sayıları yineleyebilen bir oluşturucuya sahip 
bir sınıf tanımlayın.

Programa aşağıdaki girdinin sağlandığını varsayalım:

7
Ardından çıktı şu şekilde olmalıdır:

0
7
14

-------------------------------------bak cözemedim--------------------------------------------
"""
"""
class sayi:

     def bul(self,n):
         list = [0 for i in range]
         j = 0
         for i in range(0,int(n)+1):

             if i%7==0:
                 list[j]=i
             j = j + 1
         retun list
eleman=sayi()
eleman.bul(14).list

print(list)
"""
"""
Bir robot, orijinal noktadan (0,0) başlayarak bir düzlemde hareket eder. Robot belirli adımlarla YUKARI,
AŞAĞI, SOLA ve SAĞA doğru hareket edebilir. Robot hareketinin izi aşağıdaki gibi gösterilir:

Yönden sonraki sayılar adımlardır. Lütfen bir dizi hareket ve orijinal noktadan sonra mevcut konumdan
mesafeyi hesaplamak için bir program yazın. Mesafe bir kayan nokta ise, en yakın tamsayıyı
yazdırmanız yeterlidir. Örnek: Aşağıdaki demetler programa girdi olarak verilirse:

UP 5
DOWN 3
LEFT 3
RIGHT 2
Ardından, programın çıktısı şöyle olmalıdır:

2
"""
"""
import  math

x,y = 0,0
while True:
    s = input().split()
    if not s:
        break
    if s[0]=='UP':                  # s[0] indicates command
        x+=int(s[1])                # s[1] indicates unit of move
    if s[0]=='DOWN':
        x-=int(s[1])
    if s[0]=='LEFT':
        print(s[1])
        y+=int(s[1])
    if s[0]=='RİGHT':
        print(s[1])
        y-=int(s[1])
print(str(x)+" "+str(y))                                    # N**P means N^P
dist = round(math.sqrt(x**2 + y**2))  # euclidean distance = square root of (x^2+y^2) and rounding it to nearest integer
print(dist)
"""
"""
Girişteki kelimelerin frekansını hesaplamak için bir program yazın. Anahtar alfanümerik olarak
sıralandıktan sonra çıktı çıkmalıdır.

Programa aşağıdaki girdinin sağlandığını varsayalım:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Ardından çıktı şu şekilde olmalıdır:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
"""
dict1={}
x=input("cümleyi giriniz.").split(" ")
dict1[x[0]]=0
for i in x:
    if i in dict1:
        dict1[i] = int(dict1[i]) + 1
    elif i!=dict1.keys():
        dict1[i]=1
    else:
        pass

for j in sorted(dict1):
    print(j+":"+str(dict1[j]))
"""
"""
Sayının kare değerini hesaplayabilen bir yöntem yazın
"""
"""
def karesi(n):
    solve=n*n
    return solve
print(str(karesi(3)))
"""
"""
----------------------------ANLAMADIM--------------------------------------
Python'un birçok yerleşik işlevi vardır ve onu nasıl kullanacağınızı bilmiyorsanız,
belgeyi çevrimiçi okuyabilir veya bazı kitaplar bulabilirsiniz. Ancak Python, her 
yerleşik işlev için yerleşik bir belge işlevine sahiptir.

Lütfen abs (), int (), raw_input () gibi bazı Python yerleşik işlev belgelerini
yazdırmak için bir program yazın

Ve kendi işleviniz için belge ekleyin

İpuçları:
The built-in document method is __doc__
"""
"""
Bir sınıf parametresi olan ve aynı örnek parametresine sahip bir sınıf tanımlayın.
"""
"""
class hayvan:
    kedi="hayvan"
    def __init__(self,name=None):
        self.name=name
kopek=hayvan("boncuk")
print(kopek.name)
"""
"""
İki sayının toplamını hesaplayabilen bir fonksiyon tanımlayın.
"""
"""
def toplam(n,y):
    return n+y
x=input("sayı gırınız").split(" ") 
solve=toplam(int(x[0]),int(x[1]))
print(str(solve))
#-----
sum = lambda n1,n2 : n1 + n2      # here lambda is use to define little function as sum
print(sum(1,2))
"""
"""
Bir tamsayıyı dizeye dönüştürebilen ve konsolda yazdırabilen bir işlev tanımlayın.
"""
"""
don=lambda n: str(n)
print(don(3))
print(type(don(3)))
"""
"""
Dize biçiminde iki tamsayı alabilen ve toplamlarını hesaplayabilen ve ardından konsolda
yazdırabilen bir işlev tanımlayın.
"""
"""
def top(a,b):
    return int(a)+int(b)
print(top("2","6"))
#-----------
solve=lambda a,b : int(a)+int(b)
print(solve("3","7"))
"""
"""
İki dizeyi girdi olarak kabul edip birleştirebilen ve ardından konsolda yazdırabilen
bir işlev tanımlayın.
"""
"""
def bir(a,b):
    print(a+b)
bir("ali","veli")
#-----
birl=lambda a,b:print(a+b)
birl("asuman","yılmaz")
"""
"""
Giriş olarak iki dizeyi kabul edebilen ve dizeyi maksimum uzunlukta konsolda yazdırabilen
bir işlev tanımlayın. İki dizge aynı uzunluğa sahipse, işlev tüm dizeleri satır satır
yazdırmalıdır.
"""
"""
def uz(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    else:
        print(a)
        print(b)
uz("ali","veli")
uz("veyla","kx")
uz("alı","alı")
"""
"""
Anahtarların 1 ile 20 arasında sayılar (her ikisi de dahil) ve değerlerin anahtarların
karesi olduğu bir sözlük yazdırabilen bir işlev tanımlayın.
"""
"""
def show():
    dict1={}
    for i in range(1,21):
        dict1[i]=i*i
    print(dict1)
show()
"""
"""
Anahtarların 1 ile 20 arasında sayılar (her ikisi de dahil) ve değerlerin anahtarların
karesi olduğu bir sözlük oluşturabilen bir işlev tanımlayın. İşlev yalnızca tuşları
yazdırmalıdır.
"""
"""
def show():
    dict1={}
    for i in range(1,21):
        dict1[i]=i*i
    for k in dict1.keys():
        print(k)
show()
"""
"""
Değerlerin 1 ile 20 arasında sayıların karesi olduğu bir liste oluşturabilen ve
yazdırabilen bir işlev tanımlayın (her ikisi de dahil).
"""
"""

def show():
 list=[]
 for i in range(1,21):
     list.append(i*i)
 for j in list:
     print(j)
show()
"""
"""
Değerlerin 1 ile 20 arasında sayıların karesi olduğu bir liste oluşturabilen
bir işlev tanımlayın (her ikisi de dahil). Daha sonra işlevin listedeki ilk
5 öğeyi yazdırması gerekir.
"""
"""
def show():
 list1=[]
 for i in range(1,21):
     solve=i**2
     list1.append(solve)
 print(list1[:5])
show()
"""
"""
Değerlerin 1 ile 20 arasında sayıların karesi olduğu bir liste oluşturabilen bir
işlev tanımlayın (her ikisi de dahil). Daha sonra işlevin listedeki son 5 öğeyi
yazdırması gerekir.
"""
"""
def show():
 list1=[]
 for i in range(1,21):
     solve=i**2
     list1.append(solve)
 print(list1[-5:])
show()
"""
"""
Değerlerin 1 ile 20 arasında sayıların karesi olduğu bir liste oluşturabilen
bir işlev tanımlayın (her ikisi de dahil). Daha sonra işlevin listedeki ilk 5 
öğe dışındaki tüm değerleri yazdırması gerekir.
"""
"""
def show():
 list1=[]
 for i in range(1,21):
     solve=i**2
     list1.append(solve)
 print(list1[5:])
show()
"""
"""

Değerin 1 ile 20 arasında sayıların karesi olduğu bir demet oluşturabilen ve
yazdırabilen bir işlev tanımlayın (her ikisi de dahil).
"""
"""
def show():
 tupple1=list()
 for i in range(1,21):
     tupple1.append(i**2)
 print(tupple1)
show()
"""
"""
Belirli bir demetle (1,2,3,4,5,6,7,8,9,10), ilk yarı değerleri bir satırda
ve son yarı değerleri bir satırda yazdırmak için bir program yazın.
"""
"""
def show():
 list1=(1,2,3,4,5,6,7,8,9,10)
 print(list1[:5])
 print(list1[5:])
show()
"""
"""
Verilen demetteki değerleri çift sayı olan başka bir demet oluşturmak ve
yazdırmak için bir program yazın (1,2,3,4,5,6,7,8,9,10).
"""
"""
def show():
 tupple1=(1,2,3,4,5,6,7,8,9,10)
 nwtpple=list()
 j=0
 for i in tupple1:
    if int(i)%2==0:
        nwtpple.append(i)
        j+=1
        
 n=tupple(nwtpple)
 print(nwtpple)
 
show()
"""
"""
Dize "evet" veya "EVET" veya "Evet" ise "Evet" yazdırmak için girdi
olarak kabul eden bir program yazın, aksi takdirde "Hayır" yazdırın.
"""
"""
x=input("giriniz")
if x=="yes" or x=="Yes" or x=="YES":
    print("yes")
else:
    print("no")
"""
"""

[1,2,3,4,5,6,7,8,9,10] 'daki elemanların kareleri olan bir liste yapmak
için map () yapabilen bir program yazın.

-----map () işlevi, belirli bir yinelenebilir öğenin (liste, tuple vb.)
her bir öğesine verilen işlevi uyguladıktan sonra sonuçların bir eşleme
nesnesini (yineleyici olan ) döndürür.
map(yapılacak işlem ,işlem yapılacak liste vb.)
"""
"""

list1 = [1,2,3,4,5,6,7,8,9,10]
k = map(lambda x: x**2, list1)
print(list(k))
"""
"""
[1,2,3,4,5,6,7,8,9,10] 'da cift elemanları kare kare olan bir liste oluşturmak
 için map () ve filter () yapabilen bir program yazın.
 --------filter() fonksiyonu ise çağırılan fonksiyonun döndürdüğü değerin
true olduğu durumlara göre liste döndürür. Yani fonksiyona gönderilen
değerler içerisinden istediklerimizi alarak yeni liste oluşturmamızı sağlar.
"""
"""
list1 = [1,2,3,4,5,6,7,8,9,10]
k=map(lambda x:x*x,filter(lambda y:y%2==0,list1))
print(list(k))
"""
"""
Öğeleri 1 ile 20 arasında çift sayı olan (her ikisi de dahil) bir liste
oluşturmak için süzebilen () bir program yazın.
"""
"""
list1=filter(lambda x: x%2==0,range(1,21))
print(list(list1))
"""
"""
Öğeleri 1 ile 20 arasında sayıların karesi olan bir liste yapmak map ()
eşleştirebilen bir program yazın (her ikisi de dahil).
"""
"""
x=map(lambda x: x*x,range(1,21))
print(list(x))
"""
"""
PrintNationality adlı statik bir yönteme sahip olan American
adlı bir sınıf tanımlayın.
"""
"""
class American(object):
    @staticmethod
    def PrintNationality():
        print("american")
ameri=American()
ameri.PrintNationality()
American.PrintNationality()
"""
"""
American adlı bir sınıfı ve onun alt sınıfı NewYorker'ı tanımlayın
"""
"""
class American(object):
    pass
class Newyork (American):
    pass
anAmerican = American()
aNewYorker = Newyork()
print(anAmerican)
print (aNewYorker)
"""
"""
Bir yarıçapla oluşturulabilen Circle adında bir sınıf tanımlayın.
Circle sınıfı, alanı hesaplayabilen bir yönteme sahiptir.
"""
"""
import math
class Circle(object):
    r=0
    def __init__(self,r):
        self.r=r
    def alan(self):
        return math.pi*self.r**2
a=Circle(2)
print(a.alan())
"""
"""
Uzunluk ve genişliğe göre oluşturulabilen Rectangle adlı bir
sınıf tanımlayın. Rectangle sınıfı, alanı hesaplayabilen bir yönteme sahiptir.
"""
"""
class Rectangle(object):
    def __init__(self,en,boy):
        self.en=en
        self.boy=boy
    def alan(self):
        return self.en*self.boy
r=Rectangle(2,3)
print(r.alan())
"""
"""

Shape adlı bir sınıfı ve alt sınıfı Square'i tanımlayın. Square sınıfı,
bağımsız değişken olarak uzunluk alan bir init işlevine sahiptir.
Her iki sınıfın da, Shape'in alanının varsayılan olarak 0 olduğu
şeklin alanını yazdırabilen bir alan işlevi vardır.
"""
"""
class Shape(object):
    def __init__(self):
        pass
    def alan(self):
        return 0
class Squre(Shape):
    def __init__(self,uzunluk):
        Shape.__init__(self)
        self.uzunluk=uzunluk
    def alan(self):
        return self.uzunluk*self.uzunluk
a=Squre(3)
b=Shape()
print(b.alan())
print(a.alan())
"""
"""
Lütfen bir RuntimeError rasie oluşturun.
"""
"""
raise RuntimeError('yanlışş')
"""
"""
5/0 hesaplamak için bir işlev yazın ve 
istisnaları yakalamak için try / except  kullanın.
"""
"""
def dene():
    return 5/0
try:
    dene()
except ZeroDivisionError:
    print("hatalı")
except Exception:
    print("haata")
finally:
    print("ddscd")
"""
"""
Öznitelik olarak bir dize mesajı alan özel bir istisna sınıfı tanımlayın.
"""
"""
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
"""
"""
" Username@companyname.com " biçiminde bazı e-posta adreslerimiz
olduğunu varsayarak , lütfen belirli bir e-posta adresinin kullanıcı
adını yazdırmak için program yazın. Hem kullanıcı adları hem de şirket
adları yalnızca harflerden oluşur.

Örnek: Aşağıdaki e-posta adresi programa girdi olarak verilirse:

john@google.com
Ardından, programın çıktısı şöyle olmalıdır:

john
"""
"""
x=input("mail griiniz").split("@")
print(x[0])
"""
"""
" Username@companyname.com " biçiminde bazı e-posta adreslerimiz olduğunu
varsayarak , lütfen belirli bir e-posta adresinin şirket adını yazdırmak
için bir program yazın. Hem kullanıcı adları hem de şirket adları yalnızca
harflerden oluşur.

Örnek: Aşağıdaki e-posta adresi programa girdi olarak verilirse:

john@google.com
Ardından, programın çıktısı şöyle olmalıdır:

google
"""
"""
mail=input("mail griiniz").split("@")
x=mail[1]
i=0
y=" "
while  True:
    if x[i]==".":
        break
    y=y+x[i]
    i+=1
print(y)
"""
"""
Yalnızca rakamlardan oluşan sözcükleri yazdırmak için giriş olarak boşluklarla ayrılmış sözcük
dizisini kabul eden bir program yazın.

Örnek: Aşağıdaki kelimeler programa girdi olarak verilirse:

2 cats and 3 dogs.
Ardından, programın çıktısı şöyle olmalıdır:

['2', '3']
"""
"""
list1=[]
x=input("giriniz").split(" ")
for i in x:
    if i.isdigit():
        list1.append(i)
print(list1)
"""
"""
Unicode stringi "merhaba dünya" yazdırın.
"""
"""
un=u"hello word"
print(un+" "+str(type(un)))
"""
"""
Bir ASCII dizesini okumak ve onu utf-8 ile kodlanmış bir unicode dizesine dönüştürmek için bir program yazın.
"""
"""
s = input("giriniz")
u = s.encode('utf-8')
print(u)
"""
"""

Bir Python kaynak kodu dosyasının unicode'da olduğunu belirtmek için özel bir yorum yazın.
"""
# - * - kodlama: utf-8 - * -
"""
Konsol tarafından verilen bir n girişiyle (n> 0) 1/2 + 2/3 + 3/4 + ... + n / n + 1'i 
hesaplamak için bir program yazın.

Örnek: Aşağıdaki n, programa girdi olarak verilirse:

5
Ardından, programın çıktısı şöyle olmalıdır:

3.55
"""
"""
n=int(input("n sayısını gır"))
i=1
solve=0.00
while i<=n:
    solve += float(i / (i + 1))
    i+=1

print(round(solve,2))
"""
"""
Hesaplamak için bir program yazın:

f(n)=f(n-1)+100 when n>0
and f(0)=0
konsol tarafından verilen bir n girişi ile (n> 0).

Örnek: Aşağıdaki n, programa girdi olarak verilirse:

5
Ardından, programın çıktısı şöyle olmalıdır:

500

"""
"""
def s(n):
    if n==0:
        return 0
    else:
        return s(n-1)+100
n=int(input())
print(s(n))
"""
"""
Fibonacci Dizisi aşağıdaki formüle göre hesaplanır:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Konsol tarafından verilen bir n girdisi ile f (n) 'nin değerini hesaplamak için lütfen bir program yazın.

Örnek: Aşağıdaki n, programa girdi olarak verilirse:

7
Ardından, programın çıktısı şöyle olmalıdır:

13

"""
"""
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    elif n>1:
        return fib(n-1)+fib(n-2)
print(str(fib(7)))
"""
"""
Fibonacci Dizisi aşağıdaki formüle göre hesaplanır:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Konsol tarafından verilen bir n girdisi ile f (n) 'nin değerini hesaplamak için lütfen bir program yazın.

Örnek: Aşağıdaki n, programa girdi olarak verilirse:

7
Ardından, programın çıktısı şöyle olmalıdır:

0,1,1,2,3,5,8,13
"""
"""
def fib(n):
        if n==0:
            return 0
        if n==1:
            return 1
        elif n>1:
            return fib(n-1)+fib(n-2)
n=int(input("sayıyı gırınız"))
for i in range(0,n+1):
 print(str(fib(i)))
 """

"""
--------------------anlamadım----------------------bak---------------
N, konsol tarafından girilirken, 0 ile n arasındaki çift sayıları virgülle ayrılmış biçimde 
yazdırmak için generator  kullanarak bir program yazın.

Örnek: Aşağıdaki n, programa girdi olarak verilirse:

10
Ardından, programın çıktısı şöyle olmalıdır:

0,2,4,6,8,10
"""
"""
--------------------anlamadım----------------------bak---------------
N, konsol tarafından girilirken virgülle ayrılmış biçimde 0 ile n arasında 5 ve 7'ye
bölünebilen sayıları yazdırmak için lütfen oluşturucu kullanarak bir program yazın.

Örnek: Aşağıdaki n, programa girdi olarak verilirse:

100
Ardından, programın çıktısı şöyle olmalıdır:

0,35,70
"""
"""
Lütfen [2,4,6,8] listesindeki her sayının çift olduğunu doğrulamak için assert ifadeleri yazın.

"""
"""
list1=[2,4,6,8]
for i in list1:
   assert i%2==0
"""
"""
Lütfen konsoldan temel matematiksel ifadeyi kabul eden bir program yazınız ve değerlendirme
sonucunu yazdırınız.

Örnek: Aşağıdaki n, programa girdi olarak verilirse:

35 + 3
Ardından, programın çıktısı şöyle olmalıdır:
"""
"""
expression = input()
print(eval(expression)) ####-------eval yanına yazılan matematıksel işlemi hesaplar sonuç dondurur
"""
"""
----------------67 anlamadım bakk---------------------
Lütfen sıralı bir listede bir öğeyi arayan bir ikili arama işlevi yazın. İşlev, listede aranacak
öğenin dizinini döndürmelidir.
"""
"""
----------------68 anlamadım bakk---------------------
Lütfen sıralı bir listede bir öğeyi arayan bir ikili arama işlevi yazın. İşlev, listede aranacak
 öğenin dizinini döndürmelidir.
"""
"""
Lütfen Python modülünü kullanarak değerin 10 ile 100 arasında olduğu rastgele bir kayan nokta oluşturun.
"""
"""
import random
rand_num = random.uniform(10,100)
print(rand_num)
"""
"""
Lütfen Python modülünü kullanarak değerin 5 ile 95 arasında olduğu rastgele bir kayan nokta oluşturun
"""
"""
import random
rands=random.uniform(5,95)
print(rands)
"""
"""
Lütfen rastgele modül ve liste anlama kullanarak 0 ile 10 arasında rastgele bir çift sayı 
çıkaracak bir program yazın.
"""
"""
li=[2,4,6,8]
import random
print (random.choice(li))#--choice dizi gibi seylerden bir tanesını rastgele dondurur
print (random.choice([i for i in range(11) if i%2==0]))
"""
"""
Lütfen rastgele modül ve liste anlama kullanarak 10 ile 150 arasında 5 ile 7'ye
bölünebilen rastgele bir sayı çıkaracak bir program yazın.
"""
"""
import random
print(random.choice([i for i in range(10,150)if i%7==0 and i%5==0]))
"""
"""
Lütfen 100 ile 200 arasında 5 rastgele sayı içeren bir liste oluşturmak için bir program yazın.
"""
"""
import random
list1=[]
for i in range(0,5):
    list1.append([random.choice([x for x in range(100,200)])])
print(list1)
#-----------
import random
print random.sample(range(100,201), 5)
# random.sample (sıra, k)    diziden seçilen elemanların k uzunluğunda yeni listesi.
"""
"""
Lütfen rastgele olarak 100 ile 200 arasında 5 çift sayı içeren bir liste oluşturmak için bir program yazın.
"""
"""
import random
print(random.sample([i for i in range(100,200) if i%2==0],5))
"""
"""
Lütfen rastgele olarak 5 ile 7'ye bölünebilen, 1 ile 1000 dahil 5 sayıdan oluşan bir liste
oluşturmak için bir program yazın.
"""
"""
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))
"""
"""
Lütfen rastgele olarak 7 ile 15 arasında bir tam sayı yazdırmak için bir program yazın.
"""
"""
import random
print(random.randint(7,15))# --randint= ıkı aralıklı tam sayı randrange=tek parametreli
"""
"""
---------------76 anlamadım bakkkk ---------------
Lütfen "merhaba dünya! Merhaba dünya! Merhaba dünya! Merhaba dünya!" Dizesini sıkıştırmak
ve açmak için bir program yazın.

import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print( zlib.decompress(t))
"""
"""
Lütfen "1 + 1" çalışma süresini 100 kez yazdırmak için bir program yazın.
"""
"""
from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())
"""
#----- Python timeit (), kodun performansını kontrol etmeye yardımcı olan kullanışlı bir yöntemdir.
#---- Python timeit (), kodun performansını kontrol etmeye yardımcı olan kullanışlı bir yöntemdir.
"""
stmt : Bu, yürütme süresini ölçmek istediğiniz kodu alacaktır. Varsayılan değer "geçer" dir.
kurulum : Bu, stmt'den önce yürütülmesi gereken kurulum ayrıntılarına sahip olacaktır. Varsayılan değer "başarılı" dır.
timer : Bu timer değerine sahip olacak, timeit () zaten varsayılan bir değere sahip ve bunu göz ardı edebiliriz.
sayı : stmt burada verilen sayıya göre yürütülecektir. Varsayılan değer 1000000'dür.
"""
"""
Lütfen listeyi karıştırmak(shuffle()) ve yazdırmak için bir program yazın [3,6,7,8].
"""
#----Bir listeyi karıştırın (liste öğelerinin sırasını yeniden düzenleyin):
"""
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
"""
""" 
----------bak anlamadım
Konunun ["I", "Sen"] ve fiilin ["Oyna", "Aşk"] ve nesnenin ["Hokey", "Futbol"] olduğu tüm cümleleri
oluşturmak için lütfen bir program yazın.
"""
"""
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))
"""

"""
Lütfen [5,6,77,45,22,12,24] 'deki çift sayıları çıkardıktan sonra listeyi yazdırmak için
bir program yazın.
"""
"""
list1=[5,6,77,45,22,12,24]
li=[i for i in list1 if i%2==0]
print(li)
"""
"""
Liste anlama özelliğini kullanarak, lütfen [12,24,35,70,88,120,155] 'de 5 ve 7'ye
bölünebilen sayıları çıkardıktan sonra listeyi yazdırmak için bir program yazın.
"""
"""
list1=[12,24,35,70,88,120,155]
li=[i for i in list1 if i%5==0 and i%7==0 ]
print(li)
"""
"""
Liste anlama özelliğini kullanarak, lütfen [12,24,35,70,88,120,155] 'deki 0., 2., 4., 6. 
sayıları çıkardıktan sonra listeyi yazdırmak için bir program yazın.
"""
"""
list1=[12,24,35,70,88,120,155]
li=[]
for i in range(0,7):
    if i%2!=0:
       li.append(list1[i])
print(li)

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2 != 0 and i <= 6]#listın index no ve degerini dondurdu
print(li)
"""
"""
Liste anlama özelliğini kullanarak, lütfen [12,24,35,70,88,120,155] 'deki 2. - 4. sayıları
çıkardıktan sonra listeyi yazdırmak için bir program yazın.
"""
"""
list1=[12,24,35,70,88,120,155]
li=[x for (i,x) in enumerate(list1) if i < 3  or  4 < i]## i!=2 and i!=3 and i!=4
print(li)
"""

"""
---------bak anlamadım-----------------
Liste anlama özelliğini kullanarak, lütfen her elemanı 0 olan 3 * 5 * 8 3 boyutlu
bir dizi oluşturan bir program yazın.
"""
"""
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
"""
"""
Liste anlama özelliğini kullanarak, lütfen [12,24,35,70,88,120,155] 'deki 0., 4., 5.
sayıları çıkardıktan sonra listeyi yazdırmak için bir program yazın.
"""
"""
list1=[12,24,35,70,88,120,155]
li=[x for (i,x) in enumerate(list1) if i!=0 and i!=4 and i!=5]
# li  = [ x  for ( i , x ) in  enumerate ( li ) if  i  not  in ( 0 , 4 , 5 )]
print(li)
"""
"""
Liste anlama özelliğini kullanarak, lütfen [12,24,35,24,88,120,155] 'deki 24 
değerini çıkardıktan sonra listeyi yazdırmak için bir program yazın.
"""
"""
list1=[12,24,35,70,88,120,155]
li=[x for x in list1 if x!=24]
print(li)

#li = [12,24,35,24,88,120,155]
#li.remove(24)  # this will remove only the first occurrence of 24
#print(li)
"""
"""
Verilen iki liste [1,3,6,78,35,55] ve [12,24,35,24,88,120,155] ile,
elemanları yukarıda verilen listelerin kesişimi olan bir liste yapmak için bir program yazın.
"""
"""
list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
set1=set(list1).intersection(set(list2))
print(set1)
"""
"""
Verilen bir listeyle [12,24,35,24,88,120,155,88,120,155], orijinal sıraya göre ayrılmış
tüm yinelenen değerleri kaldırdıktan sonra bu listeyi yazdırmak için bir program yazın.
"""
"""
li = [12,24,35,24,88,120,155,88,120,155]
for i in li:
    if li.count(i) > 1:#li listesindeki deger birden fazlaysa sil count= değeri saydiriyor
        li.remove(i)
print(li)
"""
"""
Bir sınıf Kişi ve onun iki çocuk sınıfını tanımlayın: Erkek ve Kadın. Tüm sınıflar,
Erkek sınıfı için "Erkek" ve Kadın sınıfı için "Kadın" yazabilen bir "getGender"
yöntemine sahiptir.

"""
"""
class Kisi(object):
    def getGender(self):
       print("bilinmeyen ")
class Erkek(Kisi):
     def getGender(self ):
       print("Erkek")
class Kadın(Kisi):
     def getGender(self ):
       print("Kadın")
erk=Erkek()
kad=Kadın()
erk.getGender()
kad.getGender()
"""
"""
Lütfen konsol tarafından bir dizge girdisindeki her karakterin sayısını sayan
 ve yazdıran bir program yazın.

Örnek: Aşağıdaki dize programa girdi olarak verilirse:
abcdefgabc
Ardından, programın çıktısı şöyle olmalıdır:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""
"""
x=input("giriniz")
li={}
for i in x:

        if i not in  li.keys():
            li[i]=1
        else:
            li[i]=int(li[i])+1
for i in sorted(set(x)):
        print(str(i)+ ","+ str(li[i]))
#for i in sorted(set(x)):
    #print(f'{i}, {x.count(i)}')
"""
"""
Lütfen konsoldan bir dizi kabul eden bir program yazın ve bunu ters sırada yazdırın.

Örnek: Aşağıdaki dize programa girdi olarak verilirse: *

rise to vote sir
Ardından, programın çıktısı şöyle olmalıdır:

ris etov ot esir
"""
"""
x=input("giriniz")
print(x[::-1]) #[::-1] bu yapı dızıyı ters cevırır
"""
"""
Lütfen konsoldan bir dizeyi kabul eden bir program yazın ve dizinleri
çift olan karakterleri yazdırın.

Örnek: Aşağıdaki dize programa girdi olarak verilirse:
H1e2l3l4o5w6o7r8l9d
Ardından, programın çıktısı şöyle olmalıdır:

Helloworld
"""
"""
x=input("giriniz")
y=[x for (i,x) in enumerate(x) if i%2==0]
print(''.join(y))
#print(x[::2]) #------------> cift indissleri yazdır
"""
"""
Lütfen [1,2,3] 'ün tüm permütasyonlarını yazdıran bir program yazın
"""
"""
import itertools
print(list(itertools.permutations([1,2,3])))
"""
"""
-------------94 anlamadım bak-------------------------
Klasik bir antik Çin bulmacasını çözmek için bir program yazın:
Bir çiftlikte tavuklar ve tavşanlar arasında 35 kafa ve 94 bacak sayıyoruz.
Kaç tavşanımız ve kaç tavuğumuz var?
"""
"""
Katılımcıların Üniversite Spor Gününüz için puan cetveli göz önüne alındığında,
ikincilik puanını bulmanız gerekir. Size puan verilir. Bunları bir listede
saklayın ve ikincinin skorunu bulun.

Aşağıdaki dize programa girdi olarak verilirse:

5
2 3 6 6 5
Ardından, programın çıktısı şöyle olmalıdır:

5
"""
"""
arr = map(int, input().split())# map bir sayı dızı olusturmak ıcın kullanılıyor dısardan girdi 
arr = list(set(arr))            #alıp int cevirip lisete atıyor
arr.sort()
print(arr[-2])
"""
"""
Size bir S ve W genişliği verilir. Göreviniz, dizeyi genişlikte bir paragrafa kaydırmaktır.

Aşağıdaki dize programa girdi olarak verilirse:

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Ardından, programın çıktısı şöyle olmalıdır:

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
"""
from textwrap import wrap
x = str(input(': '))
w = int(input())
z = list(wrap(x, w)) #verilen dizgiyi x parcalara ayırır
for i in z:
    print(i)
"""
"""
--------------------- anlamadım bak 97------------------------
Size bir tam sayı, N verilir. Göreviniz, N büyüklüğünde bir alfabe rangoli yazdırmaktır
(Rangoli, desenlerin yaratılmasına dayanan bir Hint halk sanatı biçimidir.)

Farklı boyutlarda alfabe rangoli aşağıda gösterilmiştir
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
"""
import string
def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, '-')
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
"""
"""
Size bir tarih veriliyor. Senin görevin o tarihte günün ne olduğunu bulmak.

Giriş

AA GG YYYY biçiminde sırasıyla ay, gün ve yılı ayırarak boşluk içeren tek bir girdi satırı.

08 05 2015
Çıktı

Doğru günü büyük harflerle yazdırın.

WEDNESDAY
"""
"""
import datetime
y=input().split(" ")
x = datetime.datetime(int(y[2]),int(y[1]),int(y[0]))


print(x.strftime("%A"))

import calendar

month, day, year = map(int, input().split())

dayId = calendar.weekday(year, month, day)
print(calendar.day_name[dayId].upper())
"""
"""
2 tam sayı kümesi verildiğinde, M ve N, simetrik farklarını artan sırada yazdırın.
 Simetrik fark terimi, M veya N'de bulunan ancak her ikisinde de bulunmayan değerleri belirtir.

Giriş

İlk girdi satırı bir tamsayı, M içerir. İkinci satır M boşlukla ayrılmış tamsayı içerir.
Üçüncü satır bir tam sayı içerir, N Dördüncü satır boşlukla ayrılmış N tamsayı içerir.

4
2 4 5 9
4
2 4 11 12
Çıktı

Simetrik fark tam sayılarını artan sırada, her satırda bir tane olacak şekilde çıktılar.

5
9
11
12
"""
"""
if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int,input().split()))

    m = int(input())
    set2 = set(map(int, input().split()))

    ans = list(set1 ^ set2)
    ans.sort()
    for i in ans:
        print(i)
"""
"""
---------------anlamadım bak 100 ---------------------------
Size kelimeler veriliyor. Bazı kelimeler tekrar edebilir. Her kelime için, 
geçtiği sayıların çıktısını alın. Çıktı sırası, kelimenin giriş görünüm sırasına
karşılık gelmelidir. Açıklama için örnek giriş / çıkışa bakın.

Aşağıdaki dize programa girdi olarak verilirse:

4
bcdef
abcdefg
bcdef
cbdef
Ardından, programın çıktısı şöyle olmalıdır:

3
2 1 1
"""
"""

n = int(input())

word_list = []
word_dict = {}

for i in range(n):
    word = input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word] = word_dict.get(word, 0) + 1

print(len(word_list))
for word in word_list:
    print(word_dict[word], end=' ')
"""

"""
Size bir dize verilir. Göreviniz dizedeki harflerin sıklığını saymak ve harfleri
azalan sıklık sırasına göre yazdırmaktır.

Aşağıdaki dize programa girdi olarak verilirse:

aabbbccde
Ardından, programın çıktısı şöyle olmalıdır:

b 3
a 2
c 2
d 1
e 1
"""
"""
X = input()
my_set = set(X)
arr = []
for item in my_set:
    arr.append([item,X.count(item)])
tmp = sorted(arr,key = lambda x: (-x[1],x[0]))

for i in tmp:
    print(i[0]+' '+str(i[1]))

"""
"""
Bir dizeyi kabul eden ve rakam ve harflerin sayısını hesaplayan bir Python programı yazın.
Hello321Bye360
Çıktı

Digit - 6
Letter - 8
"""
"""
x=input()
say=0
word=0
for i in x:
    if i.isdigit():
        say+=1
    elif i.isalpha():
        word+=1
print("sayı: "+str(say))
print("word: "+str(word))
"""
"""
N sayısı verildiğinde Özyineleme Kullanarak 1'den N'ye Toplamı Bulun

Giriş

5
Çıktı

15
"""
"""
def top(n):
    if n==0:
        return n
    return top(n-1)+n
x=int(input())
print(top(x))
"""
