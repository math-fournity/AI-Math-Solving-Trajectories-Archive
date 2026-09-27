# 证明：36 阶群必有非平凡正规子群

**定理.** 设 $G$ 是 36 阶群，则存在 $N \trianglelefteq G$，$N \neq \{e\}$，$N \neq G$。

---

## 证明

对 $|G| = 36 = 2^2 \times 3^2$ 做 Sylow 分析。

### Sylow 3-子群的个数

设 $n_3$ 为 $G$ 的 Sylow 3-子群的个数。由 Sylow 定理：

- $n_3 \mid \frac{36}{9} = 4$，即 $n_3 \mid 4$；
- $n_3 \equiv 1 \pmod{3}$。

$4$ 的约数为 $\{1, 2, 4\}$，其中满足 $\equiv 1 \pmod{3}$ 的只有 $1$ 和 $4$。故

$$n_3 \in \{1, 4\}.$$

### 情形一：$n_3 = 1$

此时 $G$ 有唯一的 Sylow 3-子群 $P$，$|P| = 9$。唯一性意味着 $P$ 在共轭作用下不变，即对所有 $g \in G$，$gPg^{-1} = P$，故 $P \trianglelefteq G$。

$P$ 的阶为 $9$，故 $P \neq \{e\}$；$P$ 的阶为 $9 < 36$，故 $P \neq G$。

因此 $P$ 即为所求的非平凡正规子群。$\square$

### 情形二：$n_3 = 4$

设 $G$ 的四个 Sylow 3-子群为 $P_1, P_2, P_3, P_4$，记 $\operatorname{Syl}_3(G) = \{P_1, P_2, P_3, P_4\}$。

**共轭作用.** $G$ 通过共轭作用在 $\operatorname{Syl}_3(G)$ 上：$g \cdot P_i = gP_ig^{-1}$。由 Sylow 定理，共轭作用在 Sylow 3-子群的集合上保持不变（Sylow 3-子群的共轭仍是 Sylow 3-子群），故这是一个良定义的群作用。

此作用给出同态

$$\varphi : G \longrightarrow S_4,$$

其中 $S_4$ 是 $\{P_1, P_2, P_3, P_4\}$ 上的对称群。由同态基本定理，

$$G / \ker(\varphi) \cong \operatorname{im}(\varphi) \leqslant S_4.$$

特别地，$\ker(\varphi) \trianglelefteq G$。下面证明 $\ker(\varphi)$ 是非平凡且非全体的。

**$\ker(\varphi) \neq G$.** $\ker(\varphi) = G$ 意味着每个 $g \in G$ 都固定所有的 $P_i$，即 $gP_ig^{-1} = P_i$ 对所有 $i$ 成立，亦即每个 $P_i$ 都是 $G$ 的正规子群。但正规子群总是唯一的（若 $P_i \trianglelefteq G$，则 $P_i$ 是唯一的 Sylow 3-子群），这与 $n_3 = 4 > 1$ 矛盾。故 $\ker(\varphi) \neq G$。

**$\ker(\varphi) \neq \{e\}$.** 若 $\ker(\varphi) = \{e\}$，则 $\varphi$ 是单射，$G$ 同构于 $S_4$ 的一个子群，从而 $|G| \mid |S_4|$。但

$$|G| = 36, \quad |S_4| = 24, \quad 36 \nmid 24,$$

矛盾。故 $\ker(\varphi) \neq \{e\}$。

**结论.** $\ker(\varphi)$ 是 $G$ 的正规子群，且 $\{e\} \subsetneq \ker(\varphi) \subsetneq G$，即 $\ker(\varphi)$ 是 $G$ 的非平凡正规子群。$\square$

---

## 综合

无论 $n_3 = 1$ 还是 $n_3 = 4$，$G$ 都存在非平凡正规子群：

- $n_3 = 1$ 时，唯一的 Sylow 3-子群 $P$（阶 $9$）即为非平凡正规子群；
- $n_3 = 4$ 时，共轭作用 $\varphi: G \to S_4$ 的核 $\ker(\varphi)$ 即为非平凡正规子群。

因此，**任意 36 阶群 $G$ 都有非平凡正规子群**。

**证毕.** $\blacksquare$
