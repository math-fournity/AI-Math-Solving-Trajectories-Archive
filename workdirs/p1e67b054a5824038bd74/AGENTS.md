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

In a specialized nanotechnology lab, an engineer is assembling a high-capacity thermal core. The core is a large $3\times 3 \times 3$ cube composed of $27$ identical cubic sensors. 

Each individual sensor has exactly four of its six faces coated in a heat-resistant orange polymer. The remaining two uncoated faces are positioned such that they always share a common edge.

To assemble the thermal core, the engineer places the $27$ sensors into a $3 \times 3 \times 3$ grid. Each sensor is oriented randomly, with all $24$ possible rotations of a cube being equally likely. For the core to function at maximum efficiency, the entire exterior surface area of the resulting $3 \times 3 \times 3$ large cube must be completely orange (no uncoated faces can be visible on any of the six exterior sides).

If the probability that the entire exterior surface of the large cube is orange can be expressed in the form $\frac{p^a}{q^br^c}$, where $p$, $q$, and $r$ are distinct prime numbers and $a$, $b$, and $c$ are positive integers, calculate the value of $a+b+c+p+q+r$.

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
