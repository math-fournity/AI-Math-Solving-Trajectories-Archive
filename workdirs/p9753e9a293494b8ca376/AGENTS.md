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

In a remote desert, three observation outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. Two secondary supply depots, Mike ($M$) and Nano ($N$), are positioned along the direct paths between the outposts. Depot $M$ is located on the path between Alpha and Bravo such that its distance to Alpha is exactly equal to its distance to Charlie ($AM = MC$). Similarly, Depot $N$ is located on the path between Alpha and Charlie such that its distance to Alpha is equal to its distance to Bravo ($AN = NB$).

A central Command Hub ($P$) is established at a specific coordinate such that the straight-line communication beams from the Hub to Bravo ($PB$) and from the Hub to Charlie ($PC$) are perfectly tangent to the unique circular boundary passing through outposts Alpha, Bravo, and Charlie.

A logistics team measures the following boundary lengths:
1. The total perimeter of the triangular patrol route connecting the Hub ($P$), Depot $M$, and Depot $N$ is exactly $21$ units.
2. The total perimeter of the quadrilateral transport route connecting Bravo ($B$), Charlie ($C$), Depot $N$, and Depot $M$ is exactly $29$ units.
3. The direct distance from the Command Hub ($P$) to Outpost Bravo ($B$) is measured at $5$ units.

Based on these survey measurements, calculate the precise distance of the straight-line path between Outpost Bravo ($B$) and Outpost Charlie ($C$).

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
