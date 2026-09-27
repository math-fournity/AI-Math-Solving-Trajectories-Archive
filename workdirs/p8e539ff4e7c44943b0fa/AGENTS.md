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

In a remote industrial shipyard, a specialized logistics team is designing modular shipping containers. Each container is built by stacking identical $1 \times 1 \times 1$ steel crates into a solid rectangular block with dimensions $m$, $n$, and $r$. These dimensions are restricted to positive integers such that $m \le n \le r$.

To prepare for high-seas transport, the entire outer surface of the finished block is coated with a protective red anti-corrosive sealant. Afterward, for distribution, the block is disassembled back into its individual $1 \times 1 \times 1$ crates. The team categorizes the crates based on their exposure to the sealant:
- $k_0$ represents the number of crates that have no red faces.
- $k_1$ represents the number of crates that have exactly one red face.
- $k_2$ represents the number of crates that have exactly two red faces.

The quality control supervisor discovers a specific structural phenomenon where the quantity $k_0 + k_2 - k_1$ exactly equals $1985$.

Determine all possible sets of dimensions $(m, n, r)$ that satisfy this specific condition. If the complete set of all such valid dimension triples is $\{(m_1, n_1, r_1), (m_2, n_2, r_2), \dots, (m_k, n_k, r_k)\}$, calculate the total sum of all the dimensions involved: $\sum_{i=1}^k (m_i + n_i + r_i)$.

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
