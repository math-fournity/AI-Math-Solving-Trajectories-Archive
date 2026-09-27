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

A regional agricultural developer is planning a triangular irrigation zone, defined by three primary pump stations: Alpha ($A$), Bravo ($B$), and Charlie ($C$). To optimize water distribution, the developer has established three internal junctions—Delta ($D$), Echo ($E$), and Foxtrot ($F$)—located on the boundary pipelines $BC$, $AC$, and $AB$, respectively.

The planning board has confirmed two initial baseline metrics:
1. The distance from station Bravo to junction Foxtrot ($|BF|$) relates to the distance from junction Foxtrot to station Alpha ($|FA|$) in a strict ratio of $3:2$.
2. The sector bounded by Bravo, Delta, and Foxtrot ($\triangle BDF$) covers exactly $9$ square kilometers.

An analyst needs to determine the total area of the entire triangular zone $ABC$. They are presented with five independent sets of supplementary data. Your task is to determine how many of these five scenarios provide sufficient information, on their own, to calculate the total area of the irrigation zone $ABC$:

*   Scenario 1: The central sector $DEF$ covers $12$ square kilometers and the northern sector $AEF$ covers $6$ square kilometers.
*   Scenario 2: The central sector $DEF$ covers exactly $9$ square kilometers.
*   Scenario 3: The central sector $DEF$ covers exactly $6$ square kilometers.
*   Scenario 4: The northern sector $AEF$ covers $6$ square kilometers and the eastern sector $CDE$ covers $4$ square kilometers.
*   Scenario 5: Both the northern sector $AEF$ and the eastern sector $CDE$ cover exactly $5$ square kilometers each.

How many of these five statements are sufficient alone to calculate the area of the irrigation zone $ABC$?

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
