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
            * Decomposition: $x = x_e + x_o$ where $x_e = \frac{1}{2}(x + x_{reflected})$, $x_o = \frac{1}{2}(x - x_{reflected})$.
        * **Periodicity**: Periodic (repeats over $T_0$ or $K_0$) vs. Aperiodic.
        * **Energy vs. Power**:
            * Energy Signal: $0 < E_x < \infty$, $P_x=0$. Typically aperiodic, finite duration.
            * Power Signal: $0 < P_x < \infty$, $E_x=\infty$. Typically periodic or random.
        * **Formulas**:
            * Energy (CT): $E_x = \int_{-\infty}^{\infty} |x(t)|^2 dt$
            * Power (CT, General): $P_x = \lim_{T\to\infty} \frac{1}{T} \int_{-T/2}^{T/2} |x(t)|^2 dt$
            * Power (CT, Periodic): $P_x = \frac{1}{T_0} \int_{T_0} |x(t)|^2 dt$
            * Energy (DT): $E_x = \sum_{n=-\infty}^{\infty} |x[n]|^2$
            * Power (DT, General): $P_x = \lim_{K\to\infty} \frac{1}{2K+1} \sum_{n=-K}^{K} |x[n]|^2$
            * Power (DT, Periodic): $P_x = \frac{1}{K_0} \sum_{n=<K_0>} |x[n]|^2$
        """)

    with st.expander("1.2 Elementary & Singularity Signals"):
        st.markdown("""
        * **Elementary**: Exponential ($e^{at}$), Sinusoidal ($A\cos(\omega t+\theta)$), Complex Exponential ($Ae^{j(\omega t+\theta)}$).
        * **Singularity**:
            * Unit Impulse (Dirac Delta): $\delta(t)$ (CT), $\delta[n]$ (DT). Area=1. Sifting: $\int x(t)\delta(t-t_0)dt = x(t_0)$.
            * Unit Step: $u(t)$ (CT), $u[n]$ (DT). Value 1 for $t/n \ge 0$, else 0. $u(t) = \int_{-\infty}^t \delta(\tau)d\tau$.
            * Signum (Sign): $sgn(t) = 2u(t)-1$.
            * Rectangular Pulse: $rect(t/T)$ (CT), $rect[n/K]$ (DT). Value 1 for $|t| \le T/2$ or $|n| \le K/2$.
            * Sinc Function: $sinc(x) = \frac{\sin(\pi x)}{\pi x}$.
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
        * **Stability (BIBO)**: Bounded Input $\implies$ Bounded Output. LTI: $\int |h(t)| dt < \infty$ or $\sum |h[n]| < \infty$.
        * **Memory**: Output depends on past/future input. Memoryless: Output depends only on current input. LTI: Memoryless if $h(t)=c\delta(t)$ or $h[n]=c\delta[n]$.
        * **Causality**: Output depends only on present/past input. LTI: $h(t)=0$ for $t<0$ or $h[n]=0$ for $n<0$.
        * **Linearity**: Obeys superposition: $T\{a x_1 + b x_2\} = a T\{x_1\} + b T\{x_2\}$.
        * **Time Invariance**: $T\{x(t-t_0)\} = y(t-t_0)$.
        * **LTI**: Linear AND Time-Invariant. Fully characterized by impulse response $h(t)$ or $h[n]$.
        """)

    with st.expander("2. LTI Systems & Convolution"):
        st.markdown("""
        * **Output**: $y = x * h$.
        * **Convolution Integral (CT)**: $y(t) = \int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau$.
        * **Convolution Sum (DT)**: $y[n] = \sum_{m=-\infty}^{\infty} x[m] h[n-m]$.
        * **Properties**: Commutative ($x*h=h*x$), Distributive ($x*(h_1+h_2)=x*h_1+x*h_2$), Associative ($x*(h_1*h_2)=(x*h_1)*h_2$).
        * **Convolution with Delta**: $x(t) * \delta(t-T_0) = x(t-T_0)$.
        * **Step Response $s$**: Response to unit step $u$. $s(t) = \int_{-\infty}^{t} h(\tau) d\tau$, $h(t) = \frac{ds(t)}{dt}$. $s[n] = \sum_{m=-\infty}^{n} h[m]$, $h[n]=s[n]-s[n-1]$.
        """)

    with st.expander("2.4 Correlation Functions"):
        st.markdown("""
        * Measures similarity between shifted signals.
        * **Autocorrelation (Energy)**: $R_x(\tau) = x(\tau) * x^*(-\tau) = \int x(t) x^*(t-\tau) dt$.
        * **Autocorrelation (Power)**: $R_x(\tau) = \lim_{T\to\infty} \frac{1}{T} \int_{-T/2}^{T/2} x(t) x^*(t-\tau) dt$.
        * **Cross-correlation (Energy)**: $R_{xy}(\tau) = x(\tau) * y^*(-\tau) = \int x(t) y^*(t-\tau) dt$.
        * **Cross-correlation (Power)**: $R_{xy}(\tau) = \lim_{T\to\infty} \frac{1}{T} \int_{-T/2}^{T/2} x(t) y^*(t-\tau) dt$.
        * **(DT versions use sums instead of integrals/limits).**
        """)
    st.divider()

    # --- Part 2 Topics ---
    st.subheader("Part 2: Fourier Analysis, Sampling (Weeks 6-11)")

    with st.expander("1. Sinusoids & Phasors"):
        st.markdown("""
        * **Standard Form**: $x(t) = A \cos(2\pi f_0 t + \theta)$ or $A \cos(\omega_0 t + \theta)$. $A>0, f_0 \ge 0, \theta \in [-\pi, \pi]$.
        * Period $T_0 = 1/f_0$. Average Power $P = A^2/2$. RMS $= A/\sqrt{2}$.
        * **Operations**: Time scale $\to$ freq scale; Time shift $\to$ phase shift; Square $\to$ DC + double freq.
        * **Adding Sinusoids (Same Freq)**: Use Phasors. $x(t) = \text{Re}\{ \mathbf{X} e^{j\omega_0 t} \}$. Sum $\sum A_k \cos(\omega_0 t + \theta_k) = \text{Re}\{ (\sum A_k e^{j\theta_k}) e^{j\omega_0 t} \}$.
        * **Relation to Complex Exponential**: $A \cos(\omega_0 t + \theta) = \frac{A}{2}e^{j\theta}e^{j\omega_0 t} + \frac{A}{2}e^{-j\theta}e^{-j\omega_0 t}$. Sum of two counter-rotating phasors.
        * **Adding Sinusoids (Different Freqs)**: Periodic if $f_1/f_2$ is rational. $f_0 = \text{HCF}(f_1, f_2)$. $T_0 = \text{LCM}(T_1, T_2)$.
        """)

    with st.expander("2. Fourier Series (Periodic Signals)"):
        st.markdown("""
        * **Complex Exponential Form**: $x(t) = \sum_{n=-\infty}^{\infty} c_n e^{j n \omega_0 t}$, where $\omega_0 = 2\pi/T_0$.
            * $c_n = \frac{1}{T_0} \int_{T_0} x(t) e^{-j n \omega_0 t} dt$.
            * $c_0$ is the DC average value.
            * For real $x(t)$, $c_{-n} = c_n^*$. $|c_n|$ is even, $\angle c_n$ is odd.
        * **Trigonometric Form**: $x(t) = a_0 + \sum_{n=1}^{\infty} [a_n \cos(n \omega_0 t) + b_n \sin(n \omega_0 t)]$.
            * $a_0 = c_0$.
            * $a_n = 2 \text{Re}\{c_n\} = \frac{2}{T_0} \int_{T_0} x(t) \cos(n \omega_0 t) dt$ for $n \ge 1$.
            * $b_n = -2 \text{Im}\{c_n\} = \frac{2}{T_0} \int_{T_0} x(t) \sin(n \omega_0 t) dt$ for $n \ge 1$.
        * **Amplitude-Phase Form**: $x(t) = A_0 + \sum_{n=1}^{\infty} A_n \cos(n \omega_0 t + \phi_n)$.
            * $A_0 = c_0$. $A_n = 2|c_n| = \sqrt{a_n^2 + b_n^2}$. $\phi_n = \angle c_n = \text{atan2}(-b_n, a_n)$.
        * **Symmetry**: Helps simplify coefficient calculation (see notes).
        * **Parseval's (Power)**: $P_x = \sum_{n=-\infty}^{\infty} |c_n|^2 = A_0^2 + \frac{1}{2} \sum_{n=1}^{\infty} A_n^2$.
        """)

    with st.expander("3. Fourier Transform (Aperiodic/Energy Signals)"):
        st.markdown("""
        * **Definition**: $X(f) = \int_{-\infty}^{\infty} x(t) e^{-j2\pi f t} dt$, $x(t) = \int_{-\infty}^{\infty} X(f) e^{j2\pi f t} df$. (Can use $\omega=2\pi f$ as variable).
        * **Spectrum**: $X(f) = |X(f)| e^{j\angle X(f)}$. $|X(f)|$: Amplitude Spectrum, $\angle X(f)$: Phase Spectrum.
        * **Properties**: See formula sheet. Key ones:
            * Linearity, Time/Freq Shifting, Time/Freq Scaling, Duality.
            * Time Convolution $\Leftrightarrow$ Freq Multiplication: $x_1(t)*x_2(t) \leftrightarrow X_1(f)X_2(f)$.
            * Time Multiplication $\Leftrightarrow$ Freq Convolution: $x_1(t)x_2(t) \leftrightarrow X_1(f)*X_2(f)$.
            * Differentiation: $\frac{dx}{dt} \leftrightarrow j2\pi f X(f)$.
        * **Common Pairs**: See formula sheet (Rect $\leftrightarrow$ Sinc, Triangle $\leftrightarrow$ Sinc$^2$, Exp Decay $\leftrightarrow 1/(a+j\omega)$, Gaussian $\leftrightarrow$ Gaussian).
        * **Delta Functions**: $\delta(t) \leftrightarrow 1$, $1 \leftrightarrow \delta(f)$, $\cos(\omega_0 t) \leftrightarrow \pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$.
        * **Periodic Signals FT**: $\mathcal{F}\{\sum c_n e^{j n \omega_0 t}\} = \sum 2\pi c_n \delta(\omega - n\omega_0)$. Consists of impulses at harmonic frequencies, weighted by $2\pi c_n$.
        * **Rayleigh's (Energy)**: $E_x = \int |x(t)|^2 dt = \int |X(f)|^2 df = \frac{1}{2\pi} \int |X(\omega)|^2 d\omega$. $|X(f)|^2$ is Energy Spectral Density (ESD).
        """)

    with st.expander("4. Frequency Domain Analysis of LTI Systems"):
        st.markdown("""
        * **Frequency Response**: $H(f) = \mathcal{F}\{h(t)\}$ (or $H(\omega)$).
        * **Input/Output**: $Y(f) = H(f) X(f)$.
        * **Response to $A\cos(\omega_0 t + \theta)$**: Output is $A|H(\omega_0)|\cos(\omega_0 t + \theta + \angle H(\omega_0))$. Amplitude scaled by $|H|$, phase shifted by $\angle H$.
        * **Distortionless Transmission**: Needs constant amplitude $|H|=K$ and linear phase $\angle H = -\omega t_0$ over the signal bandwidth. Output $y(t) = K x(t-t_0)$.
        * **Ideal Filters**: LPF passes $|f| \le B$, HPF passes $|f| \ge B$, etc. Ideal filters have sharp cutoffs, constant passband gain, linear phase, but are non-causal ($h(t)$ is non-zero for $t<0$).
        * **Spectral Density**: Output ESD $\Psi_y(f) = |H(f)|^2 \Psi_x(f)$. Output PSD $S_y(f) = |H(f)|^2 S_x(f)$.
        """)

    with st.expander("5. Sampling & Aliasing"):
        st.markdown("""
        * **Ideal Sampling**: $x_s(t) = x(t) \sum \delta(t-nT_s)$. $T_s$: sampling period, $f_s=1/T_s$: sampling frequency.
        * **Spectrum of Sampled Signal**: $X_s(f) = \frac{1}{T_s} \sum_{n=-\infty}^{\infty} X(f - n f_s)$. Replicas of $X(f)$ centered at multiples of $f_s$.
        * **Sampling Theorem**: If $x(t)$ is bandlimited to $f_M$ ($X(f)=0$ for $|f|>f_M$), perfect reconstruction is possible if $f_s \ge 2f_M$.
        * **Nyquist Rate**: $f_N = 2f_M$. Minimum $f_s$ to avoid aliasing.
        * **Aliasing**: If $f_s < f_N$, spectral replicas overlap. High frequencies appear as lower frequencies in the baseband $[-f_s/2, f_s/2]$.
        * **Reconstruction**: Use ideal LPF with cutoff $f_s/2$ and gain $T_s$ on $x_s(t)$.
        * **Digital Frequency**: $x[n] = x(nT_s)$. For $x(t)=\cos(2\pi f_0 t)$, $x[n]=\cos(2\pi (f_0/f_s) n) = \cos(\omega_d n)$. $\omega_d = 2\pi f_0 / f_s$ (rad/sample). Range $[-\pi, \pi]$.
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
        * **Spectrum**: $X_{AM}(f) = \frac{A_c}{2}[\delta(f\pm f_c)] + \frac{A_c k_a}{2}[M(f\pm f_c)]$. (Using $f_c = \omega_c/2\pi$). Carrier + Upper/Lower Sidebands.
        * **Bandwidth**: $BW_{AM} = 2 B$, where $B$ is bandwidth of $m(t)$.
        * **Power**: $P_T = P_c + P_{SB} = \frac{A_c^2}{2} + \frac{A_c^2 k_a^2 P_m}{2}$. $P_m$ is power of $m(t)$.
        * **Efficiency (Sinusoidal Mod)**: $\eta = \frac{P_{SB}}{P_T} = \frac{\mu^2}{2+\mu^2}$. Max 33.3% at $\mu=1$.
        * **Generation**: [Bias + Message] x Carrier. $(B+m(t)) \times A_c' \cos(\omega_c t)$.
        * **Demodulation (Envelope Detector)**: Diode + RC filter. Recovers envelope $A_c[1+k_a m(t)]$. Requires $1/(RC) \ll \omega_c$ and $1/(RC) \gg \omega_M$.
        """)

# --- Solved Examples Tab ---
with tab2:
    st.header("💡 Solved Examples")
    st.markdown("Examples based on lectures and past papers.")

    with st.expander("Example: Even/Odd Decomposition (Lec 1, Slide 28)"):
        st.markdown("Find even/odd parts of $x(t) = \cos(t) + \sin(t) \cos(t)$.")
        st.markdown("**Solution Steps:**")
        st.code("""
1. Find x(-t):
   x(-t) = cos(-t) + sin(-t)cos(-t) = cos(t) - sin(t)cos(t)
2. Calculate Even Part:
   x_e(t) = 0.5 * [x(t) + x(-t)]
          = 0.5 * [ (cos(t)+sin(t)cos(t)) + (cos(t)-sin(t)cos(t)) ]
          = 0.5 * [ 2cos(t) ] = cos(t)
3. Calculate Odd Part:
   x_o(t) = 0.5 * [x(t) - x(-t)]
          = 0.5 * [ (cos(t)+sin(t)cos(t)) - (cos(t)-sin(t)cos(t)) ]
          = 0.5 * [ 2sin(t)cos(t) ] = sin(t)cos(t)""", language="text")

    with st.expander("Example: Convolution (Lec 1, Slide 109)"):
        st.markdown("Sketch $y(t) = rect(t/2) * rect(t/2)$.")
        st.markdown("**Solution Approach (Graphical):**")
        st.markdown("""
        1.  $x_1(\tau) = rect(\tau/2)$ is 1 from $\tau=-1$ to 1.
        2.  Flip $x_2(\tau)$ to get $x_2(-\tau)$, which is the same rect.
        3.  Shift by $t$ to get $x_2(t-\tau)$, which is 1 from $\tau=t-1$ to $\tau=t+1$.
        4.  Find the integral of the product $x_1(\tau) x_2(t-\tau)$ vs $t$.
            * No overlap if $|t| > 2 \implies y(t)=0$.
            * Partial/Full overlap for $|t| \le 2$.
        5.  Result is a **triangular pulse** centered at $t=0$, starting at $t=-2$, peaking at $t=0$ (height = Area of rect = 2), ending at $t=2$. Mathematically: $y(t) = (2 - |t|) rect(t/4)$. Or scaled $\Lambda(t/2)$.
        """)

    with st.expander("Example: Fourier Series Coefficients (Lec 2, Slide 37)"):
        st.markdown("Find $c_n$ for a periodic train of rectangular pulses (Amplitude A, duration $\\tau$, period $T_0$).")
        st.latex(r"c_n = \frac{1}{T_0} \int_{-\tau/2}^{\tau/2} A e^{-j n \omega_0 t} dt \quad (\omega_0 = 2\pi/T_0)")
        st.latex(r"= \frac{A}{T_0} \left[ \frac{e^{-j n \omega_0 t}}{-j n \omega_0} \right]_{-\tau/2}^{\tau/2} = \frac{A}{-j n \omega_0 T_0} (e^{-j n \omega_0 \tau/2} - e^{j n \omega_0 \tau/2})")
        st.latex(r"= \frac{A}{n \omega_0 T_0} \frac{e^{j n \omega_0 \tau/2} - e^{-j n \omega_0 \tau/2}}{2j} \times 2 = \frac{2A}{n \omega_0 T_0} \sin(n \omega_0 \tau/2)")
        st.latex(r"= \frac{2A}{n (2\pi/T_0) T_0} \sin(n (2\pi/T_0) \tau/2) = \frac{A}{n\pi} \sin(n \pi \tau / T_0)")
        st.latex(r"= \frac{A\tau}{T_0} \frac{\sin(n \pi \tau / T_0)}{n \pi \tau / T_0} = \frac{A\tau}{T_0} \text{sinc}\left(\frac{n \tau}{T_0}\right)")
        st.markdown("*Note: Uses $\text{sinc}(x) = \sin(\pi x)/(\pi x)$ definition.*")

    with st.expander("Example: Fourier Transform (Lec 2, Slide 11)"):
        st.markdown("Find $\mathcal{F}\{ A \, rect(t/\tau) \}$.")
        st.latex(r"X(f) = \int_{-\tau/2}^{\tau/2} A e^{-j2\pi f t} dt = A \left[ \frac{e^{-j2\pi f t}}{-j2\pi f} \right]_{-\tau/2}^{\tau/2}")
        st.latex(r"= \frac{A}{-j2\pi f} (e^{-j\pi f \tau} - e^{j\pi f \tau}) = \frac{A}{\pi f} \sin(\pi f \tau)")
        st.latex(r"= A\tau \frac{\sin(\pi f \tau)}{\pi f \tau} = A\tau \, \text{sinc}(f \tau)")
        st.markdown("*Note: Uses $\text{sinc}(x) = \sin(\pi x)/(\pi x)$ definition.*")

    with st.expander("Example: Aliasing (Lec 2, Slide 33)"):
        st.markdown("Signal $x(t) = 10 \cos(426\pi t)$ ($f_0=213$ Hz). Sampled at $f_s = 200$ Hz. Find the apparent frequency.")
        st.markdown("**Solution:**")
        st.markdown(f"Nyquist rate $f_N = 2 \times 213 = 426$ Hz.")
        st.markdown(f"Since $f_s=200 < f_N$, aliasing occurs.")
        st.latex(r"x[n] = 10 \cos(426 \pi n T_s) = 10 \cos(426 \pi n / 200) = 10 \cos(2.13 \pi n)")
        st.latex(r"= 10 \cos( (2 + 0.13) \pi n ) = 10 \cos(2\pi n + 0.13 \pi n)")
        st.latex(r"= 10 \cos(0.13 \pi n) = 10 \cos(2 \pi (0.065) n)")
        st.markdown("The discrete frequency is $\omega_d = 0.13\pi$ rad/sample, or $f_d = 0.065$ cycles/sample.")
        st.markdown("Apparent analog frequency $f_a = f_d \times f_s = 0.065 \times 200 = 13$ Hz.")
        st.markdown("The 213 Hz signal appears as a 13 Hz signal after sampling and reconstruction.")

    with st.expander("Example: AM Spectrum (PYP Q2b)"):
        st.markdown("Given $m_1(t) = 4\cos(100\pi t)$ and $m_2(t) = 400 \text{sinc}(200t)$. AM signal is $z(t) = \{4+m_1(t)\}\cos(2000\pi t) + \{4+m_2(t)\}\cos(2400\pi t)$. Sketch $Z(f)$.")
        st.markdown("**Solution Approach:**")
        st.markdown("""
        1.  **Find spectra of messages:**
            * $m_1(t)$: Freq $f_{m1} = 100\pi/(2\pi) = 50$ Hz. $M_1(f) = 2[\delta(f-50) + \delta(f+50)]$. BW = 50 Hz.
            * $m_2(t) = 400 \frac{\sin(200\pi t)}{200\pi t}$. This fits $sinc(2Wt)$ form with $2W = 200 \implies W=100$ Hz. $M_2(f) = \frac{400}{2W} rect(\frac{f}{2W}) = \frac{400}{200} rect(\frac{f}{200}) = 2 rect(\frac{f}{200})$. BW = 100 Hz.
        2.  **Analyze first AM term:** Carrier $f_{c1}=1000$ Hz.
            * Carrier component: $4/2[\delta(f\pm 1000)] = 2[\delta(f\pm 1000)]$.
            * Sidebands: $\frac{1}{2} M_1(f\pm 1000) = [\delta(f-1000\pm 50) + \delta(f+1000\pm 50)]$. Impulses at $\pm 950$ Hz and $\pm 1050$ Hz, amplitude 1.
        3.  **Analyze second AM term:** Carrier $f_{c2}=1200$ Hz.
            * Carrier component: $2[\delta(f\pm 1200)]$.
            * Sidebands: $\frac{1}{2} M_2(f\pm 1200) = rect(\frac{f\pm 1200}{200})$. Rectangular pulses of height 1, centered at $\pm 1200$ Hz, width 200 Hz (from 1100 to 1300 Hz and -1300 to -1100 Hz).
        4.  **Sketch Z(f):** Sum the components. Draw impulses at $\pm 950, \pm 1000, \pm 1050, \pm 1200$ Hz. Draw rectangles from $\pm 1100$ to $\pm 1300$ Hz.
        5.  **Total BW:** Highest freq = 1300 Hz. BW = 1300 Hz (assuming baseband). Or Passband BW = $1300-950 = 350$ Hz? *Check typical definition - usually max freq - min freq for positive frequencies.* BW = $1300 - (-1300) = 2600$ Hz if double-sided, or max positive freq is 1300 Hz. The signal occupies $[950, 1050]$ and $[1100, 1300]$. Max freq is 1300 Hz.
        6.  **Guard Band:** Frequency gap between first signal's upper edge (1050 Hz) and second signal's lower edge (1100 Hz). Guard Band = $1100 - 1050 = 50$ Hz.
        """)

# --- Problem-Solving Tips Tab ---
with tab3:
    st.header("🚀 Problem-Solving Tips & Hacks")

    with st.expander("General Approach"):
        st.markdown("""
        * **Classify**: CT/DT? Periodic/Aperiodic? LTI system? Causal? Stable? $\implies$ Tools to use.
        * **Goal**: Analyze signal? Analyze system? Find output?
        * **Formula Sheet**: Use it! Know where things are. Check definitions (e.g., sinc).
        * **Sketch**: Signals, impulse responses, spectra. Helps visualize convolution, filtering, modulation.
        * **Units**: Hz vs rad/s? Check factors of $2\pi$.
        * **Symmetry**: Exploit even/odd properties to simplify integrals/sums.
        """)

    with st.expander("Tips for Specific Topics"):
        st.markdown("""
        * **Signal Ops (DT)**: $y[n]=x[an]$ or $x[n/a]$ are tricky. Write out indices carefully.
        * **Convolution**: Graphical good for simple shapes. Frequency domain ($Y=HX$) often faster if FTs are known or easy.
        * **Fourier Series**: Use Complex form ($c_n$) for calculations, convert to other forms if needed ($A_n = 2|c_n|$, $a_n=2Re\{c_n\}$, $b_n=-2Im\{c_n\}$).
        * **Fourier Transform**: Properties are powerful! Combine basic pairs using linearity, shifting, modulation theorem etc.
        * **Filtering**: $Y(f)=H(f)X(f)$. Visualize multiplication in freq domain. Ideal LPF cuts off frequencies above $f_c$.
        * **AM**: Remember spectrum = carrier impulses + shifted/scaled message spectrum $M(f)$. $BW = 2 \times BW_{message}$.
        * **Sampling**: Find $f_M$. $f_N=2f_M$. Check $f_s$ vs $f_N$. If $f_s < f_N$, find aliased frequency $f_a$ where $|f_a - k f_s| = f_{original}$ for some integer $k$, such that $|f_a| < f_s/2$.
        """)

    with st.expander("Exam Strategy"):
        st.markdown("""
        * **Time**: Allocate roughly equal time per question (check marks). Move on if stuck.
        * **Working**: Show steps clearly for partial credit.
        * **Check**: Arithmetic, signs, factors of $2\pi$.
        * **Keywords**: Sketch (label axes/values), Determine/Find (calculate), Explain/Justify (use definitions/theorems).
        * **Formula Sheet**: Is your best friend in a closed-book exam.
        """)