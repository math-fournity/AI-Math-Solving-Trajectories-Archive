# 最小的 $n$ 使得 $x^2+7$ 是 $n$ 个有理系数多项式的平方和

## 答案

$$\boxed{n = 5}$$

## 解答

### 第一步：所有 $f_i$ 的次数至多为 1

设 $f_i \in \mathbb{Q}[x]$ 满足 $x^2 + 7 = \sum_{i=1}^n f_i(x)^2$。

**断言**：每个 $f_i$ 的次数至多为 1。

设 $d = \max_i \deg(f_i)$。若 $d \geq 2$，取达到最大次数的那些 $f_i$，设其最高次项系数为 $c_i \neq 0$。则 $\sum f_i^2$ 的最高次项为

$$\left(\sum_{i:\,\deg f_i = d} c_i^2\right) x^{2d}.$$

由于 $\mathbb{Q}$ 是形式实域（$-1$ 不是有理数的平方和），$c_i^2 > 0$，故上述系数严格为正。因此 $\deg\!\left(\sum f_i^2\right) = 2d \geq 4$，与 $\deg(x^2+7) = 2$ 矛盾。

故每个 $f_i$ 至多是一次多项式：$f_i(x) = a_i x + b_i$，其中 $a_i, b_i \in \mathbb{Q}$。

### 第二步：翻译为二次型问题

将条件代入：

$$x^2 + 7 = \sum_{i=1}^n (a_i x + b_i)^2 = \left(\sum a_i^2\right) x^2 + 2\left(\sum a_i b_i\right) x + \sum b_i^2.$$

比较系数，得到方程组：

$$\sum_{i=1}^n a_i^2 = 1, \qquad \sum_{i=1}^n a_i b_i = 0, \qquad \sum_{i=1}^n b_i^2 = 7. \tag{$*$}$$

引入向量 $\mathbf{a} = (a_1, \ldots, a_n) \in \mathbb{Q}^n$，$\mathbf{b} = (b_1, \ldots, b_n) \in \mathbb{Q}^n$，以及标准二次型 $q = \langle \underbrace{1, \ldots, 1}_{n} \rangle$（即 $q(\mathbf{v}) = \sum v_i^2$）。则 $(*)$ 等价于：

$$q(\mathbf{a}) = 1, \quad \mathbf{a} \cdot \mathbf{b} = 0, \quad q(\mathbf{b}) = 7.$$

即：$\mathbf{a}$ 是 $q$ 的一个范数为 1 的向量，$\mathbf{b}$ 在 $\mathbf{a}$ 的正交补 $\mathbf{a}^\perp$ 中，且 $q$ 限制在 $\mathbf{a}^\perp$ 上的二次型 $q'$ 表示 7。

**这就是关键的"翻译"**：原问题从"寻找多项式"翻译为"二次型 $q = \langle 1^n \rangle$ 在 $\mathbb{Q}$ 上能否分解为 $\langle 1 \rangle \oplus q'$，且 $q'$ 表示 7"。

### 第三步：$n \leq 4$ 不可能

#### 3.1 限制型 $q'$ 的不变量

设 $\mathbf{a} \in \mathbb{Q}^n$，$q(\mathbf{a}) = 1$。将 $q$ 分裂为 $q \cong \langle 1 \rangle \oplus q'$，其中 $q'$ 是 $q$ 在 $\mathbf{a}^\perp$ 上的限制，是 $n-1$ 维二次型。

$q'$ 的不变量（由分裂公式确定）：

- **行列式**：$\det(q') = \det(q) / q(\mathbf{a}) = 1 / 1 = 1$（在 $\mathbb{Q}^* / \mathbb{Q}^{*2}$ 中）。
- **Hasse 不变量**：由分裂关系 $c(q) = (q(\mathbf{a}),\, \det(q')) \cdot c(\langle q(\mathbf{a}) \rangle) \cdot c(q')$。由于 $q(\mathbf{a}) = 1$，$c(\langle 1 \rangle) = 1$，$(1, 1) = 1$，故 $c(q') = c(q) = 1$（在所有素数 $p$ 处）。
- **符号**：$q$ 正定，故 $q'$ 正定，符号为 $(n{-}1,\, 0)$。

**关键结论**：无论选择哪个范数为 1 的有理向量 $\mathbf{a}$，限制型 $q'$ 的等价类完全相同——由维数、行列式、Hasse 不变量、符号唯一决定（Hasse-Minkowski 定理）。

#### 3.2 $n = 4$：$q' \cong \langle 1, 1, 1 \rangle$，不表示 7

当 $n = 4$ 时，$q'$ 是 3 维正定二次型，$\det = 1$，$c = 1$。由 Hasse-Minkowski 定理：

$$q' \cong \langle 1, 1, 1 \rangle \quad \text{over } \mathbb{Q}.$$

（$\langle 1, 1, 1 \rangle$ 同样是 3 维、正定、$\det = 1$、$c = 1$，故二者等价。）

**$\langle 1, 1, 1 \rangle$ 不表示 7**：这等价于 7 不是三个有理数的平方和。由 Legendre 三平方定理的推广：

> 正有理数 $r$ 是三个有理数的平方和，当且仅当存在正整数 $d$，使得 $r \cdot d^2$ 不是 $4^a(8b+7)$ 的形式（$a, b$ 为非负整数）。

对 $r = 7$：设 $d = 2^s \cdot d'$（$d'$ 为奇数），则

$$7 d^2 = 7 \cdot 4^s \cdot d'^2 = 4^s \cdot (7 d'^2).$$

由于 $d'$ 奇数，$d'^2 \equiv 1 \pmod{8}$，故 $7 d'^2 \equiv 7 \pmod{8}$，即 $7 d'^2 = 8m + 7$ 对某非负整数 $m$。因此

$$7 d^2 = 4^s \cdot (8m + 7),$$

恒为禁止形式。故 **7 不是三个有理数的平方和**，$\langle 1, 1, 1 \rangle$ 不表示 7，从而 $q'$ 不表示 7。

因此 $n = 4$ 不可能。

#### 3.3 $n = 1, 2, 3$ 也不可能

- **$n = 1$**：$x^2 + 7 = f(x)^2$ 要求 $\sqrt{x^2 + 7}$ 是多项式，不可能。
- **$n = 2$**：$q' \cong \langle 1 \rangle$（1 维，$\det = 1$，$c = 1$），表示 7 当且仅当 $7 = t^2$（$t \in \mathbb{Q}$），即 $\sqrt{7} \in \mathbb{Q}$，不可能。
- **$n = 3$**：$q' \cong \langle 1, 1 \rangle$（2 维，$\det = 1$，$c = 1$），表示 7 当且仅当 7 是两个有理数的平方和。但 $7 \equiv 3 \pmod{4}$，而素数 $p \equiv 3 \pmod{4}$ 在 $n$ 的素因子分解中奇数次出现时，$n$ 不是两个有理数的平方和。$7^1$ 中指数 1 为奇数，故 7 不是两个有理数的平方和。不可能。

### 第四步：$n = 5$ 可行

取

$$f_1(x) = x, \quad f_2(x) = 2, \quad f_3(x) = 1, \quad f_4(x) = 1, \quad f_5(x) = 1.$$

验证：

$$f_1^2 + f_2^2 + f_3^2 + f_4^2 + f_5^2 = x^2 + 4 + 1 + 1 + 1 = x^2 + 7. \quad \checkmark$$

对应的向量：$\mathbf{a} = (1, 0, 0, 0, 0)$，$q(\mathbf{a}) = 1$；$\mathbf{b} = (0, 2, 1, 1, 1)$，$\mathbf{a} \cdot \mathbf{b} = 0$，$q(\mathbf{b}) = 4 + 1 + 1 + 1 = 7$。

此时 $q' \cong \langle 1, 1, 1, 1 \rangle$（4 维），由 Lagrange 四平方定理，每个非负有理数都是四个有理数的平方和，故 $q'$ 表示 7（$7 = 2^2 + 1^2 + 1^2 + 1^2$）。

### 结论

$n \leq 4$ 不可能（核心障碍：限制型 $q' \cong \langle 1, 1, 1 \rangle$ 不表示 7，由 Legendre 三平方定理的 $4^a(8b+7)$ 障碍保证），$n = 5$ 可行。

$$\boxed{n = 5}$$

$\blacksquare$
