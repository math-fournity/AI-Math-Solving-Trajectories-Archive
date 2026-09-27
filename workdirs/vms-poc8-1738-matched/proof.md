# 求最小的 $n$ 使得 $x^2 + 7 = f_1(x)^2 + \cdots + f_n(x)^2$（$f_i \in \mathbb{Q}[x]$）

## 答案

$$\boxed{n = 5}$$

## 证明

### 第一步：所有 $f_i$ 的次数至多为 1

设 $d = \max_i \deg(f_i)$。$f_i^2$ 的首项系数为 $(\text{lc}(f_i))^2 > 0$（因为 $\mathbb{Q}$ 是形式实域，有理数的平方和为零当且仅当每一项为零）。因此 $\sum f_i^2$ 中 $x^{2d}$ 的系数为

$$\sum_{\deg(f_i) = d} (\text{lc}(f_i))^2 > 0,$$

故 $\deg\!\left(\sum f_i^2\right) = 2d$。由于 $x^2 + 7$ 的次数为 $2$，得 $d = 1$，即所有 $f_i$ 至多是一次多项式。

### 第二步：建立方程组

设 $f_i(x) = a_i x + b_i$，其中 $a_i, b_i \in \mathbb{Q}$。比较 $x^2 + 7 = \sum (a_i x + b_i)^2$ 的系数，得：

$$
\begin{cases}
\displaystyle\sum_{i=1}^{n} a_i^2 = 1 & (x^2 \text{ 系数}) \\[6pt]
\displaystyle\sum_{i=1}^{n} a_i b_i = 0 & (x \text{ 系数}) \\[6pt]
\displaystyle\sum_{i=1}^{n} b_i^2 = 7 & (\text{常数项})
\end{cases}
$$

### 第三步：用正交补将问题归结为"7 是否被 $(n-1)$ 维二次型 $\langle 1,\ldots,1 \rangle$ 表示"

令 $\mathbf{a} = (a_1, \ldots, a_n) \in \mathbb{Q}^n$，$\mathbf{b} = (b_1, \ldots, b_n) \in \mathbb{Q}^n$。条件为：

- $\|\mathbf{a}\|^2 = 1$（$\mathbf{a}$ 是模 $\langle 1,\ldots,1 \rangle$ 的 1 的向量），
- $\mathbf{a} \cdot \mathbf{b} = 0$（$\mathbf{b} \in \mathbf{a}^\perp$），
- $\|\mathbf{b}\|^2 = 7$（$\mathbf{b}$ 在 $\mathbf{a}^\perp$ 中的范数为 7）。

由 **Witt 延拓定理**（对特征 $\neq 2$ 的域成立）：$\mathbb{Q}^n$ 上任意两个范数为 1 的向量可通过等距变换互换。特别地，取 $\mathbf{e}_1 = (1, 0, \ldots, 0)$，存在 $\langle 1,\ldots,1 \rangle$ 的等距自同构 $\sigma$ 使 $\sigma(\mathbf{a}) = \mathbf{e}_1$。于是 $\sigma$ 将 $\mathbf{a}^\perp$ 等距映射到 $\mathbf{e}_1^\perp$。

$\mathbf{e}_1^\perp = \{(0, x_2, \ldots, x_n)\}$ 上的限制型为 $\langle 1, 1, \ldots, 1 \rangle$（$n-1$ 个 1）。

因此，**原问题等价于：$7$ 是否被 $(n-1)$ 维二次型 $\langle 1, \ldots, 1 \rangle$ 在 $\mathbb{Q}$ 上表示**，即是否存在 $n-1$ 个有理数 $c_1, \ldots, c_{n-1}$ 使得

$$c_1^2 + c_2^2 + \cdots + c_{n-1}^2 = 7.$$

### 第四步：排除 $n = 1, 2, 3, 4$

#### $n = 1$：需要 $7$ 是有理数的平方

$7$ 不是有理数的平方（$\sqrt{7}$ 是无理数）。不可行。

#### $n = 2$：需要 $7$ 是两个有理数的平方和

有理数 $r$ 是两个有理数平方和当且仅当：将 $r$ 写成既约分数 $p/q$ 后，$p$ 和 $q$ 的每个素因子 $p \equiv 3 \pmod{4}$ 出现的次数之和为偶数。

$7$ 是素数且 $7 \equiv 3 \pmod{4}$，在 $7$ 的素因子分解中 $7$ 出现 1 次（奇数）。故 $7$ 不是两个有理数的平方和。不可行。

#### $n = 3$：需要 $7$ 是三个有理数的平方和

有理数 $r$ 是三个有理数平方和 $\Leftrightarrow$ 存在正整数 $q$ 使得 $rq^2$ 是三个整数平方和。

由 **Legendre 三平方定理**：正整数 $N$ 是三个整数平方和当且仅当 $N$ **不是** $4^a(8b+7)$ 的形式（$a, b \geq 0$）。

对 $N = 7q^2$：设 $q = 2^s \cdot m$（$m$ 为奇数），则

$$7q^2 = 7 \cdot 4^s \cdot m^2 = 4^s \cdot 7m^2.$$

因为 $m$ 为奇数，$m^2 \equiv 1 \pmod{8}$，所以 $7m^2 \equiv 7 \pmod{8}$，即 $7m^2 = 8b + 7$ 对某个 $b$。因此

$$7q^2 = 4^s(8b + 7),$$

恒为 Legendre 定理中的禁形。故对**任意** $q$，$7q^2$ 都不是三个整数的平方和，从而 $7$ 不是三个有理数的平方和。不可行。

#### $n = 4$：需要 $7$ 是四个有理数的平方和——但这还不够

由第三步，$n = 4$ 时需要 $7$ 是**三个**有理数的平方和（正交补是 3 维的）。由上面的论证，这不可能。不可行。

### 第五步：构造 $n = 5$ 的解

取

$$f_1(x) = x, \quad f_2(x) = 1, \quad f_3(x) = 1, \quad f_4(x) = 1, \quad f_5(x) = 2.$$

验证：

$$f_1^2 + f_2^2 + f_3^2 + f_4^2 + f_5^2 = x^2 + 1 + 1 + 1 + 4 = x^2 + 7. \quad \checkmark$$

对应方程组：$\mathbf{a} = (1, 0, 0, 0, 0)$，$\mathbf{b} = (0, 1, 1, 1, 2)$。

- $\sum a_i^2 = 1$ ✓
- $\sum a_i b_i = 0$ ✓
- $\sum b_i^2 = 0 + 1 + 1 + 1 + 4 = 7$ ✓

这里正交补是 4 维的 $\langle 1,1,1,1 \rangle$，由 **Lagrange 四平方定理**，每个非负整数都是四个整数的平方和，故 $7 = 1^2 + 1^2 + 1^2 + 2^2$ 给出解。

### 结论

$n = 1, 2, 3, 4$ 均不可行，$n = 5$ 可行。故最小的 $n$ 为

$$\boxed{n = 5}.$$

**证毕.** $\blacksquare$
