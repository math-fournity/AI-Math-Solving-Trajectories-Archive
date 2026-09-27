# 解答

## 问题

证明：对所有充分大的整数 $N$，存在集合 $A\subset\{1,2,\dots,N\}$ 满足 $|A|\ge \frac{1}{100}\sqrt{N\log N}$，并且对每个整数 $s$，方程 $a+b=s,\ a,b\in A,\ a<b$ 的解的个数不超过 $20\log N$。

## 证明

我们用**概率方法**（probabilistic method）。构造一个随机子集 $B\subset\{1,2,\dots,N\}$，其中每个元素独立地以概率 $p$ 被选中，然后证明以正概率同时满足两个条件。

### 参数选取

取
$$
p = 3\sqrt{\frac{\log N}{N}}.
$$
当 $N$ 充分大时，$p \le 1$（具体地，需要 $N \ge 9\log N$，这对 $N \ge 100$ 成立）。

### 第一步：$|B|$ 的下界

$|B|$ 服从二项分布 $\operatorname{Bin}(N, p)$，期望为
$$
\mu_B = \mathbb{E}[|B|] = Np = 3\sqrt{N\log N}.
$$

由 Chernoff 不等式（乘法形式：$\Pr[X \le \mu/2] \le e^{-\mu/8}$），
$$
\Pr\!\left[|B| < \frac{3}{2}\sqrt{N\log N}\right] = \Pr\!\left[|B| < \frac{\mu_B}{2}\right] \le e^{-\mu_B/8} = e^{-\frac{3}{8}\sqrt{N\log N}}.
$$

当 $N\to\infty$ 时，$\frac{3}{8}\sqrt{N\log N}\to\infty$，故此概率趋于 $0$。

### 第二步：每个和的表示数上界

对每个整数 $s$，定义随机变量
$$
X_s = \#\{(a,b) : a, b \in B,\ a < b,\ a+b = s\}.
$$

对固定的 $s$，满足 $a < b$、$a+b=s$、$1\le a,b\le N$ 的候选对 $(a,b)$ 的个数记为 $m_s$。这些对中 $a$ 的取值范围为 $\max(1, s-N) \le a \le \lfloor(s-1)/2\rfloor$，故
$$
m_s \le \frac{N}{2}.
$$

每个候选对 $(a,b)$ 同时属于 $B$ 的概率为 $p^2$。

**关键观察：这些候选对两两不相交（不共享任何元素）。**

事实上，候选对形如 $(a, s-a)$，其中 $a < s/2$。设 $(a, s-a)$ 和 $(a', s-a')$ 是两个不同的对（$a \ne a'$）。若它们共享某元素，则有以下可能：
- $a = a'$：不可能，因为 $a \ne a'$；
- $a = s - a'$：则 $a + a' = s$，但 $a < s/2$ 且 $a' < s/2$ 推出 $a + a' < s$，矛盾；
- $s - a = a'$：同上，$a + a' = s$，矛盾；
- $s - a = s - a'$：则 $a = a'$，矛盾。

因此所有候选对两两不相交，对应的指示随机变量 $Y_i = \mathbf{1}[\text{第 }i\text{ 个对的两元素都在 }B]$ 是**完全独立**的 Bernoulli 随机变量。于是 $X_s$ 服从二项分布 $\operatorname{Bin}(m_s, p^2)$，期望为
$$
\mu_s = \mathbb{E}[X_s] = m_s \cdot p^2 \le \frac{N}{2} \cdot \frac{9\log N}{N} = \frac{9}{2}\log N.
$$

我们需证 $\Pr[X_s \ge 20\log N]$ 很小。注意
$$
20\log N \ge 2 \cdot \frac{9}{2}\log N = 9\log N \ge 2\mu_s.
$$

由 Chernoff 不等式（$\Pr[X \ge 2\mu] \le e^{-\mu/3}$），
$$
\Pr[X_s \ge 20\log N] \le \Pr[X_s \ge 2\mu_s] \le e^{-\mu_s/3} \le e^{-\frac{9}{6}\log N} = e^{-\frac{3}{2}\log N} = N^{-3/2}.
$$

### 第三步：联合控制所有和

和 $s$ 的可能取值范围为 $3 \le s \le 2N-1$（因为 $a \ge 1, b \ge 2, a < b$，最小和为 $1+2=3$；最大和为 $(N-1)+N=2N-1$），共至多 $2N$ 个值。

由联合界（union bound），
$$
\Pr\!\left[\exists\, s:\ X_s \ge 20\log N\right] \le 2N \cdot N^{-3/2} = 2N^{-1/2}.
$$

当 $N\to\infty$ 时，$2N^{-1/2}\to 0$。

### 第四步：综合

综合第一步和第三步，
$$
\Pr\!\left[|B| < \frac{3}{2}\sqrt{N\log N}\ \text{或}\ \exists\, s:\ X_s \ge 20\log N\right] \le e^{-\frac{3}{8}\sqrt{N\log N}} + 2N^{-1/2}.
$$

当 $N$ 充分大时，右端 $< 1$。因此，以正概率，以下两条件**同时**成立：

1. $|B| \ge \frac{3}{2}\sqrt{N\log N} \ge \frac{1}{100}\sqrt{N\log N}$；
2. 对所有整数 $s$，$X_s \le 20\log N$。

取 $A = B$，即得所求集合。

$\square$

### 证毕

**注**：常数 $3$（即 $p$ 中的系数 $c=3$）的选择并非最优。关键约束是 $c^2/3 > 1$（即 $c > \sqrt{3}$），以保证联合界趋于 $0$。取 $c=3$ 留有充分余量。实际上，$|B|$ 的期望 $3\sqrt{N\log N}$ 远超所需的 $\frac{1}{100}\sqrt{N\log N}$，而表示数上界 $9\log N$（即 $2\mu_s$）也远低于允许的 $20\log N$。
