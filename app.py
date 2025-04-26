import streamlit as st

# Page configuration
st.set_page_config(page_title="IE2110 Revision Cheat Sheet", layout="wide")

# Title
st.title("IE2110: Signals & Systems — Revision Cheat Sheet & Hacks")

# Table of Contents
st.markdown("""
**Contents**  
1. Classification of Signals  
2. Elementary & Singularity Signals  
3. Operations on Signals  
4. LTI System Properties  
5. Convolution  
6. Fourier Transform & Spectra  
7. Sampling & Aliasing  
8. Amplitude Modulation  
""")

# 1. Classification of Signals
st.header("1. Classification of Signals")

st.subheader("1.1 Continuous vs Discrete Signals")
st.markdown("""
**Definition:** A continuous-time signal is $x(t)$ for real $t$.  
A discrete-time signal is $x[n]$ for integer $n$.  

$$x(t)\quad\text{vs}\quad x[n]$$

⚡ Quick Tip: spot `t` vs `[n]`.  
""")

st.subheader("1.2 Continuous-Value vs Discrete-Value Signals")
st.markdown("""
**Definition:** Continuous-value signal amplitudes lie in $\mathbb{R}$.  
Discrete-value amplitudes take values from a finite set.  

⚡ Quick Tip: smooth curve vs staircase plot.  
""")

st.subheader("1.3 Even vs Odd Signals")
st.markdown("""
**Even:** $x(t) = x(-t)$.  **Odd:** $x(t) = -x(-t)$.  

$$x_e(t)=\frac{1}{2}[x(t)+x(-t)],\quad x_o(t)=\frac{1}{2}[x(t)-x(-t)]$$

⚡ Hack: any odd-signal integral over symmetric limits is zero.  
""")

st.subheader("1.4 Periodic vs Aperiodic Signals")
st.markdown("""
**Periodic:** there exists $T_0>0$ such that $x(t)=x(t+T_0)$.  
**Aperiodic:** no finite $T_0$ satisfies this.  

⚡ Quick Tip: pure sinusoids are periodic; decaying exponentials are aperiodic.  
""")

st.subheader("1.5 Energy-Type vs Power-Type Signals")
st.markdown("""
**Energy:** $$E=\int_{-\infty}^{\infty}|x(t)|^2\,dt < \infty.$$  
**Power:** $$P=\lim_{T\to\infty}\frac{1}{T}\int_{-T/2}^{T/2}|x(t)|^2\,dt < \infty.$$  

⚡ Quick Tip: periodic signals ⇒ power-type; pulses/exponentials ⇒ energy-type.  
""")

# 2. Elementary & Singularity Signals
st.header("2. Elementary & Singularity Signals")

st.subheader("2.1 Exponential Signal")
st.markdown("""
**Formula:** $$x(t)=A e^{a t}$$  
⚡ Hack: appears in LTI homogeneous solution.  
""")

st.subheader("2.2 Sinusoidal Signal")
st.markdown("""
**Formula:** $$x(t)=A \cos(2\pi f_0 t + \phi)$$  
Periodic with period $T_0=1/f_0$.  
⚡ Hack: cosine is even, sine is odd (±90° phase).  
""")

st.subheader("2.3 Complex Exponential Signal")
st.markdown("""
**Formula:** $$x(t)=A e^{j2\pi f_0 t}$$  
Represents a single spectral line at $f_0$.  
⚡ Hack: use phasors for sinusoid sums.  
""")

st.subheader("2.4 Impulse Function")
st.markdown("""
**Formula:** $$\delta(t)$$  
Area = 1; sampling: $$x(t)*\delta(t-t_0)=x(t_0).$$  
⚡ Hack: convolution with δ shifts the argument.  
""")

st.subheader("2.5 Step Function")
st.markdown("""
**Formula:** $$u(t)=\begin{cases}1, & t\ge0\\0, & t<0\end{cases}$$  
Derivative = δ(t).  
⚡ Hack: use u(t) to gate signals in integrals.  
""")

st.subheader("2.6 Rectangular Pulse")
st.markdown("""
**Formula:** $$\mathrm{rect}\bigl(\frac{t}{T}\bigr)$$  
Width $T$, FT ↔ $T\,\mathrm{sinc}(fT)$.  
⚡ Hack: ideal LPF impulse in time domain.  
""")

st.subheader("2.7 Sinc Function")
st.markdown("""
**Formula:** $$\mathrm{sinc}(t)=\frac{\sin(\pi t)}{\pi t}$$  
Zeros at nonzero integers; FT ↔ rect(f).  
⚡ Hack: ideal interpolation kernel.  
""")

# 3. Operations on Signals
st.header("3. Operations on Signals")

st.markdown("""
**Amplitude Scaling**  
$$y(t)=A\,x(t)$$  
⚡ Hack: multiplies convolution output by A.  

**Time Shifting**  
$$y(t)=x(t-T)$$  
⚡ Hack: in freq domain, multiply X(f) by $e^{-j2\pi fT}$.  

**Time Reversal**  
$$y(t)=x(-t)$$  
⚡ Hack: flips spectrum: $X(f)\to X(-f)$.  

**Time Scaling**  
$$y(t)=x(a t)$$  
⚡ Hack: freq scales: $X(f)\to \frac{1}{|a|}X(\frac{f}{a})$.  

**DT Shift**  
$$y[n]=x[n-k]$$  

**DT Scale**  
$$y[n]=x[k n]\quad\text{(decimate)},\quad y[n]=x[n/k]\text{(expand)}$$  
""")

# 4. LTI System Properties
st.header("4. LTI System Properties")

st.markdown("""
**BIBO Stability**: bounded input ⇒ bounded output if  
$$\sum_{n=-\infty}^{\infty}|h[n]|<\infty\quad\text{or}\quad\int_{-\infty}^{\infty}|h(t)|dt<\infty.$$  

**Causality**:  $$h(t)=0 \text{ for } t<0.$$  

**Memoryless**:  $$h(t)=k\,\delta(t).$$  

**Linearity**: superposition holds.  

**Time-Invariance**: shift input ⇒ shift output.  
""")

# 5. Convolution
st.header("5. Convolution")

st.markdown("""
**Continuous:**  
$$y(t)=\int_{-\infty}^{\infty}x(\tau)\,h(t-\tau)\,d\tau$$

**Discrete:**  
$$y[n]=\sum_{m=-\infty}^{\infty}x[m]\,h[n-m]$$

⚡ Hack: find overlap region first, then multiply & integrate.  
""")

# 6. Fourier Transform & Spectra
st.header("6. Fourier Transform & Spectra")

st.markdown("""
**Definition (CT):**  
$$X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}dt,\quad x(t)=\int_{-\infty}^{\infty}X(f)e^{j2\pi ft}df$$

**Key Pairs:**  
- $\delta(t)\leftrightarrow1$  
- $1\leftrightarrow\delta(f)$  
- $e^{j2\pi f_0t}\leftrightarrow\delta(f-f_0)$  
- $\cos(2\pi f_0t)\leftrightarrow\tfrac12[\delta(f-f_0)+\delta(f+f_0)]$  
- $\mathrm{rect}(t/T)\leftrightarrow T\,\mathrm{sinc}(fT)$  

⚡ Hacks: time shift→phase; scale→freq scale; mult→conv.  
""")

# 7. Sampling & Aliasing
st.header("7. Sampling & Aliasing")

st.markdown("""
**Model:**  
$$x_s(t)=x(t)\sum_{n}\delta(t-nT_s),\quad T_s=1/f_s$$

**Spectrum:**  
$$X_s(f)=f_s\sum_{k}X(f-kf_s)$$

⚡ Hack: ensure $f_s/2\ge f_{\max}$ to avoid aliasing.  
""")

# 8. Amplitude Modulation
st.header("8. Amplitude Modulation")

st.markdown("""
**Time-Domain:**  
$$x_{AM}(t)=A_c[1+\mu m(t)]\cos(2\pi f_c t),\quad \mu=\frac{A_{max}-A_{min}}{A_{max}+A_{min}}\le1$$

**Freq-Domain:** carrier at ±f_c; sidebands at f_c±f_m; BW=2B.  

**Power:**  
$$P_c=\frac{A_c^2}{2},\quad P_{SB}=\frac{A_c^2\mu^2}{4},\quad\eta=\frac{\mu^2}{2+\mu^2}$$

⚡ Hacks: envelope detects if μ≤1; compute Pc,Psb from Amax,Amin.  
""" )
