# 证明：圆周排列实数的相邻乘积之和上界

## 题目

设 $n \ge 5$，实数 $a_1, a_2, \ldots, a_n$ 围成一个圆圈，满足

$$
\sum_{i=1}^n a_i = 0, \qquad \sum_{i=1}^n a_i^2 = 1,
$$

其中下标按模 $n$ 理解。证明：

$$
\sum_{i=1}^n a_i a_{i+1} \le \cos\frac{2\pi}{n},
$$

并说明等号可以达到。

---

## 证明

### 第一步：将目标写成二次型

记 $\mathbf{a} = (a_1, a_2, \ldots, a_n)^T \in \mathbb{R}^n$。设 $P$ 为 $n$ 阶**循环移位矩阵**（cyclic permutation matrix），其定义为

$$
P_{i,j} = \begin{cases} 1, & j \equiv i+1 \pmod{n}, \\ 0, & \text{否则}. \end{cases}
$$

即 $P$ 将向量 $(a_1, \ldots, a_n)^T$ 映射为 $(a_2, a_3, \ldots, a_n, a_1)^T$，于是 $(P\mathbf{a})_i = a_{i+1}$（下标模 $n$）。因此

$$
\sum_{i=1}^n a_i a_{i+1} = \mathbf{a}^T P\, \mathbf{a}.
$$

由于 $\mathbf{a}^T P\, \mathbf{a}$ 是标量，等于其转置：

$$
\mathbf{a}^T P\, \mathbf{a} = \left(\mathbf{a}^T P\, \mathbf{a}\right)^T = \mathbf{a}^T P^T \mathbf{a}.
$$

故

$$
\sum_{i=1}^n a_i a_{i+1} = \mathbf{a}^T \frac{P + P^T}{2}\, \mathbf{a}.
$$

令

$$
S := \frac{P + P^T}{2},
$$

则 $S$ 是**实对称矩阵**，且

$$
\sum_{i=1}^n a_i a_{i+1} = \mathbf{a}^T S\, \mathbf{a}.
$$

### 第二步：求 $S$ 的特征值与特征向量

矩阵 $P$ 是循环移位矩阵，其特征向量为 Fourier 向量

$$
\mathbf{v}_k = \frac{1}{\sqrt{n}}\left(1,\; \omega^k,\; \omega^{2k},\; \ldots,\; \omega^{(n-1)k}\right)^T, \qquad k = 0, 1, \ldots, n-1,
$$

其中 $\omega = e^{2\pi i / n}$。对应的特征值为 $\omega^k$。

由于 $P$ 和 $P^T = P^{-1}$ 共享相同的特征向量 $\mathbf{v}_k$，且 $P^T$ 在 $\mathbf{v}_k$ 上的特征值为 $\omega^{-k}$，故 $S = \frac{P+P^T}{2}$ 在 $\mathbf{v}_k$ 上的特征值为

$$
\lambda_k = \frac{\omega^k + \omega^{-k}}{2} = \cos\frac{2\pi k}{n}, \qquad k = 0, 1, \ldots, n-1.
$$

因此 $S$ 的全部特征值为

$$
\lambda_k = \cos\frac{2\pi k}{n}, \qquad k = 0, 1, \ldots, n-1.
$$

这些特征向量 $\{\mathbf{v}_0, \mathbf{v}_1, \ldots, \mathbf{v}_{n-1}\}$ 构成 $\mathbb{C}^n$ 的一组标准正交基。

特别地，$k=0$ 对应 $\mathbf{v}_0 = \frac{1}{\sqrt{n}}(1,1,\ldots,1)^T$，特征值 $\lambda_0 = \cos 0 = 1$。

### 第三步：利用约束条件

约束 $\sum a_i = 0$ 等价于

$$
\mathbf{a} \cdot \mathbf{v}_0 = \frac{1}{\sqrt{n}}\sum_{i=1}^n a_i = 0,
$$

即 $\mathbf{a}$ 与 $\mathbf{v}_0$ 正交。

约束 $\sum a_i^2 = 1$ 即 $\|\mathbf{a}\|^2 = 1$，$\mathbf{a}$ 是单位向量。

因此，$\mathbf{a}$ 是**与 $\mathbf{v}_0$ 正交的单位向量**，即 $\mathbf{a}$ 属于 $\mathbf{v}_0$ 的正交补空间 $W = \mathbf{v}_0^\perp$。

空间 $W$ 由 $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_{n-1}$ 张成，$S$ 在 $W$ 上的特征值为

$$
\lambda_k = \cos\frac{2\pi k}{n}, \qquad k = 1, 2, \ldots, n-1.
$$

### 第四步：求二次型的最大值

由实对称矩阵的谱定理，对于 $W$ 中的单位向量 $\mathbf{a}$，有

$$
\mathbf{a}^T S\, \mathbf{a} \le \max_{k=1,\ldots,n-1} \lambda_k = \max_{k=1,\ldots,n-1} \cos\frac{2\pi k}{n}.
$$

现在确定 $\max_{k=1,\ldots,n-1} \cos\frac{2\pi k}{n}$。

当 $k$ 从 $1$ 取到 $n-1$ 时，$\frac{2\pi k}{n}$ 从 $\frac{2\pi}{n}$ 取到 $\frac{2\pi(n-1)}{n} = 2\pi - \frac{2\pi}{n}$。

- $k=1$：$\cos\frac{2\pi}{n}$；
- $k = n-1$：$\cos\frac{2\pi(n-1)}{n} = \cos\!\left(2\pi - \frac{2\pi}{n}\right) = \cos\frac{2\pi}{n}$。

对于 $n \ge 5$，$\frac{2\pi}{n} \le \frac{2\pi}{5} < \frac{\pi}{2}$，所以 $\cos\frac{2\pi}{n} > 0$。

对于 $2 \le k \le n-2$，角 $\frac{2\pi k}{n}$ 满足 $\frac{4\pi}{n} \le \frac{2\pi k}{n} \le \frac{2\pi(n-2)}{n} = 2\pi - \frac{4\pi}{n}$。

- 当 $2 \le k \le \lfloor n/2 \rfloor$ 时，$\frac{2\pi k}{n} \in \left[\frac{4\pi}{n}, \pi\right]$，$\cos\frac{2\pi k}{n} \le \cos\frac{4\pi}{n}$。
- 当 $\lceil n/2 \rceil \le k \le n-2$ 时，由对称性 $\cos\frac{2\pi k}{n} = \cos\frac{2\pi(n-k)}{n}$，同样有 $\cos\frac{2\pi k}{n} \le \cos\frac{4\pi}{n}$。

由于 $n \ge 5$，$\frac{4\pi}{n} \ge \frac{4\pi}{n}$，且 $\frac{4\pi}{n} > \frac{2\pi}{n}$，在 $[0, \pi]$ 上余弦函数递减，故

$$
\cos\frac{4\pi}{n} < \cos\frac{2\pi}{n}.
$$

因此

$$
\max_{k=1,\ldots,n-1} \cos\frac{2\pi k}{n} = \cos\frac{2\pi}{n},
$$

最大值在 $k=1$ 和 $k=n-1$ 处取到。

综上，

$$
\sum_{i=1}^n a_i a_{i+1} = \mathbf{a}^T S\, \mathbf{a} \le \cos\frac{2\pi}{n}.
$$

### 第五步：等号可以达到

取

$$
a_j = \sqrt{\frac{2}{n}}\,\cos\frac{2\pi j}{n}, \qquad j = 1, 2, \ldots, n.
$$

**验证 $\sum a_j = 0$：**

$$
\sum_{j=1}^n a_j = \sqrt{\frac{2}{n}} \sum_{j=1}^n \cos\frac{2\pi j}{n} = \sqrt{\frac{2}{n}} \cdot \operatorname{Re}\sum_{j=1}^n \omega^j = \sqrt{\frac{2}{n}} \cdot \operatorname{Re}\!\left(\omega \cdot \frac{1 - \omega^n}{1 - \omega}\right) = 0,
$$

因为 $\omega^n = 1$，故 $1 - \omega^n = 0$。

**验证 $\sum a_j^2 = 1$：**

$$
\sum_{j=1}^n a_j^2 = \frac{2}{n}\sum_{j=1}^n \cos^2\frac{2\pi j}{n} = \frac{2}{n}\sum_{j=1}^n \frac{1 + \cos\frac{4\pi j}{n}}{2} = \frac{2}{n}\left(\frac{n}{2} + \frac{1}{2}\sum_{j=1}^n \cos\frac{4\pi j}{n}\right).
$$

同理 $\sum_{j=1}^n \cos\frac{4\pi j}{n} = \operatorname{Re}\sum_{j=1}^n \omega^{2j} = 0$（因为 $\omega^{2n} = 1$ 且 $\omega^2 \ne 1$，后者当 $n \ge 3$ 时成立）。故

$$
\sum_{j=1}^n a_j^2 = \frac{2}{n} \cdot \frac{n}{2} = 1. \quad \checkmark
$$

**验证 $\sum a_j a_{j+1} = \cos\frac{2\pi}{n}$：**

利用积化和差公式：

$$
\cos\frac{2\pi j}{n}\cos\frac{2\pi(j+1)}{n} = \frac{1}{2}\left[\cos\frac{2\pi}{n} + \cos\frac{2\pi(2j+1)}{n}\right].
$$

因此

$$
\sum_{j=1}^n a_j a_{j+1} = \frac{2}{n}\sum_{j=1}^n \cos\frac{2\pi j}{n}\cos\frac{2\pi(j+1)}{n} = \frac{2}{n}\cdot\frac{1}{2}\left[n\cos\frac{2\pi}{n} + \sum_{j=1}^n \cos\frac{2\pi(2j+1)}{n}\right].
$$

计算第二个求和：

$$
\sum_{j=1}^n \cos\frac{2\pi(2j+1)}{n} = \operatorname{Re}\sum_{j=1}^n e^{i\frac{2\pi(2j+1)}{n}} = \operatorname{Re}\!\left(e^{i\frac{2\pi}{n}}\sum_{j=1}^n e^{i\frac{4\pi j}{n}}\right) = \operatorname{Re}\!\left(e^{i\frac{2\pi}{n}} \cdot \omega^2 \cdot \frac{1 - \omega^{2n}}{1 - \omega^2}\right) = 0,
$$

因为 $\omega^{2n} = 1$，故 $1 - \omega^{2n} = 0$。

因此

$$
\sum_{j=1}^n a_j a_{j+1} = \frac{2}{n}\cdot\frac{1}{2}\cdot n\cos\frac{2\pi}{n} = \cos\frac{2\pi}{n}. \quad \checkmark
$$

等号达到。

---

## 结论

$$
\boxed{\sum_{i=1}^n a_i a_{i+1} \le \cos\frac{2\pi}{n}}
$$

等号在 $a_j = \sqrt{\dfrac{2}{n}}\cos\dfrac{2\pi j}{n}$（$j=1,\ldots,n$）时达到。

**证毕。** $\blacksquare$

---

## 证明思路说明

核心思想是将 $\sum a_i a_{i+1}$ 视为实对称矩阵 $S = \frac{P+P^T}{2}$（$P$ 为循环移位矩阵）的二次型 $\mathbf{a}^T S \mathbf{a}$。矩阵 $S$ 是**循环矩阵**（circulant matrix），其特征值恰为 $\cos\frac{2\pi k}{n}$（$k=0,1,\ldots,n-1$），对应特征向量为 Fourier 向量。约束 $\sum a_i = 0$ 将 $\mathbf{a}$ 限制在 $\mathbf{v}_0$（全 $1$ 向量，特征值 $1$）的正交补空间中，因此 $\mathbf{a}^T S \mathbf{a}$ 的最大值等于 $S$ 在该补空间中的最大特征值，即 $\max_{k \ge 1}\cos\frac{2\pi k}{n} = \cos\frac{2\pi}{n}$。等号在 $\mathbf{a}$ 取 $k=1$ 对应特征向量的实部时达到。
