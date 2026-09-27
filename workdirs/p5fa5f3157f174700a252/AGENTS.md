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

In a remote territory, three survey outposts—Alpha (A), Bravo (B), and Charlie (C)—form a triangular perimeter. The distance between Alpha and Bravo is exactly 10 kilometers, the distance between Bravo and Charlie is 14 kilometers, and the distance between Alpha and Charlie is 16 kilometers. 

A specialized circular communication signal is broadcast such that its boundary passes perfectly through the locations of Alpha, Bravo, and Charlie. 

A secondary, larger triangular patrol route is established by three checkpoints: Delta (D), Echo (E), and Foxtrot (F). This outer route is designed so that the path from Delta to Echo is parallel to the road between Alpha and Bravo, the path from Echo to Foxtrot is parallel to the road between Bravo and Charlie, and the path from Delta to Foxtrot is parallel to the road between Alpha and Charlie. Furthermore, the patrol route is scaled such that the circular communication signal mentioned above acts as the perfect inscribed circle of triangle DEF (it is tangent to all three sides of the patrol route). Checkpoint Delta is located on the same side of the line connecting Bravo and Charlie as outpost Alpha.

An engineer travels in a straight line from checkpoint Echo toward outpost Bravo. This line of travel continues past Bravo until it intersects the boundary of the circular communication signal at a secondary point, X.

Calculate the square of the distance between outpost Bravo (B) and point X.

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
