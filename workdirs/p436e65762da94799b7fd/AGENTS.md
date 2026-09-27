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

A high-security vault uses a complex digital keypad where ten distinct security protocols, coded 0 through 9, are assigned to the unique letters A, B, C, D, E, F, G, H, and J. To unlock the system, a technician must verify three horizontal data streams and three vertical data streams.

**Horizontal Data Streams:**
1. The product of the two-digit code $AB$ and the two-digit code $CA$ must equal the three-digit system ID $DEB$.
2. The difference between the two-digit code $FC$ and the two-digit code $DG$ must equal the single-digit checksum $D$.
3. The sum of the two-digit code $EG$ and the two-digit code $HJ$ must equal the three-digit total $AAG$.

**Vertical Data Streams:**
1. the sum of $AB$ and $FC$ must equal the value $EG$.
2. The sum of $CA$ and $DG$ must equal the value $HJ$.
3. The quotient of $DEB$ divided by $D$ must equal the value $AAG$.

In these codes, $AB$ represents $10A + B$, $DEB$ represents $100D + 10E + B$, and so on. Each letter represents a unique digit from 0 to 9. Determine the unique digit assigned to each letter and calculate the sum $A + B + C + D + E + F + G + H + J$.

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
