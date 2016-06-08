import string
def CeaserCipher(b):
    a=list(string.ascii_lowercase)
    e=[]
    for x in range(0,len(b)):
        if b[x]!=string.ascii_lowercase:
            e.append(b[x])
        else:
            c=b[x]
            d=a.index(c)+13
            if d>25:
                d=d-26
                e.append(a[d])
            else:
                e.append(a[d])
    f=''
    f+=str(e)
    print (f)
def AffineCipher(b,k1,k2):
    a=list(string.ascii_lowercase)
    x=y=0.0
    e=[]
    for i in range(0,len(b)):
        c=b[i]
        d=a.index(c)+13
        if d>25:
            d=d-26
            e.append(a[d])
        else:
            e.append(a[d])
    print(e)
print("Enter Secret Code: ")
b=list(input())
CeaserCipher(b)