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

A specialized aerospace engineering firm, Orbit-X, is designing a propulsion thruster. The performance efficiency of the thruster is governed by the energy function $E(t) = a_1 t^2 + a_2 t + a_3$, where $t$ represents the time in milliseconds and $a_1, a_2, a_3$ are design coefficients. 

Two lead engineers, Alice and Bob, are tasked with selecting these three coefficients. There are three available slots for these values: Slot 1 ($a_1$), Slot 2 ($a_2$), and Slot 3 ($a_3$). The engineers must select distinct integers from the set $\{1, 2, 3, 4, 5\}$ to fill these slots. No integer can be reused.

The selection process is turn-based. Alice goes first and chooses one integer from the set and assigns it to one of the empty slots. Then Bob chooses one of the remaining integers and assigns it to one of the two remaining slots. Finally, Alice takes one of the three remaining integers and places it in the final empty slot.

Alice’s objective is to minimize the absolute minimum value $M$ that the function $E(t)$ reaches over all real values of $t$. Conversely, Bob’s objective is to maximize this minimum value $M$.

Assuming both Alice and Bob follow their optimal strategies to achieve their respective goals, determine the final three-digit configuration of the coefficients expressed as $100 a_1 + 10 a_2 + a_3$.

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
