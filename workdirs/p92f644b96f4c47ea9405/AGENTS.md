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

In a remote sector of the ocean, three research buoys—Station Alpha ($A$), Station Beta ($B$), and Station Gamma ($C$)—are anchored to form a triangular surveillance perimeter. The nautical distance between Alpha and Beta is $4$ units, between Beta and Gamma is $6$ units, and between Alpha and Gamma is $5$ units.

A central Command Hub ($O$) is positioned at the exact circumcenter of this triangular formation, equidistant from all three stations. This configuration creates three distinct circular sub-zones:
1. Sub-zone 1: The circular region defined by the coordinates of Alpha, Beta, and the Command Hub.
2. Sub-zone 2: The circular region defined by the coordinates of Beta, Gamma, and the Command Hub.
3. Sub-zone 3: The circular region defined by the coordinates of Alpha, Gamma, and the Command Hub.

A massive perimeter containment fence, designed as a perfect circle $\Gamma$, is constructed such that it is tangent to each of these three sub-zones. Furthermore, the fence is built to completely enclose all three sub-zones within its interior.

Calculate the total diameter of this circular containment fence $\Gamma$.

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
