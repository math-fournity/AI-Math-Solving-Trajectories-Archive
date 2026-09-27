# IMO 1985 Problem 6 — 解答

## 题目

对每个实数 $x_1$，定义序列 $\{x_1, x_2, \ldots\}$：
$$x_{n+1} = x_n\!\left(x_n + \frac{1}{n}\right), \quad n \geq 1.$$
证明：存在唯一的 $x_1$，使得对一切 $n \geq 1$ 同时成立
$$0 < x_n, \qquad x_n < x_{n+1}, \qquad x_{n+1} < 1.$$

---

## 条件化简

记 $f_n(x) = x\!\left(x + \tfrac{1}{n}\right) = x^2 + \tfrac{x}{n}$，则 $x_{n+1}=f_n(x_n)$。

**条件 (ii)** $x_n < x_{n+1}$：
$$x_{n+1}-x_n = x_n^2 + \frac{x_n}{n} - x_n = x_n\!\left(x_n + \frac{1}{n} - 1\right) > 0.$$
由 $x_n>0$ 得 $x_n > 1 - \tfrac{1}{n}$。

**条件 (iii)** $x_{n+1} < 1$：
$$x_n^2 + \frac{x_n}{n} < 1.$$
方程 $x^2 + x/n = 1$ 的正根记为
$$a_n = \frac{-\tfrac{1}{n} + \sqrt{\tfrac{1}{n^2}+4}}{2},$$
则条件为 $x_n < a_n$。

**条件 (i)** $0 < x_n$：当 $n\geq 1$ 时 $1-\tfrac{1}{n}\geq 0$，故由 $x_n > 1-\tfrac{1}{n}$ 自动保证。

> **验证** $1 - \tfrac{1}{n} < a_n$：$f_n\!\left(1-\tfrac{1}{n}\right) = \left(1-\tfrac{1}{n}\right)\!\left(1-\tfrac{1}{n}+\tfrac{1}{n}\right) = 1-\tfrac{1}{n} < 1 = f_n(a_n)$，而 $f_n$ 严格递增，故 $1-\tfrac{1}{n} < a_n$。

因此三个条件等价于：
$$\boxed{1 - \frac{1}{n} < x_n < a_n, \quad \forall\, n \geq 1.} \tag{$\ast$}$$

注意 $1-\tfrac{1}{n}\to 1$ 且 $a_n\to 1$（因 $a_n = 1 - \tfrac{1}{2n} + O(n^{-2})$），故满足条件的序列必有 $x_n \to 1$。

---

## 关键函数性质

$f_n(x) = x^2 + x/n$ 在 $(0,\infty)$ 上严格递增（$f_n'(x) = 2x + 1/n > 0$），故存在反函数
$$g_n(y) = \frac{-\tfrac{1}{n}+\sqrt{\tfrac{1}{n^2}+4y}}{2}, \qquad y > 0,$$
同样严格递增。关键值：
- $f_n\!\left(1-\tfrac{1}{n}\right) = 1 - \tfrac{1}{n}$，即 $g_n\!\left(1-\tfrac{1}{n}\right) = 1 - \tfrac{1}{n}$。
- $f_n(a_n) = 1$，即 $g_n(1) = a_n$。

**导数（收缩性）：**
$$g_n'(y) = \frac{1}{\sqrt{\tfrac{1}{n^2}+4y}}.$$
当 $y \geq \tfrac{1}{2}$ 时（注意 $n\geq 2$ 时 $1-\tfrac{1}{n}\geq \tfrac{1}{2}$，$n=1$ 时 $y > 1-\tfrac{1}{2}=\tfrac{1}{2}$）：
$$g_n'(y) \leq \frac{1}{\sqrt{4\cdot\tfrac{1}{2}}} = \frac{1}{\sqrt{2}}. \tag{$\dagger$}$$

---

## 存在性（嵌套区间非空）

对每个 $N\geq 1$，定义 $S_N$ 为满足 $(\ast)$ 中 $n=1,\ldots,N$ 部分的 $x_1$ 全体。我们用反向归纳构造区间 $J_k^{(N)}$（$k=N,N-1,\ldots,1$），使得 $S_N = J_1^{(N)}$。

- **起点**：$J_N^{(N)} = \left(1-\tfrac{1}{N},\; a_N\right)$（$x_N$ 的允许范围）。
- **归纳步**：给定 $J_{k+1}^{(N)} = (l_{k+1},\, u_{k+1})$，令
$$J_k^{(N)} = \left(1-\tfrac{1}{k},\; a_k\right) \cap \bigl(g_k(l_{k+1}),\; g_k(u_{k+1})\bigr).$$
（因 $f_k$ 递增，$x_k \in (g_k(l_{k+1}),g_k(u_{k+1}))$ 等价于 $f_k(x_k) \in (l_{k+1},u_{k+1})$。）

**断言**：每个 $J_k^{(N)}$ 是非空开区间，且 $J_k^{(N)} \subseteq \left(1-\tfrac{1}{k},\, a_k\right)$。

*归纳基础*：$J_N^{(N)} = (1-1/N, a_N) \neq \emptyset$（已验证 $1-1/N < a_N$）。

*归纳步*：设 $J_{k+1}^{(N)} = (l_{k+1}, u_{k+1})$ 非空，则 $l_{k+1} < u_{k+1}$，且由归纳假设
$$1 - \tfrac{1}{k+1} \leq l_{k+1} < u_{k+1} \leq a_{k+1} < 1.$$

需证 $(1-\tfrac{1}{k},\, a_k) \cap (g_k(l_{k+1}),\, g_k(u_{k+1})) \neq \emptyset$，即证：
1. $g_k(l_{k+1}) < a_k$：因 $l_{k+1} < 1 = f_k(a_k)$ 且 $g_k$ 递增，故 $g_k(l_{k+1}) < g_k(1) = a_k$。 ✓
2. $g_k(u_{k+1}) > 1 - \tfrac{1}{k}$：因 $u_{k+1} > l_{k+1} \geq 1-\tfrac{1}{k+1} > 1-\tfrac{1}{k} = f_k(1-\tfrac{1}{k})$ 且 $g_k$ 递增，故 $g_k(u_{k+1}) > g_k(1-\tfrac{1}{k}) = 1-\tfrac{1}{k}$。 ✓

又 $g_k(l_{k+1}) < g_k(u_{k+1})$（$g_k$ 递增），故两区间相交，$J_k^{(N)}$ 非空。且 $J_k^{(N)} \subseteq (1-1/k, a_k)$ 由构造保证。 ✓

因此 $S_N = J_1^{(N)}$ 对所有 $N$ 非空。又 $S_{N+1} \subseteq S_N$（条件更多），故 $\{S_N\}$ 是嵌套非空有界闭区间列（取闭包）。由嵌套区间定理，$\bigcap_N \overline{S_N} \neq \emptyset$，即存在 $x_1$ 满足 $(\ast)$ 对所有 $n$。

---

## 唯一性（区间长度趋于零）

由中值定理，对 $J_{k+1}^{(N)} = (l_{k+1}, u_{k+1})$：
$$\bigl|g_k(u_{k+1}) - g_k(l_{k+1})\bigr| = g_k'(\xi)\,(u_{k+1}-l_{k+1}), \quad \xi \in (l_{k+1}, u_{k+1}).$$

因 $J_{k+1}^{(N)} \subseteq (1-\tfrac{1}{k+1},\, a_{k+1})$，故 $\xi > 1 - \tfrac{1}{k+1} \geq \tfrac{1}{2}$（对 $k\geq 1$）。由 $(\dagger)$：
$$\bigl|J_k^{(N)}\bigr| \leq \bigl|g_k(J_{k+1}^{(N)})\bigr| \leq \frac{1}{\sqrt{2}}\,\bigl|J_{k+1}^{(N)}\bigr|.$$

反复应用（$k=1,2,\ldots,N-1$）：
$$\bigl|S_N\bigr| = \bigl|J_1^{(N)}\bigr| \leq \frac{1}{(\sqrt{2})^{N-1}}\,\bigl|J_N^{(N)}\bigr| = \frac{a_N - (1-\tfrac{1}{N})}{(\sqrt{2})^{N-1}}.$$

因 $a_N - (1-\tfrac{1}{N}) < 1$（实际上 $\sim \tfrac{1}{2N}$），故
$$|S_N| \leq \frac{1}{(\sqrt{2})^{N-1}} \xrightarrow{N\to\infty} 0.$$

因此 $\bigcap_N S_N$ 至多含一个点。结合存在性，**恰含一个点**。

---

## 结论

存在唯一的 $x_1$（数值上 $x_1 \approx 0.44653$），使得由 $x_{n+1} = x_n(x_n + 1/n)$ 定义的序列对所有 $n\geq 1$ 满足 $0 < x_n$、$x_n < x_{n+1}$、$x_{n+1} < 1$。该序列单调递增趋于 $1$。

$\blacksquare$
