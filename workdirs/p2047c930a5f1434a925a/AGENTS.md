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

In a remote territory, three supply depots, Alpha ($A$), Bravo ($B$), and Charlie ($C$), are situated such that the distance from each to a central command hub ($O$) is exactly $R = 100$ kilometers. The terrain forms a triangle $ABC$ with unequal side lengths.

For the Alpha sector, an auxiliary communications tower ($A'$) is positioned along the straight path extending from Alpha through the hub $O$. The tower $A'$ is located at a specific point such that the angle formed between the path to Bravo, the tower, and Alpha ($\angle BA'A$) is identical to the angle formed between the path to Charlie, the tower, and Alpha ($\angle CA'A$).

To ensure signal coverage, two relay stations are built: Station $A_1$ is the closest point on the straight road $AB$ to tower $A'$, and Station $A_2$ is the closest point on the straight road $AC$ to tower $A'$. Additionally, a monitoring post $H_A$ is established at the closest point on the straight road $BC$ to depot $Alpha$. A specialized circular maintenance route is paved to connect $H_A, A_1,$ and $A_2$; the radius of this circular route is denoted as $R_A$.

Following the same geometric protocol, radii $R_B$ and $R_C$ are determined for sectors Bravo and Charlie respectively (by cyclically permuting the roles of the depots).

Calculate the value of:
$$\frac{1000}{R_A} + \frac{1000}{R_B} + \frac{1000}{R_C}$$

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
