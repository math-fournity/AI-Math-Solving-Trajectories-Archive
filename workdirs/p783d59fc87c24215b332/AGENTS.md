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

In a specialized logistics hub, six unique parcels are arranged in a circular sorting carousel. There are three pairs of items, each pair consisting of one heavy crate (representing a boy) and one light package (representing a girl). The six items are labeled: Michael, Agnes, Ines, Steffen, Jörg, and Kerstin.

The automated sorting system operates under the following structural constraints:
1. No two items belonging to the same pair can be placed in adjacent slots on the carousel.
2. Steffen is positioned exactly opposite the oldest of the three heavy crates; this oldest crate is confirmed to be either Michael or Jörg.
3. Viewing the carousel from above, in a clockwise direction, Michael is placed in the slot immediately preceding Agnes, and Ines is placed in the slot immediately following Agnes.
4. Kerstin and Steffen do not belong to the same pair.
5. Jörg is classified as one of the three heavy crates.

To calibrate the system, you must determine the unique circular arrangement (starting from Michael and moving clockwise) and identify which light package belongs to which heavy crate. 

Assign values to the variables $a$, $b$, and $k$ based on the following pair identifications:
- $a$: Set to 1 if Agnes is paired with Michael, 2 if with Steffen, or 3 if with Jörg.
- $b$: Set to 1 if Ines is paired with Michael, 2 if with Steffen, or 3 if with Jörg.
- $k$: Set to 1 if Kerstin is paired with Michael, 2 if with Steffen, or 3 if with Jörg.

Calculate the final system code $X = 100a + 10b + k$.

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
