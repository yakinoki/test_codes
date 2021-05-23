# coding: utf-8
import numpy as np
import numpy.linalg
from src import Gauss_Jordan 



#係数行列を定義。例えば3と書くときは3ではなく3.と書くこと。
A = np.array([[4.,2.,1.],[2.,-1.,2.],[1.,4.,1.]])

#定数項ベクトルを定義。
b = np.array([[10.],[5.],[12.]])


if __name__ == "__main__":
    Gauss_Jordan.Gauss_J(A,b)

#linalgを使うと１行で済む。（確認用）
#print(np.linalg.solve(A,b))

