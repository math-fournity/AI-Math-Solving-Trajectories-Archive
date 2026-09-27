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

In a remote industrial zone, three monitoring stations $A$, $B$, and $C$ are positioned sequentially along a straight pipeline. A security drone is stationed at point $A$, while a transport unit is located at point $B$, tasked with delivering two sensitive data canisters to a secure vault at point $C$.

The distance between the drone (A) and the transport unit's starting point (B) is $a$ meters, and the distance from the transport unit's starting point (B) to the vault (C) is $b$ meters. These distances satisfy the constraint $\frac{17}{27} b < a < 3 b$.

The transport unit and the two canisters initially begin moving from $B$ towards $C$ at a speed of $0.5$ m/s. At a specific moment, the drone at $A$ detects the canisters and begins a pursuit at a speed of $2$ m/s. Simultaneously, the transport unit and canisters receive an alert and increase their pace toward the vault. 

The transport unit has a maximum speed of $1.5$ m/s. It can carry one canister at a time to keep that canister moving at the unit's own speed of $1.5$ m/s (the time to pick up or drop off a canister is negligible). Any canister not being carried by the transport unit moves at its own independent speed of $1$ m/s.

What is the maximum distance (in meters) the transport unit and canisters can be from point $B$ when the drone begins its pursuit, such that all three (the transport unit and both canisters) can just reach the safety of the vault at point $C$ before the drone catches any of them?

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
