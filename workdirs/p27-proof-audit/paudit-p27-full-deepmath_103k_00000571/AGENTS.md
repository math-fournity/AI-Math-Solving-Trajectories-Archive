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

Is the set of states $S(A)$ weak${}^*$ compact if $A$ is a non-zero, non-unital $C^*$-algebra?

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出：
```

### 标准答案

```
（标准答案缺失）
```

### 待审计的 proof.md

```
# Is $S(A)$ weak${}^*$ compact if $A$ is a non-zero, non-unital $C^*$-algebra?

## Answer

$$\boxed{\text{No.}$$

There exists a non-zero, non-unital $C^*$-algebra $A$ such that $S(A)$ is not weak${}^*$ compact. In particular, $A = C_0(\mathbb{R})$ is a counterexample.

---

## Preliminaries

Let $A$ be a $C^*$-algebra. A **state** on $A$ is a positive linear functional $\omega \in A^*$ with $\|\omega\| = 1$. The set of all states is
$$
S(A) = \{\omega \in A^* : \omega \geq 0,\; \|\omega\| = 1\}.
$$

Every state has norm $1$, so $S(A) \subseteq \overline{B}_{A^*}$, the closed unit ball of $A^*$. By the **Banach–Alaoglu theorem**, $\overline{B}_{A^*}$ is weak${}^*$ compact. Therefore
$$
S(A) \text{ is weak}^* \text{ compact} \iff S(A) \text{ is weak}^* \text{ closed in } A^*.
$$

**Unital case (for contrast).** If $A$ has a unit $\mathbf{1}$, then for every positive functional $\omega$ one has $\|\omega\| = \omega(\mathbf{1})$, so
$$
S(A) = \{\omega \in A^* : \omega \geq 0,\; \omega(\mathbf{1}) = 1\}.
$$
The positivity condition $\omega \geq 0$ is weak${}^*$ closed (it is the intersection of the weak${}^*$ closed half-spaces $\{\omega : \omega(a) \geq 0\}$ over $a \in A_+$), and the map $\omega \mapsto \omega(\mathbf{1})$ is weak${}^*$ continuous, so $\{\omega : \omega(\mathbf{1})=1\}$ is weak${}^*$ closed. Hence $S(A)$ is weak${}^*$ closed, and therefore weak${}^*$ compact.

The key point: in the unital case the norm condition $\|\omega\|=1$ can be rewritten as the weak${}^*$ continuous condition $\omega(\mathbf{1})=1$. In the **non-unital** case there is no unit element to play this role, and the norm condition $\|\omega\|=1$ is **not** weak${}^*$ closed (the norm is weak${}^*$ lower semi-continuous, so $\{\|\omega\|\leq 1\}$ is weak${}^*$ closed, but $\{\|\omega\|\geq 1\}$ is not). This suggests that $S(A)$ may fail to be weak${}^*$ closed, and we now exhibit a concrete counterexample.

---

## Counterexample: $A = C_0(\mathbb{R})$

Let
$$
A = C_0(\mathbb{R}) = \{f : \mathbb{R} \to \mathbb{C} \text{ continuous} : f(x) \to 0 \text{ as } |x|\to\infty\},
$$
with the supremum norm. This is a commutative $C^*$-algebra.

- **Non-zero:** The function $f(x) = e^{-x^2}$ lies in $A$ and is non-zero. ✓
- **Non-unital:** The constant function $\mathbf{1}$ does not vanish at infinity, so $\mathbf{1} \notin A$. ✓

By the **Riesz representation theorem**, the positive linear functionals on $C_0(\mathbb{R})$ are exactly the integration functionals against positive regular Borel measures, and the states are exactly the probability measures. In particular, for each $n \in \mathbb{N}$, the **point evaluation (Dirac measure)**
$$
\delta_n(f) := f(n), \qquad f \in C_0(\mathbb{R}),
$$
is a state:

- **Positivity:** If $f \geq 0$ pointwise, then $f(n) \geq 0$, so $\delta_n(f) \geq 0$. ✓
- **Norm one:** Clearly $|\delta_n(f)| = |f(n)| \leq \|f\|_\infty$, so $\|\delta_n\| \leq 1$. For the reverse inequality, take any $f \in C_0(\mathbb{R})$ with $f(n) = 1$ and $\|f\|_\infty = 1$ (such $f$ exists, e.g. a bump function peaked at $n$). Then $|\delta_n(f)| = 1 = \|f\|_\infty$, giving $\|\delta_n\| = 1$. ✓

Hence $\{\delta_n : n \in \mathbb{N}\} \subseteq S(A)$.

---

## The sequence $\delta_n$ converges weak${}^*$ to $0$

The weak${}^*$ topology on $A^*$ is the topology of pointwise convergence on elements of $A$. For any $f \in C_0(\mathbb{R})$, by definition $f(x) \to 0$ as $|x| \to \infty$, so in particular
$$
\delta_n(f) = f(n) \xrightarrow{n\to\infty} 0.
$$
Therefore $\delta_n \to 0$ in the weak${}^*$ topology, where $0 \in A^*$ denotes the zero functional.

---

## $0 \notin S(A)$

The zero functional has norm $\|0\| = 0 \neq 1$, so it is not a state. Thus $0 \notin S(A)$.

---

## Conclusion

We have exhibited a sequence $\{\delta_n\} \subseteq S(A)$ with $\delta_n \to 0$ in the weak${}^*$ topology, but $0 \notin S(A)$. Therefore $S(A)$ is **not** weak${}^*$ closed. Since $S(A) \subseteq \overline{B}_{A^*}$ (which is weak${}^*$ compact by Banach–Alaoglu), a subset of a compact space is compact if and only if it is closed. Hence $S(A)$ is **not** weak${}^*$ compact.

This shows that for the non-zero, non-unital $C^*$-algebra $A = C_0(\mathbb{R})$, the state space $S(A)$ is not weak${}^*$ compact. $\blacksquare$

---

### Remark

In fact one can show the sharper result: $S(A)$ is weak${}^*$ compact **if and only if** $A$ is unital. The reverse direction is the unital argument above; the forward direction follows because if $A$ is non-unital, one can always construct a net of states converging weak${}^*$ to $0$ (using the structure theory of non-unital $C^*$-algebras — approximate units, hereditary subalgebras, or the one-point unitization). The counterexample $A = C_0(\mathbb{R})$ above is the concrete, most transparent instance of this general phenomenon.

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
  <problem_id>p27-full-deepmath_103k_00000571</problem_id>
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
