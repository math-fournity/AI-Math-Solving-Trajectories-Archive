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

In a remote territory, three supply depots—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter $ABC$ connected by straight-line roads. A circular irrigation canal, which acts as the incircle of $\triangle ABC$, is installed within the perimeter, perfectly touching the road $AC$ at a maintenance station $P$ and the road $BC$ at a maintenance station $Q$.

A long, straight underground fiber-optic cable is laid along the line connecting stations $P$ and $Q$. This cable line extends in both directions until it intersects a circular high-speed rail track that circumscribes the entire $ABC$ triangular region. The two intersection points where the cable meets the rail track are designated as Relay Station $K$ (located on the minor arc $AC$) and Relay Station $L$ (located on the minor arc $BC$).

The surveyors have determined that Relay Station $K$ is positioned exactly at the midpoint of the curved rail segment (the arc) between Depot $A$ and Depot $C$.

Calculate the exact ratio of the distance between the two Relay Stations ($KL$) to the distance of the straight-line road between Depot $A$ and Depot $B$ ($AB$).

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
