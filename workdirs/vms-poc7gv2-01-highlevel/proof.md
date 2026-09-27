# 证明：36 阶群必有非平凡正规子群

**定理.** 设 $G$ 是 36 阶群，则存在 $N \trianglelefteq G$，使得 $N \neq \{e\}$ 且 $N \neq G$。

---

## 证明

$|G| = 36 = 2^2 \cdot 3^2$。

设 $n_3$ 为 $G$ 中 Sylow 3-子群的个数。由 Sylow 定理：

$$n_3 \equiv 1 \pmod{3}, \qquad n_3 \mid 4.$$

因此 $n_3 \in \{1, 4\}$。分两种情形讨论。

### 情形一：$n_3 = 1$

设 $P$ 为 $G$ 唯一的 Sylow 3-子群，则 $|P| = 3^2 = 9$。

由于 $P$ 是唯一的 Sylow 3-子群，对任意 $g \in G$，$gPg^{-1}$ 也是 Sylow 3-子群，故 $gPg^{-1} = P$，即 $P \trianglelefteq G$。

又 $|P| = 9 \neq 1$ 且 $|P| = 9 \neq 36$，故 $P$ 是 $G$ 的非平凡正规子群。

### 情形二：$n_3 = 4$

设 $\mathcal{S} = \{P_1, P_2, P_3, P_4\}$ 为 $G$ 的全部 Sylow 3-子群。

**翻译到同态语言.** $G$ 通过共轭作用在 $\mathcal{S}$ 上：$g \cdot P_i = gP_ig^{-1}$。这给出同态

$$\varphi : G \longrightarrow \mathrm{Sym}(\mathcal{S}) \cong S_4.$$

同态的核

$$\ker(\varphi) = \{g \in G : gP_ig^{-1} = P_i,\ \forall\, i=1,\dots,4\} = \bigcap_{i=1}^{4} N_G(P_i)$$

是 $G$ 的正规子群（同态核恒为正规子群）。

**核的非平凡性.** 由第一同构定理，$|\varphi(G)| = |G|/|\ker(\varphi)|$，故 $|\varphi(G)| \mid |G| = 36$。又 $\varphi(G) \leqslant S_4$，故 $|\varphi(G)| \mid |S_4| = 24$。因此

$$|\varphi(G)| \mid \gcd(36, 24) = 12.$$

于是

$$|\ker(\varphi)| = \frac{36}{|\varphi(G)|} \geqslant \frac{36}{12} = 3 > 1.$$

故 $\ker(\varphi)$ 是非平凡的。

**核不等于 $G$.** 若 $\ker(\varphi) = G$，则 $\varphi$ 为平凡同态，即共轭作用平凡，所有 Sylow 3-子群在共轭下不动，这意味着 $n_3 = 1$，与 $n_3 = 4$ 矛盾。故 $\ker(\varphi) \neq G$。

因此 $\ker(\varphi)$ 是 $G$ 的非平凡正规子群。

### 结论

无论 $n_3 = 1$ 还是 $n_3 = 4$，$G$ 都存在非平凡正规子群。

$$\boxed{N \trianglelefteq G,\quad N \neq \{e\},\quad N \neq G.}$$

证毕。$\blacksquare$
