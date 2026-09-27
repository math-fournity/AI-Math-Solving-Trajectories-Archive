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

In a remote territory, three supply depots—Station Alpha, Station Beta, and Station Gamma—are positioned at the corners of a triangular flight zone. The flight corridors connecting them have lengths of 7 miles between Beta and Gamma, 8 miles between Gamma and Alpha, and 9 miles between Alpha and Beta. A circular perimeter fence, $\Omega$, perfectly encloses these three stations.

Three emergency landing pads are being constructed within this zone. Pad A is a circular zone tangent to the interior of the perimeter fence along the shorter arc between Beta and Gamma; it is also tangent to the direct path between Beta and Gamma at a specific refueling point $X$. Pad B is tangent to the interior of the fence along the shorter arc between Gamma and Alpha, and tangent to the path between Gamma and Alpha at point $Y$. Pad C is tangent to the interior of the fence along the shorter arc between Alpha and Beta, and tangent to the path between Alpha and Beta at point $Z$.

The refueling points are strategically placed such that the distance from Beta to $X$ is exactly half the distance from $X$ to Gamma. Similarly, the distance from Gamma to $Y$ is half the distance from $Y$ to Alpha, and the distance from Alpha to $Z$ is half the distance from $Z$ to Beta.

To coordinate logistics, engineers must calculate the lengths of the direct external bridge connections between the circular pads. Let $t_{AB}$ be the length of the common external tangent between Pad A and Pad B, let $t_{BC}$ be the length of the common external tangent between Pad B and Pad C, and let $t_{CA}$ be the length of the common external tangent between Pad C and Pad A.

If the total length of these three bridges, $t_{AB} + t_{BC} + t_{CA}$, is expressed as a simplified fraction $\frac{m}{n}$ for relatively prime positive integers $m$ and $n$, find the value of $m+n$.

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
