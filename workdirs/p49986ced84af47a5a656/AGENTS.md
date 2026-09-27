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

In a remote territory, three supply depots—Sector Alpha, Sector Bravo, and Sector Charlie—form a triangular perimeter. The drone flight path from Alpha to Bravo is exactly 6 miles, from Bravo to Charlie is 7 miles, and from Charlie back to Alpha is 8 miles.

To optimize regional surveillance, three relay stations were constructed at the exact midpoints of these paths: Station Delta sits halfway between Bravo and Charlie; Station Echo sits halfway between Alpha and Charlie; and Station Foxtrot sits halfway between Alpha and Bravo.

The territory is further divided into three triangular "Sub-Zones":
1.  Sub-Zone A is defined by the coordinates of Alpha, Foxtrot, and Delta.
2.  Sub-Zone B is defined by the coordinates of Bravo, Delta, and Echo.
3.  Sub-Zone C is defined by the coordinates of Charlie, Echo, and Foxtrot.

A central monitoring hub is placed at the circumcenter of each Sub-Zone. Hub $O_A$ is the point equidistant from the three corners of Sub-Zone A; Hub $O_B$ is the point equidistant from the three corners of Sub-Zone B; and Hub $O_C$ is the point equidistant from the three corners of Sub-Zone C.

Calculate the area of the triangular region formed by the locations of the three monitoring hubs $O_A$, $O_B$, and $O_C$.

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
