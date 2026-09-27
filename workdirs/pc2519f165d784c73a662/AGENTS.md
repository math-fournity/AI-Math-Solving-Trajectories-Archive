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

A high-security facility features ten locked vaults, designated as Vault 0, Vault 1, ..., Vault 9. Each vault is protected by a unique 3-digit access code that must be determined according to a strict set of protocols:

1. **Code Composition**: Every code must consist of three distinct digits (from 0 to 9) that sum exactly to 15. The first digit (the hundreds place) cannot be 0.
2. **Identification Rule**: Vault $k$ must contain the digit $k$ somewhere within its 3-digit code (for example, Vault 0 must use a 0, Vault 1 must use a 1, and so on).
3. **Uniqueness Rule**: No two vaults may use the same set of three digits. (For instance, if one vault uses {1, 5, 9}, no other vault can use any permutation of {1, 5, 9}).
4. **Synchronization Constraints**: For specific pairs of vaults $(V_i, V_j)$, the code assigned to $V_i$ must be numerically smaller than the code assigned to $V_j$. Additionally, these two codes must share at least one digit in the exact same positional column (hundreds, tens, or units). This rule applies to the following thirteen pairs:
$(V_0, V_1), (V_0, V_3), (V_3, V_4), (V_1, V_5), (V_5, V_4), (V_6, V_5), (V_6, V_2), (V_2, V_7), (V_7, V_3), (V_6, V_9), (V_9, V_8), (V_8, V_4), (V_7, V_8)$.

Determine the sum of the ten 3-digit access codes for Vault 0 through Vault 9.

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
