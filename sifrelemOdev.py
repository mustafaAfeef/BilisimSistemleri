from mustafaafeefascii import anahtar_ascii


def replace_special_chars(txt):
    txt = txt.strip()
    dic = {" ": "_", "ğ": "g", "Ğ": "G", "ı": "i", "İ": "I", "ö": "o", "Ö": "O", "ü": "u", "Ü": "U", "ş": "s", "Ş": "S",
           "ç": "c", "Ç": "C"}
    t = txt.maketrans(dic)
    txt = txt.translate(t)
    return txt

#bu fonksyon da turkçe harfları yerini inglizce harfları getirmek için kullanarız 
########################################################################

def sifreleme():
    txt = replace_special_chars(input("Şifrelenecek metni girin: ")) 
    ascii_vals = [ord(char) for char in txt]
    #burda turkçe harfları kontrol edeck sonra ascii bir lıste olarak göndirecek aldığı liste ascii de ki değerleri alacak
    encrypted_chars = [] #bu boş listeye aktıracak
    for i in range(len(ascii_vals)):
        x = anahtar_ascii[i] + ascii_vals[i]
        mod = (x % 126) + 33  # burada aldığı değer modunu alıp 33 ekliyecek ascii de ki ilk 33 boş(sistmde yazılmayacak şeyler )olduğu için ekledik
        encrypted_chars.append(chr(mod))

    encrypted_text = "".join(encrypted_chars) 
    print('-------------------------')
    print("Result: ", encrypted_text)# bnrada Şifrelenmiş  metni çıkacak
    print('-------------------------')


#bu fanksyon da Şifreleme yapılacak 
#####################################################################

def cozuma():
    encrypted_text = input("Şifrelenmiş veriler girin: ")
    ascii_vals = [ord(char) for char in encrypted_text]
    

    decrypted_chars = []
    for y in range(len(ascii_vals)): 
        char = (ascii_vals[y] - 33) + (126 - anahtar_ascii[y])#burad işleme tam ters yapıyoruz şıfrlediği metin çözümak için
        decrypted_chars.append(chr(char)) #burda  ascii de ki değerleri alacak metin olarak göndirecek
        #
    decrypted_text = "".join(decrypted_chars)
    decrypted_text = decrypted_text.replace("_", " ") 

    print('-------------------------')
    print("Result: ", decrypted_text)# burada metin çözülanmış halı çıkacak
    print('-------------------------')


#########################################################################
def main():
    while True:
        print("1. Şifrelemek icin")
        print("2. Çözümak için ")
        print("3. çıkmak için")
        selection = input("Seçme: ")
        if selection == "1":
            ifreleme()
        elif selection == "2":
            cozuma()
        elif selection == "3":
            break
        else:
            print("Wrong selection....")
main()

# buarada ki fonksyon hangi işlem yapmak istediğimizde seçmek için kullanıyoruz

########################################################################


