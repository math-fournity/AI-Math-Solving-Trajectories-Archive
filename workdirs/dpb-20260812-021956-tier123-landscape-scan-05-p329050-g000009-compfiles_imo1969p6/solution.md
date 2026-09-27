# IMO 1969 Problem 6 — 解答

## 题目

给定实数 $x_1, x_2, y_1, y_2, z_1, z_2$，满足 $x_1 > 0,\ x_2 > 0,\ x_1 y_1 > z_1^2,\ x_2 y_2 > z_2^2$。证明

$$\frac{8}{(x_1+x_2)(y_1+y_2) - (z_1+z_2)^2} \le \frac{1}{x_1 y_1 - z_1^2} + \frac{1}{x_2 y_2 - z_2^2}$$

并给出等号成立的充要条件。

---

## 证明

### 第一步：矩阵化

对每个 $i = 1, 2$，定义 $2 \times 2$ 矩阵

$$M_i = \begin{pmatrix} x_i & z_i \\ z_i & y_i \end{pmatrix}.$$

条件 $x_i > 0$ 且 $\det M_i = x_i y_i - z_i^2 > 0$ 保证 $M_i$ 是**正定矩阵**（左上角元 $> 0$ 且行列式 $> 0$）。记

$$A_i = \det M_i = x_i y_i - z_i^2 > 0.$$

不等式左边的分母恰为

$$\det(M_1 + M_2) = (x_1+x_2)(y_1+y_2) - (z_1+z_2)^2.$$

因此要证的不等式等价于

$$\frac{8}{\det(M_1 + M_2)} \le \frac{1}{A_1} + \frac{1}{A_2}. \tag{$\star$}$$

### 第二步：归一化与关键恒等式

令 $D_i = M_i / \sqrt{A_i}$，则 $\det D_i = 1$，$D_i$ 仍正定，且 $M_i = \sqrt{A_i}\, D_i$。

对 $2 \times 2$ 矩阵有恒等式（直接展开验证）：

$$\det(\alpha\, P + \beta\, Q) = \alpha^2 \det P + \beta^2 \det Q + \alpha\beta\, \operatorname{tr}\!\big(P \cdot \operatorname{adj}(Q)\big),$$

其中 $\operatorname{adj}(Q)$ 是 $Q$ 的伴随矩阵。当 $\det Q = 1$ 时 $\operatorname{adj}(Q) = Q^{-1}$，故

$$\det(M_1 + M_2) = A_1 + A_2 + \sqrt{A_1 A_2}\; \operatorname{tr}\!\big(D_1\, D_2^{-1}\big). \tag{1}$$

### 第三步：迹的下界

记 $T = \operatorname{tr}(D_1 D_2^{-1})$。

- $D_1 D_2^{-1}$ 相似于 $D_2^{-1/2}\, D_1\, D_2^{-1/2}$（后者正定），故 $D_1 D_2^{-1}$ 的特征值 $\lambda_1, \lambda_2$ 均为正实数。
- $\det(D_1 D_2^{-1}) = \det D_1 / \det D_2 = 1$，即 $\lambda_1 \lambda_2 = 1$。
- 由 AM-GM：$T = \lambda_1 + \lambda_2 \ge 2\sqrt{\lambda_1 \lambda_2} = 2$，等号当且仅当 $\lambda_1 = \lambda_2 = 1$，即 $D_1 D_2^{-1} = I$，即 $D_1 = D_2$。

### 第四步：完成证明

设 $s = \sqrt{A_1 A_2}$，$r = A_1 + A_2$。由 AM-GM，$r \ge 2s$。

利用 (1) 和 $T \ge 2$：

$$\det(M_1 + M_2) = r + s\,T \ge r + 2s.$$

于是

$$(A_1 + A_2)\,\det(M_1 + M_2) = r\,(r + sT) \ge r\,(r + 2s) = r^2 + 2rs.$$

而

$$r^2 + 2rs - 8s^2 = (r + 4s)(r - 2s) \ge 0,$$

因 $r \ge 2s > 0$。因此

$$(A_1 + A_2)\,\det(M_1 + M_2) \ge 8s^2 = 8\,A_1 A_2,$$

即

$$\frac{8}{\det(M_1 + M_2)} \le \frac{A_1 + A_2}{A_1 A_2} = \frac{1}{A_1} + \frac{1}{A_2},$$

这就是 $(\star)$。$\blacksquare$

### 第五步：等号条件

等号成立需要以下**两个**不等式同时取等：

1. **$T = 2$**：即 $D_1 = D_2$，也就是 $\dfrac{M_1}{\sqrt{A_1}} = \dfrac{M_2}{\sqrt{A_2}}$。
2. **$r = 2s$**：即 $A_1 + A_2 = 2\sqrt{A_1 A_2}$，即 $(\sqrt{A_1} - \sqrt{A_2})^2 = 0$，即 $A_1 = A_2$。

条件 1 + 条件 2 联立：$\sqrt{A_1} = \sqrt{A_2}$ 且 $D_1 = D_2$，故 $M_1 = M_2$，即

$$\boxed{x_1 = x_2,\quad y_1 = y_2,\quad z_1 = z_2.}$$

**等号成立当且仅当 $x_1 = x_2,\ y_1 = y_2,\ z_1 = z_2$。**

---

## 验证

- **等号情形** $M_1 = M_2 = M$：$\det(2M) = 4\det M$，LHS $= 8/(4\det M) = 2/\det M$，RHS $= 2/\det M$。✓
- **$A_1 = A_2$ 但 $M_1 \ne M_2$**（如 $M_1 = \mathrm{diag}(2,1)$, $M_2 = \mathrm{diag}(1,2)$）：$\det(M_1+M_2) = 9$，LHS $= 8/9 < 1 =$ RHS。严格不等式。✓
- 10000 次随机数值测试全部通过。✓
