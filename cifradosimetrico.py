
def vector(bi): ### recibe arreglo con los caracteres representados numericamente
    size=len(bi)
    
    v1=bi[size-1]  ### se toma el ultimo valor
    v2=bi[int(size/2)+1] ### se toma el valor de en medio + 1 (arbitrario)
    r= (v1^v2)|(v1&v2) # operacion logica que genera el vector
    return int(r) # se retorna el vector de inicializacion como un numero entero

def cifrar(st,key):  ## se reciben los dos strings, el texto a cifrar y la llave
    asci=[]
    tocf=[]
    sk=[]
    xor=[]
    r=''
    for item in st:
        asci.append(int(ord(item))) # se transforma cada caracter del texto a cifrar en su valor numerico 
     
    
    
    sizek=len(key)
    

    for item in key:
        sk.append(int(ord(item)))
    iv=vector(sk)   ## se genera el vector de inicializacion a partir de la llave
    for item in asci: 
        some=item^iv   ## se realiza la operacion logica xor entre el vector y los valores a cifrar
        tocf.append(some) 
    if len(sk) < len(tocf):
        lim=len(tocf)-len(sk)
        for i in range(0,lim):
            sk.append(lim)

        for i in range(0,len(sk)): ### en estos if se genera el cifrado mediante la operacion logica XOR
            xo=sk[i]^tocf[i]
            r=r+chr(xo)
    elif len(sk)>len(tocf):
        for i in range(0,len(tocf)):
            xor=sk[i]^tocf[i]
            r=r+chr(xor)
    else:
        for i in range(0,len(tocf)):
            shift2=(sk[i]^tocf[i])
            r=r+chr(shift2)
    return r

def decifrar(st,key):
    asci=[]
    tocf=[]
    sk=[]
    xor=[]
    r=''
    for item in st:
        asci.append(int(ord(item))) # se transforma cada caracter del texto a cifrar en su valor numerico 
     
    
    sizek=len(key)
    
    for item in key:
        sk.append(int(ord(item)))
    iv=vector(sk)       ## se genera el vector de inicializacion a partir del texto a cifra
    if len(sk) < len(asci):
        lim=len(asci)-len(sk)
        for i in range(0,lim):
            sk.append(lim)   ### se genera el decifrado haciendo XOR entre el texto cifrado y la llave
        for i in range(0,len(asci)):
            xor.append(sk[i]^asci[i])
            
           
           
    else:
        for i in range(0,len(asci)):
            xor.append(sk[i]^asci[i])
            
    for item in xor:
        f=item^iv                #se genera el decifrado utilizando el vector de inicializacion
        r=r+chr(f)

    
    return r

a=input("ingresa pass\n")
b=input("ingresa key\n")
print(cifrar(a,b))
c=input("ingresa cifrado\n")
d=input("ingresa key\n")
print(decifrar(c,d))