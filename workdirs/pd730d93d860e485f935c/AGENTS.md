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

A high-tech hexagonal research campus is divided into six main laboratory zones, denoted $A, B, C, D, E,$ and $F$, arranged in a perfect regular hexagon. Six security checkpoints—$G, H, I, J, K,$ and $L$—are positioned exactly at the midpoints of the perimeter fences $AB, BC, CD, DE, EF,$ and $AF$, respectively.

To secure the campus core, the administration installs six straight laser barriers connecting specific labs to specific checkpoints:
- Lab $A$ connects to checkpoint $H$
- Lab $B$ connects to checkpoint $I$
- Lab $C$ connects to checkpoint $J$
- Lab $D$ connects to checkpoint $K$
- Lab $E$ connects to checkpoint $L$
- Lab $F$ connects to checkpoint $G$

These intersecting laser lines enclose a smaller, perfectly regular hexagonal high-security vault in the center of the campus.

Let the ratio of the surface area of this central vault to the total surface area of the entire $ABCDEF$ campus be expressed as a simplified fraction $\frac{m}{n}$, where $m$ and $n$ are relatively prime positive integers. Find the value of $m + n$.

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
