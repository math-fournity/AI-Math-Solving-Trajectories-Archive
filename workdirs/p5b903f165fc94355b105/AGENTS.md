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

A specialized deep-sea salvage operation is being conducted in a grid-based underwater zone. A robotic Retrieval Unit (RU) is deployed at the surface coordinates (0,0), while a rogue Automated Submersible (AS) is located at the seafloor coordinates (6,8).

The RU is programmed to intercept the AS and can only move 1 unit at a time in the positive x or positive y direction. Simultaneously, the AS is programmed to return to the surface dock at (0,0) to offload data and can only move 1 unit at a time in the negative x or negative y direction.

The operation proceeds in discrete intervals called "pulses." Every pulse, both units detect each other’s current position, independently select a valid direction, and move simultaneously to their next coordinates. The RU successfully "captures" the AS if they occupy the exact same coordinate at the same time. The AS wins the encounter if it reaches the dock at (0,0) without ever being captured; otherwise, the RU wins.

Both units are controlled by advanced AI playing optimally to maximize their respective probabilities of winning. If the probability that the AS wins is expressed as an irreducible fraction $a/b$, find the value of $a+b$.

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
