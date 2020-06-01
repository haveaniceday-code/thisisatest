#from math import sqrt
a = float(input("introduce el valor de a: "))

b = float(input("introduce el valor de b: "))
print("el valor de la suma es:",a+b)
print("el valor de la suma es: %.1f" %(a+b))
print("el valor de la suma es: "+str(a+b))
"""
lista=["h","a","c","k",111]
print(lista)
print(type(lista))

for elemento in lista:
    print (elemento)

user=input("Usuario: ")
password=input("Contraseña: ")
print("El usuario es:  %s \n La contraseña es: %s" %(user,password))
print("El usuario es: ",user ,"\n La contrseña es: ",password)

mod=a%b
div=a//b
print(div,"*",b,"+",mod,"= ",a)
pot=a**b
print(a,"elevado a la", b, "es:",pot)
if(a>b):
    print("a es mayor que b")
elif(a==b):
    print("a es igual que b")
else:
    print("b es mayor que a")

num1=int(input("ingresa un numero: "))
num2=int(input("ingresa un segundo numero: "))
if(num1==num2):
    print("el numero {0} es igual al numero {1}".format(num1,num2))
elif(num1!=num2):
    print("el numero {0} es diferente al numero {1}".format(num1,num2))+

texto="par" if (a%2)==0 else "impar" #atribucion condicional!!!!!!
print("el numero es;",texto)
lista=list(range(10))
print(lista)
lista2=list(range(2,16,3))
print(lista2)
for i in range(1,67,5):
    print(i)

for item in range(10):
    print(item)
    if item==6:
        print("llegó a 6")
        continue

print()
print("inicio")
i=10
while(i<100):
    i+=1
    if(i%2==0):
        continue
    print(i)
else:
    print("else")
print("fin")

lista=[[1,4],[3,78,6.6],[54,0.65]]
print(lista[1][2])
for i in lista:
    print(i)
a=(5)
print(type(a))
b=(4,)
print(type(b))

lista2=lista+[7]
print(lista2)
lista.append(23)
print(lista)
del(lista[-1])
print(lista)
lista_nums=[10,43,65,0.3,0.433,54]
for i in lista_nums:
    print(i)
lista_nums2=[]
j=0
while(True):
    elemento=input("ingrese una valor para la posicion {0} (intro si desea terminar): ".format(j))
    lista_nums2.append(elemento)
    j+=1
    if elemento=="":
        lista_nums2.pop()
        break
print(lista_nums2)
lista_nums2.reverse()
print("reverse\n",lista_nums2)
lista_nums2.sort()
print("sort",lista_nums2)
print(lista_nums2)
    
print(lista_nums2)
lita=[0,32,230,7.8,3,"tr"]
print(lita[5])
lita.insert(1,"dea")
print(lita)
lita[1]="sasdsad"
print(lita)"""
lista=[1,2,3,4,5]
lista=lista+[6]
print(1300/18)
tel={31345630:'ana',3244342:'juan',31244533:'pedro',423123:'andrea'}
print(len(tel))
del(tel[31345630])
print(tel)