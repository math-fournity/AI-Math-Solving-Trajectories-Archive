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

In a vast desert, three specialized communication outposts—Apex (A), Base (B), and Core (C)—form a triangular network. Long-range scans indicate that the signal path from Apex to Base and the path from Apex to Core meet at an angle of $60^\circ$. At the Base outpost, the angle formed between the signals from Apex and Core is $70^\circ$, while at the Core outpost, the angle between Apex and Base is $50^\circ$.

To optimize the network, engineers have identified three "Drop-zones," $D, E,$ and $F$, which are the points on each perimeter path closest to the opposite outpost (specifically, $D$ is the point on the $BC$ path closest to $A$, $E$ is on $AC$ closest to $B$, and $F$ is on $AB$ closest to $C$). The direct maintenance road $AD$, representing the shortest distance from Apex to the line connecting Base and Core, is exactly $\frac{1}{2}$ units long.

A central navigation hub, $O$, is located at the unique point equidistant from all three outposts. A straight fiber-optic cable is laid starting from Apex and passing directly through the navigation hub $O$. This cable continues until it intersects the perimeter road $BC$ at a junction point designated as $O'$.

Find the exact length of the fiber-optic cable segment $AO'$.

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
