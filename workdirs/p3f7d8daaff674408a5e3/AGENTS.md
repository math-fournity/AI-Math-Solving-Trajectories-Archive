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

In a specialized industrial chemical facility, a series of $n$ reactors are arranged in a sequence. A pipeline passes through these reactors, carrying a reagent whose density fluctuates according to a specific periodic cycle. For each reactor index $k$ (where $k$ ranges from $0$ to $n-1$), the reagent flows through a specific segment of the pipe corresponding to the interval $[2k\pi, (2k+1)\pi]$.

The "accumulation potential" within each of these segments is defined by the integral of the function $x^p \sin^3 x \cos^2 x$ over that interval, where $p$ is a fixed positive physical constant. To calculate the total yield of the entire system, a technician sums these accumulation potentials for all reactors from $k=0$ up to $k=n-1$.

The final efficiency rating of the facility, denoted as $E$, is determined by taking this total sum and dividing it by $n^{p+1}$. As the facility scales up toward an infinite number of reactors ($n \to \infty$), the efficiency rating approaches a stable limit.

Determine the value of this limit in terms of the constant $p$.

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
