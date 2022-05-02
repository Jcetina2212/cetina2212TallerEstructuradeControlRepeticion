"""
programa que de los valores de n hasta que llegue a k, donde k<N
"""
v=input("Digite n y k:")
n,k=v.split(" ")
n=int(n)
k=int(k)
print(n)
while(k<n):
  n-=1
  print (n)