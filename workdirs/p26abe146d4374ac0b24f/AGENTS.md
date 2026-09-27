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

A high-tech automated sorting facility features four specialized containment vaults, labeled Phase 1 through Phase 4. Initially, Phase 1 holds fifteen data canisters, each uniquely indexed with a serial number from 1 to 15. The other three vaults are currently empty.

The facility operates via a specific extraction protocol: 
In Phase 1, a robotic arm randomly selects two canisters at a time. The canister with the lower serial number is permanently decommissioned and removed from the system, while the canister with the higher serial number is transferred into the Phase 2 vault. This extraction cycle repeats until only one canister remains in Phase 1.

Once Phase 1 is processed, the robot moves to Phase 2. It again selects two canisters at random, decommissions the one with the lower serial number, and transfers the higher-numbered one into Phase 3. This continues until only one canister remains in Phase 2. Finally, the process is repeated for the canisters in Phase 3, with the survivors being moved into Phase 4 until only a single canister remains in Phase 3.

At the end of these operations, exactly one canister is left sitting in each of the four vaults. What is the probability that the canister with serial number 14 is one of the four remaining canisters? If the probability is expressed as an irreducible fraction $\frac{a}{b}$, compute $a + b$.

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
