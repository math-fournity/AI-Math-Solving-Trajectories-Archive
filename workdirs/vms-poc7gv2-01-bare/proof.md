# 证明：36 阶群必有非平凡正规子群

**命题.** 设 $G$ 是 36 阶群，则存在 $N \trianglelefteq G$，使得 $N \neq \{e\}$ 且 $N \neq G$。

---

## 证明

注意到 $|G| = 36 = 2^2 \cdot 3^2$。

### Sylow 3-子群的个数

设 $n_3$ 为 $G$ 的 Sylow 3-子群的个数。由 Sylow 定理：

- $n_3 \mid \frac{36}{9} = 4$，
- $n_3 \equiv 1 \pmod{3}$。

满足这两个条件的正整数只有 $n_3 = 1$ 和 $n_3 = 4$。以下分两种情形讨论。

---

### 情形一：$n_3 = 1$

此时 $G$ 有唯一的 Sylow 3-子群 $P$，其阶为 $|P| = 9$。唯一性意味着 $P$ 在共轭作用下不变，即对所有 $g \in G$ 有 $gPg^{-1} = P$，故 $P \trianglelefteq G$。

由于 $|P| = 9$，有 $P \neq \{e\}$（阶为 9）且 $P \neq G$（阶为 36）。因此 $P$ 是 $G$ 的非平凡正规子群。$\square$

---

### 情形二：$n_3 = 4$

设 $G$ 的四个 Sylow 3-子群为 $P_1, P_2, P_3, P_4$。$G$ 通过共轭作用在这些子群上：

$$
G \times \{P_1, P_2, P_3, P_4\} \to \{P_1, P_2, P_3, P_4\}, \quad (g, P_i) \mapsto gP_ig^{-1}.
$$

由 Sylow 定理，共轭作用在 Sylow $p$-子群的集合上是**可迁**的（任意两个 Sylow 3-子群互相共轭），因此该作用诱导出群同态

$$
\varphi: G \to S_4,
$$

其中 $S_4$ 是 4 个元素上的对称群，$|S_4| = 24$。

**像的阶的估计。** 由同态基本定理，$\text{im}(\varphi) \cong G / \ker(\varphi)$，故 $|\text{im}(\varphi)|$ 整除 $|G| = 36$。同时 $\text{im}(\varphi) \leq S_4$，故 $|\text{im}(\varphi)|$ 整除 $|S_4| = 24$。因此

$$
|\text{im}(\varphi)| \mid \gcd(36, 24) = 12.
$$

另一方面，作用是可迁的，由轨道-稳定子定理，轨道大小 $4 = |\text{im}(\varphi)| / |\text{Stab}(P_1)|$，故 $4 \mid |\text{im}(\varphi)|$。

综合这两个条件：

$$
|\text{im}(\varphi)| \in \{4, 12\}.
$$

**核的阶。** 由 $|\ker(\varphi)| = |G| / |\text{im}(\varphi)|$：

- 若 $|\text{im}(\varphi)| = 4$，则 $|\ker(\varphi)| = 36 / 4 = 9$；
- 若 $|\text{im}(\varphi)| = 12$，则 $|\ker(\varphi)| = 36 / 12 = 3$。

**核是非平凡的。** 因为 $|\text{im}(\varphi)| \leq 12 < 36 = |G|$，所以 $|\ker(\varphi)| = 36 / |\text{im}(\varphi)| \geq 3 > 1$，即 $\ker(\varphi) \neq \{e\}$。

**核是真子群。** 若 $\ker(\varphi) = G$，则 $\varphi$ 是平凡同态，意味着每个 $g \in G$ 都固定所有 $P_i$，即每个 Sylow 3-子群都是正规的，从而 $n_3 = 1$，与 $n_3 = 4$ 矛盾。因此 $\ker(\varphi) \neq G$。

**核是正规的。** 同态的核恒为正规子群：$\ker(\varphi) \trianglelefteq G$。

因此 $N = \ker(\varphi)$ 是 $G$ 的非平凡正规子群（阶为 9 或 3）。$\square$

---

### 结论

无论 $n_3 = 1$ 还是 $n_3 = 4$，$G$ 都存在非平凡正规子群：

- $n_3 = 1$ 时，唯一的 Sylow 3-子群（阶 9）是非平凡正规子群；
- $n_3 = 4$ 时，共轭作用同态 $\varphi: G \to S_4$ 的核（阶 9 或 3）是非平凡正规子群。

这穷尽了所有可能情形，故 **36 阶群必有非平凡正规子群**。

$\blacksquare$
