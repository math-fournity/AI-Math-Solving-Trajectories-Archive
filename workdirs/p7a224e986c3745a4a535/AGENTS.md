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

A specialized logistics hub is designed as an isosceles trapezoidal zone $ABCD$. The northern security fence $AB$ measures 5 km, and the southern boundary $CD$ measures 7 km. Two equal perimeter walls, $BC$ and $AD$, each span $2\sqrt{10}$ km. A circular patrol road $\omega$, centered at a central command tower $O$, perfectly circumscribes the four corners of the hub.

A straight supply pipeline originates at corner $A$, passes through the exact midpoint $M$ of the southern boundary $CD$, and extends until it hits the circular road $\omega$ again at a pressure station $E$. A high-speed rail line is laid in a straight path between corner $B$ and station $E$. This rail line crosses the southern boundary $CD$ at a junction point $P$. A maintenance facility $N$ is built at the exact midpoint of the rail line $BE$.

A surveyor establishes a line of sight starting from the command tower $O$, passing through the maintenance facility $N$, and extending until it intersects the southern boundary line $DC$ (extended if necessary) at a landmark $Q$. 

A drone $R$ is hovering at a specific point on the circle that passes through $P$, $N$, and $Q$. From the perspective of this drone, the angle formed between the path to junction $P$ and the path to corner $C$ (angle $\angle PRC$) is exactly $45^\circ$. 

The distance from the corner $D$ to the drone $R$ can be expressed as a simplified fraction $\frac{m}{n}$. What is the value of $m+n$?

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
