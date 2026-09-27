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

In a remote archipelago, a research council has identified 11 unique mineral deposits, known as "Core Sites," which are the only sources of a rare element. Two rival mining conglomerates, Argent and Boron, are competing to claim these sites one by one.

The acquisition process follows strict regulatory protocols:
1. The companies take turns claiming one site at a time, with Argent always taking the first site.
2. For each company’s very first selection, they may choose any of the 11 sites.
3. For every subsequent selection, a company must choose a site that is connected by a pre-existing subterranean tunnel to at least one site that the same company already owns.
4. If a company reaches a state where they cannot claim any more sites because none of the remaining available sites are connected to their current network, they must forfeit all remaining turns, allowing the other company to continue claiming all reachable sites.

The network of subterranean tunnels is mapped out by the council before the claiming begins. To ensure fair competition or strategic advantage, the council designs the tunnel layout specifically to benefit the second company (Boron).

Let $N$ be the maximum number of Core Sites that Boron can be guaranteed to acquire, regardless of which sites Argent chooses to claim, provided the subterranean tunnel network is arranged optimally to favor Boron. Find $N$.

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
