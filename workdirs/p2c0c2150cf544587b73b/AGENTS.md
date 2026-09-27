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

In a remote territory, three survey outposts define a large triangular region $ABC$ with a total land area of $I$ square kilometers. A central conservation zone has been established in the shape of a triangle $A_1B_1C_1$, where the corner $A_1$ is located exactly halfway between outposts $B$ and $C$, $B_1$ is halfway between $C$ and $A$, and $C_1$ is halfway between $A$ and $B$.

A secondary research team is constructing a mobile triangular platform $KLM$. The three anchor points of this platform are restricted to specific border paths: 
- Point $K$ must be positioned somewhere along the path connecting outpost $A$ to the conservation corner $B_1$.
- Point $L$ must be positioned somewhere along the path connecting outpost $C$ to the conservation corner $A_1$.
- Point $M$ must be positioned somewhere along the path connecting outpost $B$ to the conservation corner $C_1$.

As the researchers move the anchor points $K$, $L$, and $M$ along their respective segments, the overlap between the mobile platform $KLM$ and the central conservation zone $A_1B_1C_1$ changes. What is the minimum possible area that this intersection can cover? 

If the minimum area is expressed as a fraction of the total land area $\frac{a}{b} \cdot I$ (where $\frac{a}{b}$ is an irreducible fraction), calculate the value of $a + b$.

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
