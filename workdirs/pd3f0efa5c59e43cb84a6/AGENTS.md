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

In a specialized research laboratory, two rival server clusters, the Alpha Array and the Gamma Grid, are competing to solve a complex encryption sequence. The sequence is processed in cycles, alternating between the two environments. The first cycle is hosted by the Gamma Grid, and each subsequent cycle switches to the other environment.

When a cycle is hosted by the Gamma Grid, there is a 50% probability that the Gamma Grid will complete its assigned task first. When a cycle is hosted by the Alpha Array, there is a 60% probability that the Alpha Array will complete its task first.

Normally, the competition concludes as soon as one cluster has completed three more tasks than its rival. However, the Gamma Grid is located in a seismically active zone. Immediately following the conclusion of any cycle hosted by the Gamma Grid, there is a 50% probability that an earthquake will occur. If an earthquake occurs, the entire competition is terminated instantly, and the cluster that has completed the greater total number of tasks is declared the overall winner.

The Gamma Grid wins the competition if it either reaches a three-task lead or is ahead when an earthquake terminates the process. What is the probability that the Gamma Grid will win? If the answer is expressed as an irreducible fraction $\frac{a}{b}$, compute the value of $a+b$.

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
