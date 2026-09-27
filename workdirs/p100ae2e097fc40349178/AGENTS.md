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

In a remote industrial outpost, there are $n$ docking bays arranged in a single row, numbered 1 to $n$ from west to east. To facilitate the storage of hazardous fuel canisters, specialized containment valves are installed: one valve is located between every two adjacent docking bays, and a final valve is positioned to the immediate east of bay $n$. Consequently, bay 1 is adjacent to exactly one valve (on its east), while every other bay is adjacent to two valves (one to its west and one to its east).

A fleet of $n$ cargo drones, each carrying a single fuel canister, arrives to offload. One by one, each drone selects an unoccupied docking bay uniformly at random and executes the following protocol:
- If the drone occupies a bay with two adjacent empty valves, it deposits its canister into the western valve with probability $1/2$ or the eastern valve with probability $1/2$.
- If the drone occupies a bay with only one adjacent empty valve, it must deposit its canister into that specific valve.
- If the drone occupies a bay where both adjacent valves are already occupied, it must retain the canister in its internal storage.

Let $p_n$ represent the probability that all $n$ drones successfully deposit their canisters into valves.

Determine the value of the infinite sum $p_{1}+p_{2}+p_{3}+\cdots$

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
