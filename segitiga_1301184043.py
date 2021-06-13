# R-Ready


print('Masukan a: ')
a = eval(input())
round(a)

print('Masukan b: ')
b = eval(input())
round(b)

print('Masukan c: ')
c = eval(input())
round(c)

if(a<=0 or b<=0 or c<=0):
    print("segitiga tidak dapat dibangun, If 1")
else:
    max_angka = max(a,b,c)
    # print(max_angka)
    if(max_angka == a):
        # print("a adalah max")
        temp = b + c;
        kuadrat_b = pow(b,2)
        kuadrat_c = pow(c,2)
        temp_kuadrat = kuadrat_b + kuadrat_c
        # print("temp : ", temp)
    elif(max_angka == b):
        # print("b adalah max")
        temp = a + c;
        kuadrat_a = pow(a,2)
        kuadrat_c = pow(c,2)
        temp_kuadrat = kuadrat_a + kuadrat_c
        # print("temp : ", temp)
    elif(max_angka == c):
        # print("c adalah max")
        temp = a + b;
        kuadrat_b = pow(b,2)
        kuadrat_a = pow(a,2)
        temp_kuadrat = kuadrat_b + kuadrat_a
        # print("temp : ", temp)

    
    max_angka_kuadrat = pow(max_angka,2)

    # print("max kuadrat = ",max_angka_kuadrat)
    # print("temp_kuadrat = ",temp_kuadrat)
    

    if(max_angka>=temp):
        print("segitiga tidak dapat dibangun, If 2")
    else:
        if(a == b or b == c or a == c):
            print("segitiga sama kaki")
        elif(a==b and b==c):
            print("segitiga sama sisi")
        elif( max_angka_kuadrat == temp_kuadrat):
             print("segitiga siku siku")
        else:
            print("segita bebas")

