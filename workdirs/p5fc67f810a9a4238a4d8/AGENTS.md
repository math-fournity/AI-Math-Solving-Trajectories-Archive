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

In a remote territory, three survey outposts—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. The distance between Alpha and Bravo is 5 km, Bravo to Charlie is 7 km, and Charlie to Alpha is 8 km. These three outposts lie on a circular boundary defined by a signal range $\omega$.

A central transmission hub ($P$) is located within this triangle. Technicians have determined that the distances from the hub to the outposts follow a specific ratio: the distance to Alpha ($PA$), the distance to Bravo ($PB$), and the distance to Charlie ($PC$) are in a ratio of $2:3:6$, respectively.

To expand the network, engineers project three signal beams starting from each outpost and passing through the hub $P$ until they hit the circular boundary $\omega$. The beam from Alpha through $P$ hits the boundary at station $X$; the beam from Bravo through $P$ hits at station $Y$; and the beam from Charlie through $P$ hits at station $Z$.

A new conservation zone is formed by the triangular region connecting the boundary stations $X$, $Y$, and $Z$. The area of this triangle $XYZ$ can be expressed in the simplified radical form $\frac{p\sqrt{q}}{r}$, where $p$ and $r$ are relatively prime positive integers and $q$ is a square-free positive integer.

Calculate the value of $p+q+r$.

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
