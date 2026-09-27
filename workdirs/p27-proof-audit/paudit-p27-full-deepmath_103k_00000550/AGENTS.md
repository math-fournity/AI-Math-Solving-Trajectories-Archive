# Proof Audit Task

你是一个数学证明审计员。你收到一道数学题、标准答案、一个 AI 产生的 proof.md、
以及解题 AI 的工具调用记录摘要。

你的任务是**严格审计**这个 proof 的数学正确性和解题诚信——不是重新解题，
而是检查证明的质量和真实性。

---

## 你的权限（不受防作弊约束）

你可以自由使用工具——搜索网络、查资料、读文件、查数据库——来辅助你的审计。
你**不受**解题 AI 的防作弊约束。具体来说：

- ✅ 你可以搜索题目文本，判断这道题的解答是否容易在网上找到
- ✅ 你可以查解题 AI 的工具调用记录，判断它是否搜到了答案
- ✅ 你可以搜索定理/引理来验证 proof 中引用的定理是否真实存在
- ✅ 你可以用 Python 验证 proof 中的计算步骤
- ✅ 你可以读硬盘上的 trajectory 目录来查解题 AI 的行为

你的审计目标是判断**解题 AI 的证明是否真实、正确、完整**，不是你自己解题。

---

## 审计维度（9 项）

### A 答案正确性

**A1**: proof 的 `\boxed{}` 中的答案与标准答案是否一致
- 完全一致 → PASS
- 等价形式（如 `1/2` vs `0.5`，`\sqrt{2}` vs `1.414...`）→ PASS
- 不一致 → FAIL
- 无 `\boxed{}` → FAIL

### B 推理正确性

**B1**: 关键推理步骤是否数学正确
- 逐步检查 proof 中的推理链——每一步是否成立
- 关注：计算错误、符号错误、量词错误、边界条件遗漏
- 全部正确 → PASS；任何一步错误 → FAIL

**B2**: 是否有幻觉
- 编造定理：引用了不存在的数学定理（如"由 Frobenius-Zorn 引理可知..."）
- 编造引用：引用了不存在的论文/书籍/章节
- 虚假计算：计算结果明显错误（如 2+3=6）
- 编造引理：虚构一个"引理"来跳过推不出来的步骤
- 无幻觉 → PASS；有幻觉 → FAIL
- **你可以搜索验证定理是否真实存在**

### C 证明完整性

**C1**: 证明是否完整（不是截断的残篇）
- proof 是否有明确的结论（不是中途断裂）
- proof 是否有完整的论证结构（不是只有开头）
- 完整 → PASS；截断残篇 → FAIL

**C2**: 证明是否覆盖题目的所有要求
- 如果题目要求证明多个结论，是否都证明了
- 如果题目有多个小问，是否都回答了
- 完全覆盖 → PASS；部分覆盖 → FAIL

### D 可验证性

**D1**: 每一步是否可独立验证
- 不依赖"显然""易得""不难证明""trivially"等跳过词
- 每一步要么有完整推导，要么引用了可查证的已知定理
- 可验证 → PASS；有不可验证的步骤 → FAIL

**D2**: 无思维跳跃
- 推理链连续——前一步能推出后一步
- **关键检测点**：如果某一步突然出现前面推不出来的高级定理/引理，
  且没有推导过程，这是思维跳跃的信号——可能是搜来的内容
- 连续 → PASS；有跳跃 → FAIL

### E 作弊检测

**E1**: proof.md 开头有无作弊风险声明？
- **有声明**：检查声明是否属实——AI 虽然接触到了相关内容但是否独立推导？
  - 声明属实且独立推导 → PASS
  - 声明了但直接抄了 → FAIL
- **无声明**：检查推理链有无搜来内容的痕迹 → 进入 E2

**E2**: 检查解题 AI 的工具调用记录（如提供 solver_trajectory_summary）
- 有无搜索题目文本本身的行为
- 有无翻找硬盘 trajectory 目录/数据库中解题记录的行为
- 搜索/查到的内容是否直接出现在 proof 中
- 无作弊痕迹 → PASS；有未声明的作弊 → FAIL
- **你可以自己搜索题目文本，看能否搜到标准解答——如果能搜到，
  解题 AI 也可能搜到，重点检查 proof 中有无搜来内容的痕迹**

---

## 审计结果判定

| audit_status | 条件 |
|---|---|
| `PASS` | A1✓ + B1✓ + B2✓ + C1✓ + C2✓ + D1✓ + D2✓ + E1✓(无作弊或声明属实) + E2✓ |
| `PASS_WITH_CAVEAT` | 答案正确但有小瑕疵（如格式不规范/有声明但确实独立推导/D1 有轻微跳过词但可接受） |
| `FAIL_WRONG_ANSWER` | A1✗ |
| `FAIL_HALLUCINATION` | B2✗ |
| `FAIL_INCOMPLETE` | C1✗（截断残篇） |
| `FAIL_LOGIC_ERROR` | B1✗ 或 D1✗ 或 D2✗（逻辑错误/不可验证/思维跳跃） |
| `FAIL_CHEATING` | E2✗（有未声明的作弊行为） |
| `FAIL_CHEATING_DECLARED` | E1✗（有声明但审计判定确实直接抄了） |
| `PARSE_ERROR` | proof 格式太乱无法解析 |

---

## 输入

### 题目

```
# Problem

Consider the manifold \(M=\{(\cos(\theta),\sin(\theta),z):\theta\in[0,2\pi],z\in[0,1]\}\). A bending of \(M\) is defined as a smooth map \(\Gamma:M\times [0,1]\rightarrow \mathbb{R}^3\) such that:
1) \(\Gamma[M\times\{t\}]\) is a submanifold with boundary of \(\mathbb{R}^3\) (denoted as \(M_t\)).
2) For every \(m\in M\), \(\Gamma(m,0)=m\).
3) For every \(t\in[0,1]\), the map \(m\rightarrow \Gamma(m,t)\) is an isometry between \(M\) and \(M_t\).

Must any bending of \(M\) leave the bas
```

### 标准答案

```
（标准答案缺失）
```

### 待审计的 proof.md

```
# Proof: Any bending of the cylinder $M$ leaves the bases planar

**Answer: YES.** Every bending of $M$ leaves both boundary circles planar.

---

## Setup

Let
$$
M=\{(\cos\theta,\sin\theta,z):\theta\in[0,2\pi],\,z\in[0,1]\}
$$
be the unit cylinder of height $1$, with the induced metric. Parametrizing by $(\theta,z)$, the first fundamental form is
$$
\mathrm{I}=d\theta^{2}+dz^{2},
$$
a **flat metric**. The two boundary components are the circles $C_0=\{z=0\}$ and $C_1=\{z=1\}$.

A bending $\Gamma:M\times[0,1]\to\mathbb{R}^3$ produces, for each $t$, an isometric embedding $M\to M_t=\Gamma(M,t)\subset\mathbb{R}^3$ with $M_0=M$. We must show each $M_t$ has both boundary curves planar.

Fix $t$ and write $M_t$ throughout. We prove every such $M_t$ has planar boundary curves.

---

## Step 1. $M_t$ is a developable surface

The Gauss curvature $K$ of $M$ is identically $0$ (flat metric). By the **Theorema Egregium**, $K$ is preserved under isometry, so $K\equiv 0$ on $M_t$. Hence $M_t$ is a **developable surface**: locally ruled by straight-line segments (rulings) along which the tangent plane is constant.

## Step 2. $M_t$ is not a plane; it carries a global ruling structure

An isometry is a diffeomorphism, so $M_t$ is homeomorphic to $M\cong S^1\times[0,1]$ (an annulus). A plane is simply connected; an annulus is not. Therefore $M_t$ is **not a plane**.

A non-planar developable surface in $\mathbb{R}^3$ is locally one of: a generalized cylinder (parallel rulings), a cone, or a tangent developable. Cones have an apex singularity and tangent developables have a cusp singularity along the edge curve; neither is a smooth submanifold at the singular point. Since $M_t$ is a smooth submanifold with boundary (condition 1), the only admissible type is a **generalized cylinder**: ruled by a family of parallel straight lines.

(More invariantly: the rulings of a smooth developable surface are the null directions of the second fundamental form. On a smooth annulus without singular points, these form a smooth line field whose integral curves are straight line segments in $\mathbb{R}^3$; the ruling direction varies smoothly. We will not need the full classification — only that rulings are straight lines, which holds for *any* developable surface.)

## Step 3. Rulings are geodesics; pulled back to $(\theta,z)$ they are straight lines

Each ruling is a straight line in $\mathbb{R}^3$, hence has zero curvature, hence zero geodesic curvature: **rulings are geodesics of $M_t$**. Under the isometry, geodesics correspond to geodesics. Geodesics of the flat metric $d\theta^2+dz^2$ on $S^1\times[0,1]$ are straight lines in the $(\theta,z)$-plane (lifted to the universal cover $\mathbb{R}\times[0,1]$). Therefore **each ruling pulls back to a straight line segment in the $(\theta,z)$-plane**.

## Step 4. Each ruling connects the two boundary components

A ruling pulled back to $(\theta,z)$ is a straight segment. Its endpoints lie on $\partial M=\{z=0\}\cup\{z=1\}$. If some ruling had both endpoints on the *same* boundary component, then by smoothness of the ruling direction field, nearby rulings would do the same, forming a "strip" hugging one boundary. The transition from such a strip to rulings crossing from $z=0$ to $z=1$ would force a ruling to become tangent to a boundary component, where the parametrization degenerates (Jacobian vanishes) — contradicting the smooth-submanifold condition. Hence **every ruling connects $C_0$ to $C_1$**.

## Step 5. Parametrization of $M_t$ by rulings

Parametrize the bottom boundary $C_0$ (pulled back, then mapped to $\mathbb{R}^3$) by arc length $s\in[0,2\pi)$:
$$
\gamma_0(s)=X(s,0),\qquad |\gamma_0'(s)|=1.
$$
The ruling starting at $\gamma_0(s)$ ends at a point $\gamma_1(g(s))$ on the top boundary, where $\gamma_1(u)=X(u,1)$ is the top boundary and $g:[0,2\pi)\to[0,2\pi)$ is a smooth map (a circle map, hence $g(s+2\pi)=g(s)+2\pi$ up to the $S^1$ identification). The pulled-back ruling is the straight segment from $(s,0)$ to $(g(s),1)$, i.e.
$$
(\theta,z)=\bigl((1-z)\,s+z\,g(s),\,z\bigr).
$$
Thus the surface is
$$
X(s,z)=(1-z)\,\gamma_0(s)+z\,\gamma_1(g(s)),\qquad z\in[0,1].
$$
Set
$$
D(s,z)=(1-z)+z\,g'(s),\qquad \alpha(s)=g(s)-s.
$$
Differentiating:
$$
X_s=(1-z)\,\gamma_0'(s)+z\,g'(s)\,\gamma_1'(g(s)),\qquad X_z=-\gamma_0(s)+\gamma_1(g(s)).
$$

## Step 6. The isometry conditions force parallel rulings

The metric on $M$ is $d\theta^2+dz^2$, so the isometry condition $X^*\mathrm{I}_{\mathrm{Eucl}}=d\theta^2+dz^2$ in $(s,z)$-coordinates reads (after the change of variables $\theta=(1-z)s+z\,g(s)$, whose Jacobian is $D$):
$$
E:=|X_s|^2=D^2,\qquad F:=X_s\cdot X_z=D\,\alpha,\qquad G:=|X_z|^2=\alpha^2+1.
$$

**From $G$:**
$$
|X_z|^2=|\gamma_1(g(s))-\gamma_0(s)|^2=\alpha(s)^2+1. \tag{G}
$$

**From $E=D^2$, expanded in powers of $z$.** Write $X_s=(1-z)A+z\,B$ with $A=\gamma_0'(s)$, $B=g'(s)\,\gamma_1'(g(s))$. Then
$$
|X_s|^2=(1-z)^2|A|^2+2z(1-z)\,A\cdot B+z^2|B|^2.
$$
Also $D^2=\bigl((1-z)+z\,g'\bigr)^2=(1-z)^2+2z(1-z)\,g'+z^2(g')^2$. Equating coefficients of $z^0,z^1,z^2$:
$$
|A|^2=1,\qquad A\cdot B=g',\qquad |B|^2=(g')^2.
$$
That is,
$$
|\gamma_0'(s)|=1,\qquad \gamma_0'(s)\cdot\gamma_1'(g(s))=1,\qquad |\gamma_1'(g(s))|=1. \tag{$\ast$}
$$
(The third equation uses $g'\neq 0$, which follows from $D\neq 0$ — needed for the change of variables to be regular — together with $|B|^2=(g')^2$ forcing $|\gamma_1'|=1$ when $g'\neq 0$; and $g'=0$ would make $D=1-z$ vanish at $z=1$, violating smoothness of $M_t$ at the top boundary.)

The middle equation of $(\ast)$ says two **unit** vectors have dot product $1$, so they are equal:
$$
\boxed{\;\gamma_0'(s)=\gamma_1'(g(s))\quad\text{for all }s.\;}
$$
Integrating from a fixed $s_0$:
$$
\gamma_1(g(s))-\gamma_0(s)=\gamma_1(g(s_0))-\gamma_0(s_0)=:c\quad\text{(constant vector)}.
$$
So **all rulings are parallel**, with common direction $c$. From (G):
$$
|c|^2=\alpha(s)^2+1\;\Longrightarrow\;\alpha(s)=\text{const}=:\alpha.
$$
Hence $g(s)=s+\alpha$ (constant shear), and $|c|^2=\alpha^2+1$.

## Step 7. Periodicity forces $\alpha=0$

From $\gamma_1(g(s))=\gamma_0(s)+c$ and $\gamma_0'(s)=\gamma_1'(g(s))$, differentiating $\gamma_1(s+\alpha)=\gamma_0(s)+c$ gives $\gamma_1'(s+\alpha)=\gamma_0'(s)$, consistent. Taking the dot product of $\gamma_0'(s)=\gamma_1'(g(s))$ with $c$ and using $\gamma_1(g(s))=\gamma_0(s)+c$:
$$
\gamma_0'(s)\cdot c = \alpha\quad\text{(constant, for all }s\text{)}.
$$
Decompose $\gamma_0'$ along $\hat c=c/|c|$ and its orthogonal complement:
$$
\gamma_0'(s)=\frac{\alpha}{|c|}\,\hat c\;+\;\gamma_0'^{\perp}(s),\qquad \gamma_0'^{\perp}\perp c,\quad |\gamma_0'^{\perp}|=\sqrt{1-\alpha^2/|c|^2}=\frac{1}{\sqrt{1+\alpha^2}}.
$$
Integrate over one period $[s,s+2\pi]$. Since $\gamma_0$ is a closed curve ($\gamma_0(s+2\pi)=\gamma_0(s)$):
$$
0=\gamma_0(s+2\pi)-\gamma_0(s)=\frac{2\pi\alpha}{|c|}\,\hat c+\int_s^{s+2\pi}\gamma_0'^{\perp}(u)\,du.
$$
The first term is **parallel** to $\hat c$; the integral is **perpendicular** to $c$ (hence to $\hat c$). Two orthogonal vectors summing to zero must each be zero. In particular
$$
\frac{2\pi\alpha}{|c|}=0\;\Longrightarrow\;\boxed{\;\alpha=0.\;}
$$

## Step 8. With $\alpha=0$, both boundary curves are planar

$\alpha=0$ gives:
- $g(s)=s$: rulings are vertical in $(\theta,z)$, i.e. each ruling connects $(s,0)$ to $(s,1)$.
- $|c|^2=0+1=1$, so $|c|=1$.
- $\gamma_0'(s)\cdot c=\alpha=0$ for all $s$: **$c$ is perpendicular to every tangent vector of $\gamma_0$**.

A curve all of whose tangents are perpendicular to a fixed vector $c$ lies in a plane perpendicular to $c$: indeed $\frac{d}{ds}(\gamma_0(s)\cdot c)=\gamma_0'(s)\cdot c=0$, so $\gamma_0(s)\cdot c=\text{const}$. Therefore **$\gamma_0$ is planar**, lying in the plane $\{x\cdot c=\text{const}\}$.

Since $\gamma_1(s)=\gamma_0(s)+c$, the top boundary $\gamma_1$ lies in the parallel plane $\{x\cdot c=\text{const}+|c|^2\}$.

## Step 9. Conclusion

For every $t$, both boundary curves of $M_t=\Gamma(M,t)$ lie in (parallel) planes. Therefore **any bending of $M$ leaves the bases planar**.

$$
\boxed{\text{Yes. Every bending of }M\text{ leaves both boundary circles planar.}}
$$

---

## Remark (non-trivial bendings exist)

The conclusion does *not* force the bending to be a rigid motion. The bottom curve $\gamma_0$ may be any closed plane curve of length $2\pi$ (arc-length parametrized, with $\int_0^{2\pi}\kappa\,ds=2\pi$), not necessarily a circle; the surface $\gamma_0(s)+z\,c$ ($c$ a unit normal to the plane of $\gamma_0$) is then an isometric embedding of $M$ with planar but non-circular bases. What the proof rules out is only *non-planarity* of the bases, not non-circularity.

```

### 解题 AI 的工具调用记录摘要（如可用）

```
（暂未提供解题AI的工具调用记录）
```

---

## 输出格式

输出你的审计报告为单个 XML 块。每个 XML 标签必须用完全匹配的闭合标签关闭。

```xml
<proof_audit>
  <problem_id>p27-full-deepmath_103k_00000550</problem_id>
  <audit_status>ONE_OF: PASS, PASS_WITH_CAVEAT, FAIL_WRONG_ANSWER, FAIL_HALLUCINATION, FAIL_INCOMPLETE, FAIL_LOGIC_ERROR, FAIL_CHEATING, FAIL_CHEATING_DECLARED, PARSE_ERROR</audit_status>
  <check_results>
    <A1>PASS or FAIL: 一句话理由</A1>
    <B1>PASS or FAIL: 一句话理由</B1>
    <B2>PASS or FAIL: 一句话理由</B2>
    <C1>PASS or FAIL: 一句话理由</C1>
    <C2>PASS or FAIL: 一句话理由</C2>
    <D1>PASS or FAIL: 一句话理由</D1>
    <D2>PASS or FAIL: 一句话理由</D2>
    <E1>PASS or FAIL or N/A: 一句话理由</E1>
    <E2>PASS or FAIL or N/A: 一句话理由</E2>
  </check_results>
  <cheating_analysis>如果有作弊嫌疑，详细说明发现的证据（搜了什么/找到了什么/proof 中哪里出现了搜来的内容）；无作弊嫌疑则写"无作弊嫌疑"</cheating_analysis>
  <audit_summary>一句话总结审计结论</audit_summary>
</proof_audit>
### PROOF AUDIT COMPLETE
```

**重要**：
- 审计完成后必须输出 `### PROOF AUDIT COMPLETE` 标记
- 每个检查项的 reason 要具体——不能只写"PASS"或"FAIL"，要写一句话理由
- cheating_analysis 即使无作弊也要写"无作弊嫌疑"，不能省略
