# 从 $S_3$ 到 $Z_2$ 的所有群同态

## 问题

给定对称群 $S_3 = \{e, (12), (13), (23), (123), (132)\}$（6阶）和循环群 $Z_2 = \{0, 1\}$（2阶，模2加法）。

1. 求所有从 $S_3$ 到 $Z_2$ 的群同态 $\varphi: S_3 \to Z_2$
2. 对每个同态，确定其核 $\ker(\varphi)$ 和像 $\operatorname{im}(\varphi)$
3. 验证 $|S_3| = |\ker(\varphi)| \times |\operatorname{im}(\varphi)|$

---

## 预备知识

### 群同态的定义

$\varphi: S_3 \to Z_2$ 是群同态，当且仅当对所有 $g, h \in S_3$：

$$\varphi(gh) = \varphi(g) + \varphi(h) \pmod{2}$$

### 第一同构定理

对任意群同态 $\varphi: G \to H$，有

$$G / \ker(\varphi) \cong \operatorname{im}(\varphi)$$

由此得基数关系：

$$|G| = |\ker(\varphi)| \times |\operatorname{im}(\varphi)|$$

### $S_3$ 的结构

$S_3$ 的元素及其阶：

| 元素 | 阶 | 奇偶性 |
|------|-----|--------|
| $e$ | 1 | 偶 |
| $(12)$ | 2 | 奇 |
| $(13)$ | 2 | 奇 |
| $(23)$ | 2 | 奇 |
| $(123)$ | 3 | 偶 |
| $(132)$ | 3 | 偶 |

$S_3$ 的正规子群恰好有三个：

- $\{e\}$（1阶）
- $A_3 = \{e, (123), (132)\}$（3阶，交错群，指数2）
- $S_3$（6阶）

其中 $A_3$ 是唯一的3阶子群（因为3阶子群必为循环群，由3阶元素生成，而 $S_3$ 中仅 $(123)$ 和 $(132)$ 是3阶元素，且 $\langle(123)\rangle = \langle(132)\rangle = A_3$）。指数2的子群必为正规子群，故 $A_3 \trianglelefteq S_3$。

---

## 第一步：用第一同构定理确定同态的框架

设 $\varphi: S_3 \to Z_2$ 是群同态。由第一同构定理：

$$|S_3| = |\ker(\varphi)| \times |\operatorname{im}(\varphi)|$$

即 $6 = |\ker(\varphi)| \times |\operatorname{im}(\varphi)|$。

$\operatorname{im}(\varphi)$ 是 $Z_2$ 的子群。$Z_2$ 是2阶循环群，其子群只有 $\{0\}$（1阶）和 $Z_2$ 本身（2阶）。因此 $|\operatorname{im}(\varphi)| \in \{1, 2\}$。

### 情形一：$|\operatorname{im}(\varphi)| = 1$

此时 $\operatorname{im}(\varphi) = \{0\}$，即 $\varphi(g) = 0$ 对所有 $g \in S_3$。这是**平凡同态**。

$$|\ker(\varphi)| = \frac{6}{1} = 6, \quad \ker(\varphi) = S_3$$

### 情形二：$|\operatorname{im}(\varphi)| = 2$

此时 $\operatorname{im}(\varphi) = Z_2$，且

$$|\ker(\varphi)| = \frac{6}{2} = 3$$

$\ker(\varphi)$ 是 $S_3$ 的3阶正规子群。如前所述，$S_3$ 的唯一3阶正规子群是 $A_3$。因此：

$$\ker(\varphi) = A_3 = \{e, (123), (132)\}$$

---

## 第二步：构造两个同态并验证

### 同态1：平凡同态 $\varphi_0$

**定义**：

$$\varphi_0(g) = 0, \quad \forall\, g \in S_3$$

**验证同态性质**：对任意 $g, h \in S_3$，

$$\varphi_0(gh) = 0 = 0 + 0 = \varphi_0(g) + \varphi_0(h) \pmod{2} \quad \checkmark$$

**核与像**：

$$\ker(\varphi_0) = S_3 = \{e, (12), (13), (23), (123), (132)\}, \quad |\ker(\varphi_0)| = 6$$

$$\operatorname{im}(\varphi_0) = \{0\}, \quad |\operatorname{im}(\varphi_0)| = 1$$

**基数验证**：

$$|\ker(\varphi_0)| \times |\operatorname{im}(\varphi_0)| = 6 \times 1 = 6 = |S_3| \quad \checkmark$$

### 同态2：符号同态（奇偶性映射）$\varphi_1$

**定义**：利用置换的奇偶性（符号函数）。

$$\varphi_1(g) = \operatorname{sgn}(g) \pmod{2} = \begin{cases} 0 & \text{若 } g \text{ 是偶置换} \\ 1 & \text{若 } g \text{ 是奇置换} \end{cases}$$

具体值：

| $g$ | 奇偶性 | $\varphi_1(g)$ |
|-----|--------|-----------------|
| $e$ | 偶 | 0 |
| $(12)$ | 奇 | 1 |
| $(13)$ | 奇 | 1 |
| $(23)$ | 奇 | 1 |
| $(123)$ | 偶 | 0 |
| $(132)$ | 偶 | 0 |

**验证同态性质**：

置换的符号函数满足 $\operatorname{sgn}(gh) = \operatorname{sgn}(g) \cdot \operatorname{sgn}(h)$，其中 $\operatorname{sgn}(g) \in \{+1, -1\}$。映射到 $Z_2$ 时，$+1 \mapsto 0$，$-1 \mapsto 1$，乘法变为模2加法：

$$\varphi_1(gh) = \operatorname{sgn}(gh) \bmod 2 = (\operatorname{sgn}(g) \cdot \operatorname{sgn}(h)) \bmod 2 = \varphi_1(g) + \varphi_1(h) \pmod{2} \quad \checkmark$$

**计算验证**（遍历 $S_3$ 的全部 $6 \times 6 = 36$ 个乘积组合，逐一检验 $\varphi_1(gh) = \varphi_1(g) + \varphi_1(h) \pmod{2}$，全部通过）。

**核与像**：

$$\ker(\varphi_1) = \{g \in S_3 : \varphi_1(g) = 0\} = \{e, (123), (132)\} = A_3, \quad |\ker(\varphi_1)| = 3$$

$$\operatorname{im}(\varphi_1) = \{0, 1\} = Z_2, \quad |\operatorname{im}(\varphi_1)| = 2$$

**基数验证**：

$$|\ker(\varphi_1)| \times |\operatorname{im}(\varphi_1)| = 3 \times 2 = 6 = |S_3| \quad \checkmark$$

---

## 第三步：证明只有这两个同态（完备性）

### 方法一：通过正规子群枚举

由第一同构定理，$\ker(\varphi)$ 是 $S_3$ 的正规子群，且 $S_3 / \ker(\varphi) \cong \operatorname{im}(\varphi) \leq Z_2$。

$S_3$ 的正规子群只有 $\{e\}$、$A_3$、$S_3$ 三种。逐一检验：

- $\ker(\varphi) = \{e\}$：则 $S_3/\{e\} \cong S_3 \cong \operatorname{im}(\varphi) \leq Z_2$，要求 $|S_3| = 6$ 整除 $|Z_2| = 2$，不可能。**排除**。
- $\ker(\varphi) = A_3$：则 $S_3/A_3 \cong Z_2 \leq Z_2$，$|\operatorname{im}(\varphi)| = 2$，可行。对应符号同态 $\varphi_1$。
- $\ker(\varphi) = S_3$：则 $\operatorname{im}(\varphi) = \{0\}$，可行。对应平凡同态 $\varphi_0$。

因此只有两个同态。

### 方法二：通过生成元与关系

$S_3 = \langle (12), (123) \rangle$，满足关系：

$$(12)^2 = e, \quad (123)^3 = e, \quad (12)(123)(12) = (123)^2$$

同态 $\varphi$ 必须保持这些关系：

1. $\varphi((12)^2) = \varphi(e) = 0$，即 $2\varphi((12)) = 0 \pmod{2}$。在 $Z_2$ 中此式**恒成立**（因 $Z_2$ 中 $2x = 0$ 对所有 $x$ 成立），故 $\varphi((12))$ 可取 $0$ 或 $1$。

2. $\varphi((123)^3) = \varphi(e) = 0$，即 $3\varphi((123)) = 0 \pmod{2}$。因 $3$ 是奇数，$3x \equiv x \pmod{2}$，故 $\varphi((123)) = 0$。**唯一确定**。

3. 第三条关系 $(12)(123)(12) = (123)^2$ 给出 $\varphi((12)) + \varphi((123)) + \varphi((12)) = 2\varphi((123)) \pmod{2}$，即 $2\varphi((12)) = 0$，与第1条一致，无新约束。

因此 $\varphi$ 由 $\varphi((12)) \in \{0, 1\}$ 唯一确定，恰好给出两个同态：

- $\varphi((12)) = 0$：平凡同态 $\varphi_0$。
- $\varphi((12)) = 1$：符号同态 $\varphi_1$。

### 方法三：暴力枚举验证

对全部 $2^6 = 64$ 种从 $S_3$ 到 $Z_2$ 的映射，逐一检验同态性质 $\varphi(gh) = \varphi(g) + \varphi(h) \pmod{2}$（遍历全部36个乘积对），结果恰好只有2个映射满足条件，与方法一、方法二的结论完全一致。

---

## 第四步：基数公式验证汇总

| 同态 | $\ker(\varphi)$ | $|\ker(\varphi)|$ | $\operatorname{im}(\varphi)$ | $|\operatorname{im}(\varphi)|$ | $|\ker| \times |\operatorname{im}|$ | $= |S_3|$? |
|------|-----------------|---------------------|------------------------------|----------------------------------|--------------------------------------|-----------|
| $\varphi_0$（平凡） | $S_3$ | 6 | $\{0\}$ | 1 | $6 \times 1 = 6$ | $\checkmark$ |
| $\varphi_1$（符号） | $A_3$ | 3 | $Z_2$ | 2 | $3 \times 2 = 6$ | $\checkmark$ |

---

## 结论

从 $S_3$ 到 $Z_2$ 的群同态**恰好有两个**：

1. **平凡同态** $\varphi_0: S_3 \to Z_2$，$\varphi_0(g) = 0$ 对所有 $g \in S_3$。
   - $\ker(\varphi_0) = S_3$，$|\ker(\varphi_0)| = 6$
   - $\operatorname{im}(\varphi_0) = \{0\}$，$|\operatorname{im}(\varphi_0)| = 1$
   - $6 = 6 \times 1$ ✓

2. **符号同态** $\varphi_1: S_3 \to Z_2$，$\varphi_1(g) = \operatorname{sgn}(g) \bmod 2$（偶置换 $\mapsto 0$，奇置换 $\mapsto 1$）。
   - $\ker(\varphi_1) = A_3 = \{e, (123), (132)\}$，$|\ker(\varphi_1)| = 3$
   - $\operatorname{im}(\varphi_1) = Z_2 = \{0, 1\}$，$|\operatorname{im}(\varphi_1)| = 2$
   - $6 = 3 \times 2$ ✓

完备性通过三种独立方法验证：（1）正规子群枚举、（2）生成元与关系分析、（3）暴力枚举全部 $2^6$ 种映射。三种方法均确认只有这两个同态。

证毕 / QED
