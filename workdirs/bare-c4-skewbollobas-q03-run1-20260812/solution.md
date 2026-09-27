# 斜 Bollobás 定理（Frankl 1982）

## 问题

设 $a,b$ 为正整数。给定 $m$ 对有限集合 $(A_1,B_1),(A_2,B_2),\dots,(A_m,B_m)$，满足：

1. $|A_i|\le a,\ |B_i|\le b$；
2. $A_i\cap B_i=\varnothing$ 对所有 $i$ 成立；
3. $A_i\cap B_j\ne\varnothing$ 对所有 $i<j$ 成立。

证明：$m\le \dbinom{a+b}{a}$。

---

## 证明

### 第一步：归约到 $|A_i|=a,\ |B_i|=b$ 的情形

我们可以通过**填充（padding）**将所有集合的大小统一为 $a$ 和 $b$。

**填充方法：** 引入一组全新的元素（不属于任何已有的 $A_j$ 或 $B_j$）。对每个 $i$：
- 若 $|A_i| < a$，向 $A_i$ 中添加 $a - |A_i|$ 个新元素（这些新元素不在 $B_i$ 中，因为它们是全新的）。
- 若 $|B_i| < b$，向 $B_i$ 中添加 $b - |B_i|$ 个新元素（这些新元素不在 $A_i$ 中，因为它们是全新的）。

**验证条件保持不变：**
- **条件 2**（$A_i \cap B_i = \varnothing$）：填充 $A_i$ 时添加的元素不在 $B_i$ 中，填充 $B_i$ 时添加的元素不在 $A_i$ 中，故仍不相交。
- **条件 3**（$A_i \cap B_j \ne \varnothing$ for $i < j$）：填充 $A_i$ 只会增大 $A_i$，不破坏已有的交集；填充 $B_j$ 只会增大 $B_j$，也不破坏已有的交集。而新元素不属于任何其他集合，不影响跨对的交集。

因此，填充后所有条件仍然满足，且 $|A_i| = a$，$|B_i| = b$，$|A_i \cup B_i| = a + b$（因 $A_i \cap B_i = \varnothing$）。

> 若填充后 $m$ 对集合满足条件，则原始的 $m$ 对也满足。反之亦然。因此只需对 $|A_i|=a, |B_i|=b$ 的情形证明 $m \le \binom{a+b}{a}$。

---

### 第二步：外代数（exterior algebra）设置

设 $U = \bigcup_{i=1}^m (A_i \cup B_i)$ 为基础集合，$W = \mathbb{R}^U$ 为以 $U$ 中元素为基的实向量空间。对每个 $x \in U$，记对应的基向量为 $e_x$。

对有限集合 $S = \{s_1, \ldots, s_k\} \subseteq U$（取定某个固定顺序），定义外代数 $\bigwedge W$ 中的元素：
$$e_S = e_{s_1} \wedge e_{s_2} \wedge \cdots \wedge e_{s_k} \in \bigwedge^k W.$$

**外代数的基本性质：**
- 若 $S \cap T \ne \varnothing$，则 $e_S \wedge e_T = 0$（因为某个 $e_x$ 在 wedge 积中重复出现，而 $e_x \wedge e_x = 0$）。
- 若 $S \cap T = \varnothing$，则 $e_S \wedge e_T = \pm\, e_{S \cup T} \ne 0$（所有基向量互异）。

由条件 2 和 3：
- **$e_{A_i} \wedge e_{B_i} \ne 0$**（因 $A_i \cap B_i = \varnothing$），对所有 $i$。
- **$e_{A_i} \wedge e_{B_j} = 0$**（因 $A_i \cap B_j \ne \varnothing$），对所有 $i < j$。

---

### 第三步：随机线性映射到 $\mathbb{R}^{a+b}$

设 $V = \mathbb{R}^{a+b}$。取一个随机线性映射 $\phi: W \to V$，即对每个 $x \in U$，$\phi(e_x)$ 是 $\mathbb{R}^{a+b}$ 中独立同分布的随机向量（例如各分量为 i.i.d. 标准正态分布）。

$\phi$ 诱导外代数间的线性映射 $\bigwedge^k \phi: \bigwedge^k W \to \bigwedge^k V$，满足
$$\bigwedge^k \phi(e_{s_1} \wedge \cdots \wedge e_{s_k}) = \phi(e_{s_1}) \wedge \cdots \wedge \phi(e_{s_k}).$$

**关键事实：** 对每个 $i$，向量组 $\{\phi(e_x) : x \in A_i \cup B_i\}$ 由 $|A_i \cup B_i| = a+b$ 个 $\mathbb{R}^{a+b}$ 中的随机向量组成。它们线性相关的概率为 $0$（$a+b$ 个独立连续随机向量在 $\mathbb{R}^{a+b}$ 中几乎必然线性无关）。由 union bound，对所有 $i = 1, \ldots, m$，它们同时线性独立的概率为 $1$。

因此，**存在**线性映射 $\phi: W \to V$，使得对每个 $i$：
$$\bigwedge_{x \in A_i \cup B_i} \phi(e_x) = \bigwedge^a \phi(e_{A_i}) \wedge \bigwedge^b \phi(e_{B_i}) \ne 0.$$

固定这样一个 $\phi$。

---

### 第四步：反向归纳证明线性无关

定义 $v_i = \bigwedge^a \phi(e_{A_i}) \in \bigwedge^a V$，$w_i = \bigwedge^b \phi(e_{B_i}) \in \bigwedge^b V$。

**断言：** $v_1, v_2, \ldots, v_m$ 在 $\bigwedge^a V$ 中线性无关。

**证明：** 设 $\sum_{i=1}^m c_i\, v_i = 0$，要证所有 $c_i = 0$。

**与 $w_m$ 做 wedge 积：**
$$0 = \left(\sum_{i=1}^m c_i\, v_i\right) \wedge w_m = \sum_{i=1}^m c_i\, (v_i \wedge w_m).$$

- 当 $i < m$ 时：$v_i \wedge w_m = \bigwedge^a\phi(e_{A_i}) \wedge \bigwedge^b\phi(e_{B_m}) = \bigwedge^{a+b}\phi(e_{A_i} \wedge e_{B_m})$。由于 $A_i \cap B_m \ne \varnothing$（条件 3，$i < m$），故 $e_{A_i} \wedge e_{B_m} = 0$，从而 $v_i \wedge w_m = 0$。
- 当 $i = m$ 时：$v_m \wedge w_m = \bigwedge_{x \in A_m \cup B_m} \phi(e_x) \ne 0$（由第三步的选取）。

因此 $c_m \cdot (v_m \wedge w_m) = 0$，即 $c_m = 0$。

**归纳步骤：** 假设 $c_{k+1} = c_{k+2} = \cdots = c_m = 0$（已证），则 $\sum_{i=1}^k c_i\, v_i = 0$。与 $w_k$ 做 wedge 积：

$$0 = \sum_{i=1}^k c_i\, (v_i \wedge w_k).$$

- 当 $i < k$ 时：$A_i \cap B_k \ne \varnothing$（条件 3），故 $v_i \wedge w_k = 0$。
- 当 $i = k$ 时：$v_k \wedge w_k \ne 0$（由第三步）。

因此 $c_k = 0$。

由反向归纳（$k = m, m-1, \ldots, 1$），所有 $c_i = 0$。$\square$

---

### 第五步：维数计数

$v_1, \ldots, v_m$ 是 $\bigwedge^a V = \bigwedge^a \mathbb{R}^{a+b}$ 中的线性无关向量组。

$$\dim \bigwedge^a \mathbb{R}^{a+b} = \binom{a+b}{a}.$$

因此
$$\boxed{m \le \binom{a+b}{a}.}$$

$\blacksquare$　证毕。

---

## 证明思路总结

1. **填充归约**：通过添加新元素，将所有 $|A_i|, |B_i|$ 统一为 $a, b$，条件不破坏。
2. **外代数编码**：$A_i \cap B_j \ne \varnothing \iff e_{A_i} \wedge e_{B_j} = 0$；$A_i \cap B_i = \varnothing \iff e_{A_i} \wedge e_{B_i} \ne 0$。斜条件恰好给出"上三角"结构。
3. **随机投影降维**：将外代数从 $\bigwedge^a \mathbb{R}^{|U|}$（维数 $\binom{|U|}{a}$，太大）投影到 $\bigwedge^a \mathbb{R}^{a+b}$（维数 $\binom{a+b}{a}$），利用 $|A_i \cup B_i| = a+b$ 保证投影后非零性几乎必然保持。
4. **反向归纳**：斜条件 $e_{A_i} \wedge e_{B_j} = 0$（$i < j$）使得从 $m$ 到 $1$ 逐个消去系数，证明线性无关。
5. **维数计数**：线性无关向量数不超过空间维数 $\binom{a+b}{a}$。
