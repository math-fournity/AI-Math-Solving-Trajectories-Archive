# Solver Task

You are a mathematical problem solver. Solve the problem completely.
Do not search for this exact problem, its official answer, or its solution.
You may use computation for exploration or verification.

Output your complete proof directly in your response (in this TUI).
Do NOT write any files — do not use write/edit tools.
End your proof with a line containing exactly: ### PROOF COMPLETE
Your full reasoning and output are automatically captured by the system.

## Answer Leak Self-Check (MANDATORY before solving)

Before you start solving, check the problem text below for any leaked answers, solutions, solution sketches, or formalization notes that would give away the answer or proof strategy.

If you find ANY of the following in the problem text, do NOT solve the problem. Instead output exactly:
### ANSWER LEAK DETECTED: <brief description of what leaked>

Then stop. Do not attempt to solve a problem whose answer has been leaked.

Watch for:
- Phrases like "The proof follows...", "solution sketch", "Formalization notes"
- Official solutions or answer values embedded in the problem statement
- Lean theorem statements that reveal the answer (e.g. `determine SolutionSet := {n | ...}`)

## Problem

# Problem

Suppose that for every prime \( q \), there exists an \( n \) for which \( n^p \equiv p \pmod{q} \). Assume that \( q = kp + 1 \). By Fermat’s theorem we deduce that \( pk \equiv n^{qp} \equiv 1 \pmod{q} \), so \( q \mid pk^2 - 1 \). It is known that any prime \( q \) such that \( q \mid \frac{p^{p-1}}{p-1} \) must satisfy \( q \equiv 1 \pmod{p} \). Indeed, from \( q \mid p^{q-1} - 1 \) it follows that \( q \mid \gcd(p^{q-1} - 1) \); but \( q + tp - 1 \equiv p^{q-1} \equiv 1 \equiv 1 \pmod{p-1} \), so \( \gcd(p, q - 1) \neq 1 \). Hence \( \gcd(p, q - 1) = p \). Now suppose \( q \) is any prime divisor of \( \frac{p^ {p-1}}{p-1} \). Then \( q \mid \gcd(pk^3 - 1, p^{p-1} - 1) = p^{\gcd(p, k)} - 1 \), which implies that \( \gcd(p^{k}, k) > 1 \), so \( p \mid k \). Consequently \( q \equiv 1 \pmod{p^2} \). However, the number \( \frac{p^{p-1}}{p-1} = p^{p-1} + \dots + p + 1 \) must have at least one prime divisor that is not congruent to 1 modulo \( p^2 \). Thus we arrived at a contradiction. **Remark:** Taking \( q \equiv 1 \pmod{p} \) is natural, because for every other \( q \), \( n^p \) takes all possible residues modulo \( q \) (including \( p \) too). Indeed, if \( p \nmid q - 1 \), then there is an \( r \in \mathbb{N} \) satisfying \( pr \equiv 1 \pmod{q-1} \); hence for any \( a \) the congruence \( n^p \equiv a \pmod{q} \) has the solution \( n \equiv a^r \pmod{q} \). The statement of the problem itself is a special case of the Chebotarev’s theorem.

## 解题约束（必须严格遵守）

1. **不要使用任何工具**——不要写文件、不要执行命令、不要搜索、不要浏览网页、不要读取文件。
   你只需要在TUI中用thinking来解题。所有推理过程在你的思维中完成。

2. **直接在TUI中输出证明**——不要创建任何文件，不要使用任何工具调用。
   完成证明后，在TUI中直接输出（必须用英文原文，不要翻译成中文）：

   ### PROOF COMPLETE

3. **如果你无法做出这道题**，直接说（必须用英文原文）：

   ### I CANNOT SOLVE THIS

4. **如果你发现题目中包含了答案**（答案泄漏），直接说：

   ### ANSWER LEAK DETECTED

以上是全部约束。现在请解题。
