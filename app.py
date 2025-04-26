import streamlit as st

# Page configuration
st.set_page_config(page_title="IE2110 Revision Cheat Sheet", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigate Sections")
section = st.sidebar.radio(
    "Choose a section:",
    [
        "1. Classification of Signals",
        "2. Elementary & Singularity Signals",
        "3. Operations on Signals",
        "4. LTI System Properties",
        "5. Convolution",
        "6. Fourier Transform & Spectra",
        "7. Sampling & Aliasing",
        "8. Amplitude Modulation"
    ]
)

st.title("IE2110: Signals & Systems — Revision Cheat Sheet & Hacks")

if section == "1. Classification of Signals":
    st.header(section)
    st.subheader("Continuous vs Discrete Signals")
    st.write(
        "**Definition:** A continuous-time signal is written as x(t) (t ∈ ℝ); "
        "a discrete-time signal is x[n] (n ∈ ℤ)."
    )
    st.latex(r"x(t)\quad	ext{vs}\quad x[n]")
    st.write("⚡Quick Tip: spot `t` vs `[n]` immediately.")
    st.write("---")

    st.subheader("Continuous-Value vs Discrete-Value")
    st.write(
        "**Definition:** Continuous-value amplitude ∈ ℝ; "
        "discrete-value uses a finite set of levels."
    )
    st.write("⚡Quick Tip: smooth curve vs staircase.")
    st.write("---")

    st.subheader("Even vs Odd Signals")
    st.write("**Even:** x(t)=x(−t).  **Odd:** x(t)=−x(−t).")
    st.latex(r"x_e(t)=	frac12[x(t)+x(-t)]\quad x_o(t)=	frac12[x(t)-x(-t)]")
    st.write("⚡Hack: ∫_{-A}^A odd(t) dt = 0 — use to shortcut integrals.")
    st.write("---")

    st.subheader("Periodic vs Aperiodic Signals")
    st.write(
        "**Periodic:** ∃ T₀>0 s.t. x(t)=x(t+T₀).  "
        "**Aperiodic:** no finite T₀ exists."
    )
    st.write("⚡Quick Tip: sinusoids → periodic; exponentials → aperiodic.")
    st.write("---")

    st.subheader("Energy-Type vs Power-Type Signals")
    st.write("**Energy:** E=∫_{−∞}^{∞}|x(t)|² dt < ∞")
    st.write("**Power:** P=lim_{T→∞}(1/T)∫_{−T/2}^{T/2}|x(t)|² dt < ∞")
    st.write("⚡Quick Tip: periodic → power-type; pulses → energy-type.")

elif section == "2. Elementary & Singularity Signals":
    st.header(section)
    st.subheader("Exponential Signal")
    st.latex(r"x(t)=A e^{a t}")
    st.write("Growth if a>0; decay if a<0.")
    st.write("⚡Hack: appears in LTI homogeneous solutions.")
    st.write("---")

    st.subheader("Sinusoidal Signal")
    st.latex(r"x(t)=A\cos(2\pi f_0 t+\phi)")
    st.write("Periodic with T₀=1/f₀; zero-mean if cos.")
    st.write("⚡Hack: cos = even; sin = odd → phase ±90°.")
    st.write("---")

    st.subheader("Complex Exponential")
    st.latex(r"x(t)=A e^{j2\pi f_0 t}")
    st.write("Single spectral line at +f₀.")
    st.write("⚡Hack: phasors simplify sinusoid sums.")
    st.write("---")

    st.subheader("Impulse Function")
    st.latex(r"\delta(t)")
    st.write("Area=1; x(t)*δ(t−t₀)=x(t₀).")
    st.write("⚡Hack: convolution with δ shifts function.")
    st.write("---")

    st.subheader("Step Function")
    st.latex(r"u(t)=\begin{cases}1 & t\ge0\\0 & t<0\end{cases}")
    st.write("Derivative = δ(t); builds piecewise signals.")
    st.write("⚡Hack: use u(t) to limit convolution start.")
    st.write("---")

    st.subheader("Rectangular Pulse")
    st.latex(r"\mathrm{rect}(t/T)")
    st.write("Width T; FT↔T·sinc(fT).")
    st.write("⚡Hack: ideal low-pass shape in time.")
    st.write("---")

    st.subheader("Sinc Function")
    st.latex(r"\mathrm{sinc}(t)=\frac{\sin(\pi t)}{\pi t}")
    st.write("Zeros at integers; FT↔rect(f).")
    st.write("⚡Hack: ideal interpolation kernel.")

elif section == "3. Operations on Signals":
    st.header(section)
    st.markdown("""
- **Amplitude Scaling:**
  \[y(t)=A\,x(t)\]
  ⚡Hack: scales convolution output by A.

- **Time Shifting:**
  \[y(t)=x(t-T)\]
  ⚡Hack: in freq → multiply X(f) by e^{−j2πfT}.

- **Time Reversal:**
  \[y(t)=x(−t)\]
  ⚡Hack: spectrum flips X(f)→X(−f).

- **Time Scaling:**
  \[y(t)=x(a t)\]
  ⚡Hack: frequency scales X(f)→(1/|a|)X(f/a).

- **DT Shift:**
  \[y[n]=x[n−k]\]

- **DT Scale:**
  \[y[n]=x[k n]\] (decimate), \[x[n/k]\] (expand).
"""
)

elif section == "4. LTI System Properties":
    st.header(section)
    st.markdown("""
**BIBO Stability:** bounded input ⇒ bounded output if
\[\sum|h[n]|<\infty \quad\text{or}\quad \int|h(t)|dt<\infty\]
⚡Hack: check impulse-response area.

**Causality:** \[h(t)=0 \text{ for } t<0\]

**Memoryless:** \[h(t)=k\,\delta(t)\]

**Linearity:** S[a x1 + b x2] = a y1 + b y2

**Time-Invariance:** shift input ⇒ shift output
"""
)

elif section == "5. Convolution":
    st.header(section)
    st.markdown("""
**Continuous:**
\[y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau\]

**Discrete:**
\[y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]\]

⚡Hack: sketch h flipped then shifted to find overlap, then integrate.
"""
)

elif section == "6. Fourier Transform & Spectra":
    st.header(section)
    st.markdown("""
**Definition (CT):**
\[X(f)=\int x(t)e^{-j2\pi ft}dt, \quad x(t)=\int X(f)e^{j2\pi ft}df\]

**Key Pairs:**
- $\delta(t)\leftrightarrow1$  
- $1\leftrightarrow\delta(f)$  
- $e^{j2\pi f_0t}\leftrightarrow\delta(f-f_0)$  
- $\cos(2\pi f_0t)\leftrightarrow\tfrac12[\delta(f-f_0)+\delta(f+f_0)]$  
- $\mathrm{rect}(t/T)\leftrightarrow T\,\mathrm{sinc}(fT)$

⚡Hacks:
- Time shift → e^{-j2πfT}
- Time scale → 1/|a|X(f/a)
- Multiplication time ↔ convolution freq
"""
)

elif section == "7. Sampling & Aliasing":
    st.header(section)
    st.markdown("""
**Sampling model:**
\[x_s(t)=x(t)\sum_{n}\delta(t-nT_s), \quad T_s=1/f_s\]

**Spectrum:**
\[X_s(f)=f_s\sum_kX(f-kf_s)\]

⚡Hack: ensure $f_s/2 \ge f_{max}$ to avoid aliasing.
"""
)

else:
    st.header(section)
    st.markdown("""
**Time-domain AM:**
\[x_{AM}(t)=A_c\bigl[1+\mu m(t)\bigr]\cos(2\pi f_c t),\quad \mu=\frac{A_{max}-A_{min}}{A_{max}+A_{min}}\]

**Frequency-domain AM:**
Carrier at ±f_c plus sidebands f_c±f_m; BW=2B.

**Power Efficiency:**
\[P_c=\tfrac{A_c^2}{2},\quad P_{SB}=\tfrac{A_c^2\mu^2}{4},\quad \eta=\frac{2P_{SB}}{P_c+2P_{SB}}=\frac{\mu^2}{2+\mu^2}\]

⚡Hacks:
- Envelope detector works if μ≤1.
- Compute Pc & Psb quickly from A_max, A_min.
"""
)
