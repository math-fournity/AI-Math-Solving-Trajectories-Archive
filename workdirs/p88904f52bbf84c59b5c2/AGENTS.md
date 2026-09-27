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

A specialized concrete-mixing company, "Solid Foundations," is testing the quality of various binding agents. The quality of an agent is represented by a function $f(t)$, where $t$ represents the time in hours since the start of a 1-hour curing process ($0 \le t \le 1$). The output $f(t)$ is a non-negative real value representing the structural density of the mixture.

To be considered "Standard Grade," a binding agent's density function must satisfy three criteria:
1. The density $f$ is a continuous function over the interval $[0, 1]$.
2. The mixture must be "stable," meaning the density function $f$ is convex and non-decreasing over the entire hour.
3. For a fixed sensitivity constant $\alpha \ge 0$, the mixture must pass the "Differential Stress Test." This test compares the acceleration of density at the end of the process to the acceleration at the beginning. Specifically, the function must satisfy the inequality:
$$f(1) - 2f(2/3) + f(1/3) \ge \alpha \left( f(2/3) - 2f(1/3) + f(0) \right)$$

The company wants to create "Composite Blends" by taking two agents, $f$ and $g$, that both satisfy the "Standard Grade" criteria and multiplying their density functions together to form a new agent $h(t) = f(t) \cdot g(t)$.

For which values of the constant $\alpha$ is it guaranteed that every such Composite Blend $h$ will also satisfy the "Standard Grade" criteria?

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
