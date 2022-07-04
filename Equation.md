What is G

$G_i(A)=\{z\in C | |z-a_{ii}|\le \sum_{j\ne i}|a_{ij}|\}$ $G(A)=\bigcup_{i}G_i(A)$

$\begin{pmatrix}  2 + j & j & 1 \\
                  0.25 & 3 & 0.5 \\
                  0 & 0 & 4  \end{pmatrix}$​

Thm:

1. $\forall A\in M_n, \sigma(A)\sube G(A)$. 

2. Further, if there is a connected component of $G(A)$ with k disks, then there contain exactly k eigenvalues.

#### Scene 1:

[Display]   proof of Thm (1)

[Display] $Ax=\lambda x,\forall \lambda$ （1）

[Display]  Define $k=\arg\max_i |x_i|$ （2）

[give an example, Display, then remove] $x =\begin{bmatrix} 1\\ i \\ 2+i \end{bmatrix}$,$ A \begin{bmatrix} 1\\ i \\ 2+i \end{bmatrix} = \lambda \begin{bmatrix} 1\\ i \\ 2+i \end{bmatrix}$

在$2+i$ 上面Create Rectangle表明这个entry是模长最大的。然后边上写$k=3$

#### Scene 2:

[例子消失] [（2）式移到TOP，把（1）放到（2）下面]

（1）TexReplaceTransform成：$\begin{bmatrix} a_{11} & ... & a_{1n}\\ ... &  & ... \\a_{k1} & ... & a_{kn} \\... &  & ...\\ a_{n1} & ... & a_{nn} \end{bmatrix} \begin{bmatrix} x_1\\ ...\\ x_k \\ ... \\ x_n \end{bmatrix} = \lambda \begin{bmatrix} x_1\\ ...\\ x_k \\ ... \\ x_n \end{bmatrix}$（3）

[把A的第k行圈出来，第一个x圈出来，第二个x的$x_k$圈出来，表明我们只关注第k行乘x的结果]

#### Scene 3:

(3)下面一行显示：$\lambda x_k = \sum_j a_{kj}x_j$ (4)

[把（3）删掉，（4）上移居中]

(4)变成：$\lambda x_k = \sum_{j\ne k} a_{kj}x_j + a_{kk}x_k$ (5)

(5)变成：$\lambda x_k -a_{kk}x_k = \sum_{j\ne k} a_{kj}x_j$ (6)

(6)变成：$(\lambda-a_{kk})x_k = \sum_{j\ne k} a_{kj}x_j$ （7）

#### Scene 4:

(7)变成：$|\lambda-a_{kk}||x_k| = |\sum_{j\ne k} a_{kj}x_j|$ （8）

[Display] $\triangle \ne: |a+b|\le|a|+|b|$ 然后消失这行

(8)变成：$|\lambda-a_{kk}||x_k| \le \sum_{j\ne k} |a_{kj}||x_j|$ （9）

(9)变成：$|\lambda-a_{kk}||x_k| \le |a_{k1}||x_1| + ... |a_{k,k-1}||x_{k-1}| +|a_{k,k+1}||x_{k+1}| + |a_{k,n}||x_n| $ （10）

[把（2）圈起来，或者突出显示一下。之后删掉（2）]

(10)变成：$|\lambda-a_{kk}||x_k| \le |a_{k1}||x_k| + ... |a_{k,k-1}||x_k| +|a_{k,k+1}||x_k| + |a_{k,n}||x_k| $ （11）

(11)变成：$|\lambda-a_{kk}||x_k| \le (\sum_{j\ne k} |a_{kj}|)|x_k|$ （12）

[Display] x is eigenvector, so $|x_k|\ne 0$. 然后消失这行

(12)变成：$|\lambda-a_{kk}| \le \sum_{j\ne k} |a_{kj}|$ （13）

#### Scene 5:

[（13）移到TOP] 下面画一个圆（圆心+半径。不需要有坐标轴）。圆心边上写个label（$a_{kk}$），半径边上写个label（$\sum_{j\ne k} |a_{kj}|$）。园里随便放个点，边上写个$\lambda$ 



