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

In a remote territory, three communication outposts, $A$, $B$, and $C$, form a triangular network. A circular perimeter fence $\omega$, centered at a command hub $O$, passes through all three outposts. Surveyors have measured the direct distances between outposts as $AB = 15$ kilometers and $AC = 14$ kilometers.

A specialized signal relay $P$ is positioned within the triangular region. The distance from outpost $A$ to the relay is $AP = \frac{13}{2}$ km, and the square of the distance from outpost $B$ to the relay is $BP^2 = \frac{409}{4}$ km$^2$. It is noted that the relay $P$ is located closer to the boundary line $AC$ than to the boundary line $AB$.

Engineers extend the signal paths from $B$ and $C$ through the relay $P$ until they hit the perimeter fence $\omega$ at secondary nodes $E$ and $F$, respectively. A straight service road $AQ$ is constructed starting at outpost $A$, tangent to the circular fence $\omega$. This road terminates at a junction $Q$, which lies on the straight line path connecting nodes $E$ and $F$. 

An aerial scan confirms that the four points $A$, $Q$, $O$, and $P$ all lie on a single circular monitoring path.

The square of the distance between outpost $C$ and the relay $P$, denoted as $CP^2$, can be expressed in the form $\frac{a}{b} - c \sqrt{d}$ for positive integers $a, b, c, d$, where $\gcd(a, b) = 1$ and $d$ is square-free. Compute the value of $1000a+100b+10c+d$.

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
