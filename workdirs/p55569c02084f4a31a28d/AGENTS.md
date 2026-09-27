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

A specialized microchip architecture consists of a grid-like circuit board with 4 horizontal copper power rails and 100 vertical signal buses. These rails and buses intersect at 400 distinct junction points. These junctions divide each horizontal rail into 99 individual segments and each vertical bus into 3 individual segments.

An engineer needs to disable the minimum number of junctions, denoted as $k$, to ensure that there are no feedback loops in the circuit. A feedback loop is defined as any path that starts at a specific segment and returns to that same segment by traveling through active junctions without reversing direction.

The engineer disables exactly $k$ junctions such that the circuit remains fully connected, meaning every segment is still reachable from every other segment through the remaining active junctions. Additionally, a design constraint specifies that the four corner junctions of the grid must remain active.

Let $B$ represent the number of disabled junctions that are located on the perimeter of the circuit grid. A junction is considered to be on the perimeter if it is located on either the first or fourth horizontal rail, or on either the first or 100th vertical bus.

Find the value of $k + B$.

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
