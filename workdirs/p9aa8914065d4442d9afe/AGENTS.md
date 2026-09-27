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

In a specialized fiber-optic communication hub, there are two parallel routing rails, designated as Rail Alpha and Rail Beta. On Rail Alpha, four distinct input ports are mounted: $P_1, P_2, P_3,$ and $P_4$. Directly opposite on Rail Beta, four distinct output ports are mounted: $Q_1, Q_2, Q_3,$ and $Q_4$.

To ensure full connectivity, a physical glass fiber segment must be stretched in a straight line from every input port on Rail Alpha to every output port on Rail Beta (resulting in 16 fiber segments in total). 

Data interference occurs at every location where two or more fibers physically cross one another, as well as at the connection points where the fibers plug into the ports. By strategically sliding the ports along their respective rails (while maintaining the four distinct positions on each), an engineer aims to minimize the total number of unique physical locations where fibers either intersect each other or connect to a port.

Calculate the minimum possible number of distinct points formed by the intersections of these fiber segments, including the locations of the 8 ports themselves.

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
