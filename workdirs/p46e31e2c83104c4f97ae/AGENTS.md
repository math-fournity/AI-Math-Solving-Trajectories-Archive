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

In a futuristic data center, a master control system manages a data buffer of size $n$, where $n$ is any integer from 2 to 100 inclusive. The state of the buffer is represented by a value $x$ in the range of integers $\{0, 1, \dots, n-1\}$. All operations on the buffer are performed modulo $n$.

Initially, the buffer value is set to $1$. Two technicians, Ariane and Bérénice, take turns modifying this value to test system stability, with Ariane taking the first turn. On any given turn, the technician must replace the current value $x$ with either $(x+1) \pmod n$ or $(2x) \pmod n$.

Ariane’s objective is to force the buffer value to $0$ at any point in the process, which triggers a system reset and counts as a victory for her. Bérénice’s objective is to manage the values such that the buffer never hits $0$, regardless of how many turns are played. Both technicians play with perfect logic and foresight.

Let $f(n) = 1$ if Ariane can guarantee a victory for a specific buffer size $n$, and let $f(n) = 0$ if Bérénice can successfully prevent the value $0$ from ever being reached. 

Calculate the value of the sum:
$$\sum_{n=2}^{100} f(n)$$

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
