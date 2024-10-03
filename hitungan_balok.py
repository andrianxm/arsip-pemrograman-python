def luas_balok(p, l, t):
    '''Luas = 2*(p*l+p*t+l*t)'''
    luas = 2*(p*l + p*t + l*t)
    print("Luas = ",luas)

def keliling_balok(p, l, t):
    '''Keliling = 4(p+l+t)'''
    keliling = 4*(p + l + t)
    print("Keliling = ", keliling)

def volume_balok(p, l, t):
    '''Volume=p*l*t'''
    volume= p*l*t
    print("Volume = ",volume)

def input_balok():
    panjang = float(input("Masukkan panjang :"))
    lebar = float(input("Masukkan lebar :"))
    tinggi = float(input("Masukkan tinggi :"))
    return panjang, lebar, tinggi

def utama():
    a, b, c = input_balok()
    luas_balok(a, b, c)
    keliling_balok(a, b, c)
    volume_balok(a, b, c)
    
utama()