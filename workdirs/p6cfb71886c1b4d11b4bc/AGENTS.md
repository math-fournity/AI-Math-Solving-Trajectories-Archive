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

A specialized communications hub, Point $P$, is located within a territory bounded by four direct fiber-optic cables connecting four regional stations: Alpha ($A$), Bravo ($B$), Charlie ($C$), and Delta ($D$), forming a convex quadrilateral $ABCD$.

The layout of the hub relative to the stations is governed by the following geometric synchronization protocols:

1. The sum of the visual angles from the hub to stations Alpha and Bravo ($\angle APB$) and to stations Charlie and Delta ($\angle CPD$) is exactly $180^\circ$. Similarly, the sum of the angles from the hub to Bravo and Charlie ($\angle BPC$) and to Delta and Alpha ($\angle DPA$) is $180^\circ$.

2. The combined angle formed at Alpha between the lines to Delta and the hub ($\angle PAD$) and at Charlie between the lines to Delta and the hub ($\angle PCD$) is exactly equal to the combined angle formed at Alpha between the lines to Bravo and the hub ($\angle PAB$) and at Charlie between the lines to Bravo and the hub ($\angle PCB$).

3. The combined angle formed at Delta between the lines to Charlie and the hub ($\angle PDC$) and at Bravo between the lines to Charlie and the hub ($\angle PBC$) is exactly equal to the combined angle formed at Delta between the lines to Alpha and the hub ($\angle PDA$) and at Bravo between the lines to Alpha and the hub ($\angle PBA$).

Field surveys have confirmed the following distances between the stations:
- The cable from Alpha to Bravo ($AB$) measures 13 kilometers.
- The cable from Bravo to Charlie ($BC$) measures 20 kilometers.
- The cable from Charlie to Delta ($CD$) measures 37 kilometers.

Based on these specific configurations, determine the length of the final cable connecting station Delta to station Alpha ($DA$).

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
