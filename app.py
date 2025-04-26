import streamlit as st

st.set_page_config(page_title="IE2110: Signals & Systems Revision", layout="wide")

st.title("IE2110: Signals & Systems — Detailed Revision Cheat Sheet")

# 1. Classification of Signals
st.header("1. Classification of Signals")
st.markdown(
    """
| **Property**               | **Definition**                                                                 | **⚡Quick Tip**                |
|----------------------------|--------------------------------------------------------------------------------|--------------------------------|
| Continuous vs Discrete     | CT: $x(t)$ defined ∀ real $t$; DT: $x[n]$ defined on integer $n$               | Look at argument: `t` vs `[n]` |
| Continuous vs Discrete Value | Amplitude ∈ ℝ vs amplitude ∈ finite set                                         | Smooth curve vs steps         |
| Even vs Odd                | Even: $x(t)=x(-t)$; Odd: $x(t)=-x(-t)$                                          | Test $x(t)\pm x(-t)$          |
| Periodic vs Aperiodic      | Periodic if ∃ $T_0>0$ s.t. $x(t)=x(t+T_0)$; else aperiodic                     | Sinusoids→periodic; decays→aperiodic |
| Energy vs Power type       | Energy: $E_x=\int|x|^2dt<\infty$; Power: $P_x=\lim\frac1T\int|x|^2dt<\infty$ | Periodic→power; pulses→energy   |
"""
)

st.markdown("""
**Examples:**  
- CT sinusoid $x(t)=\cos(2\pi f_0 t)$: periodic, power-type.  
- Exponential $x(t)=e^{-at}$: aperiodic, energy-type.  

**Diagnostic Flow:**  
1. Argument: `t` vs `[n]`  
2. Values: continuous vs discrete  
3. Symmetry: even/odd test  
4. Periodicity: find $T_0$  
5. Compute energy or power  
"""
)

# 2. Elementary & Singularity Signals
st.header("2. Elementary & Singularity Signals")
st.markdown(
    """
| **Signal**              | **Formula**                          | **Property**                                | **Tip**                       |
|-------------------------|--------------------------------------|---------------------------------------------|-------------------------------|
| Exponential             | $x(t)=Ae^{at}$                      | Growth if $a>0$, decay if $a<0$             | Sketch smooth curve           |
| Sinusoid                | $x(t)=A\cos(2\pi f_0t+\phi)$       | Periodic, $T_0=1/f_0$                       | Zero-mean, even-function      |
| Complex exponential     | $x(t)=A e^{j2\pi f_0t}$             | Single phasor at $+f_0$                     | Real part=cos, Imag=sin       |
| Impulse (δ)             | $\delta(t)$                          | Area 1; sampling property                  | Picks value at $t_0$          |
| Step (u)                | $u(t)=\begin{cases}1&t\ge0\\0&t<0\end{cases}$ | Derivative=δ(t)                       | Model causal signals          |
| Rectangular pulse       | $\mathrm{rect}(t/T)$                | Width $T$, height 1                         | FT ↔ $T\,\mathrm{sinc}(fT)$  |
| Sinc function           | $\mathrm{sinc}(t)=\frac{\sin(\pi t)}{\pi t}$ | Infinite duration, zeros at integers | FT ↔ $\mathrm{rect}(f)$      |
"""
)
st.markdown(
    """
**Key FT Pairs:**  
$\delta(t)\leftrightarrow1$,  $1\leftrightarrow\delta(f)$,  
$e^{j2\pi f_0t}\leftrightarrow\delta(f-f_0)$,  
$\cos(2\pi f_0t)\leftrightarrow\tfrac12[\delta(f-f_0)+\delta(f+f_0)]$,  
$\mathrm{rect}(t/T)\leftrightarrow T\,\mathrm{sinc}(fT)$,  
$\mathrm{sinc}(t)\leftrightarrow\mathrm{rect}(f)$  
"""
)

# 3. Operations on Signals
st.header("3. Operations on Signals")
st.markdown(
    """
1. **Amplitude Scaling:** $y(t)=A\,x(t)$ (vertical stretch by $A$)  
2. **Time Shifting:** $y(t)=x(t-T)$ (shift right by $T$; left if $T<0$)  
3. **Time Reversal:** $y(t)=x(-t)$ (mirror at origin)  
4. **Time Scaling:** $y(t)=x(a\,t)$  
   - $|a|>1$ compress;  $|a|<1$ expand;  $a<0$ includes flip  
5. **DT Shifting:** $y[n]=x[n-k]$ (shift by $k$ samples)  
6. **DT Scaling:** $y[n]=x[k\,n]$ (decimation) or $x[n/k]$ (expansion)  

**⚡Order:** reversal → scaling → shifting  
**Example:** $x(-2(t-1))$ → reverse → compress by 2 → shift right by 1  
"""
)

# 4. LTI System Properties
st.header("4. LTI System Properties")
st.markdown(
    """
| **Property**     | **Condition**                          | **Test/Formula**                       |
|------------------|----------------------------------------|----------------------------------------|
| BIBO Stability   | Bounded input ⇒ bounded output         | $\sum|h[n]|<\infty$ or $\int|h(t)|dt<\infty$ |
| Causality        | $h(t)=0$ for $t<0$                    | Output uses only past/present inputs   |
| Memoryless       | $y(t)$ depends only on $x(t)$          | $h(t)=k\,\delta(t)$ form             |
| Linearity        | Superposition holds                   | $S\{a x_1+b x_2\}=a S\{x_1\}+b S\{x_2\}$  |
| Time-Invariance  | $h(t,τ)=h(t-τ)$                       | Shift input → same shift in output     |
"""
)
st.markdown(
    """
**System Check Recipe:**  
1. Check $h(t)$ support $t<0$ → causality.  
2. Sum/integral of $|h|$ → stability.  
3. Impulse form → memoryless.  
4. Test additivity/homogeneity → linearity.  
5. Shift and compare → time-invariance.  
"""
)

# 5. Convolution
st.header("5. Convolution")
st.markdown(
    """
**Continuous:**  
$$y(t)=\int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$$
**Discrete:**  
$$y[n]=\sum_{m=-\infty}^{\infty} x[m]\,h[n-m]$$

**⚡Graphical Steps:**  
1. Flip $h(θ)→h(-θ)$  
2. Shift $h(-θ)→h(t-θ)$  
3. Multiply $x(θ)·h(t-θ)$  
4. Integrate/sum where both nonzero  

**Tip:** Sketch support bounds to limit integration range.  
"""
)

# 6. Fourier Transform & Spectra
st.header("6. Fourier Transform & Spectra")
st.markdown(
    """
### CT Definition  
$$X(f)=\int_{-\infty}^{\infty} x(t)e^{-j2\pi ft}\,dt, \quad x(t)=\int_{-\infty}^{\infty} X(f)e^{j2\pi ft}\,df$$

### Key Pairs  
- $\delta(t)\leftrightarrow1$  
- $1\leftrightarrow\delta(f)$  
- $e^{j2\pi f_0t}\leftrightarrow\delta(f-f_0)$  
- $\cos(2\pi f_0t)\leftrightarrow\tfrac12[\delta(f-f_0)+\delta(f+f_0)]$  
- $\mathrm{rect}(t/T)\leftrightarrow T\,\mathrm{sinc}(fT)$  

### Magnitude & Phase  
- Cosine → spikes at ±$f_0$, height=$A/2$, phase=0°  
- Sine → spikes at ±$f_0$, height=$A/2$, phase=+90°/−90°  

**⚡Sketching Trick:** Draw magnitude first, then overlay phase.  
"""
)

# 7. Sampling & Aliasing
st.header("7. Sampling & Aliasing")
st.markdown(
    """
**Sampling Model:**  
$$x_s(t)=x(t)\sum_n\delta(t-nT_s), \quad T_s=1/f_s$$

**Frequency Domain:**  
$$X_s(f)=f_s\sum_k X(f - kf_s)$$

**Nyquist:**  
To avoid aliasing: $$f_s > 2B$$ where $B$ = max signal frequency.  

**⚡Tip:** Ensure $B \le f_s/2$ before sampling.  
"""
)

# 8. Amplitude Modulation (AM)
st.header("8. Amplitude Modulation (AM)")
st.markdown(
    """
### Time-Domain  
$$x_{AM}(t)=A_c\bigl[1+\mu\,m(t)\bigr]\cos(2\pi f_c t)$$
- Modulation index $$\mu=\max|k_a m(t)|\,,\quad \mu\le1$$ for no distortion  

### Frequency-Domain  
Carrier at ±$f_c$, sidebands at $f_c\pm f_m$  
$$X_{AM}(f)=\frac{A_c}{2}[\delta(f-f_c)+\delta(f+f_c)] + \frac{A_c \mu}{2}[M(f-f_c)+M(f+f_c)]$$  
- **Bandwidth** = $2B$  

### Power Efficiency  
- Carrier power: $P_c=A_c^2/2$  
- Sideband power: $P_{SB}=A_c^2 \mu^2/4$  
- Efficiency: $$\eta=\frac{2P_{SB}}{P_c+2P_{SB}}=\frac{\mu^2}{2+\mu^2}$$  

**⚡AM Tips**  
- $$\mu=\frac{A_{max}-A_{min}}{A_{max}+A_{min}}$$ via envelope.  
- If $\mu>1$, envelope crosses zero → distortion.  
- Envelope detector recovers $m(t)$ only if $\mu\le1$.  
"""
)

st.sidebar.title("Navigation")
st.sidebar.markdown("Use headings to quickly jump to sections.")
