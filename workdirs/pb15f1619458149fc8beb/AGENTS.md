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

Let the origin of a spherical system of coordinates \((r, \theta, \phi)\) exist at the centre of the spherical resonator. The dependence on time is of the type \( e^{-i \omega t} \).\n\nOscillations of electric type are determined by the formula\n\n\[\nE_r = \frac{\partial^2}{\partial r^2} (ru) + k^2 (ru), \quad E_\theta = \frac{1}{r} \frac{\partial^2 (ru)}{\partial r \partial \theta}, \quad E_\phi = \frac{1}{r \sin \phi} \frac{\partial^2 (ru)}{\partial r \partial \phi},\n\]\n\n\[\nH_r = 0, \quad H_\theta = -\frac{ik}{\sin \theta} \frac{\partial u}{\partial \phi}, \quad H_\phi = ik \frac{\partial u}{\partial \theta},\n\]\n\nwhere \(u = u_{m,n}\) is an eigenfunction of the boundary-value problem\n\n\[\n\Delta u + k^2 u 0, \quad u = 0 \quad \text{for} \quad r = a,\n\]\n\ngiven by the formula\n\n\[\nu_{m,n}(r, \theta, \phi) = \psi_n(k_{m,n}r) Y_n^{(m)}(\theta, \phi) \quad (n = 1, 2, \ldots; \ m = 0, \pm 1, \pm 2, \ldots, \pm n),\n\]\n\nwhere \( k_{m,n} = \omega_{m,n} l / c \), the characteristic wave number, is a root of the equation\n\n\[\n\frac{J_{n + \frac{1}{2}}(ka)}{J_{n - \frac{1}{2}}(ka)} = \frac{ka}{n}, \quad \psi_n(\rho) = \sqrt{\frac{\pi}{2\rho}} J_{n + \frac{1}{2}}(\rho),\n\]\n\n\( Y_n^{(m)}(\theta, \phi) = P_n^{(m)}(\cos \theta) \cos m\phi \) is a spherical function.\n\nThe lowest natural frequency corresponds to \( n = 0 \): \( u_{m0}(r) = \psi_0(k_m r) \), where \( k_m \) is determined from the equation\n\n\[\nJ_{-\frac{1}{2}}(k_m a) = \sqrt{\frac{2}{\pi k_m a}} \cos k_m a = 0\n\]\n\nand equals\n\n\[\nk_m = \frac{(2m+1)\pi}{2a}, \quad \omega_{1,0} = \frac{\pi}{2a} c.\n\]\n\nFor oscillations of magnetic type (\( E_r = 0 \)) we have:\n\n\[\nE_r = 0, \quad E_\theta = -\frac{ik}{\sin \theta} \frac{\partial v}{\partial \phi}, \quad E_\phi = -ik \frac{\partial v}{\partial \theta},\n\]\n\n\[\nH_r = \frac{\partial^2(rv)}{\partial r^2} + k^2(rv), \quad H_\theta = \frac{1}{r} \frac{\partial^2(rv)}{\partial r \partial \theta}, \quad H_\phi = \frac{1}{r} \frac{\partial^2(rv)}{\partial r \partial \phi},\n\]\n\nwhere\n\n\[\nv = v_{m,n} = \psi_n(k_m, r) Y_n^{(m)}(\theta, \phi),\n\]\n\nwhere \( k_{m,n} \) is determined from the equation\n\n\[\nJ_{n+\frac{1}{2}}(ka) = 0.\n\]\n\nFor \( n = 0 \) we obtain:\n\n\[\nv_{m,0} = \psi_0(k_m r),\n\]\n\nwhere\n\n\[\nk_m = \frac{\pi m}{a}, \quad \omega_1 = c \frac{\pi}{a}.\n\]\n\n**Method.** Compare with problem 25 on the characteristic acoustic vibrations of the sphere.

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
