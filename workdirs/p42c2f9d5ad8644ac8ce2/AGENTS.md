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

In a specialized cyber-security competition, ten regional servers—designated Server 1 through Server 10—start with varying baseline security integrity scores. Based on their historical performance, they are assigned initial ranks and scores as follows: 
- Server 1 (Rank 1): 9 points
- Server 2 (Rank 2): 8 points
- Server 3 (Rank 3): 7 points
- Server 4 (Rank 4): 6 points
- Server 5 (Rank 5): 5 points
- Server 6 (Rank 6): 4 points
- Server 7 (Rank 7): 3 points
- Server 8 (Rank 8): 2 points
- Server 9 (Rank 9): 1 point
- Server 10 (Rank 10): 0 points

A stress-test phase is initiated where every server must undergo a peer-to-peer data exchange protocol with every other server exactly once (a round-robin tournament). In each exchange, one server must emerge as the "dominant" node.

The points for these exchanges are awarded based on the initial rankings:
- if a server with a higher rank (a lower numerical rank, e.g., Rank 1 vs Rank 4) dominates a server with a lower rank, the dominant server earns 1 point and the other earns 0.
- If a server with a lower rank (a higher numerical rank, e.g., Rank 10 vs Rank 2) dominates a server with a higher rank, the dominant server earns 2 points and the other earns 0.

Once all possible pairings have been completed, each server’s final integrity score is calculated by adding the points earned during the stress-test to its initial baseline score. The "Grand Champion" is the server (or servers, in the case of a tie) that finishes with the highest final integrity score.

What is the minimum possible final integrity score that the Grand Champion could have?

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
