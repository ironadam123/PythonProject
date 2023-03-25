print("bir işlem türü seçiniz")
print("carpma","bölme","toplama","çıkarma","üst_alma")
a = input()





def carpma():
    a = int(input("1.sayıyı giriniz"))
    b = int(input("2.sayıyı giriniz"))
    print(a*b)
def bölme():
    a = int(input("1.sayıyı giriniz"))
    b = int(input("2.sayıyı giriniz"))
    print(a/b)
def toplama():
    a = int(input("1.sayıyı giriniz"))
    b = int(input("2.sayıyı giriniz"))
    print(a+b)

def çıkarma():
    a = int(input("1.sayıyı giriniz"))
    b = int(input("2.sayıyı giriniz"))
    print(a-b)



if a == "carpma":
    carpma()
if a == "toplama":
    toplama()
if a == "bölme":
    bölme()
if a == "çıkarma":
    çıkarma()

