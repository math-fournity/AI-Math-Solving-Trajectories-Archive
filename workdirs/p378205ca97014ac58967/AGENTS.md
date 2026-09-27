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

A specialized laser-mapping drone is surveying a rectangular-shaped valley defined by four research stations: $A, B, C,$ and $D$. The stations $A$ and $B$ are situated on a straight northern perimeter of length $5$ km, while $C$ and $D$ are on a parallel southern perimeter of length $7$ km. The side boundaries $BC$ and $AD$ are both exactly $2\sqrt{10}$ km long. The entire valley is enclosed within a circular protective zone, $\omega$, centered at a control hub $O$, such that all four stations lie on its boundary.

A direct signal path is established from station $A$ through a relay point $M$, which is the exact midpoint of the southern boundary $CD$. This signal path $AM$ continues until it hits the boundary of the circular zone at a sensor labeled $E$. A technician is monitoring a straight cable line connecting station $B$ to sensor $E$. This cable $BE$ passes through a junction box $P$ located on the southern boundary $CD$.

The technician identifies $N$ as the midpoint of the cable $BE$. A specialized tracking beam is projected starting from the hub $O$, passing through the midpoint $N$, and extending until it intersects the line extending from the southern boundary $CD$ at a point $Q$.

A specialized observation drone, $R$, is hovering on the circumcircle formed by the three points $P$, $N$, and $Q$. From the drone’s perspective, the angle formed between its position and the points $P$ and $C$ (specifically $\angle PRC$) is exactly $45^\circ$. If the distance from station $D$ to the drone $R$ is represented as a simplified fraction $\frac{m}{n}$, find the value of $m+n$.

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
