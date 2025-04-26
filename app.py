import streamlit as st

# Page configuration
st.set_page_config(page_title="IE2110 Revision Cheat Sheet", layout="wide")

# Sidebar navigation links
st.sidebar.title("Sections")
st.sidebar.markdown(
    """
- [1. Classification of Signals](#1-classification-of-signals)
- [2. Elementary & Singularity Signals](#2-elementary--singularity-signals)
- [3. Operations on Signals](#3-operations-on-signals)
- [4. LTI System Properties & Hacks](#4-lti-system-properties--hacks)
- [5. Convolution & Quick Hacks](#5-convolution--quick-hacks)
- [6. Fourier Transform & Spectral Hacks](#6-fourier-transform--spectral-hacks)
- [7. Sampling & Aliasing Hacks](#7-sampling--aliasing-hacks)
- [8. Amplitude Modulation (AM) Hacks](#8-amplitude-modulation-am-hacks)
"""
)

# Title
st.title("IE2110: Signals & Systems — Detailed Revision Cheat Sheet & Hacks")

# 1. Classification of Signals
st.header("1. Classification of Signals")

st.markdown("""
**1.1 Continuous vs Discrete Signals**  
**Definition:** Continuous-time: $x(t)$; Discrete-time: $x[n]$.  
**⚡Tip:** Look at argument (`t` vs `[n]`).
""")

st.markdown("""
**1.2 Continuous‐Value vs Discrete‐Value Signals**  
**Definition:** Continuous‐value amplitude ∈ ℝ; Discrete‐value: finite levels.  
**⚡Tip:** Smooth curve vs staircase.
""")

st.markdown("""
**1.3 Even vs Odd Signals**  
**Definition:** Even: $x(t)=x(-t)$; Odd: $x(t)=-x(-t)$.  
**⚡Hack:** $\int_{-A}^A x_{odd}(t)dt=0$.  
""")

st.markdown("""
**1.4 Periodic vs Aperiodic Signals**  
**Definition:** Periodic: $x(t)=x(t+T_0)$ exists $T_0>0$; else aperiodic.  
**⚡Tip:** Sinusoids periodic, exponentials aperiodic.
""")

st.markdown("""
**1.5 Energy‐Type vs Power‐Type Signals**  
Energy: $E=\int_{-\infty}^{\infty}|x(t)|^2dt<\infty$.  
Power: $P=\lim_{T\to\infty}\tfrac1T\int_{-T/2}^{T/2}|x(t)|^2dt<\infty$.  
**⚡Tip:** Periodic ⇒ power‐type; pulses/decays ⇒ energy‐type.
""")

# 2. Elementary & Singularity Signals
st.header("2. Elementary & Singularity Signals")

st.markdown("""
**Exponential:**  $x(t)=Ae^{at}$ — growth/decay.  
**Sinusoid:**  $x(t)=A\cos(2\pi f_0t+\phi)$ — periodic, $T_0=1/f_0$.  
**Complex Exp.:**  $x(t)=Ae^{j2\pi f_0t}$ — single spike at $±f_0$.  
**Impulse:**  $\delta(t)$ — area=1, sampling: $x*\delta=x$.  
**Step:**  $u(t)=1[t\ge0]$ — derivative $=\delta(t)$.  
**Rectangular:**  $\mathrm{rect}(t/T)$ — width $T$, FT↔$T\,\mathrm{sinc}(fT)$.  
**Sinc:**  $\mathrm{sinc}(t)=\frac{\sin(\pi t)}{\pi t}$ — FT↔rect.
""")

# 3. Operations on Signals
st.header("3. Operations on Signals")

st.markdown("""
- **Amplitude Scaling:**  $y(t)=A\,x(t)$ — vertical stretch.  
- **Time Shifting:**  $y(t)=x(t-T)$ — shift right $T$.  
- **Time Reversal:**  $y(t)=x(-t)$ — mirror.  
- **Time Scaling:**  $y(t)=x(a\,t)$ — compress $|a|>1$, expand $|a|<1$.  
- **DT Shift:**  $y[n]=x[n-k]$.  
- **DT Scale:**  $y[n]=x[k\,n]$ (decimate), $x[n/k]$ (expand).

**⚡Hack:** Chain: reverse → scale → shift.  
""")

# 4. LTI System Properties & Hacks
st.header("4. LTI System Properties & Hacks")

st.markdown("""
**BIBO Stability:**  bounded input ⇒ bounded output if  
$\sum|h[n]|<\infty$ or $\int|h(t)|dt<\infty$.  
**Causality:**  $h(t)=0$ for $t<0$.  
**Memoryless:**  $h(t)=k\,\delta(t)$.  
**Linearity:**  superposition holds.  
**Time-Invariant:**  shift input ⇒ shift output.

**⚡Hacks:**  
- Stability: sum/integral of |h|.  
- Causality: integration limits from 0.  
- Memoryless: y(t)=k·x(t).  
""")

# 5. Convolution & Quick Hacks
st.header("5. Convolution & Quick Hacks")

st.markdown("""
**CT:** $y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau$  
**DT:** $y[n]=\sum x[m]h[n-m]$  

**Graphical:** flip h→shift→multiply→integrate.  
**⚡Hack:** find overlap interval first.  
""")

# 6. Fourier Transform & Spectral Hacks
st.header("6. Fourier Transform & Spectral Hacks")

st.markdown("""
**Definition:**  $X(f)=\int x(t)e^{-j2\pi ft}dt$;  $x(t)=\int X(f)e^{j2\pi ft}df$.  
**Key Pairs:**  δ↔1; 1↔δ;  e^{j2πf₀t}↔δ(f−f₀);  cos↔½[δ(f±f₀)];  rect(t/T)↔T·sinc(fT).  

**⚡Hacks:**  
- Time shift⇒phase factor e^{-j2πfT}.  
- Time scale⇒freq scale 1/a.  
- Multi in time⇒conv in freq & vice versa.  
""")

# 7. Sampling & Aliasing Hacks
st.header("7. Sampling & Aliasing Hacks")

st.markdown("""
$x_s(t)=x(t)\sum_nδ(t−nT_s)$,  $T_s=1/f_s$.  
$X_s(f)=f_s\sum_kX(f−kf_s)$.  
**⚡Hack:** ensure $f_s/2≥f_{max}$ to avoid aliasing.  
""")

# 8. Amplitude Modulation (AM) Hacks
st.header("8. Amplitude Modulation (AM) Hacks")

st.markdown("""
Time: $x_{AM}=A_c[1+μm(t)]cos(2πf_c t)$,  μ=(Amax−Amin)/(Amax+Amin)≤1.  
Freq: carrier at ±f_c, sidebands f_c±f_m; BW=2B.  
Efficiency η=μ²/(2+μ²).  

**⚡Hacks:**  
- Envelope detector works if μ≤1.  
- Compute Pc & Psb: Pc=A_c²/2, Psb=A_c²μ²/4.  
""")
