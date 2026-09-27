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

In a specialized laboratory, a head researcher is organizing a high-security storage system consisting of 7 unique chemical canisters, labeled 1 through 7. To manage these chemicals, the researcher must authorize 5 different clearance levels, represented by 5 distinct safety containers of varying sizes.

Each container must hold a specific number of canisters:
- The Tier-1 container must hold exactly 1 canister.
- The Tier-2 container must hold exactly 2 canisters.
- The Tier-3 container must hold exactly 3 canisters.
- The Tier-4 container must hold exactly 4 canisters.
- The Tier-5 container must hold exactly 5 canisters.

The safety protocol dictates a strict organizational rule for any two chosen containers (Tier $i$ and Tier $j$): the smaller container must either be stored entirely inside the larger container, or it must share no canisters at all with the larger container. (Note: Since each Tier has a different size, for any two Tiers $i$ and $j$ where $i < j$, the Tier $i$ container is the smaller one).

In how many different ways can the researcher select the sets of canisters for these five containers while satisfying all safety protocols?

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
