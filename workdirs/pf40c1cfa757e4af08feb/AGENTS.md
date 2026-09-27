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

In the coastal territory of Arcania, three strategic watchtowers—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular defensive perimeter. Surveyors have recorded the direct distances between them: the path from Alpha to Bravo is exactly 8 miles, the path from Alpha to Charlie is 12 miles, and the coastal road between Bravo and Charlie is 5 miles.

The territory’s High Architect decides to build a central Supply Hub ($M$) at a specific location. This hub is positioned such that the line of sight from Alpha to the Hub perfectly bisects the internal angle formed by the paths to Bravo and Charlie ($\angle BAC$). Furthermore, the Hub is located on the unique circular boundary that passes through all three watchtowers (the circumcircle of $\triangle ABC$).

Surrounding this Supply Hub, a circular security zone ($\omega$) is established. This zone is centered exactly at the Hub ($M$) and is designed to be perfectly tangent to the two main roads originating from Alpha: the road to Bravo ($AB$) and the road to Charlie ($AC$).

Two new auxiliary supply routes are then paved. One starts from Bravo ($B$) and is tangent to the security zone, but it follows a different path than the original road to Alpha. The second starts from Charlie ($C$) and is also tangent to the security zone, distinct from the road to Alpha. These two new routes eventually converge and intersect at a remote Outpost ($D$).

Calculate the exact distance, in miles, of the direct path from the Alpha watchtower ($A$) to the Outpost ($D$).

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
