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

In a remote industrial region, three rival mining corporations—Aurelius, Borealis, and Caelum—are competing to clear a series of underground tunnels. Each corporation employs exactly five specialized engineers, labeled by their rank: $A_1, \dots, A_5$; $B_1, \dots, B_5$; and $C_1, \dots, C_5$.

The operation begins with a technical duel between engineer $A_1$ and engineer $B_1$. The competition follows strict "survival" protocols:
1. When an engineer loses a duel, they are permanently dismissed from the site.
2. The winner of a duel remains in the tunnel to face the next challenger.
3. If an engineer $x_i$ from Corporation $X$ defeats an engineer $y_j$ from Corporation $Y$, the next challenger must come from the corporation that was **not** involved in the previous duel (Corporation $Z$), provided they still have engineers available.
4. If the uninvolved Corporation $Z$ has no engineers remaining, the next challenger is sent by the corporation of the engineer who just lost (Corporation $Y$).
5. The competition concludes only when two of the three corporations have had all five of their engineers dismissed.

The corporations earn performance credits based on the rank of their engineers. Every time an engineer of rank $i$ (where $i \in \{1, 2, 3, 4, 5\}$) wins a duel, their corporation is awarded $10^{i-1}$ credits.

Let $P_A, P_B$, and $P_C$ represent the total credits accumulated by the Aurelius, Borealis, and Caelum corporations, respectively, at the end of the tournament. Let $N$ be the total number of distinct possible ordered triples of final scores $(P_A, P_B, P_C)$.

Find the remainder when $N$ is divided by 8.

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
