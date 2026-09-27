# 解答

## 问题重述

板上写着 $(x-1)(x-2)\cdots(x-2016)=(x-1)(x-2)\cdots(x-2016)$。擦除两边的一些线性因子，使每边至少剩一个因子，且结果方程无实根。求最少擦除数。

## 答案

**最少擦除数为 $2016$。**

---

## 证明

### 第一步：下界——擦除数 $\geq 2016$

擦除后，左边保留因子对应集合 $A \subseteq \{1,2,\ldots,2016\}$，右边保留因子对应集合 $B \subseteq \{1,2,\ldots,2016\}$，需 $A \neq \emptyset$，$B \neq \emptyset$。方程为

$$\prod_{a \in A}(x-a) = \prod_{b \in B}(x-b).$$

擦除数 $= 4032 - |A| - |B|$。

**断言：$A \cap B = \emptyset$。**

若存在 $k \in A \cap B$，则 $x = k$ 时两边均为 $0$，$0 = 0$ 成立，故 $x = k$ 是方程的实根，矛盾。因此 $A \cap B = \emptyset$。

由此 $|A| + |B| \leq 2016$，擦除数 $= 4032 - |A| - |B| \geq 4032 - 2016 = \boxed{2016}$。

### 第二步：构造——模 4 分类

取

$$A = \{k \in \{1,\ldots,2016\} : k \equiv 0 \text{ 或 } 1 \pmod{4}\}, \quad B = \{k \in \{1,\ldots,2016\} : k \equiv 2 \text{ 或 } 3 \pmod{4}\}.$$

具体地，$A = \{1, 4, 5, 8, 9, 12, 13, \ldots, 2013, 2016\}$，$B = \{2, 3, 6, 7, 10, 11, \ldots, 2014, 2015\}$。

- $|A| = 504 \times 2 = 1008$，$|B| = 504 \times 2 = 1008$。
- $A \cap B = \emptyset$，$A \cup B = \{1, \ldots, 2016\}$。
- 擦除数 $= 4032 - 1008 - 1008 = 2016$。

### 第三步：证明方程无实根

将因子按 $4$ 个一组分块。对 $j = 0, 1, \ldots, 503$，令

$$P_j = (x-(4j+1))(x-(4j+4)), \quad Q_j = (x-(4j+2))(x-(4j+3)).$$

则 $\prod_{a \in A}(x-a) = \prod_{j=0}^{503} P_j$，$\prod_{b \in B}(x-b) = \prod_{j=0}^{503} Q_j$。

**关键恒等式：** $Q_j = P_j + 2$ 对所有 $j$ 成立。

*证明：* $P_j = x^2 - (8j+5)x + (4j+1)(4j+4)$，$Q_j = x^2 - (8j+5)x + (4j+2)(4j+3)$。两式 $x^2$ 和 $x$ 的系数相同，常数项之差为

$$(4j+2)(4j+3) - (4j+1)(4j+4) = (16j^2+20j+6) - (16j^2+20j+4) = 2. \quad \square$$

令 $u_j = \left(x - 4j - \dfrac{5}{2}\right)^2 \geq 0$，则

$$P_j = u_j - \frac{9}{4}, \quad Q_j = u_j - \frac{1}{4} = P_j + 2.$$

设 $f(x) = \prod_{j=0}^{503} P_j - \prod_{j=0}^{503} Q_j$。我们证明 **$f(x) < 0$ 对所有实数 $x$ 成立**。

#### 情形 1：$x \in A \cup B$

**$x \in A$**（即 $x = 4j+1$ 或 $x = 4j+4$，某个 $j$）：此时 $P_j = 0$，故 $\prod P = 0$。而 $x \notin B$，故 $\prod Q \neq 0$。$f(x) = -\prod Q < 0$（可验证 $\prod Q(x) > 0$：$B$ 中大于 $x$ 的元素个数为偶数）。

**$x \in B$**（即 $x = 4j+2$ 或 $x = 4j+3$，某个 $j$）：此时 $Q_j = 0$，故 $\prod Q = 0$。而 $x \notin A$，故 $\prod P \neq 0$。$f(x) = \prod P < 0$（可验证 $\prod P(x) < 0$：$A$ 中大于 $x$ 的元素个数为奇数）。

#### 情形 2：$x \notin A \cup B = \{1, \ldots, 2016\}$

此时所有 $P_j \neq 0$，$Q_j \neq 0$。

$P_j < 0$ 当且仅当 $u_j < \dfrac{9}{4}$，即 $\left|x - 4j - \dfrac{5}{2}\right| < \dfrac{3}{2}$，即 $x \in (4j+1, \, 4j+4)$。

区间 $(4j+1, \, 4j+4)$（$j = 0, 1, \ldots, 503$）即 $(1,4), (5,8), (9,12), \ldots, (2013, 2016)$，两两不相交（相邻间隔为 $1$）。故**至多一个 $P_j$ 为负**。

类似地，$Q_j < 0$ 当且仅当 $x \in (4j+2, \, 4j+3)$，且 $(4j+2, 4j+3) \subset (4j+1, 4j+4)$。

**子情形 2a：所有 $P_j > 0$。**

此时所有 $Q_j = P_j + 2 > P_j > 0$，故 $\prod Q_j > \prod P_j > 0$，$f(x) < 0$。$\checkmark$

**子情形 2b：恰有一个 $P_{j_0} < 0$ 且 $Q_{j_0} \geq 0$。**

即 $x \in (4j_0+1, \, 4j_0+2] \cup [4j_0+3, \, 4j_0+4)$。此时 $\prod P_j < 0$（一个负因子），$\prod Q_j > 0$（无负因子），故 $f(x) = \prod P_j - \prod Q_j < 0$。$\checkmark$

**子情形 2c：恰有一个 $P_{j_0} < 0$ 且 $Q_{j_0} < 0$。**

即 $x \in (4j_0+2, \, 4j_0+3)$。此时 $\prod P_j < 0$ 且 $\prod Q_j < 0$（各有一个负因子）。需证 $|\prod P_j| > |\prod Q_j|$，即 $\prod P_j < \prod Q_j < 0$，从而 $f(x) < 0$。

令 $v = u_{j_0} = \left(x - 4j_0 - \dfrac{5}{2}\right)^2 \in \left[0, \, \dfrac{1}{4}\right)$。则

$$\frac{|P_{j_0}|}{|Q_{j_0}|} = \frac{\frac{9}{4} - v}{\frac{1}{4} - v} = 1 + \frac{2}{\frac{1}{4} - v} \geq 1 + \frac{2}{1/4} = 9. \tag{$*$}$$

对 $j \neq j_0$，$P_j > 0$，$Q_j > 0$，$P_j / Q_j < 1$。需证

$$\frac{|\prod P_j|}{|\prod Q_j|} = \frac{|P_{j_0}|}{|Q_{j_0}|} \cdot \prod_{j \neq j_0} \frac{P_j}{Q_j} > 1,$$

即 $\prod_{j \neq j_0} \dfrac{Q_j}{P_j} < 9$。

**估计乘积：** 对 $j \neq j_0$，令 $k = |j - j_0| \geq 1$，$t = x - 4j_0 - \dfrac{5}{2} \in \left(-\dfrac{1}{2}, \dfrac{1}{2}\right)$。由三角形不等式，

$$u_j = (t - 4(j - j_0))^2 \geq (4k - |t|)^2 \geq \left(4k - \frac{1}{2}\right)^2.$$

因此

$$u_j - \frac{9}{4} \geq \left(4k - \frac{1}{2}\right)^2 - \frac{9}{4} = 16k^2 - 4k - 2 = 2(4k+1)(2k-1),$$

$$\frac{Q_j}{P_j} = 1 + \frac{2}{u_j - \frac{9}{4}} \leq 1 + \frac{1}{(4k+1)(2k-1)}.$$

对 $k \geq 1$，有 $(4k+1)(2k-1) = 8k^2 - 2k - 1 \geq 5k^2$（因 $8k^2 - 2k - 1 - 5k^2 = (3k+1)(k-1) \geq 0$）。每个 $k$ 至多对应 $2$ 个 $j$，故

$$\prod_{j \neq j_0} \frac{Q_j}{P_j} \leq \prod_{k=1}^{\infty} \left(1 + \frac{1}{5k^2}\right)^2 \leq \exp\left(2\sum_{k=1}^{\infty} \frac{1}{5k^2}\right) = \exp\left(\frac{\pi^2}{15}\right).$$

由 $\pi^2 < 10$ 得 $\dfrac{\pi^2}{15} < \dfrac{2}{3}$，故

$$\exp\left(\frac{\pi^2}{15}\right) < \exp\left(\frac{2}{3}\right) < e < 3 < 9. \tag{$**$}$$

结合 $(*)$ 和 $(**)$：

$$\frac{|\prod P_j|}{|\prod Q_j|} \geq \frac{9}{\exp(\pi^2/15)} > \frac{9}{3} = 3 > 1.$$

故 $|\prod P_j| > |\prod Q_j|$，即 $\prod P_j < \prod Q_j < 0$，$f(x) < 0$。$\checkmark$

### 第四步：结论

对所有实数 $x$，$f(x) < 0$，故 $f(x) \neq 0$，方程 $\prod_A = \prod_B$ 无实根。

擦除数 $= 4032 - 1008 - 1008 = 2016$，且由第一步知擦除数 $\geq 2016$。

**最少擦除数为 $\boxed{2016}$。** $\blacksquare$
