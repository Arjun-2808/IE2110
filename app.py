import streamlit as st
import pandas as pd
import numpy as np

# --- App Configuration ---
st.set_page_config(page_title="IE2110 Revision Helper", layout="wide")

st.title(" Signals and Systems Revision Helper 🧠")
st.markdown("""
Welcome! This app helps you revise key concepts, review solved examples, and learn **practical tips & tricks** for tackling IE2110 exam questions, especially those involving **graph sketching**.
Use the tabs below to navigate through the content.

*Note: For clarity, graphical representations are described textually. In a live app, these would be plotted visually.*
""")

# --- Main Content Sections ---
tab1, tab2, tab3 = st.tabs(["📘 Key Concepts & Formulas", "💡 Solved Examples (Focus on Method)", "🚀 Graphing & Problem-Solving Hacks"])

# --- Key Concepts Tab ---
with tab1:
    st.header("📘 Key Concepts & Formulas")
    st.markdown("Essential definitions and formulas, with emphasis on their application.")

    # --- Part 1 Topics ---
    st.subheader("Part 1: Fundamentals, LTI Systems, Convolution")

    with st.expander("1.1 Signal Classifications & Properties"):
        st.markdown(r"""
        * **CT vs. DT**: $x(t)$ vs $x[n]$. Identify the independent variable.
        * **Symmetry**:
            * Even: $x(t)=x(-t)$ or $x[n]=x[-n]$. (Symmetric about vertical axis).
            * Odd: $x(t)=-x(-t)$ or $x[n]=-x[-n]$. (Anti-symmetric about origin).
            * Decomposition: $x = x_e + x_o$.
                * $x_e = \frac{1}{2}(x + x_{\text{reflected}})$
                * $x_o = \frac{1}{2}(x - x_{\text{reflected}})$
        * **Periodicity**: Does the signal repeat? Find smallest $T_0$ (CT) or $K_0$ (DT).
            * *Test (CT)*: Is $x(t) = x(t+T_0)$ for some $T_0 > 0$?
            * *Test (DT)*: Is $x[n] = x[n+K_0]$ for some integer $K_0 > 0$? For $x[n]=e^{j\omega_0 n}$, periodic if $\omega_0/(2\pi)$ is rational.
        * **Energy vs. Power**: Finite duration/decaying $\implies$ Energy signal. Periodic/constant amplitude $\implies$ Power signal.
        """)
        st.markdown("**Formulas (Energy $E_x$, Power $P_x$)**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Continuous-Time (CT)**")
            st.latex(r"E_x = \int_{-\infty}^{\infty} |x(t)|^2 dt")
            st.latex(r"P_x = \lim_{T\to\infty} \frac{1}{T} \int_{-T/2}^{T/2} |x(t)|^2 dt \quad \text{(General)}")
            st.latex(r"P_x = \frac{1}{T_0} \int_{T_0} |x(t)|^2 dt \quad \text{(Periodic)}")
        with col2:
            st.markdown("**Discrete-Time (DT)**")
            st.latex(r"E_x = \sum_{n=-\infty}^{\infty} |x[n]|^2")
            st.latex(r"P_x = \lim_{K\to\infty} \frac{1}{2K+1} \sum_{n=-K}^{K} |x[n]|^2 \quad \text{(General)}")
            st.latex(r"P_x = \frac{1}{K_0} \sum_{n=\langle K_0 \rangle} |x[n]|^2 \quad \text{(Periodic)}") # <K0> means sum over one period

    with st.expander("1.2 Essential Signals (Know their shapes!)"):
        st.markdown(r"""
        * **Impulse $\delta$**:
            * CT $\delta(t)$: Idealized function. Zero for $t \neq 0$, infinite at $t=0$, $\int \delta(t) dt = 1$. *Sifting Property*: $\int x(t)\delta(t-t_0)dt = x(t_0)$.
            * DT $\delta[n]$: Value 1 at $n=0$, else 0. *Use for sequence representation*: $x[n] = \sum_k x[k]\delta[n-k]$.
        * **Unit Step $u$**:
            * CT $u(t)$: 0 for $t<0$, 1 for $t \ge 0$. (Value at $t=0$ can vary by definition, often 1 or 0.5). *Use for 'turning on' signals*.
            * DT $u[n]$: 0 for $n<0$, 1 for $n \ge 0$.
            * Relation: $u(t) = \int_{-\infty}^t \delta(\tau)d\tau$, $\delta(t) = \frac{du(t)}{dt}$ (loosely). $u[n] = \sum_{m=-\infty}^n \delta[m]$, $\delta[n]=u[n]-u[n-1]$.
        * **Rectangle $\text{rect}(t/T)$**: Value 1 for $|t| \le T/2$. Width $T$, centered at 0.
        * **Triangle $\Lambda(t/T)$**: Value $1-|t|/T$ for $|t| \le T$. Width $2T$, peak 1 at $t=0$. (Note: different definitions exist, check formula sheet's $\text{rect}$ and $\text{sinc}$).
        * **Sinc $\text{sinc}(x) = \frac{\sin(\pi x)}{\pi x}$**: Peak=1 at $x=0$. Zero crossings at $x = \pm 1, \pm 2, ...$. Decays as $1/x$. *Important FT pair with rect*.
        * **Exponential $e^{at}$ / $a^n$**: Decaying if $Re\{a\}<0$ or $|a|<1$. Growing if $Re\{a\}>0$ or $|a|>1$. Oscillatory if $a$ is imaginary ($e^{j\omega_0 t}$) or complex with magnitude 1 ($e^{j\omega_0 n}$).
        """)

    with st.expander("1.3 Signal Operations (How they affect graphs)"):
        st.markdown(r"""
        * **Amplitude Scale $A x$**: Stretches/shrinks vertically. Flips if $A<0$.
        * **Time Shift $x(t-T)$ / $x[n-K]$**: Shifts **right** (delay) if $T, K > 0$. Shifts **left** (advance) if $T, K < 0$. Moves the *entire shape* along the time axis.
        * **Time Scale (CT) $x(at)$**:
            * $|a|>1$: **Compresses** towards $t=0$. (Events happen faster).
            * $|a|<1$: **Expands** away from $t=0$. (Events happen slower).
            * $a<0$: Reverses time + scales. *Do scaling first, then reflect about $t=0$*.
            * *Graphing Tip*: A point at $t_1$ in $x(t)$ moves to $t_1/a$ in $x(at)$.
        * **Time Scale (DT) $x[Kn]$ (Decimation)**: Keeps samples at $n=0, \pm K, \pm 2K,...$. Discards others. *Graphing Tip*: Plot original $x[m]$, then mark and plot only points where $m$ is a multiple of $K$.
        * **Time Scale (DT) $x[n/K]$ (Expansion)**: Original sample at $m$ moves to $n=mK$. Insert $K-1$ zeros between original samples (assuming $n/K$ must be integer). *Graphing Tip*: Plot original $x[m]$, then spread points out by factor $K$ and fill gaps with zeros.
        * **Combined Ops**: $A x(a(t-T))$. Order matters! Usually: **Shift first** ($t \to t-T$), **then scale** ($(t-T) \to a(t-T)$), **then amplitude scale**. Check specific question context. For $y[n] = x[an + b]$, find integer $n$ values that make $an+b$ valid integer indices for $x$.
        """)

    with st.expander("1.4 System Properties (LTI Focus)"):
        st.markdown(r"""
        * **LTI**: Linear & Time-Invariant. Characterized by impulse response $h$.
        * **Causality**: Output depends only on *present/past* input. LTI: $h(t)=0$ for $t<0$; $h[n]=0$ for $n<0$. *Graph Check*: Impulse response is zero for negative time.
        * **Stability (BIBO)**: Bounded Input $\implies$ Bounded Output. LTI: Impulse response must be absolutely integrable/summable.
            * $\int_{-\infty}^{\infty} |h(t)| dt < \infty$
            * $\sum_{n=-\infty}^{\infty} |h[n]| < \infty$
            * *Graph Check*: Area under $|h(t)|$ or sum of $|h[n]|$ must be finite. Decaying impulse response often implies stability.
        * **Memory**: Output depends on past/future values. Memoryless if output depends only on current input. LTI: Memoryless iff $h(t)=c\delta(t)$ or $h[n]=c\delta[n]$.
        """)

    with st.expander("2. LTI Systems & Convolution"):
        st.markdown(r"""
        * **Output $y = x * h$**. The system's response $h$ shapes the input $x$.
        """)
        st.markdown("**Convolution Integral (CT)**:")
        st.latex(r"y(t) = x(t) * h(t) = \int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau")
        st.markdown("**Convolution Sum (DT)**:")
        st.latex(r"y[n] = x[n] * h[n] = \sum_{m=-\infty}^{\infty} x[m] h[n-m]")
        st.markdown(r"""
        * **Graphical Meaning**: Flip one signal ($h$), shift it by $t$ (or $n$), multiply point-by-point with the other ($x$), find the area/sum of the product. The result is the output $y$ at that specific shift $t$ (or $n$). Repeat for all shifts. (See Hacks tab for details).
        * **Properties**: Commutative ($x*h=h*x$), Distributive ($x*(h_1+h_2) = x*h_1 + x*h_2$), Associative ($(x*h_1)*h_2 = x*(h_1*h_2)$). Useful for simplifying problems.
        * **Special Cases**:
            * $x(t) * \delta(t-T_0) = x(t-T_0)$. (Shifts the input).
            * $x(t) * u(t) = \int_{-\infty}^{t} x(\tau) d\tau$. (Integrates the input).
            * $x[n] * \delta[n-K_0] = x[n-K_0]$.
            * $x[n] * u[n] = \sum_{m=-\infty}^{n} x[m]$.
        * **Step Response $s$**: Response to unit step $u$. $s(t) = h(t)*u(t) = \int_{-\infty}^{t} h(\tau) d\tau$. $h(t) = \frac{ds(t)}{dt}$. Similarly, $s[n] = \sum_{m=-\infty}^{n} h[m]$ and $h[n]=s[n]-s[n-1]$.
        """)

    st.divider()
    # --- Part 2 Topics ---
    st.subheader("Part 2: Fourier Analysis & Sampling")

    with st.expander("2. Fourier Series (Periodic CT Signals)"):
        st.markdown(r"""
        * **Idea**: Represent $x(t)$ with period $T_0$ as a sum of complex exponentials (or sinusoids) at harmonic frequencies $nf_0$, where $f_0=1/T_0$ ($\omega_0 = 2\pi f_0$).
        * **Complex Exponential Form**: $x(t) = \sum_{n=-\infty}^{\infty} c_n e^{j n \omega_0 t}$.
        """)
        st.latex(r"c_n = \frac{1}{T_0} \int_{T_0} x(t) e^{-j n \omega_0 t} dt \quad \text{(Analysis Eq.)}")
        st.markdown(r"""
            * $c_n$ is the **complex amplitude** of the $n^{th}$ harmonic.
            * $|c_n|$: Amplitude Spectrum (Plot $|c_n|$ vs $n f_0$). Usually discrete lines (impulses).
            * $\angle c_n$: Phase Spectrum (Plot $\angle c_n$ vs $n f_0$).
            * $c_0 = \frac{1}{T_0} \int_{T_0} x(t) dt$ = **DC / Average value**.
            * Real $x(t) \implies c_{-n} = c_n^*$. ($|c_n|$ is even, $\angle c_n$ is odd).
        * **Trigonometric Form**: $x(t) = a_0 + \sum_{n=1}^{\infty} [a_n \cos(n \omega_0 t) + b_n \sin(n \omega_0 t)]$.
            * $a_0 = c_0$.
            * $a_n = 2 \text{Re}\{c_n\} = \frac{2}{T_0} \int_{T_0} x(t) \cos(n\omega_0 t) dt \quad (n \ge 1)$.
            * $b_n = -2 \text{Im}\{c_n\} = \frac{2}{T_0} \int_{T_0} x(t) \sin(n\omega_0 t) dt \quad (n \ge 1)$.
        * **Amplitude-Phase Form**: $x(t) = A_0 + \sum_{n=1}^{\infty} A_n \cos(n \omega_0 t + \phi_n)$.
            * $A_0 = c_0$.
            * $A_n = 2|c_n| = \sqrt{a_n^2 + b_n^2} \quad (n \ge 1)$.
            * $\phi_n = \angle c_n = \text{atan2}(-b_n, a_n) \quad (n \ge 1)$.
        * **Parseval's (Power)**: Average power $P_x$
        """)
        st.latex(r"P_x = \frac{1}{T_0} \int_{T_0} |x(t)|^2 dt = \sum_{n=-\infty}^{\infty} |c_n|^2 = A_0^2 + \frac{1}{2}\sum_{n=1}^{\infty} A_n^2")
        st.markdown("Power in time domain = Sum of powers in frequency components.")

    with st.expander("3. Fourier Transform (Aperiodic CT Signals / Energy Signals)"):
        st.markdown(r"""
        * **Idea**: Represent a non-periodic $x(t)$ using a *continuum* of complex exponentials $e^{j 2 \pi f t}$.
        * **Definition** ($f$ in Hz):
        """)
        st.latex(r"X(f) = \mathcal{F}\{x(t)\} = \int_{-\infty}^{\infty} x(t) e^{-j2\pi f t} dt \quad \text{(Analysis Eq.)}")
        st.latex(r"x(t) = \mathcal{F}^{-1}\{X(f)\} = \int_{-\infty}^{\infty} X(f) e^{j2\pi f t} df \quad \text{(Synthesis Eq.)}")
        st.markdown(r"""
            * $X(f)$ is the **Frequency Spectrum** or **Fourier Transform**. It's a complex function of frequency $f$.
            * $|X(f)|$: Amplitude Spectrum. *Shape tells you frequency content*.
            * $\angle X(f)$: Phase Spectrum. *Tells you relative timing of frequencies*.
            * Units: If $x(t)$ is Volts, $X(f)$ is Volt-seconds or Volts/Hz.
        * **Key Properties & Pairs**: (Essential for problem solving! See Hacks tab)
            * Linearity, Time/Freq Shifting, Scaling, Duality, Differentiation, Integration.
            * **Convolution Theorem**: $x_1(t) * x_2(t) \longleftrightarrow X_1(f) X_2(f)$. (Convolution in time $\Leftrightarrow$ Multiplication in frequency). *Often easier than time-domain convolution!*
            * **Multiplication Theorem**: $x_1(t) x_2(t) \longleftrightarrow X_1(f) * X_2(f)$. (Multiplication in time $\Leftrightarrow$ Convolution in frequency). *Used in AM, Sampling*.
            * Know pairs like: $\text{rect} \leftrightarrow \text{sinc}$, $\Lambda \leftrightarrow \text{sinc}^2$, $e^{-at}u(t) \leftrightarrow 1/(a+j\omega)$, $\delta(t) \leftrightarrow 1$, $1 \leftrightarrow \delta(f)$, $e^{j\omega_0 t} \leftrightarrow \delta(f-f_0)$. (Note: $\omega=2\pi f$)
        * **Rayleigh's (Energy)**: Total energy $E_x$
        """)
        st.latex(r"E_x = \int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df")
        st.markdown(r"$|X(f)|^2$ is the Energy Spectral Density (ESD). Area under ESD = Total Energy.")

    with st.expander("4. Frequency Domain Analysis of LTI Systems"):
        st.markdown(r"""
        * **Frequency Response**: $H(f) = \mathcal{F}\{h(t)\}$. How the system affects different frequencies. Can also use $H(j\omega)$.
        * **Input/Output**: $Y(f) = H(f) X(f)$. Output spectrum = Input spectrum $\times$ Frequency Response.
            * *Graphical View*: $|Y(f)| = |H(f)| |X(f)|$. $\angle Y(f) = \angle H(f) + \angle X(f)$.
            * The system *filters* the input signal $X(f)$ based on the shape of $H(f)$.
        * **Response to Sinusoid**: Input $A\cos(\omega_0 t + \theta)$ $\implies$ Output $A|H(j\omega_0)|\cos(\omega_0 t + \theta + \angle H(j\omega_0))$.
            * *Key*: System only changes Amplitude (by $|H|$ at $\omega_0$) and Phase (by $\angle H$ at $\omega_0$) of the input sinusoid. Frequency remains the same.
        * **Ideal Filters**: LPF, HPF, BPF. Sharp cutoffs. $H(f)$ is 1 (or K) in passband, 0 in stopband. Linear phase in passband ($\angle H = -\omega t_d = -2\pi f t_d$) for no phase distortion (just delay $t_d$).
            * *Reality Check*: Ideal filters are non-causal ($h(t)$ is non-zero for $t<0$). Real filters have gradual roll-offs.
        * **Spectral Density**: Output ESD $\Psi_y(f) = |H(f)|^2 \Psi_x(f)$. Output PSD $S_y(f) = |H(f)|^2 S_x(f)$.
        """)

    with st.expander("5. Sampling & Aliasing"):
        st.markdown(r"""
        * **Sampling**: $x[n] = x(nT_s)$. Convert CT $x(t)$ to DT $x[n]$. $f_s=1/T_s$ is sampling frequency (Hz). $\omega_s = 2\pi f_s$ (rad/s).
        * **Spectrum of Sampled Signal (Ideal Sampling Model)**: $x_s(t) = x(t) \sum_{n=-\infty}^{\infty} \delta(t-nT_s)$.
        """)
        st.latex(r"X_s(f) = \mathcal{F}\{x_s(t)\} = \frac{1}{T_s} \sum_{n=-\infty}^{\infty} X(f - n f_s)")
        st.markdown(r"""
            * *Graphical View*: Replicas of the original spectrum $X(f)$, scaled by $1/T_s = f_s$, centered at multiples of $f_s$ ($0, \pm f_s, \pm 2f_s, ...$).
        * **Sampling Theorem**: If $x(t)$ is bandlimited to $f_M$ ($X(f)=0$ for $|f|>f_M$), we can perfectly recover $x(t)$ from $x[n]$ if the sampling rate $f_s \ge 2f_M$.
        * **Nyquist Rate**: $f_N = 2f_M$. Minimum $f_s$ to avoid aliasing.
        * **Aliasing**: If $f_s < f_N$, the spectral replicas **overlap**. High frequencies in $X(f)$ (e.g., $|f|>f_s/2$) get "folded" back and appear as lower frequencies in the baseband $[-f_s/2, f_s/2]$.
            * *Result*: A high frequency component $f_1 > f_s/2$ appears as a lower frequency $f_a = |f_1 - k f_s|$ such that $|f_a| \le f_s/2$. (See Hacks tab).
        * **Reconstruction**: Pass the *impulse train* $x_s(t)$ through an ideal LPF with cutoff $f_s/2$ and gain $T_s$ to recover $x(t)$ *if no aliasing occurred*.
        * **Digital Frequency**: For $x[n] = x(nT_s)$, the corresponding discrete frequencies are $\omega_d = \omega T_s = \frac{\omega}{\omega_s} 2\pi$ (rad/sample) or $f_d = f T_s = f/f_s$ (cycles/sample). The unique range is $\omega_d \in [-\pi, \pi]$ or $f_d \in [-0.5, 0.5]$.
        """)

    st.divider()
    # --- Part 3 Topics ---
    st.subheader("Part 3: Amplitude Modulation (AM)")

    with st.expander("1.2 Conventional AM"):
        st.markdown(r"""
        * **Purpose**: Shift baseband message $m(t)$ (bandwidth $B$) to higher frequency $f_c \gg B$ for transmission.
        * **Time Domain**: $x_{AM}(t) = A_c [1 + k_a m(t)] \cos(2 \pi f_c t)$. Assume carrier phase is zero.
            * $A_c$: Carrier amplitude. $k_a$: Sensitivity.
            * **Envelope**: $A_c |1 + k_a m(t)|$. If $|k_a m(t)|_{\max} = \mu < 1$, envelope is $A_c(1+k_a m(t))$ and follows $m(t)$.
        * **Modulation Index $\mu$**: $\mu = \max |k_a m(t)|$. For sinusoidal $m(t)=A_m\cos(\omega_m t)$, $\mu=k_a A_m$.
            * $\mu \le 1$: Under-modulation / Critical modulation (Good, allows envelope detection).
            * $\mu > 1$: Over-modulation (Bad, envelope distorted, information loss).
        * **Spectrum**: Use multiplication property: $x(t) \cos(\omega_c t) \longleftrightarrow \frac{1}{2}[X(f-f_c) + X(f+f_c)]$. Let $M(f)=\mathcal{F}\{m(t)\}$.
        """)
        st.latex(r"X_{AM}(f) = \mathcal{F}\{A_c \cos(2\pi f_c t) + A_c k_a m(t) \cos(2\pi f_c t)\}")
        st.latex(r"X_{AM}(f) = \underbrace{\frac{A_c}{2}[\delta(f-f_c) + \delta(f+f_c)]}_{\text{Carrier}} + \underbrace{\frac{A_c k_a}{2}[M(f-f_c) + M(f+f_c)]}_{\text{Sidebands}}")
        st.markdown(r"""
            * *Graphical View*: Carrier impulses (spikes) at $\pm f_c$. Scaled copies of the message spectrum $M(f)$ shifted to center around $\pm f_c$.
        * **Bandwidth**: $BW_{AM} = 2 B$ (where $B$ is the one-sided bandwidth of $m(t)$).
        * **Power**: $P_T = P_c + P_{SB} = \frac{A_c^2}{2} + \frac{A_c^2 k_a^2 P_m}{2}$, where $P_m$ is average power of $m(t)$.
        * **Efficiency**: $\eta = P_{SB}/P_T = \frac{k_a^2 P_m}{1 + k_a^2 P_m}$. For sinusoidal modulation, $\eta = \frac{\mu^2/2}{1 + \mu^2/2} = \frac{\mu^2}{2+\mu^2}$. Max 33.3% for $\mu=1$. (Most power is wasted in the carrier).
        * **Demodulation**: Envelope detector (Diode + RC filter) if $\mu \le 1$. Recovers the envelope $A_c[1+k_a m(t)]$. Requires $B \ll \frac{1}{RC} \ll f_c$.
        """)

# --- Solved Examples Tab ---
with tab2:
    st.header("💡 Solved Examples (Focus on Method & Visualization)")
    st.markdown("Understanding the *how* and *why*, not just the answer.")

    with st.expander("Example: Even/Odd Decomposition & Sketching (PYP 1a-i, ii)"):
        st.markdown(r"Given $x[n]=\sum_{k=-1}^{1}2^{k}\delta[n-k]$[cite: 5]. Sketch $x[n]$ and its even/odd parts[cite: 6].")
        st.markdown("**1. Evaluate $x[n]$:**")
        st.markdown(r"""
        Expand the sum[cite: 5]:
        * $k=-1: 2^{-1} \delta[n-(-1)] = 0.5 \delta[n+1]$
        * $k=0: 2^0 \delta[n-0] = 1 \delta[n]$
        * $k=1: 2^1 \delta[n-1] = 2 \delta[n-1]$
        So, $x[n] = 0.5 \delta[n+1] + \delta[n] + 2 \delta[n-1]$[cite: 5].
        """)
        st.markdown("**2. Sketch $x[n]$:**")
        st.markdown("Plot the non-zero values: Stem of height 0.5 at $n=-1$. Stem of height 1 at $n=0$. Stem of height 2 at $n=1$. Zero elsewhere[cite: 5].")
        # Description: Plot with n on x-axis, x[n] on y-axis. Stems at n=-1 (height 0.5), n=0 (height 1), n=1 (height 2).

        st.markdown("**3. Find $x[-n]$ (Reflection):**")
        st.markdown(r"$x[-n] = 0.5 \delta[-n+1] + \delta[-n] + 2 \delta[-n-1]$")
        st.markdown(r"Using $\delta[-k]=\delta[k]$ and $\delta[-(n-a)] = \delta[n-a]$:")
        st.markdown(r"$x[-n] = 0.5 \delta[n-1] + \delta[n] + 2 \delta[n+1]$.")
        st.markdown("This means: Value 0.5 at $n=1$. Value 1 at $n=0$. Value 2 at $n=-1$. It's the mirror image of $x[n]$ about $n=0$[cite: 6].")

        st.markdown(r"**4. Calculate Even Part $x_e[n] = 0.5 (x[n] + x[-n])$:** [cite: 6]")
        st.markdown(r"""
        * $n=-1: 0.5 (x[-1] + x[1]) = 0.5 (0.5 + 2) = 1.25$
        * $n=0: 0.5 (x[0] + x[0]) = 0.5 (1 + 1) = 1$
        * $n=1: 0.5 (x[1] + x[-1]) = 0.5 (2 + 0.5) = 1.25$
        * Other $n$: $0.5(0+0)=0$.
        * Result: $x_e[n] = 1.25\delta[n+1] + 1\delta[n] + 1.25\delta[n-1]$. **Check: Is it even? Yes.** [cite: 6]
        """)
        # Description: Plot with stems at n=-1 (height 1.25), n=0 (height 1), n=1 (height 1.25). Symmetric.

        st.markdown(r"**5. Calculate Odd Part $x_o[n] = 0.5 (x[n] - x[-n])$:** [cite: 6]")
        st.markdown(r"""
        * $n=-1: 0.5 (x[-1] - x[1]) = 0.5 (0.5 - 2) = -0.75$
        * $n=0: 0.5 (x[0] - x[0]) = 0.5 (1 - 1) = 0$
        * $n=1: 0.5 (x[1] - x[-1]) = 0.5 (2 - 0.5) = 0.75$
        * Other $n$: $0.5(0-0)=0$.
        * Result: $x_o[n] = -0.75\delta[n+1] + 0\delta[n] + 0.75\delta[n-1]$. **Check: Is it odd? Yes.** [cite: 6]
        """)
        # Description: Plot with stems at n=-1 (height -0.75), n=0 (height 0), n=1 (height 0.75). Anti-symmetric.
        st.markdown(r"**Verification:** Does $x_e[n] + x_o[n] = x[n]$? Yes: Check values at n=-1, 0, 1. $(1.25 - 0.75) = 0.5$. $(1 + 0) = 1$. $(1.25 + 0.75) = 2$. Matches $x[n]$[cite: 6].")
        st.markdown(r"**Energy of $x[n]$:** $E_x = \sum |x[n]|^2 = (0.5)^2 + 1^2 + 2^2 = 0.25 + 1 + 4 = 5.25$[cite: 5].")

    with st.expander("Example: DT Signal Operation & Sketching (PYP 1a-iii)"):
         st.markdown(r"Given $x[n]$ above, find and sketch $y[n]=-x[\frac{n-1}{2}]$[cite: 7]. Determine its energy level[cite: 7].")
         st.markdown("**1. Analyze the Argument:** Let $m = \frac{n-1}{2}$. We need $m$ to be an integer index where $x[m]$ is non-zero (i.e., $m = -1, 0, 1$). We also need $n$ to be an integer[cite: 7].")
         st.markdown(r"""
         * If $m = -1$: $\frac{n-1}{2} = -1 \implies n-1 = -2 \implies n = -1$.
         * If $m = 0$: $\frac{n-1}{2} = 0 \implies n-1 = 0 \implies n = 1$.
         * If $m = 1$: $\frac{n-1}{2} = 1 \implies n-1 = 2 \implies n = 3$.
         * *Observation*: This operation involves time expansion (by 2, since $n$ steps by 2 for $m$ to step by 1) and a time shift. Output $y[n]$ is non-zero only for odd values of $n$[cite: 7].
         """)
         st.markdown("**2. Calculate $y[n]$ values:** [cite: 7]")
         st.markdown(r"""
         * For $n=-1$: $y[-1] = -x[\frac{-1-1}{2}] = -x[-1] = -(0.5) = -0.5$.
         * For $n=1$: $y[1] = -x[\frac{1-1}{2}] = -x[0] = -(1) = -1$.
         * For $n=3$: $y[3] = -x[\frac{3-1}{2}] = -x[1] = -(2) = -2$.
         * For all other integer $n$, $\frac{n-1}{2}$ is either non-integer or outside $\{-1, 0, 1\}$, so $x[\dots]=0$ and $y[n]=0$.
         * Result: $y[n] = -0.5\delta[n+1] - 1\delta[n-1] - 2\delta[n-3]$.
         """)
         st.markdown("**3. Sketch $y[n]$:**")
         st.markdown("Plot the non-zero values: Stem of height -0.5 at $n=-1$. Stem of height -1 at $n=1$. Stem of height -2 at $n=3$. Zero elsewhere[cite: 7].")
         # Description: Plot with n on x-axis, y[n] on y-axis. Stems at n=-1 (height -0.5), n=1 (height -1), n=3 (height -2).
         st.markdown(r"**Energy Calculation:** $E_y = \sum |y[n]|^2 = (-0.5)^2 + (-1)^2 + (-2)^2 = 0.25 + 1 + 4 = 5.25$[cite: 7].")

    with st.expander("Example: Graphical Convolution (Lec 1, Slide 109 / Basic Shapes)"):
        st.markdown(r"Sketch $y(t) = \text{rect}(t/2) * \text{rect}(t/2)$[cite: 253].")
        st.markdown(r"**1. Define Signals:** $x(t) = \text{rect}(t/2)$ is 1 for $-1 \le t \le 1$, 0 otherwise[cite: 174]. Let $h(t)=x(t)$[cite: 253].")
        st.markdown(r"**2. Flip:** $h(-\tau)$ is also 1 for $-1 \le \tau \le 1$, 0 otherwise[cite: 255].")
        st.markdown(r"**3. Shift:** $h(t-\tau)$ is 1 for $-1 \le t-\tau \le 1$, which means $t-1 \le \tau \le t+1$. It's a rectangle of width 2, centered at $\tau = t$[cite: 255].")
        st.markdown(r"**4. Visualize Overlap:** We want $y(t) = \int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau$. $x(\tau)$ is fixed (value 1 from $\tau=-1$ to 1). $h(t-\tau)$ is a rectangle (value 1 from $\tau=t-1$ to $t+1$) that slides along the $\tau$ axis as $t$ changes[cite: 255].")
        # Description: Imagine a fixed rectangle centered at 0, and an identical rectangle sliding past it. Calculate the area of their product.
        st.markdown("**5. Identify Regions based on $t$ (where overlap changes):** [cite: 256]")
        st.markdown(r"""
            * **Region 1: No Overlap ($t+1 < -1 \implies t < -2$)**: $h(t-\tau)$ is entirely to the left of $x(\tau)$. Product is zero. Integral = 0. $y(t)=0$.
            * **Region 2: Partial Overlap (Entering, $-1 \le t+1$ and $t-1 < -1 \implies -2 \le t < 0$)**: Right edge of $h(t-\tau)$ is inside $x(\tau)$, left edge is outside. Overlap interval for $\tau$ is $[-1, t+1]$.
                * $y(t) = \int_{-1}^{t+1} (1)(1) d\tau = [\tau]_{-1}^{t+1} = (t+1) - (-1) = t+2$. (Linearly increasing slope +1).
            * **Region 3: Partial Overlap (Leaving, $-1 \le t-1$ and $t+1 \le 1 \implies$ wait, check again. Overlap changes when leading edge $t+1$ passes $1$, or trailing edge $t-1$ passes $-1$). The condition is $t-1 \ge -1$ and $t+1 > 1 \implies 0 \le t < 2$. Overlap interval for $\tau$ is $[t-1, 1]$.
                * $y(t) = \int_{t-1}^{1} (1)(1) d\tau = [\tau]_{t-1}^{1} = 1 - (t-1) = 2-t$. (Linearly decreasing slope -1).
            * **Region 4: No Overlap ($t-1 \ge 1 \implies t \ge 2$)**: $h(t-\tau)$ is entirely to the right of $x(\tau)$. Product is zero. Integral = 0. $y(t)=0$.
            """)
        st.markdown("**6. Combine & Sketch $y(t)$:**")
        st.markdown(r"The result is a **triangle** function: Starts at $t=-2$, rises linearly ($y=t+2$) to height 2 at $t=0$, falls linearly ($y=2-t$) to 0 at $t=2$. Zero elsewhere[cite: 256].")
        st.latex(r"y(t) = (2-|t|) \quad \text{for } -2 \le t \le 2, \text{ and } 0 \text{ otherwise.}")
        st.latex(r"\text{This is } 2 \Lambda(t/2)\text{, if } \Lambda \text{ is standard triangle width 2.}")
        # Description: Plot y(t) vs t. Line from (-2,0) to (0,2). Line from (0,2) to (2,0).
        st.markdown("**Key Takeaway:** Convolving two identical rectangles gives a triangle. Width of result = Sum of widths = $2+2=4$. Peak height = Area of one rect $\times$ Height of other = $2 \times 1 = 2$[cite: 555].")

    with st.expander("Example: Sketching AM Spectrum (PYP Q2b)"):
        st.markdown(r"Given $m_1(t) = 4\cos(100\pi t)$ and $m_2(t) = 400 \text{sinc}(200t)$. AM signal is $z(t) = \{4+m_1(t)\}\cos(2000\pi t) + \{4+m_2(t)\}\cos(2400\pi t)$[cite: 18]. Sketch $Z(f)$[cite: 19]. Determine BW and guard band[cite: 19, 20].")
        st.markdown("**1. Find Spectra of Messages $M(f)$:**")
        st.markdown(r"""
        * $m_1(t) = 4\cos(2\pi \cdot 50 t)$. $f_{m1}=50$ Hz. $M_1(f) = \mathcal{F}\{4\cos(2\pi 50 t)\} = 4 \times \frac{1}{2}[\delta(f-50) + \delta(f+50)] = 2[\delta(f-50) + \delta(f+50)]$. *Two impulses at $\pm 50$ Hz, height 2.* BW = 50 Hz[cite: 17, 18].
        * $m_2(t) = 400 \text{sinc}(200t)$. The problem defines $\text{sinc}(2Wt) = \frac{\sin(2W\pi t)}{2W\pi t}$[cite: 18]. So $m_2(t) = 400 \frac{\sin(200\pi t)}{200\pi t}$. Here $2W=200 \implies W=100$ Hz. The FT pair is $\text{sinc}(2Wt) \leftrightarrow \frac{1}{2W}\text{rect}(\frac{f}{2W})$[cite: 31]. So $M_2(f) = 400 \times \frac{1}{200} \text{rect}(\frac{f}{200}) = 2 \text{rect}(\frac{f}{200})$. *A rectangle from -100 Hz to 100 Hz, height 2.* BW = 100 Hz[cite: 17, 18].
        """)
        st.markdown(r"**2. Analyze First AM Term: $z_1(t)=\{4+m_1(t)\}\cos(2\pi \cdot 1000 t)$:**")
        st.markdown(r"""
        * Carrier $f_{c1}=1000$ Hz. Use modulation property $\mathcal{F}\{x(t)\cos(2\pi f_c t)\} = 0.5[X(f-f_c) + X(f+f_c)]$[cite: 527].
        * FT of $\{4+m_1(t)\} = \mathcal{F}\{4\} + M_1(f) = 4\delta(f) + 2[\delta(f-50) + \delta(f+50)]$.
        * $Z_1(f) = 0.5 \times [ \mathcal{F}\{4+m_1(t)\} \text{ shifted by } \pm 1000 ]$
        * $Z_1(f) = 0.5 \times \{ [4\delta(f-1000) + 2\delta(f-1000-50) + 2\delta(f-1000+50)] + [4\delta(f+1000) + 2\delta(f+1000-50) + 2\delta(f+1000+50)] \}$
        * $Z_1(f) = 2\delta(f-1000) + \delta(f-1050) + \delta(f-950) + 2\delta(f+1000) + \delta(f+950) + \delta(f+1050)$.
        * *Result*: Impulses: height 2 at $\pm 1000$ Hz (Carrier). Height 1 at $\pm 950$ Hz and $\pm 1050$ Hz (Sidebands)[cite: 19].
        """)
        # Description: Plot Z1(f) vs f. Impulses at -1050(1), -1000(2), -950(1), +950(1), +1000(2), +1050(1).

        st.markdown(r"**3. Analyze Second AM Term: $z_2(t)=\{4+m_2(t)\}\cos(2\pi \cdot 1200 t)$:**")
        st.markdown(r"""
        * Carrier $f_{c2}=1200$ Hz.
        * FT of $\{4+m_2(t)\} = \mathcal{F}\{4\} + M_2(f) = 4\delta(f) + 2 \text{rect}(f/200)$.
        * $Z_2(f) = 0.5 \times [ \mathcal{F}\{4+m_2(t)\} \text{ shifted by } \pm 1200 ]$
        * $Z_2(f) = 0.5 \times \{ [4\delta(f-1200) + 2\text{rect}(\frac{f-1200}{200})] + [4\delta(f+1200) + 2\text{rect}(\frac{f+1200}{200})] \}$
        * $Z_2(f) = 2\delta(f-1200) + \text{rect}(\frac{f-1200}{200}) + 2\delta(f+1200) + \text{rect}(\frac{f+1200}{200})$.
        * *Result*: Impulses: height 2 at $\pm 1200$ Hz (Carrier). Rectangles: height 1, width 200 Hz, centered at $\pm 1200$ Hz. (i.e., rectangles from 1100 to 1300 Hz, and -1300 to -1100 Hz)[cite: 19].
        """)
        # Description: Plot Z2(f) vs f. Impulses at -1200(2), +1200(2). Rectangles height 1 from -1300 to -1100 and +1100 to +1300.

        st.markdown(r"**4. Sketch $Z(f) = Z_1(f) + Z_2(f)$:**")
        st.markdown("Combine the components graphically by adding the heights at each frequency. Ensure axes are labeled (f in Hz) and heights/shapes are clear[cite: 19].")
        # Description: Combined plot shows impulses at +/-950(1), +/-1000(2), +/-1050(1), +/-1200(2) and rectangles height 1 from +/-1100 to +/-1300.

        st.markdown("**5. Determine Bandwidth & Guard Band:**")
        st.markdown(r"""
         * Total BW (positive frequencies): Highest freq - Lowest freq = $1300 - 950 = 350$ Hz[cite: 19].
         * Guard Band: Gap between upper edge of first signal (1050 Hz) and lower edge of second signal (1100 Hz). Guard Band = $1100 - 1050 = 50$ Hz[cite: 20].
         """)


# --- Problem-Solving Tips Tab ---
with tab3:
    st.header("🚀 Graphing & Problem-Solving Hacks")
    st.markdown("Focusing on visualization and common question types.")

    with st.expander("🧠 General Strategy"):
        st.markdown(r"""
        1.  **Identify**: Signal type (CT/DT, Periodic/Aperiodic), System type (LTI?), Goal (Find y, h, H, sketch?).
        2.  **Tool**: Time domain (convolution, signal ops), Frequency domain (FS, FT, Laplace/Z), Sampling theory?
        3.  **Sketch First**: Draw the input $x$, impulse response $h$, or spectra $X, H$. Visualize the operation.
        4.  **Formula Sheet**: Find the relevant property or pair. Double-check definitions (e.g., $sinc$, $rect$).
        5.  **Simplify**: Use properties (linearity, shift, convolution theorem) to break down complex problems. Look for symmetry.
        6.  **Label Graphs**: Axes (t/n/f/$\omega$), units (s/Hz/rad/s), key points (amplitudes, times, frequencies, bandwidths).
        7.  **Check Sanity**: Does the result make sense? (e.g., Convolving causal signals $\implies$ causal result. LPF output should have less high-freq content). Units correct?
        """)

    with st.expander("✍️ Sketching Signal Operations"):
         st.markdown(r"""
         * **Baseline**: Know basic shapes: $\delta, u, \text{rect}, \Lambda, \text{sinc}, \cos, e^{-at}$.
         * **Shift $x(t-T)$**: Move the *whole shape* right by $T$ if $T>0$.
         * **Scale $x(at)$**: Point at $t_1$ moves to $t_1/a$. Compresses if $|a|>1$, expands if $|a|<1$.
         * **Reverse $x(-t)$**: Flip graph about the vertical axis ($t=0$).
         * **Scale & Reverse $x(-at)$**: Scale by $|a|$ first, then reverse. Point at $t_1$ moves to $-t_1/a$.
         * **Combined $x(a(t-T))$**: Shift $x(t)$ by $T$ to get $x(t-T)$, *then* scale time axis by $a$. Point $t_1$ in $x(t)$ moves to $T + t_1/a$.
         * **DT Scaling $x[Kn]$**: Only keep points where index $m=Kn$ is an integer multiple of $K$.
         * **DT Expansion $x[n/K]$**: Spread points by factor $K$, insert $K-1$ zeros. Non-zero only if $n$ is multiple of $K$.
         * **Example $x(2t+4)$**: Method 1: $x(2(t+2))$. Shift $x(t)$ left by 2 ($x(t+2)$), then compress time by 2. Method 2: Argument mapping. If $x(\tau)$ is defined for $\tau_{\min} \le \tau \le \tau_{\max}$, then $y(t)=x(2t+4)$ is defined for $\tau_{\min} \le 2t+4 \le \tau_{\max}$. Solve for $t$.
         """)

    with st.expander("↔️ Graphical Convolution (CT: $x(t) * h(t)$)"):
        st.markdown(r"""
        Visualize $y(t) = \int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau$.
        1.  **Pick & Flip**: Choose simpler signal (e.g., $h(\tau)$ if it's symmetric or simpler shape) and sketch $h(-\tau)$ vs $\tau$.
        2.  **Sketch Both**: Draw $x(\tau)$ vs $\tau$ and the flipped $h(-\tau)$ vs $\tau$.
        3.  **Shift**: The term $h(t-\tau)$ is $h(-\tau)$ shifted **right** by $t$. Imagine sliding $h(-\tau)$ along the $\tau$ axis, controlled by the value of $t$.
        4.  **Slide & Identify Regions**: Move the sliding window $h(t-\tau)$ from $t=-\infty$ to $+\infty$. Find critical $t$ values where the **edges** of $x(\tau)$ and $h(t-\tau)$ align. These $t$ values define intervals where the *mathematical form* of the overlap changes (e.g., starts overlapping, fully overlapping, starts disengaging, stops overlapping).
        5.  **Calculate Overlap Integral for each Region**:
            * Determine the $\tau$ interval of overlap for a given $t$ within a region. These are your integration limits w.r.t $\tau$.
            * Multiply the expressions for $x(\tau)$ and $h(t-\tau)$ within that overlap.
            * Integrate the product w.r.t. $\tau$. The result is $y(t)$ for that region of $t$.
        6.  **Combine & Sketch $y(t)$**: Plot the calculated $y(t)$ for each region vs $t$. Check start/end points: $y(t)$ starts when signals first overlap, ends when they last overlap. Duration of $y(t)$ = duration($x$) + duration($h$) (for finite duration signals).
        * **Hack**: Area of $y(t)$ = Area($x$) $\times$ Area($h$). Peak value often related to areas. Rect*Rect=Triangle. Rect*Triangle=Piecewise Parabola.
        * **DT Convolution**: Similar flip-shift-sum process. $y[n] = \sum_m x[m]h[n-m]$. Sum the product over $m$. Regions defined by $n$. Easier to use table method sometimes.
        """)

    with st.expander("📊 Sketching Frequency Spectra ($X(f)$, $H(f)$, $Y(f)$)"):
        st.markdown(r"""
        * **Fourier Series $c_n$**: Plot discrete lines (impulses) at $f = n f_0 = n/T_0$. Height $|c_n|$, Phase $\angle c_n$. Usually decays for large $n$. $c_0$ is DC value. Real $x(t) \implies |c_n|$ even, $\angle c_n$ odd.
        * **Fourier Transform $X(f)$**: Continuous function. Know shapes: $\text{rect}(t/T) \leftrightarrow AT \text{sinc}(fT)$, $\Lambda(t/T) \leftrightarrow B \text{sinc}^2(fT)$, $e^{-at}u(t) \leftrightarrow 1/(a+j2\pi f)$.
        * **Magnitude $|X(f)|$**: Usually largest near $f=0$ for baseband signals. Even function for real $x(t)$. Width related to signal duration (Time-BW tradeoff: short $x(t) \implies$ wide $X(f)$).
        * **Phase $\angle X(f)$**: Odd function for real $x(t)$. Linear phase ($\angle X = -2\pi f t_d$) corresponds to time shift $t_d$.
        * **Using Properties for Sketching**:
            * *Time Shift* $x(t-t_0)$: $|X(f)|$ unchanged, adds linear phase $-2\pi f t_0$.
            * *Modulation* $x(t)\cos(2\pi f_c t)$: Shifts $|X(f)|$ to $\pm f_c$, halves height. Sketch $0.5|X(f-f_c)|$ and $0.5|X(f+f_c)|$.
            * *Filtering* $Y(f)=H(f)X(f)$: Sketch $|H(f)|$ and $|X(f)|$. Multiply heights point-by-point to get $|Y(f)|$. (e.g., Ideal LPF just cuts off $X(f)$ outside passband). Add phases: $\angle Y = \angle H + \angle X$.
        * **AM Spectrum**: Carrier impulses at $\pm f_c$. Sidebands are copies of $M(f)$ centered at $\pm f_c$. $BW = 2 \times BW_{\text{message}}$.
        * **Sampled Spectrum $X_s(f)$**: Replicas of $X(f)$ centered at $n f_s$, scaled by $1/T_s=f_s$. Check for overlap (aliasing) if $f_s < 2 f_M$.
        """)
        # Description: Visualization of Filter Action - H(f) acts as a multiplicative mask on X(f).

    with st.expander("📉 Sampling & Aliasing Visualization"):
        st.markdown(r"""
        1.  **Sketch $X(f)$**: Identify max frequency $f_M$. Determine Nyquist rate $f_N = 2f_M$.
        2.  **Given $f_s$**: Compare $f_s$ to $f_N$.
        3.  **Sketch $X_s(f)$**: Draw $X(f)$ centered at $f=0$. Draw replicas $X(f-f_s)$ centered at $f=f_s$, $X(f+f_s)$ centered at $f=-f_s$, etc. Scale height of *each* replica by $f_s=1/T_s$.
        4.  **Check Overlap**: Do the replicas overlap in the baseband $[-f_s/2, f_s/2]$?
            * If $f_s \ge f_N$: No overlap. Reconstruction LPF (cutoff $f_s/2$) recovers scaled $X(f)$.
            * If $f_s < f_N$: Overlap occurs = **Aliasing**. Parts of replicas centered at $\pm f_s, \pm 2f_s...$ fall into the baseband region $[-f_s/2, f_s/2]$ and add to the original $X(f)$.
        5.  **Finding Aliased Frequency**: A true frequency $f_{\text{orig}}$ appears as $f_{\text{alias}}$ in $[-f_s/2, f_s/2]$ where $f_{\text{alias}} = f_{\text{orig}} - k f_s$ for the integer $k$ that makes $|f_{\text{alias}}| \le f_s/2$.
            * *Graphical Trick*: Draw $f_{\text{orig}}$ on the frequency axis. Find the nearest multiple of $f_s$ (let it be $k f_s$). The aliased frequency is $f_{\text{orig}} - k f_s$. Its magnitude is the distance $|f_{\text{orig}} - k f_s|$.
        """)
        # Description: Visualization of Spectrum Replication - Draw X(f) centered at 0, f_s, -f_s. Show overlap if f_s < 2*f_M.

    with st.expander("🚫 Common Pitfalls & Checks"):
        st.markdown(r"""
        * Mixing $f$ (Hz) and $\omega$ (rad/s). Remember $\omega=2\pi f$ and factors of $2\pi$ in FT pairs/properties/integrals.
        * Incorrect limits in convolution integral. Define regions carefully! Where does overlap start and end in terms of $\tau$?
        * Sign errors in time shifts/phase shifts. Delay ($t-t_0$, $t_0>0$) $\implies$ negative linear phase ($-j\omega t_0$ or $-j2\pi f t_0$).
        * Forgetting the $1/T_s = f_s$ scaling factor in $X_s(f)$.
        * Errors in DT scaling/shifting argument mapping. Write out index relations ($m = an+b$) and solve for integer $n$.
        * Not labeling graph axes and key points clearly.
        * Assuming ideal filters when not specified. Real filters have transition bands.
        * Errors calculating Fourier Series coefficients (check integration limits, $T_0$, $\omega_0$). Using correct form (Trig vs Complex Exp).
        * AM modulation index calculation/interpretation ($\mu > 1$ issue).
        """)