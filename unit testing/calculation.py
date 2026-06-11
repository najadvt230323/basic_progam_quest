def add(a,b):
    return(a+b)

def rev(a):
    return a[::-1]

def revint(a):
    a=str(a)
    return int(a[::-1])

def revnevint(a):
    if a<0:
        a=str(a)
        b=a[1:]
        c="-"+ b[::-1]
        return int(c)
    else:
        a=str(a)
        return int(a[::-1])    

    
