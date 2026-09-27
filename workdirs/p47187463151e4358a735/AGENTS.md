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

In a remote sector of the galaxy, a specialized solar farm is constructed in the shape of a perfectly triangular region defined by three communication beacons: Alpha (A), Bravo (B), and Charlie (C). The distance between Alpha and Charlie is strictly less than the distance between Bravo and Charlie. The total operational surface area of this triangular zone is exactly $20\sqrt{3}$ square kilometers.

Two critical monitoring stations are located within the zone:
1.  **Station M (The Central Hub):** This station is positioned at the unique point equidistant from all three beacons (the circumcenter).
2.  **Station I (The Control Core):** This station is positioned at the unique point equidistant from the three linear boundary fences connecting the beacons (the incenter).

A direct maintenance corridor connects Station I and Station M. This corridor has a precise length of 1 kilometer and is oriented perfectly parallel to the boundary fence connecting beacon Alpha and beacon Bravo.

Calculate the sum of the squares of the distances between the three beacons ($AB^2 + BC^2 + CA^2$).

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
