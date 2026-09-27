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

In the digital archives of the planet Prime-11, a self-replicating data structure evolves over discrete time intervals according to a strict recursive protocol. At time $n=0$, the system initializes with a single data string represented by the polynomial $f_0(x) = x$. 

For every subsequent time step $n \ge 0$, the system processes the existing data string to generate a new one using the transformation $f_{n+1}(x) = f_n(x)^{11} - f_n(x)$. All computations and coefficients within this system are governed by the modular arithmetic of the field $\mathbb{F}_{11}$.

A specialized security scan is performed on the data string at time $n=1000$. This scan identifies all "atomic components" of the string $f_{1000}(x)$, defined as the set of nonconstant monic irreducible polynomials that divide it.

Let $N$ be the total number of these unique atomic components. To complete the security report, calculate the value of $N \pmod{1000}$.

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
