import streamlit as st
import pandas as pd
import numpy as np

# --- App Configuration ---
st.set_page_config(page_title="IE2110 Revision Helper", layout="wide")

st.title(" Signals and Systems Revision Helper 🧠")
st.markdown("""
Welcome! This app helps you revise key concepts, review solved examples, and learn some tips for tackling IE2110 exam questions, based on the provided lecture notes and past paper.
Use the tabs below to navigate through the content.
""")

# --- Main Content Sections ---
tab1, tab2, tab3 = st.tabs(["📘 Revision Notes", "💡 Solved Examples", "🚀 Problem-Solving Tips"])

# --- Revision Notes Tab ---
with tab1:
    st.header("📘 Revision Notes")
    st.markdown("Key concepts and formulas from the lectures, organized by topic.")

    # --- Part 1 Topics ---
    st.subheader("Part 1: Fundamentals, LTI Systems, Convolution (Weeks 1-5)")

    with st.expander("1.1 Signal Classifications"):
        st.markdown("""
        * **CT vs. DT**: Continuous-Time (e.g., $x(t)$) vs. Discrete-Time (e.g., $x[n]$).
        * **Value**: Continuous-Value vs. Discrete-Value (Quantized).
        * **Nature**: Deterministic (formula) vs. Random (probabilistic).
        * **Symmetry**:
            * Even: $x_e(t) = x_e(-t)$ or $x_e[n] = x_e[-n]$.
            * Odd: $x_o(t) = -x_o(-t)$ or $x_o[n] = -x_o[-n]$.
            * Decomposition: $x = x_e + x_o$ where $x_e = \ frac{1}{2}(x(t) + x(-t))$ and $x_o = \ frac{1}{2}(x(t) - x(-t))$ (similar for DT).
        * **Periodicity**: Periodic (repeats over $T_0$ or $K_0$) vs. Aperiodic.
        * **Energy vs. Power**:
            * Energy Signal: $0 < E_x < \infty$, $P_x=0$. Typically aperiodic, finite duration.
            * Power Signal: $0 < P_x < \infty$, $E_x=\infty$. Typically periodic or random.
        * **Formulas**:
        """)
        st.latex("E_x (CT) = \\int_{-\\infty}^{\\infty} |x(t)|^2 dt")
        st.latex("P_x (CT, General) = \\lim_{T\\to\\infty} \\ frac{1}{T} \\int_{-T/2}^{T/2} |x(t)|^2 dt")
        st.latex("P_x (CT, Periodic) = \\ frac{1}{T_0} \\int_{T_0} |x(t)|^2 dt")
        st.latex("E_x (DT) = \\sum_{n=-\\infty}^{\\infty} |x[n]|^2")
        st.latex("P_x (DT, General) = \\lim_{K\\to\\infty} \\ frac{1}{2K+1} \\sum_{n=-K}^{K} |x[n]|^2")
        st.latex("P_x (DT, Periodic) = \\ frac{1}{K_0} \\sum_{n=<K_0>} |x[n]|^2")


    with st.expander("1.2 Elementary & Singularity Signals"):
        st.markdown("""
        * **Elementary**: Exponential ($e^{at}$), Sinusoidal ($A\cos(\omega t+\theta)$), Complex Exponential ($Ae^{j(\omega t+\theta)}$).
        * **Singularity**:
            * Unit Impulse (Dirac Delta): $\delta(t)$ (CT), $\delta[n]$ (DT). Area=1. Sifting: $\int x(t)\delta(t-t_0)dt = x(t_0)$.
            * Unit Step: $u(t)$ (CT), $u[n]$ (DT). Value 1 for $t/n \ge 0$, else 0. $u(t) = \int_{-\infty}^t \delta(\tau)d\tau$.
            * Signum (Sign): $sgn(t) = 2u(t)-1$.
            * Rectangular Pulse: $rect(t/T)$ (CT), $rect[n/K]$ (DT). Value 1 for $|t| \le T/2$ or $|n| \le K/2$.
            * Sinc Function: $sinc(x) = \ frac{\sin(\pi x)}{\pi x}$.
        """)

    with st.expander("1.3 Operations on Signals"):
        st.markdown("""
        * **Amplitude Scaling**: $y = A x$.
        * **Time Shifting**: $y(t) = x(t-T)$ or $y[n] = x[n-K]$. (Delay if $T,K>0$).
        * **Time Scaling (CT)**: $y(t) = x(at)$. Compresses if $|a|>1$, expands if $|a|<1$. Reverses if $a<0$.
        * **Time Scaling (DT)**:
            * Decimation: $y[n]=x[Kn]$ (keeps every K-th sample).
            * Interpolation/Expansion: $y[n]=x[n/K]$ (inserts K-1 zeros between samples if $n/K$ is non-integer, or uses specific interpolation). *Check lecture definition for $x[n/K]$ implementation*.
        """)

    with st.expander("1.4 System Properties"):
        st.markdown("""
        * **Stability (BIBO)**: Bounded Input $\implies$ Bounded Output. LTI: $\int_{-\infty}^{\infty} |h(t)| dt < \infty$ or $\sum_{n=-\infty}^{\infty} |h[n]| < \infty$.
        * **Memory**: Output depends on past/future input. Memoryless: Output depends only on current input. LTI: Memoryless if $h(t)=c\delta(t)$ or $h[n]=c\delta[n]$.
        * **Causality**: Output depends only on present/past input. LTI: $h(t)=0$ for $t<0$ or $h[n]=0$ for $n<0$.
        * **Linearity**: Obeys superposition: $T\{a x_1 + b x_2\} = a T\{x_1\} + b T\{x_2\}$.
        * **Time Invariance**: $T\{x(t-t_0)\} = y(t-t_0)$.
        * **LTI**: Linear AND Time-Invariant. Fully characterized by impulse response $h(t)$ or $h[n]$.
        """)

    with st.expander("2. LTI Systems & Convolution"):
        st.markdown("""
        * **Output**: $y = x * h$.
        """)
        st.markdown("**Convolution Integral (CT)**:")
        st.latex("y(t) = x(t) * h(t) = \\int_{-\\infty}^{\\infty} x(\\tau) h(t-\\tau) d\\tau")
        st.markdown("**Convolution Sum (DT)**:")
        st.latex("y[n] = x[n] * h[n] = \\sum_{m=-\\infty}^{\\infty} x[m] h[n-m]")
        st.markdown("""
        * **Properties**: Commutative ($x*h=h*x$), Distributive ($x*(h_1+h_2)=x*h_1+x*h_2$), Associative ($x*(h_1*h_2)=(x*h_1)*h_2$).
        * **Convolution with Delta**: $x(t) * \delta(t-T_0) = x(t-T_0)$.
        * **Step Response $s$**: Response to unit step $u$. $s(t) = \int_{-\infty}^{t} h(\tau) d\tau$, $h(t) = \ frac{ds(t)}{dt}$. $s[n] = \sum_{m=-\infty}^{n} h[m]$, $h[n]=s[n]-s[n-1]$.
        """)

    with st.expander("2.4 Correlation Functions"):
        st.markdown("""
        * Measures similarity between shifted signals.
        * **Autocorrelation (Energy)**: $R_x(\tau) = x(\tau) * x^*(-\tau) = \int_{-\infty}^{\infty} x(t) x^*(t-\tau) dt$.
        * **Autocorrelation (Power)**: $R_x(\tau) = \lim_{T\to\infty} \ frac{1}{T} \int_{-T/2}^{T/2} x(t) x^*(t-\tau) dt$.
        * **Cross-correlation (Energy)**: $R_{xy}(\tau) = x(\tau) * y^*(-\tau) = \int_{-\infty}^{\infty} x(t) y^*(t-\tau) dt$.
        * **Cross-correlation (Power)**: $R_{xy}(\tau) = \lim_{T\to\infty} \ frac{1}{T} \int_{-T/2}^{T/2} x(t) y^*(t-\tau) dt$.
        * **(DT versions use sums instead of integrals/limits).**
        """)
    st.divider()

    # --- Part 2 Topics ---
    st.subheader("Part 2: Fourier Analysis, Sampling (Weeks 6-11)")

    with st.expander("1. Sinusoids & Phasors"):
        st.markdown("""
        * **Standard Form**: $x(t) = A \cos(2\pi f_0 t + \theta)$ or $A \cos(\omega_0 t + \theta)$. $A>0, f_0 \ge 0, \theta \in [-\pi, \pi]$.
        * Period $T_0 = 1/f_0$. Average Power $P = A^2/2$. RMS $= A/\sqrt{2}$.
        * **Operations**: Time scale $\to$ freq scale; Time shift $\to$ phase shift; Square $\to$ DC + double freq ($A^2 \cos^2(\dots) = A^2/2 + (A^2/2)\cos(2\dots)$).
        * **Adding Sinusoids (Same Freq)**: Use Phasors. $x(t) = \text{Re}\{ \mathbf{X} e^{j\omega_0 t} \}$. Sum $\sum A_k \cos(\omega_0 t + \theta_k) = \text{Re}\{ (\sum A_k e^{j\theta_k}) e^{j\omega_0 t} \}$.
        * **Relation to Complex Exponential**: $A \cos(\omega_0 t + \theta) = \ frac{A}{2}e^{j\theta}e^{j\omega_0 t} + \ frac{A}{2}e^{-j\theta}e^{-j\omega_0 t}$. Sum of two counter-rotating phasors.
        * **Adding Sinusoids (Different Freqs)**: Periodic if $f_1/f_2$ is rational. $f_0 = \text{HCF}(f_1, f_2)$. $T_0 = \text{LCM}(T_1, T_2)$.
        """)

    with st.expander("2. Fourier Series (Periodic Signals)"):
        st.markdown("""
        * **Complex Exponential Form**: $x(t) = \sum_{n=-\infty}^{\infty} c_n e^{j n \omega_0 t}$, where $\omega_0 = 2\pi/T_0$.
        """)
        st.latex("c_n = \\ frac{1}{T_0} \\int_{T_0} x(t) e^{-j n \\omega_0 t} dt")
        st.markdown("""
            * $c_0$ is the DC average value.
            * For real $x(t)$, $c_{-n} = c_n^*$. $|c_n|$ is even, $\angle c_n$ is odd.
        * **Trigonometric Form**: $x(t) = a_0 + \sum_{n=1}^{\infty} [a_n \cos(n \omega_0 t) + b_n \sin(n \omega_0 t)]$.
        """)
        st.latex("a_0 = c_0 = \\ frac{1}{T_0} \\int_{T_0} x(t) dt")
        st.latex("a_n = 2 \\text{Re}\\{c_n\\} = \\ frac{2}{T_0} \\int_{T_0} x(t) \\cos(n \\omega_0 t) dt \\quad (n \\ge 1)")
        st.latex("b_n = -2 \\text{Im}\\{c_n\\} = \\ frac{2}{T_0} \\int_{T_0} x(t) \\sin(n \\omega_0 t) dt \\quad (n \\ge 1)")
        st.markdown("""
        * **Amplitude-Phase Form**: $x(t) = A_0 + \sum_{n=1}^{\infty} A_n \cos(n \omega_0 t + \phi_n)$.
            * $A_0 = c_0$. $A_n = 2|c_n| = \sqrt{a_n^2 + b_n^2}$. $\phi_n = \angle c_n = \text{atan2}(-b_n, a_n)$.
        * **Symmetry**: Helps simplify coefficient calculation (see notes).
        """)
        st.markdown("**Parseval's (Power)**:")
        st.latex("P_x = \\ frac{1}{T_0} \\int_{T_0} |x(t)|^2 dt = \\sum_{n=-\\infty}^{\\infty} |c_n|^2 = A_0^2 + \\ frac{1}{2} \\sum_{n=1}^{\\infty} A_n^2")


    with st.expander("3. Fourier Transform (Aperiodic/Energy Signals)"):
        st.markdown("""
        * **Definition**: (Using $f$)
        """)
        st.latex("X(f) = \\int_{-\\infty}^{\\infty} x(t) e^{-j2\\pi f t} dt")
        st.latex("x(t) = \\int_{-\\infty}^{\\infty} X(f) e^{j2\\pi f t} df")
        st.markdown("""
            (Can use $\omega=2\pi f$ as variable, remember $df = d\omega / (2\pi)$).
        * **Spectrum**: $X(f) = |X(f)| e^{j\angle X(f)}$. $|X(f)|$: Amplitude Spectrum, $\angle X(f)$: Phase Spectrum.
        * **Properties**: See formula sheet. Key ones:
            * Linearity, Time/Freq Shifting, Time/Freq Scaling, Duality.
            * Time Convolution $\Leftrightarrow$ Freq Multiplication: $x_1(t)*x_2(t) \leftrightarrow X_1(f)X_2(f)$.
            * Time Multiplication $\Leftrightarrow$ Freq Convolution: $x_1(t)x_2(t) \leftrightarrow X_1(f)*X_2(f)$.
            * Differentiation: $\ frac{d^n x}{dt^n} \leftrightarrow (j2\pi f)^n X(f)$.
            * Integration: $\int_{-\infty}^{t} x(\\tau)d\\tau \leftrightarrow \\ frac{X(f)}{j2\\pi f} + \\ frac{X(0)}{2}\\delta(f)$.
        * **Common Pairs**: See formula sheet (Rect $\leftrightarrow$ Sinc, Triangle $\leftrightarrow$ Sinc$^2$, Exp Decay $\leftrightarrow 1/(a+j\omega)$, Gaussian $\leftrightarrow$ Gaussian).
        * **Delta Functions**: $\delta(t) \leftrightarrow 1$, $1 \leftrightarrow \delta(f)$, $e^{j2\pi f_0 t} \leftrightarrow \delta(f-f_0)$.
        * **Unit Step**: $u(t) \leftrightarrow \\ frac{1}{j2\\pi f} + \\ frac{1}{2}\\delta(f)$.
        * **Signum**: $sgn(t) \leftrightarrow \\ frac{1}{j\\pi f}$.
        * **Periodic Signals FT**: $\mathcal{F}\{\sum c_n e^{j n \omega_0 t}\} = \sum c_n \delta(f - n f_0)$ (using $f_0 = \omega_0/2\pi$). Consists of impulses at harmonic frequencies, weighted by $c_n$.
        * **Impulse Train**: $\sum_{n=-\infty}^{\infty} \delta(t-nT_0) \leftrightarrow \ frac{1}{T_0} \sum_{n=-\infty}^{\infty} \delta(f - n f_0)$.
        """)
        st.markdown("**Rayleigh's (Energy)**:")
        st.latex("E_x = \\int_{-\\infty}^{\\infty} |x(t)|^2 dt = \\int_{-\\infty}^{\\infty} |X(f)|^2 df")
        st.markdown("$|X(f)|^2$ is Energy Spectral Density (ESD).")


    with st.expander("4. Frequency Domain Analysis of LTI Systems"):
        st.markdown("""
        * **Frequency Response**: $H(f) = \mathcal{F}\{h(t)\}$ (or $H(\omega)$).
        * **Input/Output**: $Y(f) = H(f) X(f)$.
        * **Response to $A\cos(\omega_0 t + \theta)$**: Output is $A|H(\omega_0)|\cos(\omega_0 t + \theta + \angle H(\omega_0))$. Amplitude scaled by $|H|$, phase shifted by $\angle H$.
        * **Distortionless Transmission**: Needs constant amplitude $|H(f)|=K$ and linear phase $\angle H(f) = -\omega t_0 = -2\pi f t_0$ over the signal bandwidth. Output $y(t) = K x(t-t_0)$.
        * **Ideal Filters**: LPF passes $|f| \le B$, HPF passes $|f| \ge B$, etc. Ideal filters have sharp cutoffs, constant passband gain, linear phase, but are non-causal ($h(t)$ is non-zero for $t<0$). Ideal LPF impulse response $h(t) = 2B \text{sinc}(2B(t-t_0))$.
        * **Spectral Density**: Output ESD $\Psi_y(f) = |H(f)|^2 \Psi_x(f)$. Output PSD $S_y(f) = |H(f)|^2 S_x(f)$.
        """)

    with st.expander("5. Sampling & Aliasing"):
        st.markdown("""
        * **Ideal Sampling**: $x_s(t) = x(t) \sum_{n=-\infty}^{\infty} \delta(t-nT_s)$. $T_s$: sampling period, $f_s=1/T_s$: sampling frequency.
        * **Spectrum of Sampled Signal**: $X_s(f) = \ frac{1}{T_s} \sum_{n=-\infty}^{\infty} X(f - n f_s)$. Replicas of $X(f)$ centered at multiples of $f_s$.
        * **Sampling Theorem**: If $x(t)$ is bandlimited to $f_M$ ($X(f)=0$ for $|f|>f_M$), perfect reconstruction is possible if $f_s \ge 2f_M$.
        * **Nyquist Rate**: $f_N = 2f_M$. Minimum $f_s$ to avoid aliasing.
        * **Aliasing**: If $f_s < f_N$, spectral replicas overlap. High frequencies appear as lower frequencies in the baseband $[-f_s/2, f_s/2]$.
        * **Reconstruction**: Use ideal LPF with cutoff $f_s/2$ and gain $T_s$ on $x_s(t)$.
        * **Digital Frequency**: $x[n] = x(nT_s)$. For $x(t)=\cos(2\pi f_0 t)$, $x[n]=\cos(2\pi (f_0/f_s) n) = \cos(\omega_d n)$. $\omega_d = 2\pi f_0 / f_s$ (rad/sample). Range $[-\pi, \pi]$. $f_d = f_0/f_s$ (cycles/sample). Range $[-0.5, 0.5]$.
        """)
    st.divider()

    # --- Part 3 Topics ---
    st.subheader("Part 3: Modulation (Weeks 12-13)")

    with st.expander("1. Modulation Basics"):
        st.markdown("""
        * **Purpose**: Shift signal spectrum to higher frequencies for transmission, multiplexing.
        * **Components**: Message signal $m(t)$, Carrier signal $c(t) = A_c \cos(\omega_c t + \phi_c)$.
        * **Types**: AM (Amplitude), FM (Frequency), PM (Phase).
        """)

    with st.expander("1.2 Amplitude Modulation (Conventional/Full AM)"):
        st.markdown("""
        * **Time Domain**: $x_{AM}(t) = A_c [1 + k_a m(t)] \cos(\omega_c t)$. $k_a$: sensitivity.
        * **Modulation Index**: $\mu = |k_a m(t)|_{max}$. For sinusoidal $m(t)=A_m\cos(\omega_m t)$, $\mu=k_a A_m$.
            * $\mu < 1$: Under-modulation (envelope detector works).
            * $\mu = 1$: Critical modulation.
            * $\mu > 1$: Over-modulation (envelope distortion).
        * **Spectrum**: $X_{AM}(f) = \ frac{A_c}{2}[\delta(f-f_c) + \delta(f+f_c)] + \ frac{A_c k_a}{2}[M(f-f_c) + M(f+f_c)]$. (Using $f_c = \omega_c/2\pi$). Carrier + Upper/Lower Sidebands.
        * **Bandwidth**: $BW_{AM} = 2 B$, where $B$ is bandwidth of $m(t)$. Requires $f_c > B$.
        * **Power**: $P_T = P_c + P_{SB} = \ frac{A_c^2}{2} + \ frac{A_c^2 k_a^2 P_m}{2}$. $P_m$ is power of $m(t)$.
        * **Efficiency (Sinusoidal Mod)**: $\eta = \ frac{P_{SB}}{P_T} = \ frac{\mu^2}{2+\mu^2}$. Max 33.3% at $\mu=1$.
        * **Generation**: [Bias + Message] x Carrier. $(B+m(t)) \times A_c' \cos(\omega_c t)$.
        * **Demodulation (Envelope Detector)**: Diode + RC filter. Recovers envelope $A_c[1+k_a m(t)]$. Requires $1/(RC) \ll \omega_c$ and $1/(RC) \gg \omega_M$ (highest message frequency).
        """)

# --- Solved Examples Tab ---
with tab2:
    st.header("💡 Solved Examples")
    st.markdown("Examples based on lectures and past papers.")

    with st.expander("Example: Even/Odd Decomposition (Lec 1, Slide 28)"):
        st.markdown("Find even/odd parts of $x(t) = \cos(t) + \sin(t) \cos(t)$.")
        st.markdown("**Solution Steps:**")
        st.markdown("1. Find $x(-t)$:")
        st.latex("x(-t) = \cos(-t) + \sin(-t)\cos(-t) = \cos(t) - \sin(t)\cos(t)")
        st.markdown("2. Calculate Even Part:")
        st.latex("x_e(t) = 0.5 [x(t) + x(-t)]")
        st.latex("= 0.5 [ (\cos(t)+\sin(t)\cos(t)) + (\cos(t)-\sin(t)\cos(t)) ]")
        st.latex("= 0.5 [ 2\cos(t) ] = \cos(t)")
        st.markdown("3. Calculate Odd Part:")
        st.latex("x_o(t) = 0.5 [x(t) - x(-t)]")
        st.latex("= 0.5 [ (\cos(t)+\sin(t)\cos(t)) - (\cos(t)-\sin(t)\cos(t)) ]")
        st.latex("= 0.5 [ 2\sin(t)\cos(t) ] = \sin(t)\cos(t)")


    with st.expander("Example: Convolution (Lec 1, Slide 109)"):
        st.markdown("Sketch $y(t) = rect(t/2) * rect(t/2)$.")
        st.markdown("**Solution Approach (Graphical):**")
        st.markdown("""
        1.  $x_1(\tau) = rect(\tau/2)$ is 1 from $\tau=-1$ to 1.
        2.  Flip $x_2(\tau)$ to get $x_2(-\tau)$, which is the same rect.
        3.  Shift by $t$ to get $x_2(t-\tau)$, which is 1 from $\tau=t-1$ to $\tau=t+1$.
        4.  Find the integral of the product $x_1(\tau) x_2(t-\tau)$ vs $t$.
            * No overlap if $|t| > 2 \implies y(t)=0$.
            * Partial/Full overlap for $|t| \le 2$. Calculate area of overlap.
        5.  Result is a **triangular pulse** centered at $t=0$, base from $t=-2$ to $t=2$, peak height = Area of rect = 2.
        """)
        st.latex("y(t) = (2-|t|) \\quad \\text{for } -2 \le t \le 2, \\text{ and } 0 \\text{ otherwise.}")
        st.markdown("This is equivalent to $2 \Lambda(t/2)$ where $\Lambda$ is the standard triangle function from -1 to 1.")


    with st.expander("Example: Fourier Series Coefficients (Lec 2, Slide 37)"):
        st.markdown("Find $c_n$ for a periodic train of rectangular pulses (Amplitude A, duration $\\tau$, period $T_0$).")
        st.latex(r"c_n = \ frac{1}{T_0} \int_{-\tau/2}^{\tau/2} A e^{-j n \omega_0 t} dt \quad (\omega_0 = 2\pi/T_0)")
        st.latex(r"= \ frac{A}{T_0} \left[ \ frac{e^{-j n \omega_0 t}}{-j n \omega_0} \right]_{-\tau/2}^{\tau/2} = \ frac{A}{-j n \omega_0 T_0} (e^{-j n \omega_0 \tau/2} - e^{j n \omega_0 \tau/2})")
        st.latex(r"= \ frac{A}{n \omega_0 T_0} \ frac{e^{j n \omega_0 \tau/2} - e^{-j n \omega_0 \tau/2}}{2j} \times 2 = \ frac{2A}{n \omega_0 T_0} \sin(n \omega_0 \tau/2)")
        st.latex(r"= \ frac{2A}{n (2\pi/T_0) T_0} \sin(n (2\pi/T_0) \tau/2) = \ frac{A}{n\pi} \sin(n \pi \tau / T_0)")
        st.latex(r"= \ frac{A\tau}{T_0} \ frac{\sin(\pi (n \tau / T_0))}{\pi (n \tau / T_0)} = \ frac{A\tau}{T_0} \text{sinc}\left(\ frac{n \tau}{T_0}\right)")
        st.markdown("*Note: Uses $\text{sinc}(x) = \sin(\pi x)/(\pi x)$ definition.*")


    with st.expander("Example: Fourier Transform (Lec 2, Slide 11)"):
        st.markdown("Find $\mathcal{F}\{ A \, rect(t/\tau) \}$.")
        st.latex(r"X(f) = \int_{-\tau/2}^{\tau/2} A e^{-j2\pi f t} dt = A \left[ \ frac{e^{-j2\pi f t}}{-j2\pi f} \right]_{-\tau/2}^{\tau/2}")
        st.latex(r"= \ frac{A}{-j2\pi f} (e^{-j\pi f \tau} - e^{j\pi f \tau}) = \ frac{A}{\pi f} \sin(\pi f \tau)")
        st.latex(r"= A\tau \ frac{\sin(\pi f \tau)}{\pi f \tau} = A\tau \, \text{sinc}(f \tau)")
        st.markdown("*Note: Uses $\text{sinc}(x) = \sin(\pi x)/(\pi x)$ definition.*")


    with st.expander("Example: Aliasing (Lec 2, Slide 33)"):
        st.markdown("Signal $x(t) = 10 \cos(426\pi t)$ ($f_0=213$ Hz). Sampled at $f_s = 200$ Hz. Find the apparent frequency.")
        st.markdown("**Solution:**")
        st.markdown(f"Nyquist rate $f_N = 2 \times 213 = 426$ Hz.")
        st.markdown(f"Since $f_s=200 < f_N$, aliasing occurs.")
        st.markdown("Find the digital signal $x[n]$:")
        st.latex(r"x[n] = 10 \cos(426 \pi n T_s) = 10 \cos(426 \pi n / 200) = 10 \cos(2.13 \times 2\pi n)")
        st.markdown("The digital frequency $f_d = 2.13$ cycles/sample. Since $\cos(\theta) = \cos(\theta \pm 2k\pi)$, we want the equivalent frequency in $[-0.5, 0.5]$.")
        st.latex(r"f_{d, equiv} = f_d \mod 1 = 2.13 \mod 1")
        st.markdown("This notation is a bit loose. More accurately, the frequency $f_0=213$ Hz maps to $f_d = f_0/f_s = 213/200 = 1.065$. The alias in $[-0.5, 0.5]$ is $f_{alias} = f_d - \text{round}(f_d) = 1.065 - 1 = 0.065$. Or, check $|f_0 - k f_s|$ for integer $k$. For $k=1$, $|213 - 1 \times 200| = 13$. For $k=2$, $|213 - 2 \times 200| = |-187|=187$. The lowest frequency is $13$ Hz.")
        st.markdown("Alternatively, using $\omega_d = 2.13 \times 2\pi$ rad/sample.")
        st.latex(r"\omega_{d, equiv} = \omega_d \mod 2\pi = 4.26\pi \mod 2\pi = 0.26\pi ")
        st.markdown("This is incorrect calculation above. Let's stick to the $f_d$ or the $f_0 - k f_s$ method.")
        st.markdown("The alias frequency $f_a$ satisfies $|f_a| < f_s/2 = 100$ Hz and $f_a = f_0 - k f_s$ for some integer $k$.")
        st.markdown("$k=1 \implies f_a = 213 - 1(200) = 13$ Hz. Since $|13| < 100$, this is the alias.")
        st.markdown("The 213 Hz signal appears as a 13 Hz signal after sampling and reconstruction.")

    with st.expander("Example: AM Spectrum (PYP Q2b)"):
        st.markdown("Given $m_1(t) = 4\cos(100\pi t)$ and $m_2(t) = 400 \text{sinc}(200t)$. AM signal is $z(t) = \{4+m_1(t)\}\cos(2000\pi t) + \{4+m_2(t)\}\cos(2400\pi t)$. Sketch $Z(f)$.")
        st.markdown("**Solution Approach:**")
        st.markdown("""
        1.  **Find spectra of messages:**
            * $m_1(t)$: Freq $f_{m1} = 50$ Hz. $M_1(f) = 2[\delta(f-50) + \delta(f+50)]$. BW = 50 Hz.
            * $m_2(t) = 400 \ frac{\sin(200\pi t)}{\pi (200t)} \times \pi = 2 \times \ frac{\sin(\pi (200) t)}{\pi t}$. Wait, the Q definition is $sinc(2Wt)=\ frac{sin(2W\pi t)}{2W\pi t}$. So $m_2(t) = 400 \ frac{\sin(200\pi t)}{200\pi t} = 400 \text{sinc}(200t)$. Let $2W=200 \implies W=100$ Hz. $\mathcal{F}\{sinc(2Wt)\} = \ frac{1}{2W}rect(\ frac{f}{2W})$. So $M_2(f) = 400 \times \ frac{1}{200} rect(\ frac{f}{200}) = 2 rect(\ frac{f}{200})$. BW = 100 Hz.
        2.  **Analyze first AM term:** Carrier $f_{c1}=1000$ Hz. Term is $(4+m_1(t))\cos(\omega_{c1} t)$.
            * Carrier component from '4': $\ frac{4}{2}[\delta(f\pm 1000)] = 2[\delta(f\pm 1000)]$.
            * Sidebands from $m_1(t)$: $\ frac{1}{2} M_1(f\pm 1000) = \ frac{1}{2} \times 2[\delta(f\pm 1000 - 50) + \delta(f\pm 1000 + 50)]$. Gives impulses of height 1 at $\pm 950$ Hz and $\pm 1050$ Hz.
        3.  **Analyze second AM term:** Carrier $f_{c2}=1200$ Hz. Term is $(4+m_2(t))\cos(\omega_{c2} t)$.
            * Carrier component from '4': $2[\delta(f\pm 1200)]$.
            * Sidebands from $m_2(t)$: $\ frac{1}{2} M_2(f\pm 1200) = \ frac{1}{2} \times 2 rect(\ frac{f\pm 1200}{200}) = rect(\ frac{f\pm 1200}{200})$. Rectangular pulses of height 1, centered at $\pm 1200$ Hz, width 200 Hz (from 1100 to 1300 Hz and -1300 to -1100 Hz).
        4.  **Sketch Z(f):** Sum the components graphically. Plot impulses and rectangles at the calculated frequencies and heights.
        5.  **Total BW:** The overall signal occupies the frequency range from 950 Hz to 1300 Hz (on the positive side). The bandwidth is typically defined as the difference between the highest and lowest positive frequencies occupied: $BW = 1300 - 950 = 350$ Hz.
        6.  **Guard Band:** Frequency gap between first signal's upper edge (1050 Hz) and second signal's lower edge (1100 Hz). Guard Band = $1100 - 1050 = 50$ Hz.
        """)


# --- Problem-Solving Tips Tab ---
with tab3:
    st.header("🚀 Problem-Solving Tips & Hacks")

    with st.expander("General Approach"):
        st.markdown("""
        * **Classify**: CT/DT? Periodic/Aperiodic? LTI system? Causal? Stable? $\implies$ Guides tool choice.
        * **Goal**: Analyze signal properties? Find system response $h(t)$ or $H(f)$? Calculate output $y(t)$?
        * **Formula Sheet**: Use it effectively. Understand the conditions for each formula. Check definitions (e.g., different $sinc$ forms).
        * **Sketch**: Always helpful! Input signals, impulse responses, frequency spectra. Visualize convolution overlap, filter action, spectral shifts.
        * **Units**: Keep track of Hz vs rad/s ($ \omega = 2\pi f $). Ensure consistency.
        * **Symmetry**: Look for even/odd signal or system properties to simplify integrals/sums.
        """)

    with st.expander("Tips for Specific Topics"):
        st.markdown("""
        * **DT Signal Operations**: Time scaling like $x[n/2]$ (expansion) or $x[2n]$ (compression/decimation) needs careful handling of indices. Write out terms if unsure. $x[(n-1)/2]$ involves both shift and scaling.
        * **Convolution**: Graphical method: Flip, shift, multiply, integrate/sum. Define overlap regions carefully. Frequency domain method ($Y=HX$): Use FT tables/properties. Often easier if FTs are simple. Remember to IFT if $y(t)$ is needed.
        * **Fourier Series**: For periodic signals. Calculate $c_n$ using the integral definition. Symmetry simplifies things. Convert between forms ($A_n = 2|c_n|$, $a_n=2Re\{c_n\}$, etc.) as needed.
        * **Fourier Transform**: For aperiodic signals. Use tables and properties (linearity, shift, modulation, convolution theorems) extensively.
        * **Filtering**: $Y(f)=H(f)X(f)$. Draw the spectra $|X(f)|$ and $|H(f)|$. The output spectrum is the product. For ideal filters, $H(f)$ just 'cuts out' parts of $X(f)$. Distortion occurs if $H(f)$ is not flat amplitude and linear phase over the input signal's band.
        * **AM**: Spectrum has carrier spikes at $\pm f_c$ and sidebands $M(f)$ shifted to $\pm f_c$. $BW_{AM} = 2 \times BW_{message}$. FDM places different AM signals in adjacent frequency slots - check for guard bands.
        * **Sampling**: 1. Find signal bandwidth $f_M$. 2. Find Nyquist rate $f_N = 2f_M$. 3. Compare sampling rate $f_s$ with $f_N$. 4. If $f_s < f_N$, aliasing occurs. Find the aliased frequency $f_a$ such that $f_a = |f_{original} - k f_s|$ and $|f_a| < f_s/2$.
        """)

    with st.expander("Exam Strategy"):
        st.markdown("""
        * **Time Allocation**: Check marks per question/part. Budget time accordingly. Don't get stuck.
        * **Show Work**: Method marks are valuable. Write down formulas used, intermediate steps.
        * **Check Answers**: Does the result make sense? Units correct? Signs correct? Simple calculation errors?
        * **Keywords**: "Sketch" (needs labeled axes, key points), "Determine/Find" (numerical answer/expression needed), "Explain/Justify" (refer to definitions, theorems, properties).
        * **Closed Book**: Master the use of the provided formula sheet.
        """)