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

In a plane the circles  $\mathcal K_1$  and  $\mathcal K_2$  with centers  $I_1$  and  $I_2$ , respectively, intersect in two points  $A$  and  $B$ . Assume that  $\angle I_1AI_2$  is obtuse. The tangent to  $\mathcal K_1$  in  $A$  intersects  $\mathcal K_2$  again in  $C$  and the tangent to  $\mathcal K_2$  in  $A$  intersects  $\mathcal K_1$  again in  $D$ . Let  $\mathcal K_3$  be the circumcircle of the triangle  $BCD$ . Let  $E$  be the midpoint of that arc  $CD$  of  $\mathcal K_3$  that contains  $B$ . The lines  $AC$  and  $AD$  intersect  $\mathcal K_3$  again in  $K$  and  $L$ , respectively. Prove that the line  $AE$  is perpendicular to  $KL$ .

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
