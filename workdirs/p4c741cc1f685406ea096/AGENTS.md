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

In a remote territory, three major industrial hubs—Alpha (A), Bravo (B), and Charlie (C)—form a triangular network connected by straight supply lines. To optimize logistics, the regional planners established three support stations located at the precise points where an altitude from one hub meets the opposite supply line: station Delta (D) on the line BC, Echo (E) on AC, and Foxtrot (F) on AB.

A central distribution path, known as the "A-Median," runs in a straight line from hub Alpha to the exact midpoint of the supply line BC. 

The security perimeter for the northern sector is defined by a circular boundary passing through hub Alpha and stations Echo and Foxtrot. The A-Median path intersects this circular boundary at a specialized monitoring post, Zulu (Z). 

To facilitate high-speed transport, a straight rail line was constructed passing through Echo and Foxtrot. Additionally, a specialized transit corridor was built starting from hub Alpha, tangent to the northern circular boundary, extending until it meets the Echo-Foxtrot rail line at a junction point, Tango (T).

Upon inspection, surveyors discovered a unique geometric alignment: the support station Delta, the monitoring post Zulu, and the junction Tango all lie perfectly along a single straight line.

Given that the distance between hubs Alpha and Bravo is strictly less than the distance between Alpha and Charlie, determine the exact value of the ratio of the distance between Delta and Bravo to the distance between Delta and Charlie.

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
