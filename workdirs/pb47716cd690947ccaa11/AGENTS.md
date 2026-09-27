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

In the competitive world of high-performance sail design, a naval architect is drafting a triangular sail, $ABC$. To ensure structural integrity and aerodynamic efficiency, the design must adhere to three specific technical constraints:

1.  **Material Limit:** The total length of the high-tension rope used for the three edges—the luff ($a$), the leech ($b$), and the foot ($c$)—must be exactly $4$ meters.
2.  **Structural Ratio:** The length of the luff ($a$) must be equal to the product of the lengths of the other two sides ($bc$) multiplied by the square of the sine of the angle opposite the luff ($\sin^2 A$).
3.  **Non-Degeneracy:** The sail must be a real triangle with a non-zero interior area.

The architect needs to analyze the potential range of the sail's surface area. Let $M$ represent the maximum possible area of this sail and $m$ represent the minimum possible area.

If the value $M^2 + m^2$ is expressed as a fraction $\frac{a}{b}$ in lowest terms (where $a$ and $b$ are relatively prime positive integers), compute the sum $a+b$.

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
