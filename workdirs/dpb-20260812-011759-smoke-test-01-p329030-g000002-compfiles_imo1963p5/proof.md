# Proof: $\cos(\pi/7) - \cos(2\pi/7) + \cos(3\pi/7) = 1/2$

## 求证

$$\cos\frac{\pi}{7} - \cos\frac{2\pi}{7} + \cos\frac{3\pi}{7} = \frac{1}{2}.$$

## 证明

**第一步：建立关于 7 次单位根的恒等式。**

设 $\omega = e^{2\pi i/7}$，则 $\omega^0, \omega^1, \omega^2, \dots, \omega^6$ 是全部 7 次单位根。由于 $\omega \neq 1$ 是 $x^7 - 1 = (x-1)(x^6+x^5+\cdots+x+1)$ 的根，故

$$1 + \omega + \omega^2 + \omega^3 + \omega^4 + \omega^5 + \omega^6 = 0.$$

将共轭对配对（$\omega^k$ 与 $\omega^{7-k} = \overline{\omega^k}$）：

$$\omega^k + \omega^{7-k} = e^{2\pi i k/7} + e^{-2\pi i k/7} = 2\cos\frac{2k\pi}{7}.$$

因此

$$1 + 2\sum_{k=1}^{3}\cos\frac{2k\pi}{7} = 0,$$

即

$$\cos\frac{2\pi}{7} + \cos\frac{4\pi}{7} + \cos\frac{6\pi}{7} = -\frac{1}{2}. \tag{$\star$}$$

**第二步：用补角变换化简 $(\star)$。**

利用恒等式 $\cos(\pi - \theta) = -\cos\theta$：

$$\cos\frac{6\pi}{7} = \cos\!\left(\pi - \frac{\pi}{7}\right) = -\cos\frac{\pi}{7},$$

$$\cos\frac{4\pi}{7} = \cos\!\left(\pi - \frac{3\pi}{7}\right) = -\cos\frac{3\pi}{7}.$$

代入 $(\star)$：

$$\cos\frac{2\pi}{7} - \cos\frac{3\pi}{7} - \cos\frac{\pi}{7} = -\frac{1}{2}.$$

两边乘以 $-1$：

$$\cos\frac{\pi}{7} - \cos\frac{2\pi}{7} + \cos\frac{3\pi}{7} = \frac{1}{2}.$$

**证毕.** $\blacksquare$

## 数值验证

$$\cos\frac{\pi}{7} \approx 0.900969,\quad \cos\frac{2\pi}{7} \approx 0.623490,\quad \cos\frac{3\pi}{7} \approx 0.222521,$$

$$0.900969 - 0.623490 + 0.222521 = 0.500000 = \frac{1}{2}. \checkmark$$
