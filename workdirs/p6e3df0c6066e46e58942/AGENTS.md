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

In a futuristic research facility, a sprawling triangular sensor grid is laid out on the floor in the shape of an equilateral triangle $BCD$. Suspended directly above the floor is a central data hub located at point $A$. To provide structural support, three support beams connect the hub $A$ to the floor corners $B$, $C$, and $D$. These beams are positioned such that the three vertical glass panels formed between them—triangles $ABC$, $ACD$, and $ADB$—are all identical isosceles right triangles, with the $90^\circ$ right angles all meeting at the hub $A$.

A technician needs to run a single fiber-optic cable starting from floor corner $B$, clipping it to a specialized connector $P$ located somewhere along the floor perimeter edge $CD$, then pulling it up to a junction box $Q$ located somewhere along the support beam $AC$, and finally returning the cable back to the starting point $B$. 

To conserve resources, the technician must install the cable such that the total length of the path $B \to P \to Q \to B$ is the absolute minimum distance possible. If the cable is installed along this optimal path, what is the measure of the angle $PQA$ formed at the junction box on the support beam?

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
