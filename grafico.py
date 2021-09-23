from packaging import version
import primecount
import timeit
import matplotlib.pyplot as plt

mysetupPrimecount = "import primecount"
mysetupSympy = "import sympy"
code1 = "print(primecount.pi(10**10))"
code2 = "print(sympy.primepi(10**10))"
tiempos = []
ejex = []
def concatenarPotenciaPrimesCount(a):
    x = "primecount.pi(10**"
    y = ")"
    return x + str(a) + y
def concatenarPotenciaSympy(a):
    x = "sympy.primepi(10**"
    y = ")"
    return x + str(a) + y

for i in range(1,18):
    tiempos.append(timeit.timeit(setup=mysetupPrimecount, stmt = concatenarPotenciaPrimesCount(i), number = 1))
    ejex.append(i)

#Añado tiempos para comparar

plt.ylabel("Tiempo(en segundos)")
plt.xlabel("pi(1E+X)")
plt.plot(ejex,tiempos)
print(ejex)
print(tiempos)


#Ahora para sympy

tiempoSympy = []
escalaSympy = []
for i in range(1,12):
    tiempoSympy.append(timeit.timeit(setup=mysetupSympy, stmt = concatenarPotenciaSympy(i), number = 1))
    escalaSympy.append(i)
plt.plot(escalaSympy,tiempoSympy)

#Ahora beimargod

setupBeimar = '''
import math
import time
'''
codigoBeimar = '''
def Cantidad(x):
    pi_ = math.ceil(0.5 * floor((2 * x + (-1) ** x - 6 * c_(x) + 5) / 3))
    return int(pi_)
def prime_(x):
    if ((((x - 1) / 3 )% 2) == 0) and ((x - 1) / 3 ).is_integer():
        z = math.ceil((math.sqrt(x)-1) / 3)
        for i in range(1, z + 1):
            r = (2*(x - 1) - 6*i + (-1) ** i-1) / (6 * i + 3 - (-1) ** i)
            if r.is_integer():
                return False
        return True
    elif (((x - 2) / 3) % 2) != 0 and ((x - 2) / 3).is_integer():
        z = math.ceil((math.sqrt(x-1)-1) / 3)
        for i in range(1, z):
            r = (2*(x - 2) - 6*i + (-1) ** i+1) / (6 * i + 3 - (-1) ** i)
            if r.is_integer():
                return False
        return True
    else:
        return False
def formula_1(x):
    if (x < 5):
        pass
    count = 2
    for i in range(5, x):
        if prime_(i):
            count += 1
    return count
'''

def callBeimar(a):
    BeimarDice = '''
values = [10**''' + str(a) + ''']
start_time = time.time()
for v in values:
    print(f"LA CANTIDAD DE PRIMOS MENORES A {v}, ES: {formula_1(v)}")
print(f"TARDA {time.time() - start_time} SEGUNDOS")
    '''
    return codigoBeimar + BeimarDice;

tiemposBeimar = []
escalaBeimar = []

for i in range(1,7):
    tiemposBeimar.append(timeit.timeit(setup=setupBeimar, stmt = callBeimar(i), number = 1))
    escalaBeimar.append(i)
plt.plot(escalaBeimar,tiemposBeimar)
#Función truchisima para primos contando 1*1
tiemposFuncionTrucha = []
escalaFuncionTrucha = []

def callFuncionTrucha(num):

    truchoEs = '''
def es_primo(num): 
    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False
    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos probamos n números con n-1 números iterando, buscando si el mod del num % i == 0, o sea, si se divide exactamente por alguno de los menores.
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    #de lo contrario devuelve Verdadero 
    #Lo de arriba tiene complejidad n*n

contadorTrucho = 0
for i in range (1,10**''' + str(num) +'''):
    if(es_primo(i)):
        contadorTrucho += 1
    print(i)
#acá la complejidad aumenta a (n*n)*n
print(contadorTrucho)
'''
    return truchoEs
for i in range(1,6):
    tiemposFuncionTrucha.append(timeit.timeit(stmt = callFuncionTrucha(i),number=1))
    escalaFuncionTrucha.append(i)
plt.plot(escalaFuncionTrucha,tiemposFuncionTrucha)

plt.legend(["Primecount", "Sympy","BeimarGod","Forma trucha"])
plt.savefig("primespiXD.svg")

# print("Para primecount",timeit.timeit(setup = mysetupPrimecount, stmt = code1, number = 1))
# print("Para primecount",timeit.timeit(setup = mysetupSympy, stmt = code2, number = 1))
