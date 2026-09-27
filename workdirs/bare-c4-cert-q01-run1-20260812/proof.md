# Q-C4-01 证明：无三角形图上 $\sum_{uv\in E} x_u x_v \le \dfrac14$

## 定理

设 $G=(V,E)$ 是没有三角形的有限简单图。对每个顶点 $v\in V$ 赋非负实数 $x_v$，满足 $\sum_{v\in V} x_v = 1$。则

$$
\sum_{uv\in E} x_u x_v \le \frac14,
$$

且等号可以达到。

---

## 证明

记 $f(x) = \sum_{uv\in E} x_u x_v$。我们在单纯形

$$
\Delta = \Big\{x\in\mathbb{R}_{\ge 0}^{V} : \sum_{v\in V} x_v = 1\Big\}
$$

上最大化 $f$。$\Delta$ 紧致、$f$ 连续，故最大值存在。取一个最大化点 $x^*\in\Delta$，令其**支撑**为

$$
S = \{v \in V : x^*_v > 0\}.
$$

### 第一步：支撑可归约为团（Motzkin–Straus 合并引理）

**断言。** 存在一个最大化点 $x^*$，其支撑 $S$ 在 $G$ 中导出一个**团**（完全子图）。

**证明断言。** 在所有最大化点中取一个支撑 $|S|$ 最小的点 $x^*$。我们证明 $S$ 是团。

反设 $S$ 不是团，即存在 $u, v \in S$ 且 $uv \notin E$。对参数 $t$ 定义扰动 $x(t)$：

$$
x(t)_u = x^*_u + t,\quad x(t)_v = x^*_v - t,\quad x(t)_w = x^*_w\ (w\ne u,v).
$$

当 $t\in[-x^*_u,\, x^*_v]$ 时 $x(t)\in\Delta$。由于 $uv\notin E$，$f$ 中不含 $x_u x_v$ 项，故

$$
f(x(t)) - f(x^*) = t\Big(\sum_{w\sim u} x^*_w - \sum_{w\sim v} x^*_w\Big),
$$

这是关于 $t$ 的**线性**函数（没有 $t^2$ 项，因为 $uv\notin E$）。记

$$
d_u = \sum_{w\sim u} x^*_w,\qquad d_v = \sum_{w\sim v} x^*_w.
$$

- 若 $d_u \ne d_v$，则取 $t$ 与 $d_u - d_v$ 同号、且在允许区间内非零，便得 $f(x(t)) > f(x^*)$，与 $x^*$ 的最大化矛盾。
- 故必有 $d_u = d_v$。

此时 $f(x(t)) = f(x^*)$ 对所有允许的 $t$ 成立。取 $t = x^*_v$（即把 $v$ 的全部权重移到 $u$），得到新点 $x'$：

$$
x'_u = x^*_u + x^*_v > 0,\quad x'_v = 0,\quad x'_w = x^*_w\ (w\ne u,v).
$$

则 $f(x') = f(x^*)$，$x'$ 仍为最大化点，但其支撑 $S' = S\setminus\{v\}$ 比 $S$ 小，与 $|S|$ 的最小性矛盾。

因此 $S$ 必为团。$\quad\square$

### 第二步：团上的上界

由第一步，不妨设最大化点 $x^*$ 的支撑 $S$ 是一个 $k$-团（$k=|S|$）。在团上，

$$
f(x^*) = \sum_{\{u,v\}\subseteq S} x^*_u x^*_v = \frac{1}{2}\bigg[\Big(\sum_{v\in S} x^*_v\Big)^2 - \sum_{v\in S} (x^*_v)^2\bigg] = \frac{1}{2}\bigg[1 - \sum_{v\in S} (x^*_v)^2\bigg].
$$

由 Cauchy–Schwarz（或 QM–AM），

$$
\sum_{v\in S} (x^*_v)^2 \ge \frac{1}{k}\Big(\sum_{v\in S} x^*_v\Big)^2 = \frac{1}{k},
$$

等号当且仅当 $x^*_v = 1/k$ 对所有 $v\in S$ 成立。因此

$$
f(x^*) \le \frac{1}{2}\Big(1 - \frac{1}{k}\Big). \tag{$*$}
$$

### 第三步：无三角形条件给出 $k\le 2$

$G$ 无三角形，即不含 $K_3$。$S$ 是 $G$ 中的团，故 $S$ 也不能含 $K_3$，从而 $|S|=k\le 2$（$K_3$ 恰为三角形）。

- $k=1$：$f(x^*)=0\le 1/4$。
- $k=2$：由 $(*)$，$f(x^*)\le \frac12\big(1-\frac12\big)=\frac14$。

综上，对任意满足条件的赋权，

$$
\sum_{uv\in E} x_u x_v \le \frac14.
$$

### 第四步：等号可以达到

取 $G$ 中任意一条边 $uv\in E$（若 $E=\varnothing$，则 $f\equiv 0$，上式平凡成立）。令

$$
x_u = x_v = \frac12,\qquad x_w = 0\ (w\ne u,v).
$$

则 $\sum_{v\in V} x_v = 1$，且

$$
\sum_{ab\in E} x_a x_b = x_u x_v = \frac12\cdot\frac12 = \frac14.
$$

故上界 $\frac14$ 是紧的。$\quad\blacksquare$

---

## 注记

本定理是 **Motzkin–Straus 定理**（1965）在团数 $\omega(G)=2$ 时的特例。Motzkin–Straus 定理的一般形式为：对任意有限简单图 $G$，

$$
\max_{\substack{x_v\ge 0\\ \sum x_v=1}} \sum_{uv\in E} x_u x_v = \frac{1}{2}\Big(1 - \frac{1}{\omega(G)}\Big),
$$

其中 $\omega(G)$ 是 $G$ 的团数（最大团的大小）。无三角形 $\Leftrightarrow$ $\omega(G)\le 2$，代入即得 $\frac14$。本证明即 Motzkin–Straus 原始论证在该参数下的直接展开。
