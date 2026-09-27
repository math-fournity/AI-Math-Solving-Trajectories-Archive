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

A specialized architectural firm is designing a complex of four support pillars for a futuristic pavilion. The locations of these pillars are represented by the four roots $r_1, r_2, r_3, r_4$ of the polynomial equation in the complex plane:
\[x^4 - 6ax^3 + (8a^2 + 5a)x^2 - 12a^2x + 4a^2 = 0\]
where $a$ is a specific scaling constant.

The structural integrity of the pavilion requires the existence of a specific reference point $z$ (where $z$ is a non-zero complex number) such that the distance from each pillar $r_i$ to this reference point is exactly equal to the absolute value of the real coordinate of that pillar. That is, for each $i \in \{1, 2, 3, 4\}$, the condition $|r_i - z| = |\Re(r_i)|$ must be satisfied.

Find the sum of all possible values of the scaling constant $a$ that allow such a reference point $z$ to exist. If the sum is an irreducible fraction $\frac{p}{q}$, compute the final value as $p + q$.

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
