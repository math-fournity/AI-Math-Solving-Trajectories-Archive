# 证明 $A_4 \cong V_4 \rtimes Z_3$ 并构造同态 $\varphi: Z_3 \to \operatorname{Aut}(V_4)$

## 记号约定

设 $V_4 = \{e, a, b, c\}$，其中：

$$a = (12)(34), \quad b = (13)(24), \quad c = (14)(23)$$

$V_4$ 是 Klein 四元群，同构于 $Z_2 \times Z_2$，其三个非恒等元素 $a, b, c$ 均为 2 阶元，且满足 $ab = c$，$bc = a$，$ca = b$（任意两个不同非恒等元的乘积等于第三个）。

## 第一步：确认 $V_4 \trianglelefteq A_4$

此为已知条件。$V_4$ 的正规性也可直接验证：$A_4$ 由 3-轮换生成（如 $(123)$ 和 $(124)$），而共轭作用保持轮换结构。经计算验证：

- 共轭 by $(123)$：$a \mapsto c$，$b \mapsto a$，$c \mapsto b$（置换 $\{a,b,c\}$）
- 共轭 by $(124)$：$a \mapsto b$，$b \mapsto c$，$c \mapsto a$（置换 $\{a,b,c\}$）

两个生成元都将 $V_4$ 映回自身，故 $V_4 \trianglelefteq A_4$。

## 第二步：找到一个子群 $H \cong Z_3$

取 $H = \langle \sigma \rangle$，其中 $\sigma = (123)$，则：

$$H = \{e, \sigma, \sigma^2\} = \{e, (123), (132)\}$$

$H$ 是 3 阶循环群，$H \cong Z_3$。

## 第三步：验证 $V_4 \cap H = \{e\}$

$V_4$ 的元素为恒等元和三个双对换（2 阶元），而 $H$ 的元素为恒等元和两个 3-轮换（3 阶元）。双对换与 3-轮换是不同类型的置换，故：

$$V_4 \cap H = \{e\}$$

## 第四步：验证 $V_4 \cdot H = A_4$

由乘积公式：

$$|V_4 \cdot H| = \frac{|V_4| \cdot |H|}{|V_4 \cap H|} = \frac{4 \times 3}{1} = 12 = |A_4|$$

由于 $V_4 \cdot H \subseteq A_4$ 且 $|V_4 \cdot H| = |A_4|$，故 $V_4 \cdot H = A_4$。

## 第五步：应用半直积判定定理

**半直积判定定理**：设 $N \trianglelefteq G$，$H \leq G$，若 $N \cap H = \{e\}$ 且 $NH = G$，则 $G \cong N \rtimes H$，其中半直积的作用由共轭给出：$\varphi(h)(n) = hnh^{-1}$。

由第一至四步，$N = V_4$，$H = \langle (123) \rangle \cong Z_3$ 满足全部条件，因此：

$$\boxed{A_4 \cong V_4 \rtimes_\varphi Z_3}$$

## 第六步：明确构造同态 $\varphi: Z_3 \to \operatorname{Aut}(V_4)$

### $\operatorname{Aut}(V_4)$ 的结构

$V_4 \cong Z_2 \times Z_2$ 是 2 阶元构成的群。任何自同构必须将非恒等元素 $\{a, b, c\}$ 置换到非恒等元素，且 $\{a, b, c\}$ 的任意置换都唯一确定一个自同构（因为 $V_4$ 由任意两个非恒等元生成，而第三个是它们的乘积）。因此：

$$\operatorname{Aut}(V_4) \cong S_3$$

$\operatorname{Aut}(V_4)$ 中的元素对应 $\{a, b, c\}$ 的六种置换。

### $\varphi$ 的定义

$\varphi: Z_3 \to \operatorname{Aut}(V_4)$ 由共轭作用定义。设 $Z_3 = \langle \sigma \rangle$，$\sigma = (123)$，则：

$$\varphi(\sigma^k)(v) = \sigma^k \, v \, \sigma^{-k}, \quad v \in V_4, \quad k = 0, 1, 2$$

### 显式计算

**$\varphi(\sigma) = \varphi((123))$**：计算 $\sigma \, v \, \sigma^{-1}$ 对每个 $v \in V_4$：

$$\sigma \, a \, \sigma^{-1} = (123)(12)(34)(132)$$

逐元素追踪（右到左，先 $(132)$，再 $(12)(34)$，再 $(123)$）：

| 元素 | $(132)$ | $(12)(34)$ | $(123)$ | 结果 |
|------|---------|------------|---------|------|
| 1    | 3       | 4          | 4       | 1→4  |
| 4    | 4       | 3          | 1       | 4→1  |
| 2    | 1       | 2          | 3       | 2→3  |
| 3    | 2       | 1          | 2       | 3→2  |

结果为 $(14)(23) = c$，即 $\varphi(\sigma)(a) = c$。

同理计算：

$$\varphi(\sigma)(b) = (123)(13)(24)(132) = (12)(34) = a$$

$$\varphi(\sigma)(c) = (123)(14)(23)(132) = (13)(24) = b$$

因此 $\varphi(\sigma)$ 在 $\{a, b, c\}$ 上的作用为 3-轮换 $(a\; c\; b)$：

$$a \xrightarrow{\varphi(\sigma)} c \xrightarrow{\varphi(\sigma)} b \xrightarrow{\varphi(\sigma)} a$$

**$\varphi(\sigma^2) = \varphi((132))$**：这是 $\varphi(\sigma)$ 的逆，为 3-轮换 $(a\; b\; c)$：

$$a \xrightarrow{\varphi(\sigma^2)} b \xrightarrow{\varphi(\sigma^2)} c \xrightarrow{\varphi(\sigma^2)} a$$

**$\varphi(e) = \operatorname{id}$**：恒等自同构。

### 用矩阵表示（可选）

若将 $V_4$ 视为 $\mathbb{F}_2^2$（取 $a = (1,0)$，$b = (0,1)$，则 $c = (1,1)$），则 $\operatorname{Aut}(V_4) \cong \operatorname{GL}(2, \mathbb{F}_2)$。$\varphi(\sigma)$ 对应的矩阵为：

$$\varphi(\sigma): \begin{cases} a \mapsto c = a + b \\ b \mapsto a \\ c \mapsto b \end{cases} \implies M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \in \operatorname{GL}(2, \mathbb{F}_2)$$

验证 $M^3 = I \pmod{2}$：

$$M^2 = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}, \quad M^3 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \pmod{2} \quad \checkmark$$

### 验证 $\varphi$ 是同态

- $\varphi(\sigma)^3 = (a\; c\; b)^3 = \operatorname{id} = \varphi(\sigma^3) = \varphi(e)$ ✓
- $\varphi(\sigma) \circ \varphi(\sigma^2) = (a\; c\; b)(a\; b\; c) = \operatorname{id} = \varphi(\sigma \cdot \sigma^2) = \varphi(e)$ ✓

### $\varphi$ 的性质

- **核**：$\ker \varphi = \{e\}$（因为 $\varphi(\sigma)$ 和 $\varphi(\sigma^2)$ 都不是恒等自同构），故 $\varphi$ 是单射。
- **像**：$\operatorname{im} \varphi = \langle (a\; c\; b) \rangle \cong Z_3$，这是 $S_3 \cong \operatorname{Aut}(V_4)$ 中唯一的 3 阶子群，即 $A_3$。

## 结论

$$A_4 \cong V_4 \rtimes_\varphi Z_3$$

其中 $\varphi: Z_3 \to \operatorname{Aut}(V_4) \cong S_3$ 将 $Z_3$ 的生成元 $\sigma = (123)$ 映为 $\operatorname{Aut}(V_4)$ 中的 3-轮换 $(a\; c\; b)$（即 $a \to c \to b \to a$），这是一个单射同态，其像为 $S_3$ 中的唯一 3 阶子群 $A_3$。

**证毕。** $\blacksquare$

## 补充说明

$\varphi$ 的具体 3-轮换方向（$(a\; c\; b)$ 或 $(a\; b\; c)$）取决于共轭约定的选择（$\sigma v \sigma^{-1}$ 或 $\sigma^{-1} v \sigma$）。两种约定给出的同态相差 $Z_3$ 的一个自同构（生成元取逆），因此导出的半直积同构。本证明采用标准约定 $\varphi(h)(n) = hnh^{-1}$，经 Python/SymPy 计算验证。
