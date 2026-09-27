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

Let \(ABC\) be an acute triangle inscribed in a circle with center \(O\). Define the lines \(B_{a}C_{a}\), \(C_{b}A_{b}\), and \(A_{c}B_{c}\) as the perpendiculars to \(AO\), \(BO\), and \(CO\) respectively, where \(A_{b}, A_{c} \in BC\), \(B_{a}, B_{c} \in AC\), and \(C_{a}, C_{b} \in AB\). Let \(O_{a}\), \(O_{b}\), and \(O_{c}\) be the circumcenters of triangles \(AC_{a}B_{a}\), \(BA_{b}C_{b}\), and \(CA_{c}B_{c}\) respectively. If the centroid of triangle \(ABC\) is \(G\), find the value of \(\frac{OG^2}{O_{a}O_{b}^2 + O_{b}O_{c}^2 + O_{c}O_{a}^2}\).

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
