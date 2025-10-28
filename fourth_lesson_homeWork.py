import math as mt

##Task_1 
print("2*(3-1) = ", 2*(3-1))
print("(5-1)*(5+1) = ", (5-1)*(5+1))
print("0.3 * (4-1) = ", 0.3 * (4-1))
print("(91-1) / (2+1) = ",(91-1) / (2+1))
print("SQRT((5*4)/3) = ", mt.sqrt((5*4)/3))
print("(1/3) + 5 * ((0.2-0.001)/91) = ", (1/3) + 5 * ((0.2-0.001)/91))
print("0.16 * (3.2 - (3/40) + (11*2 + 3)/11) * 4.125/((4*3+3)/4) = ", 0.16 * (3.2 - (3/40) + (11*2 + 3)/11) * 4.125/((4*3+3)/4))

##Task_2
x, y = 24, 31.4
print(type(x))
print(type(y))

##Task_3
a, b = -10, 15
diff = abs(a) + abs(b)
print("diff: ",diff)

##Task_4
potato_total = 290
pocket_size = 25

full_pocket_total = potato_total // pocket_size
print("Full pockets: ", full_pocket_total)
leftover_potato = potato_total % pocket_size
print("leftover pockets: ", leftover_potato)

##Task_5
h_1, m_1 = 13, 25
h_2, m_2 = 19, 40

print("h: ", h_2-h_1)
print("m: ", m_2-m_1)

##Task_6
old_price = int(input('Write old price: '))
new_price = int(input('Write new price: '))

res = round(float(new_price * 100 / old_price - 100), 1)
print("Percent diff: ", res)


##Task_7
x = 2
y = mt.pow(mt.e, 1/(1+(mt.cos(x)*mt.cos(x))))
print("y: ", y)

##Task_8
det_count = 1500
quantity = 45
emp_count = mt.ceil(det_count / quantity)
print("Employee count: ", emp_count)

##Task_9
katet_1 = int(input('Input katet1: '))
katet_2 = int(input('Input katet2: '))
gip = mt.sqrt(mt.pow(katet_1,2) + mt.pow(katet_2,2))
min_katet = min(katet_1, katet_2)
min_sin = min_katet / gip
print("min_sin ", min_sin)

##Task_10    
katet_1 = int(input('Input katet1: '))
katet_2 = int(input('Input katet2: '))
gip = mt.sqrt(mt.pow(katet_1,2) + mt.pow(katet_2,2))
print("gipotenuza ", gip)
min_katet = min(katet_1, katet_2)
min_kat_degree = (mt.asin(min_katet / gip) * 180)/mt.pi
print("min_kat_degree ", min_kat_degree)