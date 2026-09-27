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

A specialized telecommunications firm is developing a redundant network architecture using $n$ identical fiber-optic cables housed within a central junction box. Each cable has two ends: one protruding from the left side of the box and one from the right side, resulting in $n$ connection points on each side.

An automated technician performs the following sequence of connections:
1. On the left side, the technician connects the $n$ ends into $\lfloor n/2 \rfloor$ distinct pairs. If $n$ is an odd number, exactly one connection point is left isolated.
2. On the right side, the technician independently connects the $n$ ends into $\lfloor n/2 \rfloor$ distinct pairs. If $n$ is an odd number, exactly one connection point is left isolated.

The network is considered "fully integrated" if the resulting configuration forms a single, unbroken sequence of cables. Specifically, if $n$ is even, the cables must form one continuous closed loop; if $n$ is odd, the cables must form one continuous open path.

Let $P(n)$ represent the probability that a random assignment of these connections results in a fully integrated network. Determine the exact value of $105 \times (P(6) + P(7))$.

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
