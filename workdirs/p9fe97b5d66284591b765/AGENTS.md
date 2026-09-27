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

A team of civil engineers is designing two types of modular structures for a new research station.

**Phase A: Rectangular Storage Units**
The engineers are designing rectangular storage units where the floor dimensions, $c$ and $d$ meters, must both be integers. A specialized ventilation system is required such that the floor area of the unit (in square meters) is numerically equal to exactly twice the perimeter of the floor (in meters). Let $S_a$ be the sum of all possible values of the combined length and width $(c + d)$ for all unique rectangular designs that satisfy these requirements.

**Phase B: Cuboid Living Pods**
The team is also designing pressurized living pods in the shape of a rectangular cuboid. To simplify manufacturing, two of the dimensions must be equal (each $e$ meters), while the third dimension is $f$ meters; all three dimensions $e, e,$ and $f$ must be integers. The pods are designed such that the internal volume (in cubic meters) is numerically equal to exactly twice the total exterior surface area (in square meters). Let $S_b$ be the sum of all possible values of the total linear sum of the dimensions $(2e + f)$ for all unique pod designs that satisfy these requirements.

Calculate the final value of $S_a + S_b$.

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
