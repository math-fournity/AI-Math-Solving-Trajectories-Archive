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

In a global telecommunications network, there are several data hubs. From every single hub, there are exactly two dedicated one-way fiber-optic cables transmitting data to two other distinct hubs. 

A systems architect needs to organize these hubs into $K$ distinct server clusters. To ensure signal stability and prevent interference, the following two protocols must be strictly followed:
1. No two hubs located within the same server cluster can have a direct cable connection between them.
2. For any two separate server clusters, $C_i$ and $C_j$, all existing cable connections between hubs in $C_i$ and hubs in $C_j$ must flow in the same uniform direction (for instance, all transmissions must go from $C_i$ hubs to $C_j$ hubs, or all must go from $C_j$ hubs to $C_i$ hubs, but never both).

Based on the mathematical proof that such a configuration is always achievable regardless of how the cables are laid out, what is the minimum number of clusters $K$ that the construction in the solution guarantees will satisfy these conditions?

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
