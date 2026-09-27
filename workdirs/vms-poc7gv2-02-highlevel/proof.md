# 证明：若 $p$ 是素数且 $p \equiv 3 \pmod{4}$，则 $x^2 \equiv -1 \pmod{p}$ 无解

## 定理

设 $p$ 为素数，$p \equiv 3 \pmod{4}$。则同余方程

$$x^2 \equiv -1 \pmod{p}$$

无整数解。

## 证明

采用**反证法**，并将问题从"解同余方程"翻译到**群论语言**——考察乘法群 $(\mathbb{Z}/p\mathbb{Z})^{*}$ 中元素的阶。

---

### 步骤 1：假设存在解，导出 $x^4 \equiv 1 \pmod{p}$

假设存在整数 $x$ 使得 $x^2 \equiv -1 \pmod{p}$。

由于 $p \equiv 3 \pmod{4}$ 且 $p$ 为素数，故 $p \geqslant 3$，特别地 $p > 2$，因此 $-1 \not\equiv 1 \pmod{p}$。

对 $x^2 \equiv -1 \pmod{p}$ 两边平方，得

$$x^4 \equiv (-1)^2 \equiv 1 \pmod{p}. \tag{1}$$

### 步骤 2：确定 $x$ 在 $(\mathbb{Z}/p\mathbb{Z})^{*}$ 中的阶

首先注意 $x \not\equiv 0 \pmod{p}$：若 $x \equiv 0$，则 $x^2 \equiv 0 \equiv -1 \pmod{p}$，即 $p \mid 1$，与 $p \geqslant 3$ 矛盾。故 $x$ 是乘法群 $(\mathbb{Z}/p\mathbb{Z})^{*}$ 中的元素。

由 $(1)$，$x^4 \equiv 1 \pmod{p}$，故 $x$ 在群 $(\mathbb{Z}/p\mathbb{Z})^{*}$ 中的**阶**（即满足 $x^k \equiv 1 \pmod{p}$ 的最小正整数 $k$）整除 $4$。因此 $\operatorname{ord}(x) \in \{1, 2, 4\}$。

逐一排除：

- **$\operatorname{ord}(x) = 1$**：则 $x \equiv 1 \pmod{p}$，于是 $x^2 \equiv 1 \pmod{p}$，但 $x^2 \equiv -1 \pmod{p}$，故 $1 \equiv -1 \pmod{p}$，即 $p \mid 2$，与 $p \geqslant 3$ 矛盾。排除。

- **$\operatorname{ord}(x) = 2$**：则 $x^2 \equiv 1 \pmod{p}$，但 $x^2 \equiv -1 \pmod{p}$，同样得 $1 \equiv -1 \pmod{p}$，即 $p \mid 2$，矛盾。排除。

因此

$$\operatorname{ord}(x) = 4. \tag{2}$$

### 步骤 3：用 Lagrange 定理导出矛盾

乘法群 $(\mathbb{Z}/p\mathbb{Z})^{*}$ 是有限群，其阶为 $p - 1$（它由 $\{1, 2, \ldots, p-1\}$ 构成）。

由 **Lagrange 定理**：有限群中任意元素的阶整除群的阶。故

$$\operatorname{ord}(x) \mid (p - 1). \tag{3}$$

结合 $(2)$ 与 $(3)$，得

$$4 \mid (p - 1). \tag{4}$$

但由题设 $p \equiv 3 \pmod{4}$，故

$$p - 1 \equiv 2 \pmod{4},$$

即 $4 \nmid (p - 1)$。这与 $(4)$ 矛盾。

### 结论

矛盾说明假设不成立，即不存在整数 $x$ 满足 $x^2 \equiv -1 \pmod{p}$。

**证毕。** $\blacksquare$

---

## 思路说明

本证明的核心是将原始问题**翻译**到群论语言：

| 原始语言 | 翻译后的语言 |
|---|---|
| 解同余方程 $x^2 \equiv -1 \pmod{p}$ | 在群 $(\mathbb{Z}/p\mathbb{Z})^{*}$ 中寻找阶为 $4$ 的元素 |
| 方程有解？ | 群中是否存在 $4$ 阶元？ |
| 直接枚举验证 | Lagrange 定理：元素阶整除群阶 |

翻译后问题变得几乎显然：$4$ 阶元存在当且仅当 $4 \mid (p-1)$，而 $p \equiv 3 \pmod{4}$ 恰好排除了这一可能。
