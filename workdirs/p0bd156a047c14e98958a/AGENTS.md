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

In a massive industrial manufacturing complex, a specialized 2013-meter-wide processing floor is divided into 2013 parallel vertical lanes, each exactly 1 meter wide. The lanes are indexed $i = 0, 1, \dots, 2012$, where lane $i$ covers the horizontal span from $x = i$ to $x = i+1$. To optimize sensor tracking, the floor is painted in a repeating pattern: all lanes where $i$ is an even integer are coated in pink anti-static resin, while all lanes where $i$ is an odd integer are coated in gray resin.

An architectural firm is designing a convex polygonal platform $P$ that must be installed within the boundaries of this processing floor (spanning from $x=0$ to $x=2013$). To ensure structural stability, the platform must be "anchored," meaning at least one vertex of the polygon must touch the western boundary wall at $x=0$, and at least one vertex must touch the eastern boundary wall at $x=2013$.

The efficiency of the platform is measured by its "Pink Density," $d(P)$, defined as the ratio of the area of the platform covering pink lanes to the total area of the platform.

Engineers have determined that the minimum possible value of $d(P)$ among all valid convex, non-degenerate platforms can be simplified to the mathematical expression $\frac{(1+\sqrt{p})^2}{q^2}$, where $p$ and $q$ are positive integers. Find the value of $p+q$.

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
