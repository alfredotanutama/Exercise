"""PR Konversi Kelvin ke Fahrenheit"""
print('Program Konversi Temperatur Kelvin ke Fahrenheit\n')
opt=int(input('1. K to F \n2. F to K\nPilih (1/2): '))
#1 Kelvin ke Fahrenheit
if opt == 1:
    kv=float(input('Masukan suhu Kelvin: '))
    cs=kv-273
    fht=(9/5)*cs+32
    print('Suhu awal adalah:',kv,'K')
    print('Suhu akhir adalah:',fht,'F')
#2 Fahrenheit ke Kelvin
elif opt == 2:
    fht=float(input('Masukan suhu Fahrenheit: '))
    cs=(5/9)*(fht-32)
    kv=cs+273
    print('Suhu awal adalah:',fht,'F')
    print('Suhu akhir adalah:',kv,'K')
else:
    print('Apasih yang kamu ketik :(')