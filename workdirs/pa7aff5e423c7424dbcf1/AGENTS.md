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

In a Bayesian game where two countries are deciding whether to attack, each country's type (military strength) is either \( p' \) (with probability \( q \)) or \( p'' \) (with probability \( 1 - q \)), where \( 0 < p' < p'' < 1 \). A country's payoff depends on whether it attacks, whether the other country attacks, and its type. The payoffs are structured as follows:  
- If a country attacks first (alone), it wins with probability \( xp \), where \( p \) is its type and \( x \) ensures \( p < xp < 1 \).  
- If both attack, a type \( p \) country wins with probability \( p \).  
- If a country does not attack and the other attacks, it wins with probability \( yp \), where \( 0 < yp < p \).  
- If neither attacks, the payoff is 0.  
Winning gives payoff \( W > 0 \), and losing gives \( L < 0 \).  

Derive the conditions under which it is a symmetric Bayes–Nash equilibrium for a country to attack **only if its type is \( p'' \)** (i.e., a high-type country attacks, and a low-type country does not).  

---

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
