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

In the high-tech logistics center of the Orion Nebula, a specialized robot is tasked with delivering a single package to one of 2014 distinct docking bays, labeled 1 through 2014. To ensure total fairness, the robot selects the destination bay using a quantum signal generator that produces a random sequence of binary bits (0s and 1s), where each bit has an equal 0.5 probability of occurring.

The selection process works as follows: the robot generates a binary sequence $0.b_1b_2b_3...$ to represent a real number $X$ in the interval $[0, 1)$. The target bay $K$ is determined by the formula $K = \lceil 2014X \rceil$. However, the robot is programmed for maximum efficiency; it stops generating bits as soon as the bits already produced are sufficient to uniquely determine the value of $K$, regardless of what any subsequent bits in the infinite sequence might be. For example, if the target were chosen from only 3 bays, a sequence starting with $0.011_2$ would immediately fix $K=2$, while a sequence starting with $0.010_2$ would be inconclusive and require more bits.

Given that the robot must select a bay from $N=2014$ options using this specific halting criteria, the expected number of binary bits the robot must generate is a rational number expressed in lowest terms as $\frac{m}{n}$. 

Calculate the value of $100m + n$.

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
