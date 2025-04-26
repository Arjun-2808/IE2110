import streamlit as st
import pandas as pd
import numpy as np

# --- App Configuration ---
st.set_page_config(page_title="IE2110 Revision Helper", layout="wide")

st.title(" Signals and Systems Revision Helper 🧠")
st.markdown("""
Welcome! This app helps you revise key concepts, review solved examples, and learn **practical tips & tricks** for tackling IE2110 exam questions, especially those involving **graph sketching**.
Use the tabs below to navigate through the content.
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
        st.markdown("""
        * **CT vs. DT**: $x(t)$ vs $x[n]$. Identify the independent variable.
        * **Symmetry**:
            * Even: $x(t)=x(-t)$ or $x[n]=x[-n]$. (Symmetric about vertical axis).
            * Odd: $x(t)=-x(-t)$ or $x[n]=-x[-n]$. (Anti-symmetric about origin).
            * Decomposition: $x = x_e + x_o$.
                * $x_e = \\\\frac{1}{2}(x + x_{reflected})$
                * $x_o = \\\\frac{1}{2}(x - x_{reflected})$
        * **Periodicity**: Does the signal repeat? Find smallest $T_0$ (CT) or $K_0$ (DT).
            * *Test (CT)*: Is $x(t) = x(t+T_0)$ for some $T_0$?
            * *Test (DT)*: Is $x[n] = x[n+K_0]$ for some integer $K_0$? For $x[n]=e^{j\\omega_0 n}$, periodic if $\\omega_0/(2\\pi)$ is rational.
        * **Energy vs. Power**: Finite duration/decaying $\implies$ Energy. Periodic/constant amplitude $\implies$ Power.
        """)
        st.markdown("**Formulas (Energy $E_x$, Power $P_x$)**")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Continuous-Time (CT)**")
            st.latex("E_x = \\\\int_{-\\\\infty}^{\\\\infty} |x(t)|^2 dt")
            st.latex("P_x = \\\\lim_{T\\\\to\\\\infty} \\\\frac{1}{T} \\\\int_{-T/2}^{T/2} |x(t)|^2 dt \quad \\\\text{(General)}")
            st.latex("P_x = \\\\frac{1}{T_0} \\\\int_{T_0} |x(t)|^2 dt \quad \\\\text{(Periodic)}")
        with col2:
            st.markdown("**Discrete-Time (DT)**")
            st.latex("E_x = \\\\sum_{n=-\\\\infty}^{\\\\infty} |x[n]|^2")
            st.latex("P_x = \\\\lim_{K\\\\to\\\\infty} \\\\frac{1}{2K+1} \\\\sum_{n=-K}^{K} |x[n]|^2 \quad \\\\text{(General)}")
            st.latex("P_x = \\\\frac{1}{K_0} \\\\sum_{n=<K_0>} |x[n]|^2 \quad \\\\text{(Periodic)}")

    with st.expander("1.2 Essential Signals (Know their shapes!)"):
        st.markdown("""
        * **Impulse $\\\\delta$**:
            * CT $\\\\delta(t)$: Infinite height, zero width, area=1 at $t=0$. *Use for sampling property*.
            * DT $\\\\delta[n]$: Value 1 at $n=0$, else 0. *Use for sequence representation*.
        * **Unit Step $u$**:
            * CT $u(t)$: 0 for $t<0$, 1 for $t>0$. *Use for 'turning on' signals*.
            * DT $u[n]$: 0 for $n<0$, 1 for $n \\ge 0$.
            * Relation: $u(t) = \\\\int_{-\\\\infty}^t \\\\delta(\\\\tau)d\\\\tau$, $\\\\delta(t) = \\\\frac{du(t)}{dt}$ (loosely). $u[n] = \\\\sum_{m=-\\\\infty}^n \\\\delta[m]$, $\\\\delta[n]=u[n]-u[n-1]$.
        * **Rectangle $rect(t/T)$**: Value 1 for $|t| \\le T/2$. Width $T$, centered at 0.
        * **Triangle $\\\\Lambda(t/T)$**: Value $1-|t|/T$ for $|t| \\le T$. Width $2T$, peak 1 at $t=0$. (Note: different definitions exist, check formula sheet's $rect$ and $sinc$).
        * **Sinc $\\\\text{sinc}(x) = \\\\frac{\\\\sin(\\\\pi x)}{\\\\pi x}$**: Peak=1 at $x=0$. Zero crossings at $x = \\pm 1, \pm 2, ...$. Decays as $1/x$. *Important FT pair with rect*.
        * **Exponential $e^{at}$ / $a^n$**: Decaying if $Re\{a\}<0$ or $|a|<1$. Growing if $Re\{a\}>0$ or $|a|>1$. Oscillatory if $a$ is imaginary ($e^{j\\omega_0 t}$) or complex with magnitude 1 ($e^{j\\omega_0 n}$).
        """)

    with st.expander("1.3 Signal Operations (How they affect graphs)"):
        st.markdown("""
        * **Amplitude Scale $A x$**: Stretches/shrinks vertically. Flips if $A<0$.
        * **Time Shift $x(t-T)$ / $x[n-K]$**: Shifts **right** (delay) if $T, K > 0$. Shifts **left** (advance) if $T, K < 0$. Moves the *entire shape* along the time axis.
        * **Time Scale (CT) $x(at)$**:
            * $|a|>1$: **Compresses** towards $t=0$. (Events happen faster).
            * $|a|<1$: **Expands** away from $t=0$. (Events happen slower).
            * $a<0$: Reverses time + scales. *Do scaling first, then reflect about $t=0$*.
            * *Graphing Tip*: A point at $t_1$ in $x(t)$ moves to $t_1/a$ in $x(at)$.
        * **Time Scale (DT) $x[Kn]$ (Decimation)**: Keeps samples at $n=0, \pm K, \pm 2K,...$. Discards others. *Graphing Tip*: Plot original $x[m]$, then mark and plot only points where $m$ is a multiple of $K$.
        * **Time Scale (DT) $x[n/K]$ (Expansion)**: Original sample at $m$ moves to $n=mK$. Insert $K-1$ zeros between original samples. *Graphing Tip*: Plot original $x[m]$, then spread points out by factor $K$ and fill gaps with zeros.
        * **Combined Ops**: $A x(a(t-T))$. Order matters! Usually: **Shift first** ($t \to t-T$), **then scale** ($(t-T) \to a(t-T)$), **then amplitude scale**. Check specific question context. For $y[n] = x[a n + b]$, find $n$ values that make $an+b$ valid indices for $x$.
        """)

    with st.expander("1.4 System Properties (LTI Focus)"):
        st.markdown("""
        * **LTI**: Linear & Time-Invariant. Characterized by impulse response $h$.
        * **Causality**: Output depends only on *present/past* input. LTI: $h(t)=0$ for $t<0$; $h[n]=0$ for $n<0$. *Graph Check*: Impulse response is zero for negative time.
        * **Stability (BIBO)**: Bounded Input $\implies$ Bounded Output. LTI: Impulse response must be absolutely integrable/summable.
            * $\\\\int_{-\\\\infty}^{\\\\infty} |h(t)| dt < \\\\infty$
            * $\\\\sum_{n=-\\\\infty}^{\\\\infty} |h[n]| < \\\\infty$
            * *Graph Check*: Area under $|h(t)|$ or sum of $|h[n]|$ must be finite. Decaying impulse response often implies stability.
        """)

    with st.expander("2. LTI Systems & Convolution"):
        st.markdown("""
        * **Output $y = x * h$**. The system's response $h$ shapes the input $x$.
        """)
        st.markdown("**Convolution Integral (CT)**:")
        st.latex("y(t) = x(t) * h(t) = \\\\int_{-\\\\infty}^{\\\\infty} x(\\\\tau) h(t-\\\\tau) d\\\\tau")
        st.markdown("**Convolution Sum (DT)**:")
        st.latex("y[n] = x[n] * h[n] = \\\\sum_{m=-\\\\infty}^{\\\\infty} x[m] h[n-m]")
        st.markdown("""
        * **Graphical Meaning**: Flip one signal ($h$), shift it by $t$ (or $n$), multiply point-by-point with the other ($x$), find the area/sum of the product. The result is the output $y$ at that specific shift $t$ (or $n$). Repeat for all shifts. (See Hacks tab for details).
        * **Properties**: Commutative ($x*h=h*x$), Distributive, Associative. Useful for simplifying problems.
        * **Special Cases**:
            * $x * \\\\delta(t-T_0) = x(t-T_0)$. (Shifts the input).
            * $x * u(t) = \\\\int_{-\\\\infty}^{t} x(\\\\tau) d\\\\tau$. (Integrates the input).
        * **Step Response $s$**: Response to unit step $u$. $s(t) = h(t)*u(t) = \\\\int_{-\\\\infty}^{t} h(\\\\tau) d\\\\tau$. $h(t) = \\\\frac{ds(t)}{dt}$. (Similar relations for DT).
        """)
        
    st.divider()
    # --- Part 2 Topics ---
    st.subheader("Part 2: Fourier Analysis & Sampling")

    with st.expander("2. Fourier Series (Periodic CT Signals)"):
        st.markdown("""
        * **Idea**: Represent $x(t)$ with period $T_0$ as a sum of complex exponentials (or sinusoids) at harmonic frequencies $n f_0$, where $f_0=1/T_0$ ($\\\\omega_0 = 2\\\\pi f_0$).
        * **Complex Exponential Form**: $x(t) = \\\\sum_{n=-\\\\infty}^{\\\\infty} c_n e^{j n \\\\omega_0 t}$.
        """)
        st.latex("c_n = \\\\frac{1}{T_0} \\\\int_{T_0} x(t) e^{-j n \\\\omega_0 t} dt \quad \\\\text{(Analysis Eq.)}")
        st.markdown("""
            * $c_n$ is the **complex amplitude** of the $n^{th}$ harmonic.
            * $|c_n|$: Amplitude Spectrum (Plot $|c_n|$ vs $n f_0$). Usually discrete lines.
            * $\\\\angle c_n$: Phase Spectrum (Plot $\\\\angle c_n$ vs $n f_0$).
            * $c_0 = \\\\frac{1}{T_0} \\\\int_{T_0} x(t) dt$ = **DC / Average value**.
            * Real $x(t) \\implies c_{-n} = c_n^*$. ($|c_n|$ is even, $\\\\angle c_n$ is odd).
        * **Trigonometric / Amp-Phase Forms**: Alternative ways to write the sum using $\\\\cos$ and $\\\\sin$. $A_n = 2|c_n|$ for $n>0$, $A_0=c_0$.
        * **Parseval's (Power)**:
        """)
        st.latex("P_x = \\\\frac{1}{T_0} \\\\int_{T_0} |x(t)|^2 dt = \\\\sum_{n=-\\\\infty}^{\\\\infty} |c_n|^2")
        st.markdown("Power in time domain = Sum of powers in frequency components.")

    with st.expander("3. Fourier Transform (Aperiodic CT Signals / Energy Signals)"):
        st.markdown("""
        * **Idea**: Represent a non-periodic $x(t)$ using a *continuum* of complex exponentials $e^{j 2 \pi f t}$.
        * **Definition** ($f$ in Hz):
        """)
        st.latex("X(f) = \\\\mathcal{F}\\\\{x(t)\\\\} = \\\\int_{-\\\\infty}^{\\\\infty} x(t) e^{-j2\\\\pi f t} dt \quad \\\\text{(Analysis Eq.)}")
        st.latex("x(t) = \\\\mathcal{F}^{-1}\\\\{X(f)\\\\} = \\\\int_{-\\\\infty}^{\\\\infty} X(f) e^{j2\\\\pi f t} df \quad \\\\text{(Synthesis Eq.)}")
        st.markdown("""
            * $X(f)$ is the **Frequency Spectrum** or **Fourier Transform**. It's a complex function of frequency $f$.
            * $|X(f)|$: Amplitude Spectrum. *Shape tells you frequency content*.
            * $\\\\angle X(f)$: Phase Spectrum. *Tells you relative timing of frequencies*.
            * Units: If $x(t)$ is Volts, $X(f)$ is Volt-seconds or Volts/Hz.
        * **Key Properties & Pairs**: (Essential for problem solving! See Hacks tab)
            * Linearity, Time/Freq Shifting, Scaling, Duality, Differentiation, Integration.
            * **Convolution Theorem**: $x_1(t) * x_2(t) \\longleftrightarrow X_1(f) X_2(f)$. (Convolution in time $\Leftrightarrow$ Multiplication in frequency). *Often easier than time-domain convolution!*
            * **Multiplication Theorem**: $x_1(t) x_2(t) \\longleftrightarrow X_1(f) * X_2(f)$. (Multiplication in time $\Leftrightarrow$ Convolution in frequency). *Used in AM, Sampling*.
            * Know pairs like: $rect \\leftrightarrow sinc$, $\\\\Lambda \\leftrightarrow sinc^2$, $e^{-at}u(t) \\leftrightarrow 1/(a+j\omega)$, $\\\\delta(t) \\leftrightarrow 1$, $1 \\leftrightarrow \\delta(f)$, $e^{j\omega_0 t} \\leftrightarrow 2\pi \\delta(\omega - \omega_0)$ or $\delta(f-f_0)$.
        * **Rayleigh's (Energy)**:
        """)
        st.latex("E_x = \\\\int_{-\\\\infty}^{\\\\infty} |x(t)|^2 dt = \\\\int_{-\\\\infty}^{\\\\infty} |X(f)|^2 df")
        st.markdown("$|X(f)|^2$ is the Energy Spectral Density (ESD). Area under ESD = Total Energy.")

    with st.expander("4. Frequency Domain Analysis of LTI Systems"):
        st.markdown("""
        * **Frequency Response**: $H(f) = \\\\mathcal{F}\\\\{h(t)\\\\}$. How the system affects different frequencies.
        * **Input/Output**: $Y(f) = H(f) X(f)$. Output spectrum = Input spectrum $\\\\times$ Frequency Response.
            * *Graphical View*: $|Y(f)| = |H(f)| |X(f)|$. $\\\\angle Y(f) = \\\\angle H(f) + \\\\angle X(f)$.
            * The system *filters* the input signal $X(f)$ based on the shape of $H(f)$.
        * **Response to Sinusoid**: Input $A\cos(\omega_0 t + \theta)$ $\implies$ Output $A|H(\omega_0)|\cos(\omega_0 t + \theta + \angle H(\omega_0))$.
            * *Key*: System only changes Amplitude (by $|H|$ at $\omega_0$) and Phase (by $\angle H$ at $\omega_0$) of the input sinusoid. Frequency remains the same.
        * **Ideal Filters**: LPF, HPF, BPF. Sharp cutoffs. $H(f)$ is 1 (or K) in passband, 0 in stopband. Linear phase in passband ($\angle H = - \omega t_0$) for no phase distortion (just delay).
            * *Reality Check*: Ideal filters are non-causal. Real filters have gradual roll-offs.
        """)

    with st.expander("5. Sampling & Aliasing"):
        st.markdown("""
        * **Sampling**: $x[n] = x(nT_s)$. Convert CT $x(t)$ to DT $x[n]$. $f_s=1/T_s$ is sampling frequency.
        * **Spectrum of Sampled Signal (Ideal Sampling Model)**: $x_s(t) = x(t) \sum \delta(t-nT_s)$.
        """)
        st.latex("X_s(f) = \\\\frac{1}{T_s} \\\\sum_{n=-\\\\infty}^{\\\\infty} X(f - n f_s)")
        st.markdown("""
            * *Graphical View*: Replicas of the original spectrum $X(f)$, scaled by $1/T_s$, centered at multiples of $f_s$ ($0, \pm f_s, \pm 2f_s, ...$).
        * **Sampling Theorem**: If $x(t)$ is bandlimited to $f_M$ ($X(f)=0$ for $|f|>f_M$), we can perfectly recover $x(t)$ from $x[n]$ if $f_s \ge 2f_M$.
        * **Nyquist Rate**: $f_N = 2f_M$. Minimum $f_s$ to avoid aliasing.
        * **Aliasing**: If $f_s < f_N$, the spectral replicas **overlap**. High frequencies in $X(f)$ get folded back into lower frequencies.
            * *Result*: A high frequency component (e.g., $f_1 > f_s/2$) appears as a lower frequency $f_a = |f_1 - k f_s|$ in the baseband $[-f_s/2, f_s/2]$. (See Hacks tab).
        * **Reconstruction**: Ideal LPF with cutoff $f_s/2$ and gain $T_s$ applied to $x_s(t)$ recovers $x(t)$ *if no aliasing occurred*.
        """)

    st.divider()
    # --- Part 3 Topics ---
    st.subheader("Part 3: Amplitude Modulation (AM)")

    with st.expander("1.2 Conventional AM"):
        st.markdown("""
        * **Purpose**: Shift baseband message $m(t)$ (bandwidth $B$) to higher frequency $f_c$ for transmission.
        * **Time Domain**: $x_{AM}(t) = A_c [1 + k_a m(t)] \\cos(2 \\pi f_c t)$.
            * $A_c$: Carrier amplitude. $k_a$: Sensitivity.
            * **Envelope**: $A_c |1 + k_a m(t)|$. If $|k_a m(t)|_{max} = \mu < 1$, envelope is $A_c(1+k_a m(t))$ and follows $m(t)$.
        * **Modulation Index $\\mu$**: $\\mu = |k_a m(t)|_{max}$. For sinusoid $m(t)=A_m\cos(\omega_m t)$, $\\mu=k_a A_m$.
            * $\mu < 1$: Under-modulation (Good, allows envelope detection).
            * $\mu > 1$: Over-modulation (Bad, envelope distorted, information loss).
        * **Spectrum**: Use multiplication property: $x(t) \cos(\omega_c t) \leftrightarrow \frac{1}{2}[X(f-f_c) + X(f+f_c)]$.
        """)
        st.latex("X_{AM}(f) = \\\\frac{A_c}{2}[\\delta(f-f_c) + \\delta(f+f_c)] \\\\quad \\\\text{(Carrier)}")
        st.latex("+ \\\\frac{A_c k_a}{2}[M(f-f_c) + M(f+f_c)] \quad \\\\text{(Sidebands)}")
        st.markdown("""
            * *Graphical View*: Carrier spikes at $\pm f_c$. Scaled copies of the message spectrum $M(f)$ shifted to center around $\pm f_c$.
        * **Bandwidth**: $BW_{AM} = 2 B$ (where $B$ is bandwidth of $m(t)$).
        * **Power**: $P_T = P_c + P_{SB} = \\\\frac{A_c^2}{2} (1 + k_a^2 P_m)$, where $P_m$ is power of $m(t)$.
        * **Efficiency**: $\eta = P_{SB}/P_T$. Max 33.3% for $\mu=1$ sinusoidal. (Most power is in the carrier).
        * **Demodulation**: Envelope detector (Diode + RC filter) if $\mu \le 1$. Recovers the envelope.
        """)

# --- Solved Examples Tab ---
with tab2:
    st.header("💡 Solved Examples (Focus on Method & Visualization)")
    st.markdown("Understanding the *how* and *why*, not just the answer.")

    with st.expander("Example: Even/Odd Decomposition & Sketching (PYP 1a-i, ii)"):
        st.markdown("Given $x[n]=\\\\sum_{k=-1}^{1}2^{k}\\\\delta[n-k]$. Sketch $x[n]$ and its even/odd parts.")
        st.markdown("**1. Evaluate $x[n]$:**")
        st.markdown("""
        Expand the sum:
        * $k=-1: 2^{-1} \\delta[n-(-1)] = 0.5 \\delta[n+1]$
        * $k=0: 2^0 \\delta[n-0] = 1 \\delta[n]$
        * $k=1: 2^1 \\delta[n-1] = 2 \\delta[n-1]$
        So, $x[n] = 0.5 \\delta[n+1] + \delta[n] + 2 \\delta[n-1]$.
        """)
        st.markdown("**2. Sketch $x[n]$:**")
        st.markdown("Plot the non-zero values: Value 0.5 at $n=-1$, Value 1 at $n=0$, Value 2 at $n=1$. Zero elsewhere.")
        # Placeholder for a sketch description or actual plot if using matplotlib
        st.image("https://via.placeholder.com/400x150.png?text=Sketch+of+x[n]:+Stem+at+n=-1+(ht=0.5),+n=0+(ht=1),+n=1+(ht=2)", caption="Sketch of x[n]")

        st.markdown("**3. Find $x[-n]$ (Reflection):**")
        st.markdown("$x[-n] = 0.5 \\delta[-n+1] + \\delta[-n] + 2 \\delta[-n-1] = 0.5 \\delta[-(n-1)] + \delta[-n] + 2 \delta[-(n+1)]$.")
        st.markdown("This means: Value 0.5 at $n=1$, Value 1 at $n=0$, Value 2 at $n=-1$. It's the mirror image of $x[n]$ about $n=0$.")

        st.markdown("**4. Calculate Even Part $x_e[n] = 0.5 (x[n] + x[-n])$:**")
        st.markdown("""
        * $n=-1: 0.5 (x[-1] + x[1]) = 0.5 (0.5 + 2) = 1.25$
        * $n=0: 0.5 (x[0] + x[0]) = 0.5 (1 + 1) = 1$
        * $n=1: 0.5 (x[1] + x[-1]) = 0.5 (2 + 0.5) = 1.25$
        * Other $n$: $0.5(0+0)=0$.
        * Result: $x_e[n]$ has values {1.25, 1, 1.25} at n={-1, 0, 1}. **Check: Is it even? Yes.**
        """)
        st.image("https://via.placeholder.com/400x150.png?text=Sketch+of+xe[n]:+Stem+at+n=-1+(ht=1.25),+n=0+(ht=1),+n=1+(ht=1.25)", caption="Sketch of xe[n]")


        st.markdown("**5. Calculate Odd Part $x_o[n] = 0.5 (x[n] - x[-n])$:**")
        st.markdown("""
        * $n=-1: 0.5 (x[-1] - x[1]) = 0.5 (0.5 - 2) = -0.75$
        * $n=0: 0.5 (x[0] - x[0]) = 0.5 (1 - 1) = 0$
        * $n=1: 0.5 (x[1] - x[-1]) = 0.5 (2 - 0.5) = 0.75$
        * Other $n$: $0.5(0-0)=0$.
        * Result: $x_o[n]$ has values {-0.75, 0, 0.75} at n={-1, 0, 1}. **Check: Is it odd? Yes.**
        """)
        st.image("https://via.placeholder.com/400x150.png?text=Sketch+of+xo[n]:+Stem+at+n=-1+(ht=-0.75),+n=0+(ht=0),+n=1+(ht=0.75)", caption="Sketch of xo[n]")
        st.markdown("**Verification:** Does $x_e[n] + x_o[n] = x[n]$? Yes: $\{1.25-0.75, 1+0, 1.25+0.75\} = \{0.5, 1, 2\}$.")


    with st.expander("Example: DT Signal Operation & Sketching (PYP 1a-iii)"):
         st.markdown("Given $x[n]$ above, find and sketch $y[n]=-x[\\\\frac{n-1}{2}]$.")
         st.markdown("**1. Analyze the Argument:** Let $m = \\\\frac{n-1}{2}$. We need $m$ to be an integer index where $x[m]$ is non-zero (i.e., $m = -1, 0, 1$). We also need $n$ to be an integer.")
         st.markdown("""
         * If $m = -1$: $\\\\frac{n-1}{2} = -1 \implies n-1 = -2 \implies n = -1$.
         * If $m = 0$: $\\\\frac{n-1}{2} = 0 \implies n-1 = 0 \implies n = 1$.
         * If $m = 1$: $\\\\frac{n-1}{2} = 1 \implies n-1 = 2 \implies n = 3$.
         * *Observation*: This operation involves **time expansion** (factor of 2) and a **time shift** (related to the -1). It only produces output at odd values of $n$.
         """)
         st.markdown("**2. Calculate $y[n]$ values:**")
         st.markdown("""
         * For $n=-1$: $y[-1] = -x[\\\\frac{-1-1}{2}] = -x[-1] = -(0.5) = -0.5$.
         * For $n=1$: $y[1] = -x[\\\\frac{1-1}{2}] = -x[0] = -(1) = -1$.
         * For $n=3$: $y[3] = -x[\\\\frac{3-1}{2}] = -x[1] = -(2) = -2$.
         * For all other integer $n$, $(n-1)/2$ is either non-integer or outside $\\{-1, 0, 1\\}$, so $x[\dots]=0$ and $y[n]=0$.
         """)
         st.markdown("**3. Sketch $y[n]$:**")
         st.markdown("Plot the non-zero values: Value -0.5 at $n=-1$, Value -1 at $n=1$, Value -2 at $n=3$. Zero elsewhere.")
         st.image("https://via.placeholder.com/400x150.png?text=Sketch+of+y[n]:+Stem+at+n=-1+(ht=-0.5),+n=1+(ht=-1),+n=3+(ht=-2)", caption="Sketch of y[n]")
         st.markdown("**Energy Calculation:** $E_y = \\\\sum |y[n]|^2 = (-0.5)^2 + (-1)^2 + (-2)^2 = 0.25 + 1 + 4 = 5.25$.")


    with st.expander("Example: Graphical Convolution (Lec 1, Slide 109 / Basic Shapes)"):
        st.markdown("Sketch $y(t) = rect(t/2) * rect(t/2)$.")
        st.markdown("**1. Define Signals:** $x(t) = rect(t/2)$ is 1 for $-1 \le t \le 1$, 0 otherwise. $h(t)=rect(t/2)$ is the same.")
        st.markdown("**2. Flip:** $h(-\\\\tau)$ is also 1 for $-1 \le \\tau \le 1$, 0 otherwise.")
        st.markdown("**3. Shift:** $h(t-\\\\tau)$ is 1 for $-1 \le t-\\\\tau \le 1$, which means $t-1 \le \\tau \le t+1$. It's a rectangle of width 2, centered at $\\\\tau = t$.")
        st.markdown("**4. Visualize Overlap:** We integrate $x(\\\\tau) h(t-\\\\tau)$ w.r.t $\\\\tau$. $x(\\\\tau)$ is fixed (width 2, centered at 0). $h(t-\\\\tau)$ slides along the $\\\\tau$ axis as $t$ changes.")
        st.image("https://via.placeholder.com/600x200.png?text=Visualize:+Fixed+x(tau),+Sliding+h(t-tau)", caption="Convolution Visualization")
        st.markdown("**5. Identify Regions based on $t$ (where overlap changes):**")
        st.markdown("""
            * **Region 1: No Overlap ($t+1 < -1 \implies t < -2$)**: $h(t-\\\\tau)$ is entirely to the left of $x(\\\\tau)$. Integral = 0. $y(t)=0$.
            * **Region 2: Partial Overlap (Entering) ($-1 \le t+1$ and $t-1 < -1 \implies -2 \le t < 0$)**: Right edge of $h(t-\\\\tau)$ is inside $x(\\\\tau)$, left edge is outside. Overlap is from $\\\\tau = -1$ to $\\\\tau = t+1$.
                * $y(t) = \\\\int_{-1}^{t+1} (1)(1) d\\\\tau = [\\\\tau]_{-1}^{t+1} = (t+1) - (-1) = t+2$. (Linear increase).
            * **Region 3: Full Overlap ($-1 \le t-1$ and $t+1 \le 1 \implies$ Impossible? Let's recheck edges. Ah, the *signals* are width 2. Max overlap occurs when centers align). Corrected Regions:**
            * **Region 1 (No Overlap): $t < -2$**. $y(t)=0$.
            * **Region 2 (Entering): $-2 \le t < 0$**. Overlap interval is $[-1, t+1]$. $y(t) = \\\\int_{-1}^{t+1} 1 d\\\\tau = t+2$.
            * **Region 3 (Leaving): $0 \le t < 2$**. Overlap interval is $[t-1, 1]$. $y(t) = \\\\int_{t-1}^{1} 1 d\\\\tau = 1 - (t-1) = 2-t$. (Linear decrease).
            * **Region 4 (No Overlap): $t \ge 2$**. $y(t)=0$.
            """)
        st.markdown("**6. Combine & Sketch $y(t)$:**")
        st.markdown("The result is a **triangle** function: Starts at $t=-2$, rises linearly to height 2 at $t=0$, falls linearly to 0 at $t=2$.")
        st.latex("y(t) = (2-|t|) \\\\quad \\\\text{for } -2 \\le t \\le 2, \\\\text{ and } 0 \\\\text{ otherwise.}")
        st.latex("\\\\text{This is } 2 \\\\Lambda(t/2).")
        st.image("https://via.placeholder.com/400x150.png?text=Sketch+of+y(t):+Triangle+from+t=-2+to+2,+peak+2+at+t=0", caption="Sketch of y(t)")
        st.markdown("**Key Takeaway:** Convolving two rectangles gives a triangle. Width of result = Sum of widths = $2+2=4$. Peak height = Area of one rect (if height 1) $\times$ Height of other = $2 \times 1 = 2$.")

    with st.expander("Example: Sketching AM Spectrum (PYP Q2b)"):
        st.markdown("Given $m_1(t) = 4\cos(100\pi t)$ ($f_{m1}=50$ Hz) and $m_2(t) = 400 \\text{sinc}(200t)$ (using $\\text{sinc}(x)=\\sin(\pi x)/(\pi x)$ definition, $2W=200 \implies W=100$ Hz BW). AM signal is $z(t) = \{4+m_1(t)\}\cos(2000\pi t) + \{4+m_2(t)\}\cos(2400\pi t)$. Sketch $Z(f)$.")
        st.markdown("**1. Find Spectra of Messages $M(f)$:**")
        st.markdown("""
        * $m_1(t) = 4\cos(2\pi \cdot 50 t)$. FT is $M_1(f) = 2[\delta(f-50) + \delta(f+50)]$. *Two spikes at $\pm 50$ Hz, height 2.*
        * $m_2(t) = 400 \\text{sinc}(200t) = 400 \\frac{\\sin(200\pi t)}{200\pi t} = 2 \\frac{\\sin(\pi (200) t)}{\pi t}$. This doesn't match $A \text{sinc}(Wt) = A \frac{\sin(\pi W t)}{\pi W t}$. Let's assume the intended definition is $m_2(t) = A \text{sinc}(Wt)$ where $W=200$. Or perhaps the PYP used $\text{sinc}(x)=\sin(x)/x$? Assuming the standard $\text{sinc}(x)=\sin(\pi x)/(\pi x)$ and the formula $A \text{rect}(t/T) \leftrightarrow AT \text{sinc}(fT)$, we use duality or the formula for $\text{sinc}(Wt)$.
        * Let's use the pair: $A \text{rect}(f/B) \leftrightarrow AB \text{sinc}(Bt)$. If $m_2(t) = 400 \text{sinc}(200 t)$, then $B=200$, $AB=400 \implies A=2$. So $M_2(f) = 2 \text{rect}(f/200)$. *A rectangle from -100 Hz to 100 Hz, height 2.* BW = 100 Hz.
        """)
        st.markdown("**2. Analyze First AM Term: $\{4+m_1(t)\}\cos(2\pi \cdot 1000 t)$:**")
        st.markdown("""
        * Carrier $f_{c1}=1000$ Hz. Formula: $\\\\frac{A_c}{2}[\delta(f\pm f_c)] + \\\\frac{A_c k_a}{2}[M(f\pm f_c)]$. Here, $A_c=1$ (outside bracket), and inside bracket is $A_c'[1+k_a m_1(t)] = 4+m_1(t) \implies A_c'=4, A_c'k_a=1$. Let's use the simpler form $X(f) = 0.5[\text{FT}\{4+m_1(t)\text{ evaluated at } f\pm f_c]$.
        * FT of $\{4+m_1(t)\} = 4\delta(f) + M_1(f) = 4\delta(f) + 2[\delta(f-50) + \delta(f+50)]$.
        * Shifted spectrum: $0.5 \times [ 4\delta(f\pm 1000) + 2\delta(f\pm 1000 - 50) + 2\delta(f\pm 1000 + 50) ]$
        * Result: Spikes height 2 at $\pm 1000$ Hz (Carrier). Spikes height 1 at $\pm 950$ Hz and $\pm 1050$ Hz (Sidebands).
        """)
        st.image("https://via.placeholder.com/400x150.png?text=Sketch+Term+1:+Spikes+at+-1050,-1000,-950,+950,+1000,+1050", caption="Sketch of Term 1 Spectrum")

        st.markdown("**3. Analyze Second AM Term: $\{4+m_2(t)\}\cos(2\pi \cdot 1200 t)$:**")
        st.markdown("""
        * Carrier $f_{c2}=1200$ Hz.
        * FT of $\{4+m_2(t)\} = 4\delta(f) + M_2(f) = 4\delta(f) + 2 \text{rect}(f/200)$.
        * Shifted spectrum: $0.5 \times [ 4\delta(f\pm 1200) + 2 \text{rect}((f\pm 1200)/200) ]$
        * Result: Spikes height 2 at $\pm 1200$ Hz (Carrier). Rectangles height 1, width 200 Hz, centered at $\pm 1200$ Hz (Sidebands). (i.e., from 1100 to 1300 Hz, and -1300 to -1100 Hz).
        """)
        st.image("https://via.placeholder.com/400x150.png?text=Sketch+Term+2:+Spikes+at+-1200,1200.+Rects+[-1300,-1100],+[1100,1300]", caption="Sketch of Term 2 Spectrum")

        st.markdown("**4. Sketch Z(f) (Sum of both terms):**")
        st.markdown("Combine the components graphically. Ensure axes are labeled (f in Hz) and heights are marked.")
        st.image("https://via.placeholder.com/600x200.png?text=Sketch+Z(f):+Combine+spikes+and+rects+at+correct+frequencies", caption="Sketch of Combined Spectrum Z(f)")
        st.markdown("**Observations:**")
        st.markdown("""
         * Total BW (positive frequencies): $1300 - 950 = 350$ Hz.
         * Guard Band between channels: $1100 - 1050 = 50$ Hz.
         """)


# --- Problem-Solving Tips Tab ---
with tab3:
    st.header("🚀 Graphing & Problem-Solving Hacks")
    st.markdown("Focusing on visualization and common question types.")

    with st.expander("🧠 General Strategy"):
        st.markdown("""
        1.  **Identify**: Signal type (CT/DT, Periodic/Aperiodic), System type (LTI?), Goal (Find y, h, H, sketch?).
        2.  **Tool**: Time domain (convolution, signal ops), Frequency domain (FS, FT, Laplace/Z), Sampling theory?
        3.  **Sketch First**: Draw the input $x$, impulse response $h$, or spectra $X, H$. Visualize the operation.
        4.  **Formula Sheet**: Find the relevant property or pair. Double-check definitions (e.g., $sinc$, $rect$).
        5.  **Simplify**: Use properties (linearity, shift, convolution theorem) to break down complex problems. Look for symmetry.
        6.  **Label Graphs**: Axes (t/n/f/$\omega$), units (s/Hz/rad/s), key points (amplitudes, times, frequencies, bandwidths).
        7.  **Check Sanity**: Does the result make sense? (e.g., Convolving causal signals $\implies$ causal result. LPF output should have less high-freq content). Units correct?
        """)

    with st.expander("✍️ Sketching Signal Operations"):
         st.markdown("""
         * **Baseline**: Know basic shapes: $\delta, u, rect, \Lambda, sinc, \cos, e^{-at}$.
         * **Shift $x(t-T)$**: Move the *whole shape* right by $T$ if $T>0$.
         * **Scale $x(at)$**: Point at $t_1$ moves to $t_1/a$. Compresses if $|a|>1$, expands if $|a|<1$.
         * **Reverse $x(-t)$**: Flip graph about the vertical axis ($t=0$).
         * **Scale & Reverse $x(-at)$**: Scale by $|a|$ first, then reverse. Point at $t_1$ moves to $-t_1/a$.
         * **Combined $x(a(t-T))$**: Shift $x(t)$ by $T$ to get $x(t-T)$, *then* scale time axis by $a$. Point $t_1$ in $x(t)$ moves to $T + t_1/a$.
         * **DT Scaling $x[Kn]$**: Only keep points where index is multiple of $K$.
         * **DT Expansion $x[n/K]$**: Spread points by factor $K$, insert $K-1$ zeros.
         * **Example $x(2t+4)$**: Method 1: $x(2(t+2))$. Shift $x(t)$ left by 2 ($x(t+2)$), then compress by 2. Method 2: Argument mapping. If $x(\tau)$ defined for $\tau_{min} \le \tau \le \tau_{max}$, then $y(t)=x(2t+4)$ is defined for $\tau_{min} \le 2t+4 \le \tau_{max}$. Solve for $t$.
         """)

    with st.expander("↔️ Graphical Convolution (CT: $x(t) * h(t)$)"):
        st.markdown("""
        Visualize $y(t) = \\\\int x(\\\\tau) h(t-\\\\tau) d\\\\tau$.
        1.  **Pick & Flip**: Choose simpler signal (e.g., $h(\\\\tau)$) and sketch $h(-\\\\tau)$.
        2.  **Sketch Both**: Draw $x(\\\\tau)$ and the flipped $h(-\\\\tau)$ on the $\\\\tau$ axis.
        3.  **Shift**: The term $h(t-\\\\tau)$ is $h(-\\\\tau)$ shifted **right** by $t$. Imagine sliding $h(-\\\\tau)$ along the $\\\\tau$ axis, controlled by the value of $t$.
        4.  **Slide & Identify Regions**: Move the sliding window $h(t-\\\\tau)$ from $t=-\\\\infty$ to $+\\\\infty$. Find critical $t$ values where the **edges** of $x(\\\\tau)$ and $h(t-\\\\tau)$ align. These $t$ values define intervals where the *mathematical form* of the overlap changes.
        5.  **Calculate Overlap Integral for each Region**:
            * Determine the $\\\\tau$ interval of overlap for a given $t$ within a region. These are your integration limits.
            * Multiply the expressions for $x(\\\\tau)$ and $h(t-\\\\tau)$ within that overlap.
            * Integrate the product w.r.t. $\\\\tau$. The result is $y(t)$ for that region of $t$.
        6.  **Combine & Sketch $y(t)$**: Plot the calculated $y(t)$ for each region vs $t$. Check start/end points: $y(t)$ starts when signals first overlap, ends when they last overlap. Duration of $y(t)$ = duration($x$) + duration($h$).
        * **Hack**: Area of $y(t)$ = Area($x$) $\times$ Area($h$). Peak value often related to areas. Rect*Rect=Triangle. Rect*Triangle=Piecewise Parabola.
        * **DT Convolution**: Similar flip-shift-sum process. Sum the product $x[m]h[n-m]$ over $m$. Regions defined by $n$. Easier to use table method sometimes.
        """)

    with st.expander("📊 Sketching Frequency Spectra ($X(f)$, $H(f)$, $Y(f)$)"):
        st.markdown("""
        * **Fourier Series $c_n$**: Plot discrete lines (impulses) at $f = n f_0$. Height $|c_n|$, Phase $\\\\angle c_n$. Usually decays for large $n$. $c_0$ is DC value.
        * **Fourier Transform $X(f)$**: Continuous function. Know shapes: $rect(t/T) \leftrightarrow AT sinc(fT)$, $\\\\Lambda(t/T) \leftrightarrow B sinc^2(fT)$, $e^{-at}u(t) \leftrightarrow 1/(a+j2\pi f)$.
        * **Magnitude $|X(f)|$**: Usually largest near $f=0$ for baseband signals. Even function for real $x(t)$. Width related to signal duration (Time-BW tradeoff: short $x(t) \implies$ wide $X(f)$).
        * **Phase $\\\\angle X(f)$**: Odd function for real $x(t)$. Linear phase ($\\\\angle X = -2\pi f t_0$) corresponds to time shift $t_0$.
        * **Using Properties for Sketching**:
            * *Time Shift* $x(t-t_0)$: $|X(f)|$ unchanged, adds linear phase $-2\pi f t_0$.
            * *Modulation* $x(t)\cos(2\pi f_c t)$: Shifts $|X(f)|$ to $\pm f_c$, halves height. Sketch $0.5|X(f-f_c)|$ and $0.5|X(f+f_c)|$.
            * *Filtering* $Y(f)=H(f)X(f)$: Sketch $|H(f)|$ and $|X(f)|$. Multiply heights point-by-point to get $|Y(f)|$. (e.g., Ideal LPF just cuts off $X(f)$ outside passband). Add phases: $\\\\angle Y = \angle H + \angle X$.
        * **AM Spectrum**: Carrier spikes at $\pm f_c$. Sidebands are copies of $M(f)$ centered at $\pm f_c$. $BW = 2 \times BW_{message}$.
        * **Sampled Spectrum $X_s(f)$**: Replicas of $X(f)$ centered at $n f_s$, scaled by $1/T_s$. Check for overlap (aliasing) if $f_s < 2 f_M$.
        """)
        st.image("https://via.placeholder.com/600x200.png?text=Visualize:+X(f),+H(f),+Y(f)=X(f)H(f)", caption="Filtering Visualization")

    with st.expander("📉 Sampling & Aliasing Visualization"):
        st.markdown("""
        1.  **Sketch $X(f)$**: Identify max frequency $f_M$. Determine Nyquist rate $f_N = 2f_M$.
        2.  **Given $f_s$**: Compare $f_s$ to $f_N$.
        3.  **Sketch $X_s(f)$**: Draw $X(f)$ centered at $f=0$. Draw replicas $X(f-f_s)$ centered at $f=f_s$, $X(f+f_s)$ centered at $f=-f_s$, etc. Scale height by $1/T_s$.
        4.  **Check Overlap**: Do the replicas overlap in the baseband $[-f_s/2, f_s/2]$?
            * If $f_s \ge f_N$: No overlap. Reconstruction LPF (cutoff $f_s/2$) recovers $X(f)$.
            * If $f_s < f_N$: Overlap occurs = **Aliasing**.
        5.  **Finding Aliased Frequency**: A true frequency $f_{orig}$ appears as $f_{alias}$ in $[-f_s/2, f_s/2]$ where $f_{alias} = f_{orig} - k f_s$ for some integer $k$.
            * *Graphical Trick*: Draw $f_{orig}$ on the frequency axis. Find its distance to the nearest multiple of $f_s$ ($0, \pm f_s, \pm 2f_s, ...$). That distance is $|f_{alias}|$. The sign depends on which side of the multiple $f_{orig}$ falls. Or simply find $k$ such that $|f_{orig} - k f_s| < f_s/2$.
        """)
        st.image("https://via.placeholder.com/600x250.png?text=Visualize:+Sampling+Replicas+and+Aliasing", caption="Sampling/Aliasing Visualization")

    with st.expander("🚫 Common Pitfalls & Checks"):
        st.markdown("""
        * Mixing $f$ (Hz) and $\omega$ (rad/s). Remember $\omega=2\pi f$ and factors of $2\pi$ in FT pairs/properties.
        * Incorrect limits in convolution integral. Define regions carefully!
        * Sign errors in time shifts/phase shifts. Delay ($t-T_0$, $T_0>0$) $\implies$ negative linear phase ($-j\omega T_0$).
        * Forgetting the $1/T_s$ scaling factor in $X_s(f)$.
        * Errors in DT scaling/shifting argument mapping. Write out index relations ($m = an+b$).
        * Not labeling graph axes and key points.
        * Assuming ideal filters when not specified.
        * Errors calculating Fourier Series coefficients (check integration limits, $T_0$, $\omega_0$).
        * AM modulation index calculation/interpretation ($\mu > 1$ issue).
        """)