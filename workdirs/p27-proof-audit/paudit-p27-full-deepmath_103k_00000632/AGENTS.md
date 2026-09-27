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

Let $M$ and $N$ be $d$-dimensional Riemannian manifolds, and let $f: M \to N$ be a function that is continuous and differentiable almost everywhere. Suppose that the differential $df$ is an orientation-preserving isometry almost everywhere. Is it true that there exists a ball $B_{\epsilon}(p) \subseteq M$ such that the restriction $f|_{B_{\epsilon}(p)}$ is injective?

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在T
```

### 标准答案

```
（标准答案缺失）
```

### 待审计的 proof.md

```
# Proof: Local Injectivity under a.e. Orientation-Preserving Isometric Differential

## Answer

$$\boxed{\text{No}}$$

There need not exist any ball $B_\epsilon(p)\subseteq M$ on which $f$ is injective. We construct a counterexample valid for every dimension $d\geq 1$.

---

## Step 1 — Two disjoint dense singular measures of disjoint support

Partition $\mathbb{Q}\cap[0,1]$ into two disjoint dense sets $Q^+=\{q_1,q_2,\dots\}$ and $Q^-=\{r_1,r_2,\dots\}$.

Inductively choose pairwise disjoint Cantor sets $C_n^+\subseteq(q_n-2^{-n-3},\,q_n+2^{-n-3})$ and $C_n^-\subseteq(r_n-2^{-n-3},\,r_n+2^{-n-3})$, each of Lebesgue measure $0$, with all $\{C_n^+,C_n^-\}_{n\geq 1}$ pairwise disjoint. (At step $n$ the union of previously chosen sets is closed and nowhere dense, so a Cantor set of measure $0$ fits inside the prescribed interval avoiding it.)

Let $\mu_n^\pm$ be the Cantor probability measure supported on $C_n^\pm$ (continuous, no atoms), and set
$$
\mu^+ = \sum_{n=1}^{\infty} 2^{-n}\,\mu_n^+,\qquad
\mu^- = \sum_{n=1}^{\infty} 2^{-n}\,\mu_n^-.
$$

**Properties of $\mu^\pm$.**

- Each $\mu^\pm$ is a probability measure on $[0,1]$, continuous (no atoms), since each $\mu_n^\pm$ is.
- $\operatorname{supp}\mu^+ = D^+ := \bigcup_n C_n^+$ and $\operatorname{supp}\mu^- = D^- := \bigcup_n C_n^-$.
- $D^+\cap D^-=\varnothing$ (pairwise disjoint construction).
- $D^+$ and $D^-$ are both **dense** in $[0,1]$: every $q_n$ is within $2^{-n-3}$ of $C_n^+$, and $\{q_n\}$ is dense, so $D^+$ is dense; likewise $D^-$.
- $\mu^\pm$ are **singular** w.r.t. Lebesgue measure, since $D^\pm$ has measure $0$.

---

## Step 2 — The function $f$

Define the signed distribution function
$$
g(x) = \mu^+([0,x]) - \mu^-([0,x]),\qquad x\in[0,1],
$$
extended to all of $\mathbb{R}$ by $g(x)=g(0)$ for $x<0$ and $g(x)=g(1)$ for $x>1$. Set
$$
f(x) = x + g(x).
$$

**Continuity.** $\mu^\pm$ have no atoms, so $g$ is continuous, hence $f$ is continuous.

**A.e. differentiability and $f'=1$ a.e.** Since $\mu^\pm$ are singular w.r.t. Lebesgue measure, the Radon–Nikodym derivative $d\mu^\pm/dx = 0$ a.e. By the Lebesgue decomposition theorem, $g'(x)=0$ for Lebesgue-a.e. $x$, hence
$$
f'(x) = 1 + g'(x) = 1\quad\text{a.e.}
$$
In dimension $d=1$, $f'=1$ is an orientation-preserving isometry a.e.

---

## Step 3 — $f$ is not injective on any interval

We use the classical fact (see Rudin, *Real and Complex Analysis*; or Folland, *Real Analysis*):

> **Fact (symmetric derivative of a singular measure).** If $\mu$ is a finite Borel measure singular w.r.t. Lebesgue measure, then for $\mu$-a.e. $x$,
> $$
> \lim_{r\to 0^+}\frac{\mu([x-r,x+r])}{2r}=+\infty.
> $$

In particular, for $\mu^-$-a.e. $x\in D^-$ this limit is $+\infty$, and likewise for $\mu^+$-a.e. $x\in D^+$.

Let $I\subseteq\mathbb{R}$ be any nonempty open interval.

### (a) $f$ is not strictly increasing on $I$

Since $D^-$ is dense, $D^-\cap I\neq\varnothing$. Pick $x\in D^-\cap I$ at which the symmetric derivative of $\mu^-$ is $+\infty$. For all sufficiently small $r>0$ with $[x-r,x+r]\subseteq I$:
- $\mu^-([x-r,x+r]) > 4r$ (by the symmetric-derivative fact),
- $\mu^+([x-r,x+r]) < r$ (since $\mu^+$ is a continuous measure, $\mu^+([x-r,x+r])\to 0$ as $r\to 0$).

Then
$$
g(x+r)-g-r) = \mu^+([x-r,x+r]) - \mu^-([x-r,x+r]) < r - 4r = -3r,
$$
so
$$
f(x+r)-f(x-r) = 2r + \bigl(g(x+r)-g(x-r)\bigr) < 2r - 3r = -r < 0.
$$
Since $x+r > x-r$ yet $f(x+r) < f(x-r)$, the function $f$ is **not strictly increasing** on $I$.

### (b) $f$ is not strictly decreasing on $I$

Symmetrically, $D^+\cap I\neq\varnothing$. Pick $y\in D^+\cap I$ at which the symmetric derivative of $\mu^+$ is $+\infty$. For small $r>0$:
- $\mu^+([y-r,y+r]) > 4r$,
- $\mu^-([y-r,y+r]) < r$.

Then
$$
g(y+r)-g(y-r) = \mu^+([y-r,y+r]) - \mu^-([y-r,y+r]) > 4r - r = 3r,
$$
so
$$
f(y+r)-f(y-r) = 2r + 3r = 5r > 0.
$$
Since $y+r > y-r$ and $f(y+r) > f(y-r)$, the function $f$ is **not strictly decreasing** on $I$.

### (c) Conclusion for $d=1$

A continuous function on an interval is injective if and only if it is strictly monotone. Since $f$ is continuous on $I$ and is neither strictly increasing nor strictly decreasing, $f$ is **not injective on $I$**.

As every open ball in $\mathbb{R}$ contains an open interval, $f$ is not injective on any ball.

---

## Step 4 — Higher dimensions $d\geq 2$

Take $M=N=\mathbb{R}^d$ with the Euclidean metric. Define
$$
F(x_1,x_2,\dots,x_d) = \bigl(f(x_1),\,x_2,\,\dots,\,x_d\bigr),
$$
where $f$ is the 1D function from Step 2.

**Continuity.** $F$ is continuous since $f$ is.

**A.e. differentiability.** By Fubini's theorem, $f$ is differentiable for a.e. $x_1$, so $F$ is differentiable for a.e. $(x_1,\dots,x_d)\in\mathbb{R}^d$.

**Differential is an orientation-preserving isometry a.e.** At every point of differentiability,
$$
dF = \begin{pmatrix} f'(x_1) & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} = I_d\quad\text{a.e.},
$$
since $f'=1$ a.e. The identity $I_d\in SO(d)$ is an orientation-preserving isometry.

**Non-injectivity on every ball.** Let $B_\epsilon(p)\subseteq\mathbb{R}^d$ be any ball. The line segment
$$
\ell = \bigl\{(t,\,p_2,\,\dots,\,p_d) : t\in(p_1-\epsilon,\,p_1+\epsilon)\bigr\}\subseteq B_\epsilon(p)
$$
is mapped by $F$ to $\{(f(t),\,p_2,\,\dots,\,p_d):t\in(p_1-\epsilon,p_1+\epsilon)\}$. By Step 3, $f$ is not injective on $(p_1-\epsilon,p_1+\epsilon)$, so there exist $t_1\neq t_2$ with $f(t_1)=f(t_2)$. Then
$$
F(t_1,p_2,\dots,p_d) = F(t_2,p_2,\dots,p_d),
$$
yet $(t_1,p_2,\dots,p_d)\neq(t_2,p_2,\dots,p_d)$. Hence $F$ is not injective on $B_\epsilon(p)$.

---

## Step 5 — Riemannian manifold setting

The above gives a counterexample on $M=N=\mathbb{R}^d$ (a $d$-dimensional Riemannian manifold). For general $d$-dimensional Riemannian manifolds, take any coordinate chart and transport the construction inward; the conclusion is the same. Thus the answer is negative in general.

---

## Why Positive Results Fail Here

One might hope for a positive answer via Reshetnyak's theory of quasiregular mappings: $dF=I$ a.e. implies the distortion $K=1$, which would force $F$ to be open and discrete (hence locally injective off a discrete branch set). However, Reshetnyak's theorem requires $F\in W^{1,d}_{\mathrm{loc}}$, in particular the ACL (absolute continuity on lines) property. The hypothesis of mere a.e. differentiability does **not** imply ACL — our function $f(x)=x+g(x)$ with $g$ a singular-measure distribution function is the canonical counterexample: it is differentiable a.e. with $f'=1$ but is not absolutely continuous. Hence the Sobolev/quasiregular machinery does not apply, and no local injectivity can be guaranteed.

---

### PROOF COMPLETE

$$\boxed{\text{No}}$$

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
  <problem_id>p27-full-deepmath_103k_00000632</problem_id>
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
