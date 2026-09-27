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

Let $n$ be a positive integer. Consider an $n\times n$ grid of unit squares. How many ways are there to partition the horizontal and vertical unit segments of the grid into $n(n + 1)$ pairs so that the following properties are satisfied?

(i) Each pair consists of a horizontal segment and a vertical segment that share a common endpoint, and no segment is in more than one pair.

(ii) No two pairs of the partition contain four segments that all share the same endpoint.

(Pictured below is an example of a valid partition for $n = 2$.)

[asy]
import graph; size(2.6cm); 
pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps);
pen dotstyle = black;
draw((-3,4)--(-3,2)); 
draw((-3,4)--(-1,4)); 
draw((-1,4)--(-1,2)); 
draw((-3,2)--(-1,2)); 
draw((-3,3)--(-1,3)); 
draw((-2,4)--(-2,2)); 
draw((-2.8,4)--(-2,4), linewidth(2)); 
draw((-3,3.8)--(-3,3), linewidth(2)); 
draw((-1.8,4)--(-1,4), linewidth(2)); 
draw((-2,4)--(-2,3.2), linewidth(2)); 
draw((-3,3)--(-2.2,3), linewidth(2)); 
draw((-3,2.8)--(-3,2), linewidth(2)); 
draw((-3,2)--(-2.2,2), linewidth(2)); 
draw((-2,3)--(-2,2.2), linewidth(2)); 
draw((-1,2)--(-1.8,2), linewidth(2)); 
draw((-1,4)--(-1,3.2), linewidth(2)); 
draw((-2,3)--(-1.2,3), linewidth(2)); 
draw((-1,2.8)--(-1,2), linewidth(2)); 
dot((-3,2),dotstyle); 
dot((-1,4),dotstyle); 
dot((-1,2),dotstyle); 
dot((-3,3),dotstyle); 
dot((-2,4),dotstyle); 
dot((-2,3),dotstyle);[/asy]

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
