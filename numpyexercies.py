import numpy as np
import pandas as pd

"""
0'dan 9'a kadar 1 boyutlu bir sayı dizisi oluşturun
"""
"""
li=np.arange(10)
print(li)
"""
"""
tüm True'ların 3x3 uyuşmuş bir dizisini oluşturun.
"""
"""
arr=np.full((3, 3), True, dtype=bool)
print(arr)
"""
"""
 Belirli bir koşulu karşılayan öğeler 1B dizisinden nasıl çıkarılır?
 Tüm tek sayıları çıkarın. 
"""
"""
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr=arr[arr%2==1]
print(arr)
"""
"""
Bir koşulu karşılayan öğeler numpy dizisindeki başka bir değerle nasıl değiştirilir?
tüm tek sayıları arr-1 ile değiştirin
"""
"""
arr=np.array([0,1,2,3,4,5,6,7,8,9])
arr[arr % 2 == 1] = -1
print(arr)
"""
"""
Orijinal diziyi etkilemeden bir koşulu karşılayan öğeler nasıl değiştirilir?
 Sıradaki tüm tek sayıları değiştirmeden -1 ile değiştirin
"""
"""
arr=np.array([0,1,2,3,4,5,6,7,8,9])
solve=np.where(arr%2==1,-1,arr)#where(kosul,dogrusa yapılacakolan,yanlıssa yapılacak olan)
print(solve)
"""
"""
Bir dizi nasıl yeniden şekillendirilir
1 boyutlu bir diziyi 2 satırlı 2 boyutlu bir diziye dönüştürün
"""
"""
arr=np.arange(10)
newarr=arr.reshape(2,-1)#-1 olarak ayarlamak, sütun sayısına otomatik olarak karar verir
print(newarr)
"""
"""
İki dizi dikey olarak nasıl istiflenir
Yığın diziler a ve b  dikey
"""
"""
a=np.arange(10).reshape(2,-1)
b=np.repeat(1,10).reshape(2,-1)
print("a")
print(+a)
print("b")
print(+b)
newarr=np.vstack([a,b])
print(newarr)
"""
"""
İki dizi yatay olarak nasıl istiflenir
Yığın diziler ave byatay.
"""
"""
a=np.arange(10).reshape(2,-1)
b=np.repeat(2,10).reshape(2,-1)
print("a")
print(a)
print("b")
print(b)
newar=np.hstack([a,b])
print(newar)
"""
"""
Kodlama yapmadan numpy ile özel diziler nasıl oluşturulur?
Kodlama yapmadan aşağıdaki kalıbı oluşturun. Yalnızca numpy işlevlerini ve aşağıdaki girdi dizisini kullanın
"""
"""
a=np.array([1,2,3])
newarr=np.r_[np.repeat(a, 3), np.tile(a, 3)]#r_ [a,b] a ve b dızısını bırleştirir np.tile repeatle aynı
print(newarr)
"""
"""
İki python numpy dizisi arasındaki ortak öğeler nasıl elde edilir?
a ve b arasındaki ortak öğeleri alın
"""
"""
a=np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a,b))# intersect1d==iki dizideki ortak elemanlar
"""
"""
Bir diziden diğerinde bulunan öğeler nasıl kaldırılır?
a  dizide b bulunan tüm öğeleri kaldır
"""
"""
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print(np.setdiff1d(a,b))# setdiff1d== ortak elemanların a da olanları siler ve yeni a dondurur
"""
"""
İki dizinin elemanlarının eşleştiği konumlar nası elde edilir?
Öğelerin eşleştiği a ve b eşleştiği konumları alın
"""
"""
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.where(a==b))
"""
"""
Bir numpy dizisinden verilen bir aralık arasındaki tüm sayılar nasıl çıkarılır?
5 ile 10 arasındaki tüm öğeleri şuradan alın 
"""
"""
a = np.array([2, 6, 1, 9, 10, 3, 27])
print(np.where(np.logical_and((5<=a ),(a<=10 ))))
print(np.where((a>=5) & (a<=10)))# logical_and(kosul1,kosul2)ifin ve li hali
print(a[(a>=5) & (a<=10)])
"""
"""
Numpy diziler üzerinde çalışmak için skalarları işleyen bir python işlevi nasıl yapılır?
maxxİki skaler üzerinde çalışan işlevi iki dizi üzerinde çalışacak şekilde dönüştürün 
"""
"""

def maxx(x,y):
    if x>y:
        return x
    else:
        return y
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
newarr=np.vectorize(maxx, otypes=[float])#maxx fonk kullanan ve dönüş tipi float olan bir fonk uretir.
print(newarr(a,b))
"""
"""
2d numpy dizisindeki iki sütun nasıl değiştirilir?
Dizideki 1. ve 2. sütunları değiştirin
[   [0,1,2]               [   [1,0,2]
    [3,4,5]       =           [4,3,5]
    [6,7,8]  ]                [7,6,8]   ]
"""
"""
arr=np.arange(9).reshape(3,3)
print(arr)
newar=arr[:, [1,0,2]] #if koşulu :=satırların hep,[1 0 2 ] indislerin yeni yerleri
print("dondü")
print(newar)
"""
"""
 ---------------------- slicing calısmaa------------------
"""
"""
arr=np.array([[0,1,2,3],
              [4,5,6,8],
              [9,10,11,12]])
print(arr[1,:])
print(arr[(1,2),:])
print(arr[1:,2])
print(arr[:,1:2]) ##ilk parametre sutun ikinci satıra bakıyor
a = np.array([0, 2, 4, 6, 8, 10, 12,14,16,18])
a[:9:3]=50
print(a)
np.random.seed(2)
print(np.random.randint(10))
np.random.seed(1)
print(np.random.randint(10))
"""
"""
2d numpy dizisindeki iki sütun nasıl değiştirilir?
Dizideki 1. ve 2. satırları değiştirin
"""
"""
arr=np.arange(9).reshape(3,3)
a=arr[[2,1,0],:]
print(arr)
print()
print(a)
"""
"""
19. 2B dizinin sütunları nasıl tersine çevrilir?
2D dizinin sütunlarını ters çevirin 
"""
"""
arr=np.arange(9).reshape(3,3)
print(arr)
print()
a=arr[:,[2,1,0]]
print(a)
"""
"""
20. 5 ile 10 arasında rastgele kayan sayılar içeren bir 2D dizisi nasıl oluşturulur?
5 ile 10 arasında rastgele ondalık sayılar içeren 2B 5x3 şeklinde bir dizi oluşturun.
"""
"""
rand_arr = np.random.uniform(5,10, size=(5,3))# sınır vermeyı saglar
print(rand_arr)
"""
"""
21. Python numpy dizisinde sadece 3 ondalık basamak nasıl yazdırılır?
 """
"""
arr=np.random.random(size=(5,3)) #0-1 arası rand sayı
print(arr)
print()
np.set_printoptions(precision=3)
print(arr)
a=np.random.random(size=(5,3)) #0-1 arası rand sayı
print(a[:4])
"""
"""
22. Bilimsel gösterimi (1e10 gibi) bastırarak uyuşmuş bir dizi nasıl yazdırılır?
girişi bu sekilde göterilen (1e10 gibi)cıkısı normal ondalık yapan 
"""
"""
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)
np.set_printoptions(suppress=True, precision=6)
print()
print(rand_arr)
"""
"""
23. numpy dizisinin çıktısında yazdırılan öğelerin sayısı nasıl sınırlandırılır?
[1,2,3,4,5,6,7] --girdi
[1,2,,....,6,7]---cıktı
"""
"""
np.set_printoptions(threshold=6)
a = np.arange(15)
print(a)
"""
"""
----------calışmıyor anlamadım bak ------------------
Tam numpy dizisi kesmeden nasıl yazdırılır
[1,2,.....,6,7]----girdi
[1,2,3,4,5,6,7]---cıktı
"""
"""
np.set_printoptions(threshold=6)
a = np.arange(15)

# Solution
np.set_printoptions(threshold=np.nan)
print(a)
"""
"""
25. Metni python numpy ile olduğu gibi koruyarak sayılar ve metinler içeren bir veri 
seti nasıl içe aktarılır?
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

# Print the first 3 rows
print(iris)
"""
"""
26. Belirli bir sütun 1B dizilimden nasıl çıkarılır?
Metin sütununu önceki soruda içe aktarılan species 1B'den çıkarın iris.
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(iris.shape) #veri seti elaman sayısı
species=np.array(iris[:,-1])
print(species[:5])
#species=np.array([i[4]for i in iris])## iris setindeki 4 sutunu alır
"""
"""
27. 1d'lik bir tuple dizisini 2d numpy dizisine nasıl dönüştürebilirim?
Metin alanını atlayarak 1D'yi iris2D dizisine dönüştürün
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
newiris=np.array(iris[:,:4])
#iris_2d = np.array([row.tolist()[:4] for row in iris])  print(iris_2d[:4])
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3]) # bunu kullan
print(newiris[:4])
"""
"""
28.Uyuşuk bir dizinin ortalama, medyan, standart sapması nasıl hesaplanır?
İrisin ortalama, medyan ve standart sapmasını bulun sepallength(1. sütun)
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris=np.genfromtxt(url,delimiter=',',dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
#sepallength=np.array(iris[:,:1])
print(sepallength.mean())
print(sepallength.std())
print(np.median(sepallength))
"""
"""
29. Değerler tam olarak 0 ile 1 arasında olacak şekilde bir dizi nasıl normalleştirilir?
 normalleştirilmiş bir form oluşturmak irisVar sepallengtholan değerler en küçük değeri 
 0 ve maksimum 1 değerine sahip tam olarak 0 ile 1 arasında, böylece değişir.

 bir değerin normalleşmesi===(sepallength - Smin)/(Smax - Smin)
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
S = (sepallength - sepallength.min())/(sepallength.max() - sepallength.min())
print(S)
"""
"""
 30.softmax puanı nasıl hesaplanır?
 sepallength. sutununa göre

 def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)
print(softmax(sepallength))
"""

"""
31. Uyuşuk bir dizinin yüzdelik puanları nasıl bulunur?
İrisin 5. ve 95. yüzdelik dilimini bulun sepallength
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

# Solution
print(np.percentile(sepallength, q=[5, 95]))
"""
"""
32. Bir dizide rastgele konumlara değerler nasıl eklenir?
 Veri kümesine 20 rastgele konumdaki değerleri girinnp.naniris_2d
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')

i, j = np.where(iris_2d)

# i, j contain the row numbers and column numbers of 600 elements of iris_x
np.random.seed(100)
iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan
print(iris_2d)
"""
"""
33. Numpy dizisindeki eksik değerlerin konumu nasıl bulunur?
Q. iris_2d's sepallength(1. sütun) ' da eksik değerlerin sayısını ve konumunu bulun
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float')
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
top= np.isnan(iris_2d[:,0]).sum()
arr=np.where( np.isnan(iris_2d[:,0])==True)
print(arr)

print(top)
"""
"""
34. İki veya daha fazla koşula göre bir uyuşmuş dizi nasıl filtrelenir?
Petall length (3. sütun)> 1.5 ve sepall length (1. sütun) <5.0 olan iris_2d 
satırlarını filtreleyin
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',',skip_header=1, dtype='float')
arr=np.where((iris_2d[:,2]>1.5) &( iris_2d[:,0]<5.0))
print(iris_2d[arr])
"""
"""
35. Eksik bir değer içeren satırlar bir numpy dizisinden nasıl çıkarılır?
Herhangi bir nan değeri olmayan iris_2d satırlarını seçin .
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',',skip_header=1, dtype='float', usecols=[0,1,2,3])
#arr= np.where(~np.any(np.isnan(iris_2d[:])))--- >yanlış
arr=np.array([~np.any(np.isnan(row)) for row in iris_2d])
print(iris_2d[arr][:5])
"""

"""
36. Uyuşuk bir dizinin iki sütunu arasındaki korelasyon nasıl bulunur?
iris_2d'de SepalLength (1. sütun) ile PetalLength (3. sütun) arasındaki korelasyonu bulun
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',',skip_header=1, dtype='float', usecols=[0,1,2,3])

print(np.corrcoef(iris_2d[:,0],iris_2d[:,2])[0,1])

"""

"""
37. Belirli bir dizinin herhangi bir boş değeri olup olmadığını nasıl öğrenebilirim?
iris_2dEksik değerler olup olmadığını öğrenin
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',',skip_header=1, dtype='float')

print(np.isinf(iris_2d).any())

"""

"""
38. Bir numpy dizisindeki tüm eksik değerler 0 ile nasıl değiştirilir?
nannumpy dizisindeki tüm şifreleri 0 ile değiştirin
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',',skip_header=1, dtype='float')
iris_2d[np.where(np.isnan(iris_2d))]=0
print(iris_2d[:5])
"""

"""
39. Uyuşuk bir dizideki benzersiz değerlerin sayısı nasıl bulunur?
iris'teki benzersiz değerleri ve benzersiz değerlerin sayısını bulun. species
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',',skip_header=1, dtype='float')
print(np.unique(iris_2d[:,4]))
print("sayısı")
print(np.unique(iris_2d[:,4],return_counts=True))

"""
"""
---------------anlamadım bak---------------------
40. Bir sayısal diziyi kategorik (metin) diziye nasıl dönüştürebilirim?
iris_2d'nin petal uzunluğu (3.) sütununu bir metin dizisi oluşturmak için bölüntüleyin,
 örneğin petal uzunluğu:

3'ten küçük -> 'küçük'
3-5 -> 'orta'
'> = 5 ->' büyük '
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',',skip_header=1, dtype='float')
arr=np.where((iris_2d[:,2]<3,'küçük')|(3<iris_2d[:,2]<5,'orta')| (iris_2d[:,2]>=5,'büyük'))
print(arr)
print()
print(iris_2d[arr])
#-----------------asıl cözum
# Bin petallength 
petal_length_bin = np.digitize(iris_2d[:, 2].astype('float'), [0, 3, 5, 10])

# Map it to respective category
label_map = {1: 'small', 2: 'medium', 3: 'large', 4: np.nan}
petal_length_cat = [label_map[x] for x in petal_length_bin]

# View
petal_length_cat[:4]
#> ['small', 'small', 'small', 'small']

"""

"""
41. Bir numpy dizisinin mevcut sütunlarından yeni bir sütun nasıl oluşturulur?
iris_2d'deki birim için yeni bir sütun oluşturun, burada hacim (pi x petallength
 x sepal_length^2)/3
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',',skip_header=1, dtype='float')
sepal=iris_2d[:,0].astype('float')
petal=iris_2d[:,2].astype('float')
newir=(np.pi*petal*(sepal**2))/3
newir=newir[:,np.newaxis]
print(np.hstack([iris_2d,newir]))
"""

"""
-------------anlamadım bak
42. Uyuşuklukta olasılıklı örnekleme nasıl yapılır?
 İris türlerini, setoz, versicolor ve virginica
  sayısının iki katı olacak şekilde rastgele örnekleyin.
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
species = iris[:, 4]

np.random.seed(100)
a = np.array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
species_out = np.random.choice(a, 150, p=[0.5, 0.25, 0.25])


np.random.seed(100)
probs = np.r_[np.linspace(0, 0.500, num=50), np.linspace(0.501, .750, num=50), np.linspace(.751, 1.0, num=50)]
index = np.searchsorted(probs, np.random.random(150))
species_out = species[index]
print(np.unique(species_out, return_counts=True))
"""

"""
43. Başka bir dizi ile gruplandığında bir dizinin ikinci en büyük değeri nasıl
elde edilir?
 İkinci en uzun petallength türün değeri nedir? setosa
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
petalmax=iris[iris[:, 4] == b'Iris-setosa', [2]].astype('float')
print(np.unique(np.sort(petalmax))[-2])
"""
"""
44. 2B bir diziyi bir sütuna göre sıralama
İris veri kümesini sepallength sütuna göre sıralayın .
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
arr=iris[:,0].argsort()
print(arr)
"""
"""
45. Uyuşuk bir dizide en sık görülen değer nasıl bulunur?
Iris veri kümesinde petal uzunluğunun (3. sütun) en sık değerini bulun.
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
deger,count=np.unique(iris[:,2],return_counts=True)
print(deger[np.argsort(count)[-1]])
"""
"""
46. ​​Verilen bir değerden daha büyük bir değerin ilk ortaya çıkışının konumu nasıl bulunur?
 Iris veri kümesinin petalwidth 4. sütununda 1.0'dan büyük bir değerin ilk geçtiği' \
' yerin konumunu bulun.

"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print(np.argwhere(iris[:,3].astype('float')>1.0)[0])

"""

"""
47. Belirli bir değerden büyük olan tüm değerler belirli bir kesme değerine nasıl değiştirilir?
Diziden a30'dan 30'a ve 10'dan 10'a kadar olan tüm değerleri değiştirin
"""
"""
import random
np.random.seed(100)
a=np.random.uniform(1,50,20)
print(a)
print()
a[np.where(a<10)]=1
a[np.where((10<a)&(a<30))]=2
a[np.where(a>10)]=3

# print(np.where(a < 10, 10, np.where(a > 30, 30, a)))
print(a)
"""
"""
48. n numpy bir diziden en yüksek değerlerin konumları nasıl elde edilir ?
Belirli bir dizideki ilk 5 maksimum değerin konumlarını alın a.
"""
"""
import random
np.random.seed(101)
a=np.random.randint(1,50,20)
print(a)
print()
print(a.argsort()[15:20][::-1])
print()
print(np.sort(a)[-5:])# degerler
"""
"""
49. Bir dizideki tüm olası değerlerin satır bazında sayıları nasıl hesaplanır?
Benzersiz değerlerin sayısını satır bazında hesaplayın.
"""
"""
np.random.seed(102)
arr = np.random.randint(1,11,size=(6, 10))
def coutdo(arr1):
    cout=[np.unique(row,return_counts=True )for row in arr1]
    return([[int(b[a==i]) if i in a else 0 for i in np.unique(arr1)] for a, b in cout])


print(coutdo(arr))

"""
"""
50. Bir dizi dizisi düz bir 1d dizisine nasıl dönüştürülür?
array_of_arraysDüz bir doğrusal 1d dizisine dönüştürün 
"""
"""
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)

array_of_arrays = np.array([arr1, arr2, arr3],dtype='object')
print('array_of_arrays: ', array_of_arrays)
a=np.concatenate([arr1,arr2,arr3],axis=0)
b=np.hstack([arr1,arr2,arr3])
c=np.r_[arr1,arr2,arr3]
d=[i for arr in array_of_arrays for i in arr]
print(a)
print()
print(b)
print()
print(c)
print()
print(d)
arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)

array_of_arrays = np.array([arr1, arr2, arr3],dtype='object')
print('array_of_arrays: ', array_of_arrays)

# Solution 1
arr_2d = np.array([a for arr in array_of_arrays for a in arr])

# Solution 2:
arr_2d = np.concatenate(array_of_arrays,axis=0)
print(arr_2d)

"""
"""
51. numpy'deki bir dizi için tek sıcak kodlamalar nasıl oluşturulur?
Tek sıcak kodlamaları hesaplayın (dizideki her benzersiz değer için kukla ikili değişkenler)
"""
"""
np.random.seed(101)
arr=np.random.randint(1,4,size=6)
print(arr)
def fonk1(arr):
    un=np.unique(arr)
    out=np.zeros((arr.shape[0],un.shape[0]))
    for i,j in enumerate(arr):
        out[i,(j-1)]=1
    return out
print(fonk1(arr))
"""
"""
Kategorik bir değişkenle gruplanmış satır numaraları nasıl oluşturulur?
Kategorik bir değişkenle gruplanmış satır numaraları oluşturun. Aşağıdaki örneği iris species giriş olarak kullanın .
metinsel ifadeleri sayısala donuturme
"""

"""
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris=np.genfromtxt(url,delimiter=',',dtype='object',usecols=4)
species=np.sort(np.random.choice(iris, size=20))
print(species)
print([i for val in np.unique(species) for i, grp in enumerate(species[species==val])])
"""
"""
Belirli bir kategorik değişkene dayalı olarak nasıl tanımlı kimlikler oluşturulur?
Belirli bir kategorik değişkene göre grup kimlikleri oluşturun. Aşağıdaki örneği iris speciesgiriş olarak kullanın .
"""
"""
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)
species=np.sort(np.random.choice(iris,size=20))
print(species)

output = [np.argwhere(np.unique(species) == s).tolist()[0][0] for val in np.unique(species) for s in species[species==val]]
print(output)
"""

"""
54. numpy kullanarak bir dizideki öğeler nasıl sıralanır?
Verilen sayısal dizi için sıraları oluşturun a.
"""
"""
np.random.seed(10)
arr=np.random.randint(20,size=10)
print()
print(arr)
print()
print(np.argsort(arr).argsort())
"""
"""
55. numpy kullanarak çok boyutlu bir dizideki öğeler nasıl sıralanır?
Belirli bir sayısal diziyle aynı şekle sahip bir sıra dizisi oluşturun a.
"""
"""
np.random.seed(10)
arr=np.random.randint(20,size=[2,4])

print(arr.ravel().argsort().argsort().reshape(arr.shape))
"""
"""
56. Numpy 2d dizisinin her satırındaki maksimum değer nasıl bulunur?
 Verilen dizideki her satır için maksimum değeri hesaplayın.
"""
"""
np.random.seed(100)
arr=np.random.randint(1,10,size=[5,3])
print(arr)
print()
out=np.max(arr, axis=1)
print(out)
"""
"""
57. numpy bir dizi 2d için her satır için min-by-max nasıl hesaplanır?
Verilen 2d numpy dizisi için her satır için min-by-max hesaplayın.
"""
"""
np.random.seed(100)
arr=np.random.randint(1,10,size=[5,3])
print(arr)
print()
print(np.apply_along_axis(lambda x: np.min(x)/np.max(x),arr=arr,axis=1))
"""

"""
58. numpy bir dizide yinelenen kayıtlar nasıl bulunur?
 Verilen numpy dizide yinelenen girişleri (2. oluşumdan itibaren) bulun 
ve olarak işaretleyin True. İlk kez oluşanlar olmalıdır False.
"""
"""
np.random.seed(100)
a = np.random.randint(0, 5, 10)
print('Array: ', a)
out = np.full(a.shape[0], True)
unique_positions = np.unique(a, return_index=True)[1]
print(unique_positions)
print(np.unique(a, return_index=True))
out[unique_positions] = False
print(out)
"""

"""
59. Gruplanmış ortalamayı hissiz olarak nasıl bulabilirim?
2D numpy dizisinde kategorik bir sütunla gruplandırılmış sayısal bir sütunun ortalamasını bulun
"""
"""

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
numeric_column = iris[:, 1].astype('float')  # sepalwidth
grouping_column = iris[:, 4]  # species


# List comprehension version
[[group_val, numeric_column[grouping_column==group_val].mean()] for group_val in np.unique(grouping_column)]

# For Loop version
output = []
for group_val in np.unique(grouping_column):
    output.append([group_val, numeric_column[grouping_column==group_val].mean()])

print(output)
"""

"""
60. PIL görüntüsünü numpy dizisine nasıl dönüştürebilirim?
 Aşağıdaki URL'den görüntüyü içe aktarın ve bir numpy dizisine dönüştürün.
"""
"""
from io import BytesIO
from PIL import Image
import PIL, requests

# Import image from URL
URL = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response = requests.get(URL)

# Read it as Image
I = Image.open(BytesIO(response.content))

# Optionally resize
I = I.resize([150,150])

# Convert to numpy array
arr = np.asarray(I)
# Optionaly Convert it back to an image and show
im = PIL.Image.fromarray(np.uint8(arr))
Image.Image.show(im)

"""
"""
61. Bir uyuşmuş diziden tüm eksik değerler nasıl kaldırılır?
Tüm nan değerleri bir 1D numpy dizisinden çıkarın
"""
"""
arr=np.array([1,2,3,np.nan,5,6,7,np.nan])
arrnew=arr[~np.isnan(arr)]# ~koymak bunun dışındakileri belirtir
print(arrnew)
"""
"""
62. İki dizi arasındaki öklid mesafesi nasıl hesaplanır?
İki dizi arasındaki öklid mesafesini hesaplayın a ve b.
"""
"""
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8])
out =( np.linalg.norm(a-b))
print(out)
"""
"""
63. Bir 1d dizisindeki tüm yerel maksimumları (veya zirveleri) nasıl bulabilirim?
 Bir 1B numpy dizideki tüm zirveleri bulun a. Tepeler, her iki tarafta daha küçük 
değerlerle çevrili noktalardır.
"""
"""
a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
doublediff = np.diff(np.sign(np.diff(a)))
peak_locations = np.where(doublediff == -2)[0] + 1
print(peak_locations)
"""
"""
64. Bir 2d dizisinden 1d dizisi nasıl çıkarılır, burada 1d dizisinin her bir öğesi ilgili satırdan çıkarılır?
1d dizisini b_1d2d dizisinden çıkarın a_2d, öyle ki her bir öğe, b_1dilgili satırdan çıkarır a_2d.
"""
"""
a_2d = np.array([[3,3,3],[4,4,4],[5,5,5]])
b_1d = np.array([1,2,3])

# Solution
print(a_2d - b_1d[:,None]) # none anlamadım bak sor
"""
"""
5. Bir dizideki bir öğenin n'inci tekrarının indeksi nasıl bulunur
1 numarasının 5. tekrarının dizinini bulun x.
"""
"""
x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n=5
out=[i for i,v in enumerate(x) if v==1]
print(out[n-1])
"""
"""
66. Numpy'nin datetime64 nesnesini datetime nesnesine nasıl dönüştürebilirim datetime?
Numpy'nin datetime64 nesnesini datetime'ın datetime nesnesine dönüştürün
"""
"""
dt64 = np.datetime64('2018-02-25 22:10:10')
dt=dt64.tolist()
#dt=dt64.astype('datetime')
print(dt)
"""
"""

--------- anlamadım bak -----------------
67. numpy bir dizinin hareketli ortalaması nasıl hesaplanır?
 Verilen 1D dizisi için pencere boyutu 3'ün hareketli ortalamasını hesaplayın.
"""
"""
np.random.seed(100)
arr=np.random.randint(10,size=10)
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

np.random.seed(100)
Z = np.random.randint(10, size=10)
print('array: ', Z)
# Method 1
moving_average(Z, n=3).round(2)

# Method 2:  # Thanks AlanLRH!
# np.ones(3)/3 gives equal weights. Use np.ones(4)/4 for window size 4.
np.convolve(Z, np.ones(3)/3, mode='valid') 


#> array:  [8 8 3 7 7 0 4 2 5 2]
#> moving average:  [ 6.33  6.    5.67  4.67  3.67  2.    3.67  3.  ]
"""
"""
68. Sadece başlangıç ​​noktası, uzunluk ve adım verilen bir numpy dizi dizisi nasıl oluşturulur?
 5'ten başlayarak ve ardışık sayılar arasında 3 adımı olan, 10 uzunluğunda bir uyuşmuş dizi oluşturun.
"""
"""
end = 5 + (3*10)
arr=np.arange(5,end,3)
print(arr)

#-------------
length = 10
start = 5
step = 3

def seq(start, length, step):
    end = start + (step*length)
    return np.arange(start, end, step)

seq(start, length, step)
"""

"""
69. Düzensiz bir numpy tarih dizisinde eksik tarihler nasıl doldurulur?
 Sürekli olmayan bir tarih dizisi verildiğinde. Eksik tarihleri ​​doldurarak 
bunu sürekli bir tarih dizisi haline getirin
"""
"""
arr = np.arange(np.datetime64('2018-02-01'), np.datetime64('2018-02-25'), 2)
print(arr)
filled_in = np.array([np.arange(date, (date+d)) for date, d in zip(arr, np.diff(arr))]).reshape(-1)

# add the last day
output = np.hstack([filled_in,   arr[-1]])


# For loop version -------
out = []
for date, d in zip(arr, np.diff(arr)):
    out.append(np.arange(date, (date+d)))

filled_in = np.array(out).reshape(-1)

# add the last day
output = np.hstack([filled_in, arr[-1]])
print(output)
"""

"""
-----------------anlamadım bakkk--------------
70. Belirli bir 1B dizisinden adımlar nasıl oluşturulur?
 Verilen 1d dizisinden arr, pencere uzunluğu 4 ve adım
2 olan adımlarla 2 boyutlu bir matris oluşturun, örneğin [[0,1,2,3], [2,3,4,5], [4 , 5,6,7] ..]
"""
"""
arr = np.arange(15)
def gen_strides(a, stride_len=5, window_len=5):
    n_strides = ((a.size-window_len)//stride_len) + 1
    # return np.array([a[s:(s+window_len)] for s in np.arange(0, a.size, stride_len)[:n_strides]])
    return np.array([a[s:(s+window_len)] for s in np.arange(0, n_strides*stride_len, stride_len)])

print(gen_strides(np.arange(15), stride_len=2, window_len=4))
"""

