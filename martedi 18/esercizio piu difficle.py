x= int(input("scegli numero"))

if(x==9):
    print("livello superato")
    y= int(input("scegli numero"))
    if(y<9):
        print("livello superato")
        z= int(input("seleziona numero"))    
        if(z>9):
            print("livello superato")
        else:
            print("livello non superato")
    else:
       print ("livello non superato")
else:
    print("livello non superato")


    