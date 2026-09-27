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

In a specialized urban planning project, a developer is designing a park in the shape of a perfectly symmetrical diamond-shaped plaza, labeled $ABCD$. Every outer boundary wall of this plaza ($AB$, $BC$, $CD$, and $DA$) has a length of exactly 1 kilometer.

Two security kiosks, $M$ and $N$, are positioned along the perimeter. Kiosk $M$ is located somewhere on the wall $BC$, and Kiosk $N$ is located on the wall $CD$. The planning department has enforced a specific "connectivity constraint" regarding the distance between these kiosks and the corner $C$: the distance from $M$ to $C$, plus the distance from $N$ to $C$, plus the straight-line distance between the two kiosks ($MN$), must sum exactly to 2 kilometers.

Furthermore, a central monument is located at vertex $A$. Sightlines are drawn from the monument to both kiosks ($AM$ and $AN$). The surveyors have determined a "proportionality rule" for the layout: the angle formed between the two sightlines ($\angle MAN$) is exactly half the size of the interior angle of the plaza at the monument ($\angle BAD$).

Based on these spatial constraints, determine the measures of the interior angles of the diamond-shaped plaza.

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
