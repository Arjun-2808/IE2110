import streamlit as st
import pandas as pd

st.set_page_config(page_title="IE2110: Signals & Systems Revision", layout="wide")

st.title("IE2110: Signals and Systems — Detailed Cheat Sheet & Revision App")

# --- Section 1: Classification of Signals ---
with st.expander("1. Classification of Signals (CT vs DT, Even/Odd, Periodic/Aperiodic, Energy/Power)", expanded=False):
    df1 = pd.DataFrame([
        {"Property": "Continuous vs Discrete",
         "Definition": "CT: x(t) defined ∀ real t; DT: x[n] defined on integer n", 
         "Key-Check": "Argument notation (t vs [n])",
         "⚡Tip": "t→CT, [n]→DT"},
        {"Property": "Continuous-Value vs Discrete-Value", 
         "Definition": "Amplitude ∈ ℝ vs amplitude ∈ finite set", 
         "Key-Check": "Plot shape (smooth vs steps)", 
         "⚡Tip": "Shape: continuous curve vs staircase"},
        {"Property": "Even vs Odd", 
         "Definition": "Even: x(t)=x(-t); Odd: x(t)=-x(-t)", 
         "Key-Check": "Test x(t)±x(-t)",
         "⚡Tip": "Even→sum nonzero, Odd→difference nonzero"},
        {"Property": "Periodic vs Aperiodic", 
         "Definition": "∃ T0>0: x(t)=x(t+T0); otherwise aperiodic", 
         "Key-Check": "Find fundamental period for sinusoids", 
         "⚡Tip": "Sinusoid→periodic, decays→aperiodic"},
        {"Property": "Energy-Type vs Power-Type", 
         "Definition": "Energy E=∫|x|² dt finite vs Power P=lim(1/T)∫|x|² dt finite", 
         "Key-Check": "Periodic→power, pulses/exponential→energy", 
         "⚡Tip": "Periodicity⇒power signal"}
    ])
    st.dataframe(df1)
    st.markdown(
        """
**Examples:**
- CT sinusoid x(t)=cos(2πf0 t) → periodic, power-type.  
- Exponential x(t)=e^{-at} → aperiodic, energy-type.  

**Quick Diagnostic Flow:**
1. Look at argument (t vs n)  
2. Check amplitude values (continuous vs discrete)  
3. Test symmetry (x(t) ± x(-t))  
4. Check periodicity: try candidate T0  
5. Compute energy or power formula  
"""
    )

# --- Section 2: Elementary & Singularity Signals ---
with st.expander("2. Elementary & Singularity Signals (Functions & FT Pairs)", expanded=False):
    signals = [
        ("Exponential Signal", "x(t)=A e^{at}", "Growth/decay depending on a", "Plot smooth exponential curve"),
        ("Sinusoidal Signal", "x(t)=A cos(2πf0 t + φ)", "Periodic, T0=1/f0", "Zero-mean, even mapping"),
        ("Complex Exponential", "x(t)=A e^{j2πf0 t}", "Rotating phasor", "Real part=cos, Imag=sin"),
        ("Impulse (δ)", "δ(t)", "Area=1, picks x(t0)", "Sampling property"),
        ("Unit Step (u)", "u(t)=1[t≥0]", "Derivative=δ(t)", "Define causal signals"),
        ("Signum", "sgn(t)", "Sign of t", "Odd function test"),
        ("Rectangular Pulse", "rect(t/T)", "Width T, height 1", "FT→T·sinc(fT)"),
        ("Sinc Function", "sinc(t)=sin(πt)/(πt)", "Infinite duration, zero crossings at integers", "FT→rect(f)")
    ]
    df2 = pd.DataFrame(signals, columns=["Signal","Formula","Property","⚡Revision Tip"])
    st.dataframe(df2)
    st.markdown(
        """
**Fourier Transform Pairs to Remember:**  
- δ(t) ↔ 1  
- 1 ↔ δ(f)  
- rect(t/T) ↔ T·sinc(fT)  
- sinc(t) ↔ rect(f)  
- e^{j2πf0 t} ↔ δ(f−f0)  
- cos(2πf0 t) ↔ ½[δ(f−f0)+δ(f+f0)]  
- sin(2πf0 t) ↔ (1/2j)[δ(f−f0)−δ(f+f0)]  
"""
    )

# --- Section 3: Operations on Signals ---
with st.expander("3. Signal Operations (Time & Amplitude Manipulations)", expanded=False):
    ops = [
        ("Amplitude Scaling", "y(t)=A·x(t)", "Vertical stretch/compress"),
        ("Time Shifting", "y(t)=x(t−T)", "Shift right by T, left if T<0"),
        ("Time Reversal", "y(t)=x(−t)", "Mirror at origin"),
        ("Time Scaling", "y(t)=x(a·t)", "Compress if |a|>1, expand if |a|<1, flip if a<0"),
        ("Time Shifting DT", "y[n]=x[n−k]", "Shift sequence by k samples"),
        ("Time Scaling DT", "y[n]=x[k·n] or x[n/k]", "Decimation or interpolation")
    ]
    df3 = pd.DataFrame(ops, columns=["Operation","Formula","Effect"])
    st.dataframe(df3)
    st.markdown(
        """
**⚡Order of Operations:** Always perform **time reversal → scaling → shifting** to avoid confusion.  

**Example:** y(t)=x(−2(t−1)) = reverse → compress by 2 → shift right by 1.  
"""
    )

# --- Section 4: LTI System Properties ---
with st.expander("4. System Properties (LTI Basics)", expanded=False):
    props = [
        ("BIBO Stability", "Bounded input→bounded output", "∑|h[n]|<∞ or ∫|h(t)|dt<∞"),
        ("Causality", "h(t)=0 for t<0", "Output only depends on past/present") ,
        ("Memoryless", "y(t) depends only on x(t)", "h(t)=k·δ(t) form"),
        ("Linearity", "Superposition: S(ax1+bx2)=aS(x1)+bS(x2)", "Test additivity & homogeneity"),
        ("Time-Invariance", "h(t,τ)=h(t−τ)", "Response unchanged over shifts")
    ]
    df4 = pd.DataFrame(props, columns=["Property","Condition","Test Formula"])
    st.dataframe(df4)
    st.markdown(
        """
**⚡System Diagnostic Recipe:**  
1. Check h(t) support for t<0 → causality.  
2. Sum of absolute h(t) → stability.  
3. Form of h(t) (δ-scale) → memoryless.  
4. Superposition on sample inputs → linearity.  
5. Shift inputs and compare outputs → T-invariance.  
"""
    )

# --- Section 5: Convolution ---
with st.expander("5. Convolution (Graphical & Algebraic)", expanded=False):
    st.markdown(
        """
**Continuous Convolution:**  
\[y(t)=\int_{-\infty}^{\infty} x(τ)·h(t−τ) dτ\]  
**Discrete Convolution:**  
\[y[n]=\sum_{m=-\infty}^{\infty} x[m]·h[n−m]\]  

**⚡Graphical Steps:**  
1. Flip h(θ)→h(−θ).  
2. Shift: h(−θ)→h(t−θ).  
3. Multiply x(θ)·h(t−θ).  
4. Integrate/sum over θ where both non-zero.  

**Tip:** Sketch support intervals first to limit integration range.  
"""
    )

# --- Section 6: Fourier Transform & Spectra ---
with st.expander("6. Fourier Transform & Spectral Sketching", expanded=False):
    st.markdown(
        """
### Definition (CT)
\[X(f)=\int_{-\infty}^{\infty} x(t)e^{-j2πft}dt\],  
\[x(t)=\int_{-\infty}^{\infty} X(f)e^{j2πft}df\]

### Key Transform Pairs:
- δ(t) ↔ 1  
- 1 ↔ δ(f)  
- e^{j2πf0t} ↔ δ(f−f0)  
- cos(2πf0t) ↔ ½[δ(f−f0)+δ(f+f0)]  
- sin(2πf0t) ↔ 1/(2j)[δ(f−f0)−δ(f+f0)]  
- rect(t/T) ↔ T·sinc(fT)  
- sinc(t) ↔ rect(f)

### Magnitude & Phase:
- Cosine: spikes at ±f0, height=A/2, phase=0°  
- Sine: spikes at ±f0, height=A/2, phase=+90° at +f0, −90° at −f0

**⚡Sketching Trick:** Always draw magnitude first, then overlay phase.  
"""
    )

# --- Section 7: Sampling Theory ---
with st.expander("7. Sampling & Aliasing", expanded=False):
    st.markdown(
        """
**Sampling Model:**  
\[x_s(t)=x(t)·\sum_{n}δ(t−nTs),\quad Ts=1/fs\]  

**Frequency Domain:**  
\[X_s(f)=f_s\sum_k X(f−kf_s)\]  

**Nyquist Criterion:**  
To avoid aliasing: \[f_s>2B\], where B=max signal freq.  

**⚡Tip:** Always check highest frequency in X(f) against fs/2.  
"""
    )

# --- Section 8: Amplitude Modulation ---
with st.expander("8. Amplitude Modulation (Time & Frequency)", expanded=False):
    st.markdown(
        """
### Time-Domain AM:
\[x_{AM}(t)=A_c[1+μm(t)] cos(2πf_c t)\]
- μ (modulation index)=max|ka m(t)| → under-modulation μ≤1, over-modulation μ>1

### Frequency-Domain:
Carrier at ±f_c plus sidebands from f_c−B to f_c+B  
\[X_{AM}(f)=\frac{A_c}{2}[δ(f−f_c)+δ(f+f_c)] + \frac{A_c μ}{2}[M(f−f_c)+M(f+f_c)]\]
- **Bandwidth**=2B

### Power Calculations:
- Carrier power Pc= A_c^2/2  
- Sideband power Ps= (A_c^2 μ^2)/4 (in each sideband)  
- Efficiency η=Ps_total/(Pc+Ps_total)=μ^2/(2+μ^2)

**⚡AM Tips:**
- Compute μ via envelope: (Amax−Amin)/(Amax+Amin).  
- If μ>1 the envelope crosses zero → distortion & phase reversal.  
- Envelope detector recovers m(t) only if μ≤1.  
"""
    )

st.sidebar.title("Navigation")
st.sidebar.markdown("Use the sections to expand/collapse topics for deep revision.")
