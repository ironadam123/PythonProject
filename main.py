print("""***********************
faktötiriyel bulma programı
çıkmak için 'q'ya basın
***********************""")
while True:
    sayı =("sayı:")
    if(sayı =="q"):
        print("program sonlanyor")
        break
    else:
        sayı= int(sayı)
    faktöriyel = 1
    for i in range(2,+1):
        print("Faktöriyel",faktöriyel,"i:",i)
        faktöriyel *=i
    print("faktöriyel",faktöriyel)


