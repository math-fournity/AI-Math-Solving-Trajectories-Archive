# 证明：若 $p$ 为素数且 $p \equiv 3 \pmod{4}$，则 $x^2 \equiv -1 \pmod{p}$ 无解

## 定理

设 $p$ 为素数，$p \equiv 3 \pmod{4}$。则同余方程

$$x^2 \equiv -1 \pmod{p}$$

无整数解。

## 证明

采用反证法。

**假设**存在整数 $x$，使得 $x^2 \equiv -1 \pmod{p}$。

### 步骤 1：确定 $x$ 模 $p$ 的阶

由假设 $x^2 \equiv -1 \pmod{p}$，两边再平方得

$$x^4 \equiv (-1)^2 \equiv 1 \pmod{p}.$$

因此 $x$ 模 $p$ 的阶（即满足 $x^k \equiv 1 \pmod{p}$ 的最小正整数 $k$）整除 $4$，故阶 $\operatorname{ord}_p(x) \in \{1, 2, 4\}$。

- 若阶为 $1$，则 $x \equiv 1 \pmod{p}$，于是 $x^2 \equiv 1 \pmod{p}$，与 $x^2 \equiv -1 \pmod{p}$ 矛盾（因为 $p \geq 3$，$1 \not\equiv -1 \pmod{p}$）。
- 若阶为 $2$，则 $x^2 \equiv 1 \pmod{p}$，同样与 $x^2 \equiv -1 \pmod{p}$ 矛盾。

因此 $\operatorname{ord}_p(x) = 4$。

### 步骤 2：利用 Fermat 小定理

由 Fermat 小定理，$x^{p-1} \equiv 1 \pmod{p}$。

阶的基本性质告诉我们：$\operatorname{ord}_p(x) \mid (p-1)$，即 $4 \mid (p-1)$。

### 步骤 3：推出矛盾

由题设 $p \equiv 3 \pmod{4}$，故 $p - 1 \equiv 2 \pmod{4}$，即 $4 \nmid (p-1)$。

这与步骤 2 得到的 $4 \mid (p-1)$ 矛盾。

### 结论

反证假设不成立。因此 $x^2 \equiv -1 \pmod{p}$ 无解。

**证毕。** $\blacksquare$

## 备注

此定理的逆命题也成立：当 $p \equiv 1 \pmod{4}$ 时，$x^2 \equiv -1 \pmod{p}$ 恰有二解。这可由 Wilson 定理或二次互反律得到。合起来便给出了 $-1$ 是模 $p$ 二次剩余的完整判据：

$$-1 \text{ 是模 } p \text{ 的二次剩余} \iff p \equiv 1 \pmod{4}.$$
