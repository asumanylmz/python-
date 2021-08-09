import numpy as np
import pandas as pd
#print(pd.__version__)

"""
2 Listeden, numpy diziden ve dikteden bir dizi nasıl oluşturulur?
"""
"""
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))#ziple ıkı arrayı vb.seyı dict yapabılırız.

# Solution
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)
print(ser1.head())
print(ser2.head())
print(ser3.head())
"""
"""
3 Bir serinin indeksi bir veri çerçevesinin bir sütununa nasıl dönüştürülür?
"""
"""
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

ser = pd.Series(mydict)# a 0 b 1 seklinde indexle yazdırıyor

# Solution
df = ser.to_fraem().reset_index()#reset_index dicteki index 0 ... seklinde sıralar
#işlevi, verilen dizi nesnesini bir veri çerçevesine dönüştürmek için kullanılır.
print(df.head())
"""
"""
4. Bir veri çerçevesi oluşturmak için birçok dizi nasıl birleştirilir?
Bir veri çerçevesi oluşturmak için ser1 ve ser2'yi birleştirin.
"""
"""
ser=pd.Series(list('abcdefgğiıjklmnoöprşstuüvyzxwq'))
ser1=pd.Series(np.arange(30))
df = pd.concat([ser, ser1], axis=0)#concat ıkı serıes bırlestırır axis=boyut 0-1 degerli
print(df.head())
"""
"""
5. Dizinin dizinine isim nasıl atanır?
Seriye ser'alfabe' diyen bir isim verin .
"""
"""
ser=pd.Series('abcdefghıijklmnoöprtsşuüvyzxqw')
ser.name = 'alphabets'
ser.head() #Bir Serinin adı
"""
"""
6. Seri B'de bulunmayan A serisi öğeleri nasıl elde edilir?
Gönderen ser1kaldır öğeler mevcut ser2.
"""
"""
ser1=pd.Series(np.arange(1,6))
ser2=pd.Series(np.arange(6,9))
ser1.name="ser1"
ser2.name="ser2"
print(ser1)
print(ser2)
ser1[~ser1.isin(ser2)]
"""
"""
7. Hem A serisi hem de B serisi için ortak olmayan öğeler nasıl elde edilir?
Her şeyden öğeleri alın ser1ve ser2her iki yaygın değildir.
"""
"""
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser_u = pd.Series(np.union1d(ser1, ser2))  # union tum elemanları tekrarsız verir
ser_i = pd.Series(np.intersect1d(ser1, ser2))  # intersect İki dizinin kesişimini bulun
print(ser_u[~ser_u.isin(ser_i)])
"""
"""
8. Bir sayısal serinin minimum, 25. yüzdelik dilim, medyan, 75. ve maksimum değerleri nasıl
 elde edilir?
 Minimum, 25. yüzdelik dilim, medyan, 75. ve maksimumu hesaplayın ser
"""
"""
ser = pd.Series(np.random.normal(10, 5, 25))
min=pd.Series.min(ser)
max=pd.Series.max(ser)
medyan=pd.Series.median(ser)
print(max)
print(np.percentile(ser ,q=[25,75]))#Belirtilen eksen boyunca verilerin q-inci yüzdelik dilimini hesaplayın.
"""
"""
9. Bir serinin benzersiz öğelerinin sıklık sayıları nasıl alınır?
Her benzersiz değerin sıklık sayılarını hesaplayın ser.
"""
"""
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser.value_counts()
"""
"""
10. Yalnızca en sık görülen 2 değeri olduğu gibi tutup diğer her şeyi 'Diğer' olarak nasıl
 değiştirebilirim?
 
 Gönderen ser, olduğu gibi üst 2 en sık öğeleri tutmak ve 'Diğer' olarak her şeyi değiştirin.
"""
"""
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
print("Top 2 Freq:", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
"""
"""
11. Bir sayısal seriyi eşit büyüklükteki 10 gruba nasıl ayırabilirim?
seriyi ser 10 eşit ondalık bölmeye ayırın ve değerleri bölme adıyla değiştirin.
"""
"""
ser = pd.Series(np.random.random(20))
print(ser.head())

# Solution
pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1],
        labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']).head()
#qcut=istediğimiz sekilde ayırma yapar
"""
"""
12. Bir numpy dizisini verilen şekle sahip bir veri çerçevesine nasıl dönüştürebilirim?
Ser serisini 7 satır ve 5 sütun içeren bir veri çerçevesi olarak yeniden şekillendir
"""
"""
ser = pd.Series(np.random.randint(1, 10, 35))

# Solution
df = pd.DataFrame(ser.values.reshape(7,5))
print(df)
"""

"""
-------------------calısmadı anlamadım bak-----------------
13. Bir seriden 3'ün katı olan sayıların konumları nasıl bulunur?
3'ün katları olan sayıların konumlarını bulun ser.
"""
"""
ser = pd.Series(np.random.randint(1, 10, 7))
print(ser)
ser1=np.random.randint(1,10,7)
print(np.where(ser % 3==0)[0].tolist())
"""
"""
14. Bir seriden belirli konumlardaki öğeler nasıl çıkarılır
Gönderen ser, listedeki pozisyonlarda öğeleri ayıklamak pos.
"""
"""
ser=pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
#print(ser[pos])
print(ser.take(pos))
"""

"""
15. İki seri dikey ve yatay olarak nasıl istiflenir?
Ser1 ve ser2'yi dikey ve yatay olarak yığınlayın (bir veri çerçevesi oluşturmak için).
"""
"""
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
df = pd.concat([ser1, ser2], axis=1)
#df1 = pd.concat([ser1, ser2], axis=0)
#print(df1)
ser1.append(ser2)# olmuyor anlamadım bak
print(ser1)
print(df)
"""
"""
16. Başka bir B serisindeki A serisinin öğelerinin pozisyonları nasıl alınır?
Öğeleri konumlarını alın ser2içinde ser1bir liste olarak.
"""
"""
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])
out=[np.where(i == ser1)[0].tolist()[0] for i in ser2]
#out=[pd.Index(ser1).get_loc(i) for i in ser2]
print(out)
"""

"""
17. Bir gerçek ve tahmin edilen serideki ortalama hata karesi nasıl hesaplanır?
Ortalama kare hatası truth ve pred seriyi hesaplayın
"""
"""
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
print(np.mean((truth-pred)**2))
"""
"""
18. Bir serideki her elemanın ilk karakteri büyük harfe nasıl dönüştürülür?
Her kelimenin ilk karakterini büyük harf olarak değiştirin ser.
"""
"""
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
#print(ser.map(lambda x: x.title()))
#pd.Series([i.title() for i in ser])
ser1=ser.map(lambda x: x[0].upper()+x[1:] )
print(ser1)
"""
"""
19. Bir serideki her kelimedeki karakter sayısı nasıl hesaplanır?
"""
"""
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
print(ser.map(lambda x: len(x)))
"""
"""
20. Bir serinin ardışık sayıları arasındaki farkların farkı nasıl hesaplanır?
Ardışık sayılar arasındaki farkların farkı ser.
"""
"""
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
print(ser.diff().tolist())
print(ser.diff().diff().tolist())
"""

"""
21. Bir dizi tarih dizisini bir zaman serisine nasıl dönüştürebilirim?
"""
"""
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

from dateutil.parser import parse
print(ser.map(lambda x: parse(x)))

# Solution 2
print(pd.to_datetime(ser))
"""
"""

------------------- anlamadım bak  gunun adları calısmadı---------------
22. Bir dizi tarih dizisinden ayın günü, hafta numarası, yılın günü ve haftanın günü nasıl alınır?
Ayın gününü, hafta numarasını, yılın gününü ve haftanın gününü alın ser
"""
"""
from dateutil.parser import parse
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

ser_ts = ser.map(lambda x: parse(x))

# day of month
print("Date: ", ser_ts.dt.day.tolist())

# week number
print("Week number: ", ser_ts.dt.weekofyear.tolist())

# day of year
print("Day number of year: ", ser_ts.dt.dayofyear.tolist())

# day of week
print("Day of week: ", ser_ts.dt.day_name.tolist())
"""
"""
23. Yıl-ay dizgisi ayın 4. gününe karşılık gelen tarihlere nasıl dönüştürülür?
Değişim ser, ilgili ay sonu 4 ile başlayan tarihlere.
"""
"""
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
# Solution 1
from dateutil.parser import parse
# Parse the date
ser_ts = ser.map(lambda x: parse(x))

# Construct date string with date as 4
ser_datestr = ser_ts.dt.year.astype('str') + '-' + ser_ts.dt.month.astype('str') + '-' + '04'

# Format it.
print([parse(i).strftime('%Y-%m-%d') for i in ser_datestr])

# Solution 2
print(ser.map(lambda x: parse('04 ' + x)))
"""
"""
24. Bir diziden en az 2 ünlü içeren sözcükler nasıl filtrelenir?
En ser az 2 sesli harf içeren kelimeleri çıkarın.
"""
"""
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
from collections import Counter
mask = ser.map(lambda x: sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
print(ser[mask])
"""
"""
25. Bir seriden geçerli e-postalar nasıl filtrelenir?
Seriden geçerli e-postaları çıkarın emails. Geçerli e-postalar için normal ifade
kalıbı referans olarak sağlanır.

(RE) , bir arama modelini açıklamak için kullanılan özel bir metin dizesidir.
re.match () işlevi normal ifade modelini arayacak ve ilk geçtiği yeri döndürecektir.
findall (), dosyanın tüm satırlarını yineler ve örtüşmeyen tüm model eşleşmelerini tek bir adımda döndürür.
"""
"""
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])

# Solution 1 (as series of strings)
import re
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
print(emails[mask])

# Solution 2 (as series of list)
emails.str.findall(pattern, flags=re.IGNORECASE)

# Solution 3 (as list)
y=[x[0] for x in [re.findall(pattern, email) for email in emails] if len(x) > 0]
print(y)
"""
"""
26. Başka bir seriye göre gruplandırılmış bir serinin ortalaması nasıl alınır?
weights Her birinin ortalamasını hesaplayın fruit.
"""
"""
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print(weights.tolist())
print(fruit.tolist())


# Solution
print(weights.groupby(fruit).mean())
"""
"""
27. İki seri arasındaki öklid mesafesi nasıl hesaplanır?
Paketlenmiş bir formül kullanmadan, p ve q serileri (noktaları) arasındaki öklid mesafesini hesaplayın .
"""
"""
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Solution
print(sum((p - q)**2)**.5)

# Solution (using func)
print(np.linalg.norm(p-q))
"""
"""
28. Sayısal bir serideki tüm yerel maksimumları (veya zirveleri) nasıl bulabilirim?
Tepe noktalarının konumlarını (her iki tarafta daha küçük değerlerle çevrili değerler) alın ser.
"""
"""
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])

# Solution
dd = np.diff(np.sign(np.diff(ser)))
peak_locs = np.where(dd == -2)[0] + 1
print(peak_locs)
"""

"""
29. Bir dizedeki eksik boşlukları en az sıklıkta olan karakterle nasıl değiştirebilirim?
İçindeki boşlukları my_stren az kullanılan karakterle değiştirin.
"""
"""
my_str = 'dbc deb abed gade'

# Solution
ser = pd.Series(list('dbc deb abed gade'))
freq = ser.value_counts()
print(freq)
least_freq = freq.dropna().index[-1]
"".join(ser.replace(' ', least_freq))
print(least_freq)
"""
"""
30. '2000-01-01' den başlayarak ve 10 hafta sonundan (cumartesi) sonra rasgele sayıların
değer olarak alındığı bir TimeSeries nasıl oluşturulur?
"""
"""
ser = pd.Series(np.random.randint(1,10,10), pd.date_range('2000-01-01', periods=10, freq='W-SAT'))
print(ser)
"""
"""
31. Tüm eksik tarihlerin bir önceki eksik olmayan tarihin değerleriyle görünmesi için aralıklı bir
zaman serisi nasıl doldurulur?
sertarihler ve değerler eksik. Tüm eksik tarihlerin görünmesini sağlayın ve önceki tarihin 
değeriyle doldurun.
"""
ser = pd.Series([1,10,3, np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))

# Solution
ser.resample('D').ffill()  # fill with previous value

# Alternatives
ser.resample('D').bfill()  # fill with next value
ser.resample('D').bfill().ffill()  # fill next else prev value












