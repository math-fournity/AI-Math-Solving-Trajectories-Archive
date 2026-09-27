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

In a certain power grid project involving $n$ specialized transmission hubs ($n \geq 2$), two specific hubs are designated as "Power Sources." Initially, no cables exist between any of the $n$ hubs. Two engineers, Alice and Bob, take turns installing a single high-voltage cable between any two hubs $H_1$ and $H_2$ that are not yet directly connected. 

To ensure safety, a cable can only be installed if at least one of the two hubs being connected ($H_1$ or $H_2$) is already energized. A hub is considered energized if there is a sequence of cables linking it to at least one of the two Power Sources. (Note: The two Power Sources are energized from the start).

The engineer who installs a cable that completes a circuit connecting the two Power Sources to each other (via any path of cables) causes a system overload and loses the game. Alice performs the first installation. 

For a given number of hubs $n$, we define $W(n) = 1$ if Alice has a winning strategy, and $W(n) = 0$ if Bob has a winning strategy. Calculate the value of:
$$\sum_{n=2}^{100} W(n)$$

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
