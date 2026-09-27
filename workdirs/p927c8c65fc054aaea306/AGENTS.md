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

There´s a ping pong tournament with  $n\geq 3$  participants that we´ll call  $1, 2, \dots n$ . The tournament rules are the following ones: at the start, all the players form a line, ordered from  $1$  to  $n$ . Players  $1$  and  $2$  play the first match. The winner is at the beginning of the line and the loser is placed behind the last person in the line.In the next play, the two who at that moment are the first two in line face each other, the winner is first in line and the loser goes to the end of the line, just behind the last loser. And so on. After  $N$  matches, the tournament ends.Player number  $1$  won  $a_1$  matches, player number  $2$  won  $a_2$ , and so on till player  $n$ , that has won  $a_n$  matches (it is trivial that  $a_1+a_2+\dots+a_n=N)$ .Determine how many games each player has lost, based on  $a_1, a_2, \dots , a_n$ 

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
