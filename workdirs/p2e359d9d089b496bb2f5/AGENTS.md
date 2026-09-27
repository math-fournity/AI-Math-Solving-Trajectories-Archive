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

In a specialized logistics hub, there are four designated loading bays labeled 1, 2, 3, and 4. A fleet of automated transport drones is programmed such that each drone assigned to a bay is given a single instruction: "Transfer the cargo from this bay to bay $n$," where $n$ is any one of the four bays (1, 2, 3, or 4).

The facility manager is designing a routing protocol, denoted as a configuration $f$, where every bay is assigned exactly one destination bay. This protocol determines the path of a specialized test package that begins its journey at Bay 1. 

The package undergoes a sequence of four transfers:
1. First, it is moved from Bay 1 to a destination bay determined by the protocol. Let the destination bay be $D_1$.
2. Second, the package is moved from its current location ($D_1$) to a new bay according to the same protocol. Let this destination be $D_2$.
3. Third, the package is moved from $D_2$ to a new bay according to the protocol. Let this destination be $D_3$.
4. Fourth, the package is moved from $D_3$ to a final bay according to the protocol. Let this destination be $D_4$.

To pass the safety inspection, the protocol must be designed such that the sum of the labels of the four destination bays reached during this sequence is exactly 13. That is:
$Label(D_1) + Label(D_2) + Label(D_3) + Label(D_4) = 13$

How many unique routing protocols (functions $f: \{1,2,3,4\} \to \{1,2,3,4\}$) satisfy this specific safety requirement?

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
