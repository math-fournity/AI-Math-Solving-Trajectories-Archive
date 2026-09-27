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

In a specialized laboratory, a security system is being configured using a circular sequence of 15 data ports, numbered 1 to 15 in clockwise order. To ensure maximum encryption, the system requires the installation of 15 unique hardware modules: 5 Red modules, 5 Blue modules, and 5 Green modules.

The security protocol mandates the following configuration constraints:
1.  A Red module must be plugged into Port 1.
2.  A Green module must be plugged into Port 15.
3.  No Green module may be placed in the port immediately to the left of a Red module (the port with the next higher number, where Port 1 is to the left of Port 2 and Port 15 is to the left of Port 1).
4.  No Red module may be placed in the port immediately to the left of a Blue module.
5.  No Blue module may be placed in the port immediately to the left of a Green module.

The total number of valid ways to arrange these specific 15 modules into the 15 ports is expressed as $N \cdot (5!)^3$. Find the value of $N$.

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
