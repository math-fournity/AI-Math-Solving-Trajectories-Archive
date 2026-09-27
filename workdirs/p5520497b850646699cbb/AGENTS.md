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

In a remote digital network consisting of $n$ servers, the infrastructure is designed as a tree, meaning there are exactly $n-1$ fiber-optic links ensuring a unique path between any two servers. One day, a malicious "Recursive Virus" is uploaded to a specific server $s$. 

The virus operates on a strict cycle:
1. **Every Morning (Expansion):** The virus automatically replicates and infects every healthy server directly connected via a fiber-optic link to any server already infected.
2. **Every Night (Containment):** Network security teams can permanently sever exactly one fiber-optic link anywhere in the network. They continue this nightly intervention as long as there is at least one link connecting an infected server to a healthy server.

For a fixed network topology $G$ and an initial infection point $s$, let $X(G, s)$ be the minimum number of links that must be severed to eventually prevent the virus from spreading to any more healthy servers. 

For a fixed number of servers $n$, let $M(n)$ be the maximum possible value of $X(G, s)$ across all possible tree-structured network topologies and all possible starting servers.

Calculate the value of the sum:
$\sum_{n=1}^{100} M(n)$

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
