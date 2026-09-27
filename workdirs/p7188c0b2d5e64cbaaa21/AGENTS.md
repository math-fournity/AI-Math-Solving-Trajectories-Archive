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

In the coastal territory of Aridonia, three main port cities—Port B, Port C, and Port A—form a triangular trade network. The maritime distance between Port B and Port C is exactly 700 leagues, the distance from Port C to Port A is 600 leagues, and the distance from Port A to Port B is 500 leagues. 

The regional Governor has established a central supply Depot, located at the precise point $I$ that is equidistant from the three straight shipping lanes connecting the ports. To manage local distribution, three specialized courier hubs—$D, E,$ and $F$—have been built on the shipping lanes $BC, CA,$ and $AB$ respectively, at the exact points where the circular patrol route centered at the Depot $I$ touches each lane.

A high-altitude surveillance drone tracks the region. Its circular orbit, denoted as Circle $\Omega$, passes through the three main ports $A, B,$ and $C$. A second, smaller drone monitors the northern sector; its circular path, Circle $\omega$, passes through Port $A$ and the two courier hubs $E$ and $F$. These two flight paths, $\Omega$ and $\omega$, intersect at Port $A$ and at one other specific geographical coordinate, designated as Point $X$.

The Governor is planning a new underground data cable that runs in a perfectly straight line from the surveillance coordinate $X$ to the central Depot $I$. Simultaneously, a local transit line is being laid in a straight path between courier hubs $E$ and $F$. The point where the data cable $XI$ crosses the transit line $EF$ is labeled Point $P$.

Navigational engineers need to calculate the "Interaction Product" of this infrastructure, defined as the product of the distances $XP$ and $IP$. If this product is expressed as a reduced fraction $\frac{m}{n}$ (where $m$ and $n$ are units scaled down by a factor of 100 from the original league measurements, making the triangle sides 7, 6, and 5), find the value of $m + n$.

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
