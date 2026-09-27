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

An experimental drone is programmed to navigate a linear track based on a sequence of 5 commands. The remote control has only 5 available buttons: the digits 1, 2, and 3, and two directional toggles, "Positive" (+) and "Negative" (-). 

A technician enters a sequence of 5 commands by pressing one of these five buttons at random for each instruction; every button has an equal 1/5 probability of being selected at each step. After the sequence is entered, the drone’s onboard computer evaluates the entire string to determine its final displacement $E$ from the starting point 0:

1.  **Concatenation:** Consecutive digits form multi-digit numbers (e.g., the sequence 1, 3, 2 results in 132).
2.  **Sign Parsing:** The symbols + and - act as operators or signs. Multiple consecutive symbols are simplified using standard rules of signs (e.g., - - becomes +, while - + - becomes +). If a sequence begins with symbols, they define the sign of the first number.
3.  **Operation:** The computer treats the simplified + and - as addition and subtraction between the formed numbers (e.g., 1, 3, -, 2, 2 is evaluated as $13 - 22 = -9$).
4.  **Formatting Rules:** Any symbols appearing at the very end of the 5-command sequence are ignored. If the sequence consists entirely of symbols with no digits, the displacement $E$ is 0.

Find the expected value of the drone's final displacement $E$.

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
