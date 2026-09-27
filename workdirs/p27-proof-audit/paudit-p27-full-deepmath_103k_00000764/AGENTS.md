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

Determine whether the following statement is true or false: For every natural number $n$, there exists a natural number $N$ such that for any subset $A$ of $\{1, 2, \ldots, N\}$, either $A$ or its complement contains an arithmetic progression of length $n$. Provide a justification for your answer.

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
# Proof

**Claim.** For every natural number $n$, there exists a natural number $N$ such that for any subset $A$ of $\{1, 2, \ldots, N\}$, either $A$ or its complement $\overline{A} = \{1,\ldots,N\}\setminus A$ contains an arithmetic progression of length $n$.

**Answer: TRUE.**

## Reduction to van der Waerden's theorem

We show the claim is exactly the $r=2$, $k=n$ special case of **van der Waerden's theorem**:

> **van der Waerden's theorem.** For all positive integers $r$ and $k$, there exists a number $W(r,k)$ such that every $r$-coloring of $\{1,2,\ldots,W(r,k)\}$ contains a monochromatic arithmetic progression of length $k$.

Given $n$, set $N = W(2,n)$. Let $A \subseteq \{1,\ldots,N\}$ be arbitrary. Define a 2-coloring $c:\{1,\ldots,N\}\to\{1,2\}$ by
$$
c(i) = \begin{cases} 1 & \text{if } i \in A,\\ 2 & \text{if } i \in \overline{A}.\end{cases}
$$
By van der Waerden's theorem (with $r=2$, $k=n$), there is a monochromatic arithmetic progression $a, a+d, a+2d, \ldots, a+(n-1)d$ of length $n$ inside $\{1,\ldots,N\}$. Monochromatic means all its terms share one color: either color $1$, in which case the whole progression lies in $A$; or color $2$, in which case it lies in $\overline{A}$. This is exactly what the claim requires. $\square$

## Justification of van der Waerden's theorem (proof sketch)

We recall the standard double-induction proof (Graham–Rothschild–Spencer; see also *Proofs from THE BOOK*), which establishes $W(r,k)$ for all $r,k\ge 1$.

**Base cases.** $W(1,k)=k$ (a single color makes the first $k$ points a monochromatic AP), and $W(r,1)=1$ (an AP of length $1$ is trivially monochromatic). Also $W(r,2)=r+1$ by the pigeonhole principle.

**Inductive structure.** Fix $k\ge 2$ and assume $W(r,k-1)$ exists for every $r$ (outer induction on $k$). We prove $W(r,k)$ exists by induction on $r$. The key tool is the notion of a **color-focused fan**:

> **Definition.** In an $r$-coloring of $\{1,\ldots,L\}$, a *fan of degree $m$ with focus $f$* is a collection of $m$ monochromatic APs $P_1,\ldots,P_m$, each of length $k-1$, each of a (pairwise) distinct color, with respective common differences $d_1,\ldots,d_m$ (which may differ), such that every $P_i$ ends at the same point $f$:
> $$P_i = \{f-(k-1)d_i,\; f-(k-2)d_i,\;\ldots,\; f-d_i,\; f\}\setminus\{f\}, \qquad i=1,\ldots,m.$$

The crucial observation: **if a fan of degree $r$ exists (covering all $r$ colors), then a monochromatic AP of length $k$ exists.** Indeed, the focus $f$ itself has some color $j$; appending $f$ to $P_j$ extends the color-$j$ progression $P_j$ to length $k$.

**Fan lemma.** For every $m\le r$ there exists $L_m$ such that every $r$-coloring of $\{1,\ldots,L_m\}$ contains a fan of degree $m$.

*Proof of the fan lemma (induction on $m$).* Set $w = W(r,k-1)$ (which exists by the outer induction on $k$).

- **Base $m=1$:** Take $L_1 = w$. By definition of $W(r,k-1)=w$, any $r$-coloring of $\{1,\ldots,w\}$ contains a monochromatic AP of length $k-1$; this is a fan of degree $1$ (its last element is the focus).

- **Inductive step $m-1\to m$:** Assume $L_{m-1}$ exists. Set
$$L_m = 2w\cdot L_{m-1}.$$
Partition $\{1,\ldots,L_m\}$ into $2L_{m-1}$ consecutive blocks $B_1,\ldots,B_{2L_{m-1}}$, each of size $w$. In each block $B_s$, by $W(r,k-1)=w$, there is a monochromatic AP of length $k-1$; record its color $c_s\in\{1,\ldots,r\}$ and the *relative position* of its focus within the block, i.e. an index $\rho_s\in\{1,\ldots,w\}$ (the offset of the focus from the block's left endpoint). This produces a sequence of $2L_{m-1}$ "typed" blocks, each carrying a label $(c_s,\rho_s)\in\{1,\ldots,r\}\times\{1,\ldots,w\}$.

Now apply the induction hypothesis $L_{m-1}$ to the *sequence of labels*: viewing the $2L_{m-1}$ blocks as positions colored by their label $(c_s,\rho_s)$ from a palette of $rw$ possible labels, and using $W(rw,\,2)=rw+1\le 2L_{m-1}$ (pigeonhole), we extract a sub-collection of blocks whose labels agree. More precisely, by the inductive construction of $L_{m-1}$ applied at the level of the label sequence, one obtains $m-1$ blocks $B_{s_1},\ldots,B_{s_{m-1}}$ carrying fans of degree $m-1$ that are *aligned*: their foci sit at the same relative position $\rho$ inside their respective blocks, and the blocks themselves are equally spaced (common block-difference $\Delta$). The color of the fan inside $B_{s_i}$ is some color $c^{(i)}$, and these $m-1$ colors are distinct.

Because the foci are at the same relative position $\rho$ in equally-spaced blocks, the actual foci in $\{1,\ldots,L_m\}$ form an arithmetic progression with common difference $\Delta\cdot w$. Looking one block further along this progression, at block $B_{s_m}:=B_{s_1+\Delta\cdot m}$ (which exists since we reserved $2L_{m-1}$ blocks), the point at relative position $\rho$ in $B_{s_m}$ is the common focus $f$ of a fan of degree $m$: the $m-1$ existing APs (translated to end at $f$) contribute $m-1$ distinct colors, and the AP of length $k-1$ inside $B_{s_m}$ contributes a new color (distinct from the others by construction). This yields a fan of degree $m$, completing the induction. $\square$ (fan lemma)

**Completing the proof.** Taking $m=r$ in the fan lemma gives $L_r$ such that every $r$-coloring of $\{1,\ldots,L_r\}$ contains a fan of degree $r$. As noted above, a fan of degree $r$ forces a monochromatic AP of length $k$. Hence $W(r,k)\le L_r$ exists, completing the inner induction on $r$, and thus the outer induction on $k$.

Therefore van der Waerden's theorem holds for all $r,k\ge 1$, and in particular $W(2,n)$ exists for every $n$, which is exactly what the claim requires.

$$\boxed{\text{TRUE}}$$

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
  <problem_id>p27-full-deepmath_103k_00000764</problem_id>
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
