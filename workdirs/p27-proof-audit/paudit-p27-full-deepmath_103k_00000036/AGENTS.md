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

Let $K$ be an abelian number field and $H(K)$ be the Hilbert class field of $K$. Assuming that $H(K)$ is abelian over $\mathbb{Q}$, do $K$ and $H(K)$ have the same conductor?

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
# Proof: $K$ and $H(K)$ have the same conductor

**Theorem.** Let $K$ be an abelian number field and $H(K)$ the Hilbert class field of $K$. If $H(K)$ is abelian over $\mathbb{Q}$, then $\mathfrak{f}(K) = \mathfrak{f}(H(K))$.

## Answer

$$\boxed{\text{Yes, } K \text{ and } H(K) \text{ have the same conductor.}}$$

## Proof

### Setup and the easy divisibility

Since $K \subseteq H(K)$ and both are abelian over $\mathbb{Q}$, the conductor of the subextension divides the conductor of the full extension:

$$\mathfrak{f}(K) \mid \mathfrak{f}(H(K)).$$

It remains to prove the reverse divisibility $\mathfrak{f}(H(K)) \mid \mathfrak{f}(K)$.

### Key observation: the hypothesis makes the Artin map available

The conductor $\mathfrak{f}(H(K))$ in the class field theory sense is defined via the Artin reciprocity map, which requires $H(K)/\mathbb{Q}$ to be abelian. This is precisely the hypothesis. The Artin map

$$\psi_{H(K)/\mathbb{Q}} : \{\text{ideals of } \mathbb{Z} \text{ coprime to } \mathfrak{d}(H(K))\} \longrightarrow \mathrm{Gal}(H(K)/\mathbb{Q})$$

is a surjective homomorphism, and $\mathfrak{f}(H(K))$ is the minimal modulus $\mathfrak{m}$ (finite part $\mathfrak{m}_0$, possibly with an infinite sign condition) such that $\psi_{H(K)/\mathbb{Q}}$ factors through the ray class group $\mathrm{Cl}_{\mathfrak{m}}(\mathbb{Q})$.

### Ramified primes coincide

If a prime $p$ is unramified in $K/\mathbb{Q}$, then every prime of $K$ above $p$ is unramified over $p$. Since $H(K)/K$ is unramified at all primes (finite and infinite), every prime of $H(K)$ above $p$ is unramified over $p$. Hence $p$ is unramified in $H(K)/\mathbb{Q}$.

Conversely, since $K \subseteq H(K)$, any prime ramified in $K/\mathbb{Q}$ is ramified in $H(K)/\mathbb{Q}$.

Therefore $K/\mathbb{Q}$ and $H(K)/\mathbb{Q}$ have the **same ramified primes**, and consequently the same primes appear in $\mathfrak{f}(K)$ and $\mathfrak{f}(H(K))$.

### The main argument: $\psi_{H(K)/\mathbb{Q}}$ factors through $\mathfrak{f}(K)$

To show $\mathfrak{f}(H(K)) \mid \mathfrak{f}(K)$, we must show that $\psi_{H(K)/\mathbb{Q}}$ factors through the ray class group modulo $\mathfrak{f}(K)$. Equivalently, we show:

> **Claim.** For every positive $a \in \mathbb{Q}^*$ with $a \equiv 1 \pmod{\mathfrak{f}(K)}$ and $\gcd(a, \mathfrak{f}(H(K))) = 1$, we have $\psi_{H(K)/\mathbb{Q}}((a)) = 1$.

**Well-definedness of the Artin map at $(a)$:** The condition $a \equiv 1 \pmod{\mathfrak{f}(K)}$ implies $\gcd(a, \mathfrak{f}(K)) = 1$. Since the ramified primes of $H(K)/\mathbb{Q}$ and $K/\mathbb{Q}$ coincide (established above), $\gcd(a, \mathfrak{f}(K)) = 1$ implies $\gcd(a, \mathfrak{f}(H(K))) = 1$, so the Artin map is defined at $(a)$.

**Proof of the Claim.** Let $a \in \mathbb{Q}^*$, $a > 0$, $a \equiv 1 \pmod{\mathfrak{f}(K)}$, $\gcd(a, \mathfrak{f}(H(K))) = 1$.

**Step 1 — Restriction to $K$ is trivial.** Since $a \equiv 1 \pmod{\mathfrak{f}(K)}$, by definition of the conductor of $K/\mathbb{Q}$:

$$\psi_{K/\mathbb{Q}}((a)) = 1 \in \mathrm{Gal}(K/\mathbb{Q}).$$

By the compatibility of Artin maps in the tower $H(K) \supseteq K \supseteq \mathbb{Q}$ (restriction to subextensions):

$$\psi_{H(K)/\mathbb{Q}}((a))\Big|_K = \psi_{K/\mathbb{Q}}((a)) = 1.$$

Therefore $\psi_{H(K)/\mathbb{Q}}((a)) \in \mathrm{Gal}(H(K)/K)$.

**Step 2 — Tower compatibility with $H(K)/K$.** The Artin maps in the tower $H(K) \supseteq K \supseteq \mathbb{Q}$ satisfy the standard compatibility (see e.g. Neukirch, *Class Field Theory*, or Milne, *Class Field Theory*, Ch. V):

$$\psi_{H(K)/K}(x) = \psi_{H(K)/\mathbb{Q}}(x)\Big|_{\mathrm{Gal}(H(K)/K)}$$

for any idele $x \in \mathbb{A}_{\mathbb{Q}}^*$, viewed as an idele of $K$ via the natural inclusion $\mathbb{A}_{\mathbb{Q}}^* \hookrightarrow \mathbb{A}_K^*$.

Applying this to the principal idele $x = (a) \in \mathbb{Q}^* \hookrightarrow K^*$:

$$\psi_{H(K)/K}((a)) = \psi_{H(K)/\mathbb{Q}}((a))\Big|_{\mathrm{Gal}(H(K)/K)}.$$

**Step 3 — The unramified Artin map kills principal ideals.** Since $H(K)/K$ is unramified at every prime (finite and infinite), the Artin map $\psi_{H(K)/K}$ factors through the ideal class group:

$$\psi_{H(K)/K} : \mathrm{Cl}(K) \xrightarrow{\;\sim\;} \mathrm{Gal}(H(K)/K), \qquad [\mathfrak{A}] \longmapsto \left(\frac{H(K)/K}{\mathfrak{A}}\right).$$

For the principal idele $a \in K^*$, the associated ideal is $a\mathcal{O}_K$, which is principal. Hence its class is trivial:

$$\psi_{H(K)/K}((a)) = [a\mathcal{O}_K] = 1 \in \mathrm{Cl}(K) \cong \mathrm{Gal}(H(K)/K).$$

**Step 4 — Conclusion.** From Step 1, $\psi_{H(K)/\mathbb{Q}}((a)) \in \mathrm{Gal}(H(K)/K)$. From Steps 2 and 3, this element equals $\psi_{H(K)/K}((a)) = 1$. Therefore:

$$\psi_{H(K)/\mathbb{Q}}((a)) = 1 \in \mathrm{Gal}(H(K)/\mathbb{Q}).$$

This proves the Claim. $\square$

Since $\psi_{H(K)/\mathbb{Q}}$ is trivial on all principal ideals $(a)$ with $a \equiv 1 \pmod{\mathfrak{f}(K)}$, $a > 0$, the Artin map factors through the ray class group modulo $\mathfrak{f}(K)$. By minimality of the conductor:

$$\mathfrak{f}(H(K)) \mid \mathfrak{f}(K).$$

### The infinite part

The conductor includes an infinite (sign) component: $\mathfrak{f}_\infty(L) = \infty$ if and only if $L$ is not totally real (equivalently, the sign character appears in the Dirichlet character group of $L/\mathbb{Q}$).

Since $H(K)/K$ is unramified at every infinite place, every real embedding of $K$ extends to a real embedding of $H(K)$. Therefore:

$$H(K) \text{ is totally real} \iff K \text{ is totally real},$$

which gives $\mathfrak{f}_\infty(H(K)) = \mathfrak{f}_\infty(K)$.

### Final conclusion

Combining the finite and infinite parts:

$$\mathfrak{f}(K) \mid \mathfrak{f}(H(K)) \quad \text{and} \quad \mathfrak{f}(H(K)) \mid \mathfrak{f}(K),$$

therefore

$$\mathfrak{f}(K) = \mathfrak{f}(H(K)). \qquad \blacksquare$$

### Remark on the role of the hypothesis

The hypothesis that $H(K)/\mathbb{Q}$ is abelian is essential in two ways:

1. **It makes the conductor well-defined.** The class field theory conductor (minimal modulus for the Artin reciprocity map) is defined for abelian extensions. Without this hypothesis, $\mathfrak{f}(H(K))$ in this sense would not be defined.

2. **It is not automatic.** For example, $K = \mathbb{Q}(\sqrt{-23})$ has class number $h(K) = 3$, and $\mathrm{Gal}(H(K)/\mathbb{Q}) \cong S_3$ is non-abelian. The hypothesis fails, and the question does not apply.

### Verification: $K = \mathbb{Q}(\sqrt{-5})$

- $h(K) = 2$, $\mathrm{Cl}(K) \cong \mathbb{Z}/2\mathbb{Z}$.
- $H(K) = \mathbb{Q}(\sqrt{-5}, i)$, and $\mathrm{Gal}(H(K)/\mathbb{Q}) \cong (\mathbb{Z}/2)^2$ is abelian. ✓
- $\mathfrak{f}(K) = 20$ and $\mathfrak{f}(H(K)) = 20$. ✓

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
  <problem_id>p27-full-deepmath_103k_00000036</problem_id>
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
