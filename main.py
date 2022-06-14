offset = int(input("offset giriniz: ")) # burada kullanıcı istediği offset yazacak
girilenKeliem = input("şifrelemk istediğiniz  kelime giriniz: ") # burada kullanıcı şifrelemek istediği kelime yazacak 


turkish_letters=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t",
            "u","ü","v","y","z"] # turkçe harfleri bir liste icinde tanımlanmış 

sifreli=[]  
indexes=[] 
for i in girilenKeliem: # burada girlen kelime for icinde yaziliyor
    indexes.append(turkish_letters.index(i)) 
#####################################################################

indexArtı=[]
for i in range(len(indexes)):
    x=0
    x = indexes[i]+offset
    x = x % 29
    indexArtı.append(x)

print(indexes)
# burada kelime alip girilen offset artirmak ve modun almak icin bir for dongu olusturduk 
################################################
print(indexArtı)
liste=[]
for i in indexArtı:
    liste.append(turkish_letters[i])
print(liste)
sifrelikelime=""
for i in liste:
    sifrelikelime+=i
print(sifrelikelime)

#burada yeni bir sifreli kelime oluşturduk
################################################
text = input("cozmak istediginiz sifreli kelime giriniz")  
text =list(text)
# burada kullanici çözümk istediği sifreli kelime yazacak ve bir listeye eklenecek

wordslist=[] # burada gelen kelimler için boş bir list; dizi oluşturduk

for i in range(1,30):
    word=""
    for j in text:
        harfIndis= turkish_letters.index(j)
        harfIndis += i    
        harf=turkish_letters[harfIndis%29]
        word += harf
    wordslist.append(word)
  # burada gelen kelime 29 aralığında olduğun bir for döngüsü yazdık ve onu bir listeye ekledik
##########################################

dosya = open("tdk.txt","r",encoding="UTF-8")
liste= dosya.readlines()
# burada turkce kutuphane dosyasi yukladik ve tanimlandik

kelimeler_dizisi=[]
for i in range(len(liste)-1):
    kelime=""
    kelime=liste[i].strip()
    kelimeler_dizisi.append(kelime)

print("")
print("Şifreli text", text)

#########################################

for i in range(len(wordslist)-1): 
    for j in range(len(kelimeler_dizisi)-1):
        if (wordslist[i]==kelimeler_dizisi[j]):
            print(kelimeler_dizisi[j])
            offset=wordslist.index(wordslist[i])+1
            print( "Şifreinin  offseti =", offset ) # burada kelime nerede bulundugu yazacak 
            #ve offsetini ne oldu yazacak    
print("****")
#############################################

reasult=[]
for i in text:
    reasult.append(turkish_letters[(turkish_letters.index(i)+offset) %29]) # burada textten gelen sifreli kelime offset yukladik ve modun aldik
cozulenkelime=""
for i in reasult:
    cozulenkelime+=i   

print(reasult) 
print(cozulenkelime)
# burada cozulumus siferli kelime yaziyoruz 
############################################




