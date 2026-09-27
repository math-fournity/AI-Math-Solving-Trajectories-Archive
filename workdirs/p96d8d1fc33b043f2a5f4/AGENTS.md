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

In the coastal region of Althea, three primary lighthouse stations—Alpha (A), Bravo (B), and Charlie (C)—form a triangular patrol sector. The distance from Alpha to Bravo is exactly 5 leagues, and the distance from Alpha to Charlie is 8 leagues. The angle formed between the Alpha-Bravo and Alpha-Charlie corridors is exactly $60^{\circ}$.

An automated supply drone follows a circular path, $\gamma$, that is tangent to all three corridors of the sector. The center of this path is denoted as $I$. Two specific maintenance markers, $E$ and $F$, are located where this circular path $\gamma$ touches the corridors Alpha-Charlie and Alpha-Bravo, respectively.

Three logistics hubs are positioned exactly at the midpoints of the corridors: Hub $M$ is halfway between Bravo and Charlie, Hub $N$ is halfway between Charlie and Alpha, and Hub $P$ is halfway between Alpha and Bravo. 

A straight communication cable, $L_1$, connects maintenance markers $E$ and $F$. A second cable, $L_2$, connects Hubs $M$ and $N$. A third cable, $L_3$, connects Hubs $M$ and $P$. Let $U$ be the junction point where cable $L_1$ crosses $L_2$, and let $V$ be the junction point where cable $L_1$ crosses $L_3$.

A deep-sea research buoy, $X$, is anchored in the ocean. Its position is defined by the circumcircle $\Gamma$ (the circle passing through stations Alpha, Bravo, and Charlie). Specifically, $X$ is located at the midpoint of the circular arc $\widehat{BAC}$—the arc that starts at Bravo, passes through Alpha, and ends at Charlie.

Calculate the area of the triangular region formed by the buoy $X$ and the two cable junctions $U$ and $V$.

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
