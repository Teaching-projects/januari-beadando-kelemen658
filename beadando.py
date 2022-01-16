def korterulet(r):
    korterulet=r**2*3.14
    return korterulet

def korkerulet(r):
    korkerulet=2*r*3.14
    return korkerulet

def negyzetterulet(a):
    negyzetterulet=a**2
    return negyzetterulet

def negyzetkerulet(a):
    negyzetkerulet=a*4
    return negyzetkerulet

def teglalapterulet(a,b):
    teglalapterulet=a*b
    return teglalapterulet

def teglalapkerulet(a,b):
    teglalapkerulet=2*(a+b)
    return teglalapkerulet

def haromszogterulet(a,m):
    haromszogterulet=a*m/2
    return haromszogterulet

def derekszogut(a,b):
    derekszogut=a*b/2
    return derekszogut

def haromszogk(a,b,c):
    haromszogk=a+b+c
    return haromszogk

def egyenloszaruk(a,b):
    egyenloszaruk=a+2*b
    return egyenloszaruk

def egyenlooldaluk(a):
    egyenlooldaluk=3*a
    return egyenlooldaluk

alakzat=input("Adja meg mit szeretne számolni?pl.kor,negyzet,teglalap,haromszog:")
kt=input("Kerületet vagy Területet szeretne számolni:")

if alakzat=="kor" and kt=="terulet":
    r=int(input("Adja meg a kör sugarát:"))
    print(korterulet(r),"a kör területe.")

if alakzat=="kor" and kt=="kerulet":
    r=int(input("Adja meg a kör sugarát:"))
    print(korkerulet(r),"a kör kerülete.")

if alakzat=="negyzet" and kt=="terulet":
    a=int(input("Adja meg a négyzet oldalát:")) 
    print(negyzetterulet(a),"a négyzet területe.")

if alakzat=="negyzet" and kt=="kerulet":
    a=int(input("Adja meg a négyzet oldalát:"))
    print(negyzetkerulet(a),"a négyzet kerület")

if alakzat=="teglalap" and kt=="terulet":
    a=int(input("Adja meg a téglalap egyik oldalát:"))
    b=int(input("Adja meg a téglalap másik oldalát:"))
    print(teglalapterulet(a,b), "a téglalap területe.")

if alakzat=="teglalap" and kt=="kerulet":
    a=int(input("Adja meg a téglalap egyik oldalát:"))
    b=int(input("Adja meg a téglalap másik oldalát:"))
    print(teglalapkerulet(a,b),"a téglalap kerülete.")

if alakzat=="haromszog" and kt=="terulet":
    milyen=input("Milyen háromszögnek szeretné számolni a területét?(altalanos,egyenloszaru,egyenlo oldalu,derekszogu:)")
    if milyen=="altalanos" or "egyenloszaru" or "egyenlo oldalu":
        a=int(input("Adja meg a háromszög oldalát:"))
        m=int(input("Adja meg a háromszög magasságát:"))
        print(haromszogterulet(a,m),"a háromszög területe.")
    if milyen=="derekszogu":
        a=int(input("Adja meg a háromszög egyik oldalát:"))
        b=int(input("Adja meg a háromszög másik oldalát:"))
        print(derekszogut(a,b),"a háromszögterülete.")

if alakzat=="haromszog" and kt=="kerulet":
    milyen=input("Milyen háromszögnek szeretné számolni a kerületét?(altalanos,egyenloszaru,egyenlo oldalu,derekszogu:)")
    if milyen=="altalanos" or "derekszogu":
        a=int(input("Adja meg a háromszög a oldalát:"))
        b=int(input("Adja meg a háromszög b oldalát:"))
        c=int(input("Adja meg a háromszög c oldalát:"))
        print(haromszogk(a,b,c),"a háromszög kerülete.")
    if milyen=="egyenloszaru":
        a=int(input("Adja meg a háromszög egyik oldalát:"))
        b=int(input("Adja meg a háromszög másik oldalát:"))
        print(egyenloszaruk(a,b),"a háromszög kerülete.")
    if milyen=="egyenlo oldalu":
        a=int(input("Adja meg a háromszög oldalát"))
        print(egyenlooldaluk(a),"a háromszög kerülete.")
            
