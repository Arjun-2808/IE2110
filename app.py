import streamlit as st

# Page configuration
st.set_page_config(page_title="IE2110 Revision Cheat Sheet", layout="wide")

# Title
st.title("IE2110: Signals & Systems — Detailed Revision Cheat Sheet & Hacks")

# Section 1: Classification of Signals
st.header("1. Classification of Signals")

# Continuous vs Discrete
st.subheader("1.1 Continuous vs Discrete Signals")
st.write(
    "**Definition:** CT uses $x(t)$ (continuous $t$), DT uses $x[n]$ (integer $n$)."
)
st.write("**Quick Tip:** Check argument: `t` ⇒ CT, `[n]` ⇒ DT.")
st.write("⚡HACK: In MCQs, simply spot the variable type to categorize signal immediately.")

# Continuous vs Discrete Value
st.subheader("1.2 Continuous‐Value vs Discrete‐Value Signals")
st.write(
    "**Definition:** Continuous‐value amplitude ∈ ℝ; discrete‐value has finite levels."
)
st.write("**Quick Tip:** Smooth curve ⇒ continuous; steps/dots ⇒ discrete.")
st.write("⚡HACK: When given a quantized signal, assume discrete‐value by default.")

# Even vs Odd
st.subheader("1.3 Even vs Odd Signals")
st.write(
    "**Definition:** Even: $x(t)=x(-t)$; Odd: $x(t)=-x(-t)$."
)
st.write("**Test:** Compute $x(t) ± x(-t)$." )
st.write("⚡HACK: For integrals, odd signals integrate to zero over symmetric limits—use to shortcut convolution/energy.")

# Periodic vs Aperiodic
st.subheader("1.4 Periodic vs Aperiodic Signals")
st.write(
    "**Definition:** Periodic if ∃ $T_0$ such that $x(t)=x(t+T_0)$; else aperiodic."
)
st.write("**Quick Tip:** Sinusoids are periodic; decays/ramps are aperiodic.")
st.write("⚡HACK: For sums of sinusoids, check ratio of frequencies for periodicity (rational = periodic).")

# Energy vs Power type
st.subheader("1.5 Energy‑Type vs Power‑Type Signals")
st.write("**Energy:** $E=\int|x|^2dt<∞$. **Power:** $P=\lim\frac1T\int|x|^2dt<∞$." )
st.write("**Quick Tip:** Periodic signals ⇒ power‐type; pulses/decays ⇒ energy‐type.")
st.write("⚡HACK: If you need to compute integral, choose appropriate formula (energy vs power) to simplify limits.")

# Section 2: Elementary & Singularity Signals
st.header("2. Elementary & Singularity Signals")

# List of signals
signals = [
    ("Exponential", r"x(t)=Ae^{at}", "Growth if a>0; decay if a<0.", "⚡HACK: Use for LTI response tests."),
    ("Sinusoid", r"x(t)=A\cos(2\pi f_0 t + \phi)", "Periodic, T0=1/f0.", "⚡HACK: Cosine has zero phase if φ=0; sine = ±90°.") ,
    ("Complex Exponential", r"x(t)=Ae^{j2\pi f_0 t}", "Single spike at f0.", "⚡HACK: Use phasor for summing sinusoids.") ,
    ("Impulse (δ)", r"\delta(t)", "Area=1, picks x(t0)", "⚡HACK: Convolution with δ shifts function: x*δ = x.") ,
    ("Step (u)", r"u(t)=\begin{cases}1&t\ge0\\0&t<0\end{cases}", "Derivative=δ(t)", "⚡HACK: Use to build piecewise definitions quickly.") ,
    ("Rectangular Pulse", r"\mathrm{rect}(t/T)", "Width T; FT ↔ T·sinc(fT)", "⚡HACK: Use to derive sinc shapes in frequency.") ,
    ("Sinc Function", r"\mathrm{sinc}(t)=\sin(\pi t)/(\pi t)", "FT ↔ rect(f)", "⚡HACK: Ideal low-pass impulse response.")
]
for name, formula, note, hack in signals:
    st.subheader(name)
    st.latex(formula)
    st.write(f"**Note:** {note}")
    st.write(hack)

# Section 3: Operations on Signals
st.header("3. Operations on Signals")
ops = [
    ("Amplitude Scaling", r"y(t)=A\,x(t)", "Vertical stretch by A.", "⚡HACK: Amplitude scaling distributes through convolution.") ,
    ("Time Shifting", r"y(t)=x(t-T)", "Shift right by T (left if T<0).", "⚡HACK: In frequency domain, introduces phase factor e^{-j2πfT}.") ,
    ("Time Reversal", r"y(t)=x(-t)", "Mirror around vertical axis.", "⚡HACK: Reversal flips spectrum: X(f)->X(-f).") ,
    ("Time Scaling", r"y(t)=x(a t)", "Compress if |a|>1; expand if |a|<1; flip if a<0.", "⚡HACK: Frequency domain scaling: X(f)->(1/|a|)X(f/a).") ,
    ("DT Shifting", r"y[n]=x[n-k]", "Shift by k samples.", "⚡HACK: Multiply X(e^{jω}) by e^{-jωk} in DTFT.") ,
    ("DT Scaling", r"y[n]=x[k n] or x[n/k]", "Decimation or expansion.", "⚡HACK: Watch for aliasing when decimating.")
]
for title, formula, desc, hack in ops:
    st.subheader(title)
    st.latex(formula)
    st.write(f"**Effect:** {desc}")
    st.write(hack)

# Section 4: LTI System Properties
st.header("4. LTI System Properties & Hacks")
properties = [
    ("BIBO Stability", r"Bounded input -> bounded output", r"\sum |h[n]|<∞ or ∫|h(t)|dt<∞", "⚡HACK: Check impulse response sum/integral quickly.") ,
    ("Causality", r"Output depends only on past/present inputs", r"h(t)=0 for t<0", "⚡HACK: In convolution, integrate from 0 to t.") ,
    ("Memoryless", r"Output depends only on x(t)", r"h(t)=k δ(t)", "⚡HACK: y(t)=k x(t).") ,
    ("Linearity", r"Superposition holds", r"S[a x1 + b x2] = a y1 + b y2", "⚡HACK: Test with simple impulses.") ,
    ("Time‑Invariant", r"Shifting input shifts output", r"h(t,τ)=h(t-τ)", "⚡HACK: Compare y1(t) vs y2(t-T).")
]
for name, desc, cond, hack in properties:
    st.subheader(name)
    st.write(f"**Condition:** {desc}")
    st.latex(cond)
    st.write(hack)

# Section 5: Convolution
st.header("5. Convolution & Quick Hacks")
st.write("**CT:** y(t)=∫ x(τ) h(t-τ) dτ  |  **DT:** y[n]=∑ x[m] h[n-m]")
st.write("**Graphical Steps:** Flip → Shift → Multiply → Sum/Integrate")
st.write("⚡HACK: Always identify overlapping intervals first to simplify integrals.")
st.write("⚡HACK: For LTI tests, convolve with δ to retrieve impulse response.")

# Section 6: Fourier Transform & Spectra
st.header("6. Fourier Transform & Spectral Hacks")
st.write("**Definition:** X(f)=∫ x(t)e^{-j2πft}dt; x(t)=∫ X(f)e^{j2πft}df")
st.write("⚡HACK: Use symmetry: real even signals have real even spectra.")
st.write("⚡HACK: Time shift → linear phase factor.")
st.write("⚡HACK: Time scaling → frequency scaling by 1/a.")
st.write("⚡HACK: Multiplication in time → convolution in frequency.")
st.write("⚡HACK: Convolution in time → multiplication in frequency.")

# Section 7: Sampling & Aliasing
st.header("7. Sampling & Aliasing Hacks")
st.write("**Model:** x_s(t)=x(t)∑ δ(t-nT_s), T_s=1/f_s")
st.write("⚡HACK: Always check aliasing: f_s/2 ≥ max freq.")
st.write("⚡HACK: Use ideal LPF to reconstruct if no aliasing.")

# Section 8: Amplitude Modulation
st.header("8. Amplitude Modulation (AM) Hacks")
st.write("**Time:** x_AM=Ac[1+μm(t)]cos(2πf_c t); μ=(Amax-Amin)/(Amax+Amin)")
st.write("⚡HACK: Envelope detection works only if μ≤1.")
st.write("⚡HACK: Sideband bandwidth=2B.")
st.write("⚡HACK: Compute power distribution: Pc vs Psb.")
st.write("⚡HACK: For suppressed carrier, multiply by cos then filter.")

st.sidebar.title("Jump to Section")
st.sidebar.markdown("Use headers to navigate quickly.")
