
# coding: utf-8

# In[4]:


import numpy as np
import numpy.linalg



#係数行列を定義。例えば3と書くときは3ではなく3.0と書くこと。
A = np.array([[4.,2.,1.],[2.,-1.,2.],[1.,4.,1.]])


#定数項ベクトルを定義。
b = np.array([[10.],[5.],[12.]])

# linalgを使うと１行で済む。
#print(np.linalg.solve(A,b))


#ガウス・ジョルダン法を定義。
def Gauss_J(A,b):
    
    print("3元連立一次方程式")

    for i in range(len(A)):
        print("{}x1+{}x2+{}x3 = {}".format(A[i][0],A[i][1],A[i][2], b[i]))
    
    print("の解は")  
    
    #まずAを上三角行列にする。
    for p in range(len(A)):
        pivot = A[p][p]
        for j in range(p+1, len(A)):
            coef = A[j][p] / pivot
            A[j] -= A[p] * coef
            b[j] -= b[p] * coef
    #途中経過確認。
    #print(A)
    #print(b)
    #対角成分を1にする。
    for i in range(len(A)):
        b[i] /= A[i][i]
        A[i] /= A[i][i]
    #途中経過確認。
    #print(A)
    #print(b)
    #答えを出す。
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            b[j] -= b[i] * A[j][i]
            A[j][i] = 0
    #print(A)
    print("x1 = {}".format(b[0]))
    print("x2 = {}".format(b[1]))
    print("x3 = {}".format(b[2]))
    

#ガウス・ジョルダン法で解く。

Gauss_J(A,b)
    

