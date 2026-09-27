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

In a specialized logistics network, three distinct high-security vaults—Code P, Code Q, and Code R—are each protected by a unique odd prime number of digital encryption layers, denoted by the distinct odd primes $p$, $q$, and $r$. A cargo shipment is assigned an identification number $n$, which is a natural number. The "Security Clearance Level" of a shipment, denoted as $f(n)$, is defined as the greatest common divisor of its ID number $n$ and the product of the three vault layer counts ($pqr$).

A logistics coordinator is analyzing sets of three specific shipment IDs, $(a, b, c)$, where each ID is an integer ranging from $1$ to $pqr$ inclusive. The coordinator needs to identify all possible triples $(a, b, c)$ that satisfy a "Maximum Diversity" protocol. Under this protocol, the Security Clearance Levels of the following seven configurations must all be unique values:

1. The clearance of shipment $a$: $f(a)$
2. The clearance of shipment $b$: $f(b)$
3. The clearance of shipment $c$: $f(c)$
4. The clearance of the combined weight of $a$ and $b$: $f(a+b)$
5. The clearance of the combined weight of $b$ and $c$: $f(b+c)$
6. The clearance of the combined weight of $c$ and $a$: $f(c+a)$
7. The clearance of the total weight of all three: $f(a+b+c)$

Determine the total number of such triples $(a, b, c)$ that result in seven distinct Security Clearance Levels.

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
