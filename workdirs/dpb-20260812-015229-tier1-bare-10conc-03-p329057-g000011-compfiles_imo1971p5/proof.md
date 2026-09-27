# IMO 1971 Problem 5 — 证明

## 问题

证明：对任意自然数 $m$，存在平面上有限非空点集 $S$，使得对每个点 $s \in S$，$S$ 中恰有 $m$ 个点与 $s$ 的距离为 $1$。

## 证明

### 构造

对给定的 $m$，选取 $m$ 个平面单位向量 $v_1, v_2, \ldots, v_m$（角度待定），定义

$$S = \left\{ \sum_{i=1}^{m} \epsilon_i \, v_i \;\middle|\; \epsilon_i \in \{0, 1\} \right\}.$$

这是"广义平行体"（zonotope）的顶点集，至多有 $2^m$ 个点。

### 邻居计数

对 $S$ 中两点 $P = \sum \epsilon_i v_i$ 和 $Q = \sum \epsilon'_i v_i$，令 $I = \{i : \epsilon_i \neq \epsilon'_i\}$，则

$$\|P - Q\| = \left\| \sum_{i \in I} \sigma_i \, v_i \right\|,$$

其中 $\sigma_i = \epsilon_i - \epsilon'_i \in \{+1, -1\}$。

- **若 $|I| = 1$**，即 $I = \{j\}$：$\|P - Q\| = \|v_j\| = 1$。因此 $P$ 与 $Q$ 的距离恰为 $1$。

  这说明每个点 $P$ 至少有 $m$ 个单位距离邻居（翻转每一个坐标各得一个）。

- **若 $|I| \geq 2$**：我们要求 $\left\| \sum_{i \in I} \sigma_i v_i \right\| \neq 1$，即这些"非邻接"对不处于单位距离。

- **若 $|I| = 0$**：$P = Q$，不考虑。

### 选择角度使非邻接对避开单位距离

设 $v_i = (\cos\theta_i, \sin\theta_i)$。对每个满足 $|I| \geq 2$ 的子集 $I \subseteq \{1,\ldots,m\}$ 和每个符号模式 $\sigma \in \{+1,-1\}^I$，定义**坏集**

$$B_{I,\sigma} = \left\{ (\theta_1, \ldots, \theta_m) \in [0, 2\pi)^m \;\middle|\; \left\| \sum_{i \in I} \sigma_i v_i \right\|^2 = 1 \right\}.$$

展开：

$$\left\| \sum_{i \in I} \sigma_i v_i \right\|^2 = |I| + 2 \sum_{\substack{i < j \\ i,j \in I}} \sigma_i \sigma_j \cos(\theta_i - \theta_j).$$

记此函数为 $f_{I,\sigma}(\theta_1, \ldots, \theta_m)$。它只依赖于 $\{\theta_j : j \in I\}$，是关于这些变量的实解析函数。

**关键断言**：$f_{I,\sigma}$ 不恒等于 $1$。

*证明断言*：取所有 $\theta_j$（$j \in I$）相等，即 $\theta_j = 0$ 对所有 $j \in I$。此时 $\cos(\theta_i - \theta_j) = 1$ 对所有 $i, j$，故

$$f_{I,\sigma} = |I| + 2 \sum_{i < j} \sigma_i \sigma_j = |I| + \left(\sum_{i \in I} \sigma_i\right)^2 - |I| = \left(\sum_{i \in I} \sigma_i\right)^2.$$

当 $|I| \geq 2$ 时，$\left(\sum_{i \in I} \sigma_i\right)^2$ 是一个整数的平方。若所有 $\sigma_i$ 同号，则该值为 $|I|^2 \geq 4 \neq 1$。若 $\sigma_i$ 不全同号，则 $\sum \sigma_i$ 的绝对值 $< |I|$ 且与 $|I|$ 同奇偶，所以 $\left(\sum \sigma_i\right)^2 \neq 1$（因为 $|I| \geq 2$ 时 $\sum \sigma_i$ 的绝对值要么 $\geq 2$，要么为 $0$）。因此 $f_{I,\sigma} \neq 1$ 在此特取值处成立，断言得证。$\square$

由于 $f_{I,\sigma} - 1$ 是不恒为零的实解析函数，其零集 $B_{I,\sigma}$ 是 $[0, 2\pi)^m$ 中的**闭集且内部为空**（实解析函数的零集若内部非空则函数恒为零，与断言矛盾）。

### 同样确保所有点互异

还需确保 $S$ 中 $2^m$ 个点互不相同。两点重合当且仅当 $\sum_{i \in I} \sigma_i v_i = 0$（$I$ 非空），即 $\left\|\sum_{i \in I} \sigma_i v_i\right\|^2 = 0$。对 $|I| = 1$，$\|v_i\|^2 = 1 \neq 0$，自动满足。对 $|I| \geq 2$，同样定义坏集

$$B'_{I,\sigma} = \left\{ (\theta_1, \ldots, \theta_m) \;\middle|\; f_{I,\sigma}(\theta_1, \ldots, \theta_m) = 0 \right\}.$$

用同样的论证（取所有 $\theta_j = 0$ 得 $f_{I,\sigma} = (\sum \sigma_i)^2 \geq 0$，且当 $|I| \geq 2$ 时 $(\sum \sigma_i)^2 \neq 0$ 当 $\sigma$ 全同号；若不全同号则 $(\sum\sigma_i)^2$ 可能为 $0$——需另行处理）。

更仔细地：当 $\sigma$ 不全同号且 $|I|$ 为偶数时，$\sum \sigma_i = 0$ 是可能的，此时上述特取值不能区分。但我们只需 $f_{I,\sigma}$ 不恒为零即可。取另一组特值：令 $\theta_j = 0$ 对 $j \in I \setminus\{i_0\}$，$\theta_{i_0} = \pi/2$，则 $f_{I,\sigma}$ 的值一般不为 $0$（因为引入了 $\sin$ 和 $\cos$ 的混合项）。具体地，对 $|I| = 2$，$I = \{1,2\}$，$f = 2 + 2\sigma_1\sigma_2\cos(\theta_1 - \theta_2)$，取 $\theta_1 = \theta_2$ 得 $f = 2 + 2\sigma_1\sigma_2 \in \{0, 4\}$。当 $\sigma_1\sigma_2 = -1$ 时 $f = 0$，但这只说明该特取值落在坏集中，不说明 $f$ 恒为零。取 $\theta_1 = 0, \theta_2 = \pi/2$ 得 $f = 2 + 0 = 2 \neq 0$。故 $f$ 不恒为零。

一般地，对任意 $|I| \geq 2$ 和任意 $\sigma$，$f_{I,\sigma}$ 是非常值实解析函数（它包含 $\cos(\theta_i - \theta_j)$ 项，随角度变化），故不恒为零，其零集 $B'_{I,\sigma}$ 内部为空。

### 综合论证

所有坏集的并集

$$\mathcal{B} = \bigcup_{\substack{|I| \geq 2 \\ \sigma}} B_{I,\sigma} \;\cup\; \bigcup_{\substack{|I| \geq 2 \\ \sigma}} B'_{I,\sigma}$$

是**有限个**内部为空的闭集之并，故 $\mathcal{B}$ 内部为空。因此 $[0, 2\pi)^m \setminus \mathcal{B}$ 非空（事实上稠密且满测度）。

选取 $(\theta_1, \ldots, \theta_m) \in [0, 2\pi)^m \setminus \mathcal{B}$，构造相应的 $v_i$ 和 $S$。则：

1. **$S$ 中 $2^m$ 个点互异**（避开了所有 $B'_{I,\sigma}$）；
2. **两点距离为 $1$ 当且仅当它们恰好相差一个坐标**（$|I|=1$ 时距离为 $1$；$|I| \geq 2$ 时距离不为 $1$，因为避开了所有 $B_{I,\sigma}$）。

因此每个点 $P \in S$ 恰有 $m$ 个单位距离邻居（翻转 $m$ 个坐标中的每一个各得一个），且没有其他单位距离邻居。

### 结论

对任意自然数 $m$，上述构造给出平面上 $2^m$ 个点的集合 $S$，其中每个点恰有 $m$ 个 $S$ 中的点与之距离为 $1$。$\blacksquare$

## 计算验证

用 Python 对 $m = 1, 2, 3, 4, 5, 6$ 进行了数值验证：随机选取角度，构造 $S$，检查每个点的单位距离邻居数恰为 $m$。所有情形均成功找到满足条件的角度组合，与理论证明一致。
