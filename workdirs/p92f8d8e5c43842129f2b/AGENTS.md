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

In the city of Aethelgard, a grand culinary festival is being organized. The master chef must select a trio of unique signature dishes to serve at the royal banquet. In the pantry, there are exactly 27 distinct ingredients available, each defined by three specific attributes:

1.  **The Origin:** Every ingredient comes from either the High Mountains, the Deep Sea, or the Whispering Forest.
2.  **The Flavor Profile:** Every ingredient is classified as Bitter, Sweet, or Savory.
3.  **The Preparation Style:** Every ingredient is processed by Smoking, Fermenting, or Roasting.

The pantry contains exactly one ingredient for every possible combination of these three attributes.

The chef’s rule for a "Balanced Trio" is strict: among the three chosen ingredients, no two ingredients are allowed to share more than one attribute. For instance, he could choose (Mountain-Bitter-Smoked, Mountain-Sweet-Fermented, Sea-Savory-Roasted) because no two items share more than one trait. However, he cannot choose (Mountain-Bitter-Smoked, Forest-Sweet-Roasted, Mountain-Savory-Smoked) because the first and third ingredients share two attributes (Mountain origin and Smoked style).

In how many ways can the chef select an unordered set of 3 distinct ingredients from the pantry such that no two ingredients in the set share two or more attributes?

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
