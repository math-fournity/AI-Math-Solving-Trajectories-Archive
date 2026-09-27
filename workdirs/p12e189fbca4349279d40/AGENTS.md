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

In a remote industrial district, two high-precision manufacturing plants, Alpha and Beta, each operate exactly 7 specialized production lines. Each line can produce one of four outcomes: a "Grade A" component, a "Grade B" component, a "Grade C" component, or a "Faulty" component. No two lines between the plants share the same technical specifications.

For plant Alpha, let $g_L$ be the number of Grade A components produced, $s_L$ be the number of Grade B components, and $b_L$ be the number of Grade C components. Similarly, for plant Beta, let $g_P$ be the number of Grade A components, $s_P$ be the number of Grade B components, and $b_P$ be the number of Grade C components.

An efficiency auditor determines that plant Alpha is "universally superior" to plant Beta. This is defined by the following condition: for every possible set of market values assigned to the components—where the value of a Grade C component ($w_b$), a Grade B component ($w_s$), and a Grade A component ($w_g$) are any positive real numbers satisfying $0 < w_b < w_s < w_g$—the total value of Alpha's output is strictly greater than the total value of Beta's output. Mathematically, this is expressed as:
\[w_{g} g_{L}+w_{s} s_{L}+w_{b} b_{L}>w_{g} g_{P}+w_{s} s_{P}+w_{b} b_{P}\]

Compute the total number of possible 6-tuples $(g_{L}, s_{L}, b_{L}, g_{P}, s_{P}, b_{P})$ that satisfy this universal superiority condition.

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
