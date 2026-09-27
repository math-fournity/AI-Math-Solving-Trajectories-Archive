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

In the distant star system of Prime-2017, a grand architectural project is underway to construct an infinite series of "Logic Grids." For any positive integer $n$, a Logic Grid is an $n \times n$ array of crystals. Each crystal $a_{ij}$ is assigned a resonance frequency chosen uniformly at random from the set of integers $\{0, 1, \ldots, 2016\}$.

The "Harmony Factor" of an $n \times n$ grid is defined as the determinant of the frequency matrix, calculated using standard arithmetic and then reduced modulo $2017$. A grid is considered "Perfectly Tuned" if its Harmony Factor is exactly $1$. Let $q_n$ represent the probability that a randomly generated $n \times n$ grid is Perfectly Tuned. 

As the dimensions of the grids grow toward infinity, the probability $q_n$ approaches a limiting value $q$. This limit $q$ can be expressed as a unique expansion in base $2017$:
$$q = \sum_{k=1}^{\infty} \frac{d_k}{2017^k}$$
where each $d_k$ is a digit in the set $\{0, 1, \ldots, 2016\}$.

The Architects require a checksum of the first $2017^2$ digits of this expansion to calibrate their equipment. Calculate the remainder when the sum $\sum_{k=1}^{2017^2} d_k$ is divided by $10^9$.

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
