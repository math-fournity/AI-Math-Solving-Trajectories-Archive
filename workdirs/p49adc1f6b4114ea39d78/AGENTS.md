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

In a futuristic city, an architect is designing a modular plaza consisting of two nested, "kite-shaped" zones, $ABCD$ and $AB'C'D'$. These zones are defined as quadrilaterals where the main pedestrian walkways (the diagonals) cross at exactly $90^\circ$. For the primary zone $ABCD$, the corners at sectors $B$ and $D$ are built at precise $90^\circ$ angles.

To manage the climate, a circular green space (the incircle of $ABCD$) is landscaped within the first zone. This green space touches the perimeter wall $AB$ at point $M$ and the wall $BC$ at point $N$. 

The architect then plans a second, larger zone $AB'C'D'$ that is a perfect geometric expansion (similar) of the first. The center of this expansion is anchored at point $A$. To determine the scale of this new zone, the architect defines a circular reflecting pool, $\omega$. This pool is centered at vertex $C$ and is designed to be tangent to the extended boundary lines of $AB$ and $AD$. The new zone $AB'C'D'$ is sized such that its own incircle is exactly this reflecting pool $\omega$.

In this layout, let $N'$ be the specific point where the new boundary wall $B'C'$ touches the reflecting pool $\omega$. After the survey, the engineers notice a unique alignment: the line segment connecting the original contact point $M$ to the new contact point $N'$ is perfectly parallel to the main diagonal walkway $AC$.

Based on this specific alignment, what is the ratio of the length of boundary wall $AB$ to the length of boundary wall $BC$?

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
