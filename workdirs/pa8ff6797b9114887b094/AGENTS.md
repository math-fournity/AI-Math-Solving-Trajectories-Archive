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

In a remote desert, three research stations—Alpha ($A$), Bravo ($B$), and Charlie ($C$)—form a triangular perimeter. Sensors indicate that the path from Bravo to Alpha meets the path from Bravo to Charlie at an angle of $60^\circ$. At station Charlie, the paths leading to Alpha and Bravo meet at an angle of $55^\circ$.

A technician is stationed at a supply depot ($M$) located exactly halfway along the straight pipeline connecting Bravo and Charlie. To monitor the area, a security fence is constructed along the straight path from Alpha to Charlie. A specialized relay node ($P$) is placed at a specific point on this fence.

The relay node is positioned such that two distinct patrol routes have exactly equal total lengths:
1. The first route travels from Alpha to Bravo, then to the supply depot $M$, then to the relay node $P$, and finally back to Alpha.
2. The second route travels from the relay node $P$ to the supply depot $M$, then to station Charlie, and finally back to the relay node $P$.

A surveyor needs to calibrate the directional antenna at the relay node. Find the measure of the angle formed between the path from the relay node to the supply depot ($\vec{PM}$) and the path from the relay node to station Charlie ($\vec{PC}$), expressed in degrees.

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
