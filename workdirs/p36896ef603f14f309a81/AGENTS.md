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

An elite cyber-security firm operates 8 secure data terminals, arranged in a perfect circle and labeled $P_1, P_2, P_3, P_4, P_5, P_6, P_7, \text{ and } P_8$. The system architecture allows for 20 possible direct long-distance encrypted bridges, which are defined as connections between any two terminals that are not immediate neighbors on the circle. This complete set of 20 possible bridges is denoted as $U$.

The firm’s lead architect needs to select a configuration $S$, which is a specific collection of these bridges (a subset of $U$), to be active at any given time. However, to maintain network stability, any configuration $S$ must adhere to a "Relay Consistency Rule":

If the configuration $S$ contains a direct bridge between terminal $P_i$ and terminal $P_j$, and also contains a direct bridge between terminal $P_j$ and terminal $P_k$ (where $i \neq k$), then it must also contain a direct bridge between terminal $P_i$ and terminal $P_k$ to ensure a closed loop of redundancy.

Find the total number of unique configurations $S$ that satisfy these conditions.

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
