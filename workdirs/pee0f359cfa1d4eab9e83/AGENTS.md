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

In a remote territory, three mountain peaks—Base Station A, Outpost B, and Outpost C—form an acute triangular perimeter. To improve communications, three straight supply roads were paved: Road AD (the shortest path from Station A to the straight border Road BC), Road BE (the shortest path from Outpost B to Road AC), and Road CF (the shortest path from Outpost C to Road AB). 

The mountain’s central relay station, K, is located where the maintenance path connecting E and F intersects Road AD. Due to the terrain, path EF extends further into the valley until it meets the extension of Road BC at a specialized monitoring hub, I. 

A survey team is establishing a new observation point, W, along the straight line extending from Outpost B through Road CF. They have positioned point W such that the angle formed by lines IW and FW is exactly equal to the angle formed by lines FW and EW. 

Data analysts have confirmed two specific geometric constraints for this layout:
1. A circular evacuation route can be mapped that passes perfectly through the coordinates of Station A, Relay K, Outpost B, and Hub I.
2. The cosine of the angle formed at Outpost C by the roads connecting to Station A and Outpost B is exactly 2/5.

Additionally, the distance between Station A and Outpost C is strictly greater than the distance between Station A and Outpost B.

Calculate the exact ratio of the distance from point W to Outpost B compared to the distance from point W to Hub I.

$$\frac{7 \sqrt{15} - 3 \sqrt{35}}{10}$$

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
