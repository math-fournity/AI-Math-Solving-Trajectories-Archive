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

In a specialized logistics hub, $n$ technicians are positioned around a circular conveyor belt at equally spaced workstations. The hub operates through a series of "processing cycles." In each cycle $i$, every technician performs a task on the component currently at their station and then shifts that component $k_i$ positions clockwise to another technician. A "full rotation" is defined as a sequence of $n$ such steps. A rotation is considered "complete" if every technician has worked on every one of the $n$ components exactly once.

Consider the following two scenarios regarding the possible configurations of the hub for $n \in \{2, 3, \dots, 100\}$:

a) Let $S_a$ be the set of all $n$ for which there exists a sequence of shift distances $(k_1, k_2, \dots, k_{n-1})$ such that, during the first $n-1$ shifts of a rotation, every technician passes their current component to each of the other $n-1$ technicians exactly once.

b) In this scenario, technicians perform two types of tasks: "Calibration" and "Assembly." A full rotation consists of alternating between these two tasks (Step 1: Calibrate and shift $k_1$; Step 2: Assemble and shift $k_2$; Step 3: Calibrate and shift $k_3$, and so on). 
Let $S_b$ be the set of all $n$ for which it is possible to define two different valid complete rotations (each involving $n$ steps) such that:
1. Across both rotations combined, every technician passes a component they just "Calibrated" to each of the other $n-1$ technicians exactly once.
2. Across both rotations combined, every technician passes a component they just "Assembled" to each of the other $n-1$ technicians exactly once.

Calculate the sum of all elements in $S_a$ and all elements in $S_b$.

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
