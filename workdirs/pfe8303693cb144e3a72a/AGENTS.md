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

In a remote industrial zone, three monitoring stations—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—are positioned on a flat plane. The distance between Alpha and Bravo is exactly 6 km, Bravo and Charlie is 8 km, and Alpha and Charlie is 10 km.

A drone, Delta ($D$), is hovering at a fixed point in the airspace above the plane, forming a tetrahedral volume of $\frac{15\sqrt{39}}{2}$ cubic kilometers with the three stations. 

Inside this spatial configuration, four specific "equilibrium coordinates" are calculated:
- $I_A$: The center of the largest sphere that can be inscribed within the space bounded by the drone ($D$) and stations Bravo and Charlie.
- $I_B$: The center of the largest sphere that can be inscribed within the space bounded by the drone ($D$) and stations Alpha and Charlie.
- $I_C$: The center of the largest sphere that can be inscribed within the space bounded by the drone ($D$) and stations Alpha and Bravo.
- $I_D$: The center of the largest sphere that can be inscribed within the space bounded by the three ground stations Alpha, Bravo, and Charlie.

Navigation sensors determine that the four signal paths connecting each station (or drone) to its corresponding opposite equilibrium coordinate—specifically the paths $AI_A$, $BI_B$, $CI_C$, and $DI_D$—all intersect at a single unique point in space.

The total length of the three direct transmission beams connecting the drone Delta ($D$) to each of the ground stations Alpha ($A$), Bravo ($B$), and Charlie ($C$) can be expressed as a reduced fraction $\frac{a}{b}$. 

Find the value of $a + b$.

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
