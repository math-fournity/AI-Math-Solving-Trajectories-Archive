# 证明：若 $p$ 是素数且 $p \equiv 3 \pmod{4}$，则 $x^2 \equiv -1 \pmod{p}$ 无解

## 定理

设 $p$ 是素数且 $p \equiv 3 \pmod{4}$。证明：同余方程

$$x^2 \equiv -1 \pmod{p}$$

无整数解。

## 证明

采用反证法。假设存在整数 $x$，使得

$$x^2 \equiv -1 \pmod{p}. \tag{$\star$}$$

### 步骤 1：$x$ 与 $p$ 互素，故 $x \in \mathbb{Z}_p^*$

若 $p \mid x$，则 $x^2 \equiv 0 \pmod{p}$，而由 $(\star)$ 有 $x^2 \equiv -1 \pmod{p}$，故 $0 \equiv -1 \pmod{p}$，即 $p \mid 1$。这与 $p$ 是素数（$p \geq 2$）矛盾。

因此 $p \nmid x$，即 $\gcd(x, p) = 1$，于是 $x$ 在模 $p$ 的乘法群

$$\mathbb{Z}_p^* = \{1, 2, \ldots, p-1\}$$

中是一个元素。该群的阶为 $|\mathbb{Z}_p^*| = p - 1$。

### 步骤 2：$x$ 在 $\mathbb{Z}_p^*$ 中的阶整除 4

由 $(\star)$，$x^2 \equiv -1 \pmod{p}$，两边再平方：

$$x^4 = (x^2)^2 \equiv (-1)^2 = 1 \pmod{p}.$$

因此 $x^4 \equiv 1 \pmod{p}$，即 $x$ 在 $\mathbb{Z}_p^*$ 中的阶 $\operatorname{ord}(x)$ 整除 4。

### 步骤 3：$x$ 的阶恰好为 4

4 的正因子为 $1, 2, 4$。我们逐一排除 $\operatorname{ord}(x) = 1$ 和 $\operatorname{ord}(x) = 2$。

- **$\operatorname{ord}(x) \neq 1$**：若 $\operatorname{ord}(x) = 1$，则 $x \equiv 1 \pmod{p}$，故 $x^2 \equiv 1 \pmod{p}$。但由 $(\star)$，$x^2 \equiv -1 \pmod{p}$，于是 $1 \equiv -1 \pmod{p}$，即 $p \mid 2$。由于 $p \equiv 3 \pmod{4}$，故 $p \geq 3$，矛盾。

- **$\operatorname{ord}(x) \neq 2$**：若 $\operatorname{ord}(x) = 2$，则 $x^2 \equiv 1 \pmod{p}$。同样由 $(\star)$ 得 $x^2 \equiv -1 \pmod{p}$，于是 $1 \equiv -1 \pmod{p}$，即 $p \mid 2$，与 $p \geq 3$ 矛盾。

因此 $\operatorname{ord}(x) = 4$。

### 步骤 4：由 Lagrange 定理推出 $4 \mid (p-1)$

**Lagrange 定理**：有限群中任意元素的阶整除群的阶。

$\mathbb{Z}_p^*$ 是阶为 $p - 1$ 的有限群，$x \in \mathbb{Z}_p^*$ 且 $\operatorname{ord}(x) = 4$。由 Lagrange 定理：

$$4 \mid (p - 1).$$

### 步骤 5：$p \equiv 3 \pmod{4}$ 与 $4 \mid (p-1)$ 矛盾

由 $p \equiv 3 \pmod{4}$，可设 $p = 4k + 3$（$k \geq 0$ 为整数），则

$$p - 1 = 4k + 2 = 2(2k + 1).$$

因此

$$(p - 1) \bmod 4 = 2,$$

即 $4 \nmid (p - 1)$。

这与步骤 4 得出的 $4 \mid (p - 1)$ 矛盾。

### 结论

矛盾说明假设不成立，即不存在整数 $x$ 满足 $x^2 \equiv -1 \pmod{p}$。

**证毕。** $\blacksquare$

## 备注

本证明的核心是 Lagrange 定理在乘法群 $\mathbb{Z}_p^*$ 上的应用。证明的关键链条为：

$$x^2 \equiv -1 \pmod{p} \;\Longrightarrow\; \operatorname{ord}(x) = 4 \;\Longrightarrow\; 4 \mid (p-1) \;\Longrightarrow\; p \equiv 1 \pmod{4}.$$

取逆否命题即得：若 $p \equiv 3 \pmod{4}$，则 $x^2 \equiv -1 \pmod{p}$ 无解。

事实上，这个论证还证明了更强的结论：$x^2 \equiv -1 \pmod{p}$ 有解当且仅当 $p = 2$ 或 $p \equiv 1 \pmod{4}$（其中 $p = 2$ 时 $x = 1$ 是解）。
