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

Compute the genus of the graph with vertex set \( V(G) = \{u_1, \cdots, u_7, v_1, \cdots, v_9, w_1, \cdots, w_5\} \) and edge set \( E(G) = \bigcup_{i=1}^{11} E_i \), where:

\[ E_1 = \{u_1u_j \mid 2 \leq j \leq 7\} \cup \{u_1v_j \mid j=1,3,5,6,8,9\} \cup \{u_1w_3, u_1w_4\} \; ; \]
\[ E_2 = \{u_2u_j \mid j=3,4,6,7\} \cup \{u_2v_j \mid j=4,5,6,7\} \cup \{u_2w_5\} \; ; \]
\[ E_3 = \{u_3u_j \mid j=4,5,7\} \cup \{u_3v_j \mid j=1,7,8,9\} \cup \{u_3w_2\} \; ; \]
\[ E_4 = \{u_4u_j \mid j=5,6\} \cup \{u_4v_j \mid j=1,2,3,4\} \cup \{u_4w_1\} \; ; \]
\[ E_5 = \{u_5u_j \mid j=6,7\} \cup \{u_5v_j \mid j=4,5,6,7\} \cup \{u_5w_5\} \; ; \]
\[ E_6 = \{u_6u_7\} \cup \{u_6v_j \mid j=1,7,8,9\} \cup \{u_6w_2\} \; ; \]
\[ E_7 = \{u_7v_j \mid j=1,2,3,4\} \cup \{u_7w_1\} \; ; \]
\[ E_8 = \{v_1v_5, v_1v_6\} \; ; \]
\[ E_9 = \{v_2v_7\} \; ; \]
\[ E_{10} = \{v_3v_7\} \; ; \]
\[ E_{11} = \{v_4v_8, v_4v_9\} \; . \]

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
