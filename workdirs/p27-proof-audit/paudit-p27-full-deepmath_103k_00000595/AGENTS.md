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

For what integer values of $d$ does the twisted tangent bundle $E = T\mathbb{P}^n \otimes \mathcal{O}_X(d-1)$ have a globally nonvanishing section, where $X = \mathbb{P}^n$ is the projective space over an algebraically closed field?

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出（必须用英文原文，不要翻译成中文）：
```

### 标准答案

```
（标准答案缺失）
```

### 待审计的 proof.md

```
# Proof: Nowhere-Vanishing Sections of $T\mathbb{P}^n \otimes \mathcal{O}(d-1)$

**Problem.** For what integer values of $d$ does $E = T\mathbb{P}^n \otimes \mathcal{O}_X(d-1)$ admit a globally nonvanishing (nowhere-zero) section, where $X = \mathbb{P}^n$ over an algebraically closed field?

**Answer.** In characteristic $0$:

$$\boxed{d = -1 \text{ if } n = 1; \quad \text{no integer } d \text{ if } n \geq 2.}$$

(The $n = 1$ case holds in **all** characteristics; for $n \geq 2$ the cases $d \leq 1$ are ruled out in all characteristics, and $d \geq 2$ is ruled out by the Chern class argument in characteristic $0$.)

---

## Setup: The Euler Sequence and Sections of $E$

The Euler exact sequence on $\mathbb{P}^n$ is:
$$0 \to \mathcal{O}_{\mathbb{P}^n} \to \mathcal{O}_{\mathbb{P}^n}(1)^{\oplus(n+1)} \to T\mathbb{P}^n \to 0.$$

Tensoring by $\mathcal{O}(d-1)$ (which is locally free, hence exact):
$$0 \to \mathcal{O}(d-1) \to \mathcal{O}(d)^{\oplus(n+1)} \to E \to 0. \tag{$\star$}$$

**Key equivalence.** A nowhere-zero section $s \in H^0(E)$ is equivalent to an injection of vector bundles $\mathcal{O} \hookrightarrow E$, which (tensoring by $\mathcal{O}(1-d)$) is equivalent to an injection $\mathcal{O}(1-d) \hookrightarrow T\mathbb{P}^n$ as a sub-line-bundle. The equivalence between "sheaf injection" and "nowhere-zero" holds because a morphism of line bundles $\mathcal{O} \to E$ that is injective as a sheaf map is fiberwise injective: if it vanished at some point $x$, the kernel would be nonzero at $x$, contradicting injectivity.

---

## Case $n = 1$: $d = -1$

For $n = 1$, $T\mathbb{P}^1 \cong \mathcal{O}(2)$, so:
$$E = \mathcal{O}(2) \otimes \mathcal{O}(d-1) = \mathcal{O}(d+1).$$

A nowhere-zero section of $\mathcal{O}(d+1)$ on $\mathbb{P}^1$ is a homogeneous polynomial of degree $d+1$ in two variables with no zero on $\mathbb{P}^1$.

- **$d + 1 > 0$** (i.e., $d \geq 0$): A nonzero homogeneous polynomial of positive degree in two variables over an algebraically closed field factors completely into linear factors, hence has a zero on $\mathbb{P}^1$. No nowhere-zero section exists.

- **$d + 1 = 0$** (i.e., $d = -1$): $E = \mathcal{O}(0) = \mathcal{O}$. The constant section $1$ is nowhere zero. ✓

- **$d + 1 < 0$** (i.e., $d \leq -2$): $H^0(\mathcal{O}(d+1)) = 0$, so no sections exist at all.

**Conclusion for $n = 1$:** The unique solution is $d = -1$, valid in all characteristics.

---

## Case $n \geq 2$: No Solution (Characteristic $0$)

We show that no integer $d$ yields a nowhere-zero section, by treating four ranges of $d$.

### Step 1: $d \leq -1$ — No Sections Exist

From $(\star)$, taking global sections (and using $H^1(\mathcal{O}(d-1)) = 0$ for $n \geq 2$ since $0 < 1 < n$):
$$H^0(E) \hookrightarrow H^0(\mathcal{O}(d))^{\oplus(n+1)} \quad \text{(surjection from the middle term)}.$$

For $d \leq -1$: $H^0(\mathcal{O}(d)) = 0$ and $H^0(\mathcal{O}(d-1)) = 0$, so from the long exact cohomology sequence of $(\star)$:
$$0 \to H^0(\mathcal{O}(d-1)) \to H^0(\mathcal{O}(d))^{\oplus(n+1)} \to H^0(E) \to H^1(\mathcal{O}(d-1)) \to \cdots$$

Since $H^0(\mathcal{O}(d-1)) = 0$, $H^0(\mathcal{O}(d)) = 0$, and $H^1(\mathcal{O}(d-1)) = 0$ (for $n \geq 2$), we get $H^0(E) = 0$.

**No section exists, hence no nowhere-zero section.** (Valid in all characteristics.)

### Step 2: $d = 0$ — Every Nonzero Section Vanishes at a Point

Here $E = T\mathbb{P}^n \otimes \mathcal{O}(-1)$. From $(\star)$ with $d = 0$:
$$0 \to \mathcal{O}(-1) \to \mathcal{O}(0)^{\oplus(n+1)} \to E \to 0.$$

Since $H^0(\mathcal{O}(-1)) = 0$ and $H^1(\mathcal{O}(-1)) = 0$ (for $n \geq 2$):
$$H^0(E) \cong H^0(\mathcal{O})^{\oplus(n+1)} \cong k^{n+1}.$$

A section $s$ corresponds to a vector $(a_0, \ldots, a_n) \in k^{n+1}$. Under the map $\mathcal{O}^{\oplus(n+1)} \to E = T\mathbb{P}^n \otimes \mathcal{O}(-1)$, the section $s$ at the point $x = [x_0 : \cdots : x_n]$ is the projection of $(a_0, \ldots, a_n)$ modulo the line $\text{span}(x_0, \ldots, x_n)$ (which is the image of $\mathcal{O}(-1) \to \mathcal{O}^{\oplus(n+1)}$ fiberwise).

Thus $s(x) = 0$ if and only if $(a_0, \ldots, a_n) \in \text{span}(x_0, \ldots, x_n)$, i.e., $[x_0 : \cdots : x_n] = [a_0 : \cdots : a_n]$.

For any nonzero $(a_0, \ldots, a_n)$, the section vanishes at the point $[a_0 : \cdots : a_n] \in \mathbb{P}^n$.

**No nowhere-zero section exists.** (Valid in all characteristics.)

### Step 3: $d = 1$ — Every Vector Field Vanishes Somewhere

Here $E = T\mathbb{P}^n$ and $H^0(T\mathbb{P}^n) \cong \mathfrak{pgl}_{n+1}(k)$, the Lie algebra of $(n+1)\times(n+1)$ matrices modulo scalars.

A vector field corresponds to a matrix $A \in M_{(n+1)\times(n+1)}(k)$ (defined up to adding a scalar matrix). The vector field vanishes at $x = [x_0 : \cdots : x_n]$ if and only if $Ax$ is proportional to $x$, i.e., $x$ is an eigenvector of $A$.

**Key fact:** Over an algebraically closed field, every $(n+1)\times(n+1)$ matrix has an eigenvalue (the characteristic polynomial splits completely), hence has an eigenvector. This holds in **any characteristic**.

Therefore every vector field on $\mathbb{P}^n$ vanishes at some point (the eigenvector of the corresponding matrix).

**No nowhere-zero section exists.** (Valid in all characteristics.)

### Step 4: $d \geq 2$ — Chern Class Obstruction (Characteristic $0$)

This is the only step requiring characteristic $0$.

**Necessary condition.** If $E$ has a nowhere-zero section, then $E \cong \mathcal{O} \oplus F$ where $F$ is a vector bundle of rank $n - 1$. Since $F$ has rank $n-1 < n$, its top Chern class satisfies $c_n(F) = 0$, and therefore:
$$c_n(E) = c_n(\mathcal{O} \oplus F) = c_n(\mathcal{O}) \cdot c_n(F) = 1 \cdot 0 = 0.$$

So **$c_n(E) = 0$ is a necessary condition** for a nowhere-zero section to exist.

**Computing $c_n(E)$.** From the Euler sequence, $c(T\mathbb{P}^n) = (1+H)^{n+1}$, so $c_k(T\mathbb{P}^n) = \binom{n+1}{k} H^k$ where $H = c_1(\mathcal{O}(1))$ is the hyperplane class.

The Chern roots of $T\mathbb{P}^n$ are formal elements $\alpha_1, \ldots, \alpha_n$ with $\prod_{i=1}^n(1+\alpha_i) = (1+H)^{n+1}$. Tensoring by $\mathcal{O}(d-1)$ shifts each Chern root to $\alpha_i + (d-1)H$, so:

$$c_n(E) = \prod_{i=1}^{n}\bigl(\alpha_i + (d-1)H\bigr) = \sum_{k=0}^{n} \binom{n+1}{k}(d-1)^{n-k}\, H^n.$$

Setting $u = d - 1$, this sum equals:
$$\sum_{k=0}^{n}\binom{n+1}{k}u^{n-k} = \frac{(1+u)^{n+1} - 1}{u} = \frac{d^{n+1} - 1}{d - 1} = 1 + d + d^2 + \cdots + d^n$$

(for $d \neq 1$; for $d = 1$ the value is $n+1$, consistent with the limit). Thus:

$$\boxed{c_n(E) = (1 + d + d^2 + \cdots + d^n)\, H^n.}$$

**Characteristic $0$ analysis.** For $d \geq 2$ in characteristic $0$:
$$1 + d + d^2 + \cdots + d^n = \frac{d^{n+1} - 1}{d - 1} > 0,$$
since $d \geq 2$ implies $d^{n+1} > 1$ and $d - 1 > 0$. Therefore $c_n(E) \neq 0$, contradicting the necessary condition.

**No nowhere-zero section exists for $d \geq 2$ in characteristic $0$.**

---

## Summary

| Range of $d$ | $n = 1$ | $n \geq 2$ (char $0$) | Reason |
|---|---|---|---|
| $d \leq -2$ | $H^0 = 0$ | $H^0 = 0$ | No sections |
| $d = -1$ | ✓ $\mathcal{O}$ has constant section | $H^0 = 0$ | $n=1$: $\mathcal{O}(0)$; $n\geq2$: no sections |
| $d = 0$ | Polynomial has zero | Every section vanishes at $[a]$ | Direct analysis |
| $d = 1$ | Polynomial has zero | Every vector field vanishes (eigenvector) | Matrix eigenvalue argument |
| $d \geq 2$ | Polynomial has zero | $c_n(E) \neq 0$ | Chern class obstruction (char $0$) |

**Final answer (characteristic $0$):**

$$\boxed{d = -1 \text{ if } n = 1; \quad \text{no integer } d \text{ works if } n \geq 2.}$$

### PROOF COMPLETE

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
  <problem_id>p27-full-deepmath_103k_00000595</problem_id>
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
