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

In a remote research outpost, a security console features a control panel with a 3x2 rectangular grid of six identical, unlabeled toggle switches. Each switch can be either in the "on" position (emitting a bright green light) or the "off" position (remaining dark).

Due to a total power failure in the facility, the room is in pitch-black darkness. An operator looking at the console can only see the glowing lights of the "on" switches; the physical frame of the panel, the labels, and the unlit switches are completely invisible. Because the switches are identical and the grid's borders cannot be seen, two different sets of activated switches are indistinguishable to the operator if one set can be rotated 180 degrees to look exactly like the other. (For example, if only one switch is lit, the operator will observe the same single point of light regardless of which of the six switches it is, as the panel’s orientation is not fixed in the dark).

If at least one of the six switches is currently toggled to the "on" position, how many visually distinct arrangements of lights can the operator observe?

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
