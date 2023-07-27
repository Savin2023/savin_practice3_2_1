# Перемножение матриц
from random import randint

# Функция вывода на печать
def print_prod(a,b,n,m):
    print("\nМатрица A\n")
    for i in range(n):
            for j in range(m):
                print(a[i][j],end=" ")
            print()
            
    print("\nМатрица B\n")
    for i in range(m):
            for j in range(n):
                print(b[i][j],end=" ")
            print()
            
    print("\nПроизведение:\n")
    for i in range(n):
        for j in range(n):
            for k in range(m):
                if k<(m-1):
                    print(a[i][k],"x",b[k][j],"+",end=" ")
                else:
                    print(a[i][k],"x",b[k][j],end="       ")
        print("\n\n\n")

    print("\nИтоговая матрица:\n")
    for i in range(n):
        for j in range(n):
            s=0
            for k in range(m):
                s+=(a[i][k]*b[k][j])
            print(s,end="   ")
        print("\n\n")


    
# формирование матриц
n=2
m=4



matr_A=[[randint(1,9) for j in range(m)] for i in range(n)] 
matr_B=[[randint(1,9) for j in range(n)] for i in range(m)] 

print_prod(matr_A,matr_B,n,m)
                  

