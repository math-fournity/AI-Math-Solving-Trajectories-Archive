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

A specialized laser defense system is being calibrated between three key points: a Command Center ($B$), a Power Station ($A$), and a Relay Hub ($C$). The Power Station and the Relay Hub are connected by a straight underground cable. The Command Center is positioned such that the path to the Power Station ($BA$) is perfectly perpendicular to the path to the Relay Hub ($BC$).

Engineers are extending the reach of the system to a new Remote Terminal ($D$). This terminal is placed on the same straight line as the Power Station and Relay Hub, located further out so that the Relay Hub ($C$) sits exactly between the Power Station ($A$) and the Remote Terminal ($D$). To ensure signal stability, the distance between the Power Station and the Command Center ($AB$) must be exactly equal to the distance between the Relay Hub and the Remote Terminal ($CD$).

A technician measures the angle between the lines of sight from the Command Center to the Relay Hub and from the Command Center to the Remote Terminal (angle $\angle CBD$) and finds it to be exactly $30^\circ$.

Based on this configuration, determine the value of the squared ratio of the distance between the Power Station and the Relay Hub ($AC$) to the distance between the Relay Hub and the Remote Terminal ($CD$). That is, calculate $\left(\frac{AC}{CD}\right)^2$.

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
