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

In a remote automated factory, a robotic sorting arm processes a sequence of specialized glass canisters. The volume of liquid in the first canister, measured in liters, is exactly $a_1 = 1$.

The factory’s central computer determines the volume of liquid for the next canister in the series, $a_{n+1}$, based on the volume of the current canister, $a_n$, according to a precise calibration protocol. To calculate the volume for the next canister, the computer first identifies the integer portion of the current volume (the floor value, $\lfloor a_n \rfloor$). It then doubles this integer, subtracts the actual current volume $a_n$, and adds $1$ to the result. Finally, it takes the reciprocal of this total value to set the volume for the next canister.

Following this strict recursive calibration for every canister $n \ge 1$:
$$a_{n+1}=\frac{1}{2\lfloor a_n \rfloor -a_n+1}$$

Find the volume of the liquid in the 2024th canister, $a_{2024}$.

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
