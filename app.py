import streamlit as st

st.set_page_config(
    page_title="IE2110 Signals & Systems Master Review",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Sidebar navigation ---
st.sidebar.title("IE2110 Review")
sections = {
    "1. Signals & Systems Overview": [
        "1.1 Classification of Signals",
        "1.2 Elementary & Singularity Signals",
        "1.3 Operations on Signals",
        "1.4 Properties of Systems",
    ],
    "2. LTI Systems & Fourier Series": [
        "2.1 Discrete‑Time & Continuous‑Time LTI",
        "2.2 Convolution",
        "2.3 Fourier Series (Trigonometric, Amplitude‑Phase, Complex)",
        "2.4 Parseval’s Theorem",
    ],
    "3. Fourier Transform & Spectra": [
        "3.1 Derivation of FT",
        "3.2 FT Pair & Inversion",
        "3.3 FT Properties",
    ],
    "4. Sinusoids & Line Spectra (Part II)": [
        "4.1 Sinusoidal Signal Representation",
        "4.2 Phasor & Line Spectrum",
        "4.3 Addition & Multiplication of Sinusoids",
    ],
    "5. Modulation (Part III)": [
        "5.1 Types of Modulation",
        "5.2 Amplitude Modulation Theory",
        "5.3 AM Generation & Demodulation",
    ],
}
section = st.sidebar.radio("Module", list(sections.keys()))
topic = st.sidebar.radio("Topic", sections[section])
st.title(f"{section} → {topic}")

# --- Content definitions ---
content = {}

# 1.1 Classification
content["1.1 Classification of Signals"] = r"""
### 1.1 Classification of Signals

1. **Continuous‑Time vs Discrete‑Time**  
   - Continuous‑time: \(x(t)\)  
   - Discrete‑time: \(x[n]\)

2. **Continuous‑Value vs Discrete‑Value**  
   - Continuous amplitude: real valued  
   - Discrete amplitude: finite set of levels

3. **Deterministic vs Random**  
   - Deterministic: \(x(t)\) known exactly, e.g. \(A\sin(2\pi f_0t)\)  
   - Random: described by statistics, e.g. noise

4. **Even / Odd Decomposition**  
   \[
     x_e(t)=\tfrac12\bigl[x(t)+x(-t)\bigr],\quad
     x_o(t)=\tfrac12\bigl[x(t)-x(-t)\bigr]
   \]

5. **Periodic vs Aperiodic**  
   \[
     x(t)=x(t+T_0),\quad
     x[n]=x[n+N_0]
   \]

6. **Energy‑Type vs Power‑Type**  
   - Energy: \(E=\int_{-\infty}^\infty |x(t)|^2\,dt\), finite \(E\)  
   - Power: \(P=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}|x(t)|^2dt\), finite \(P\)

---

**Example 1**  
Show \(x(t)=t^3\cos^3(10t)\) is odd, thus 
\(\displaystyle\int_{-T}^T x(t)\,dt = 0\).  

> **Solution:**  
> \(x(-t)=(-t)^3\cos^3(10(-t))=-t^3\cos^3(10t)=-x(t)\).  
> Integral over symmetric limits of an odd function is zero.
"""

# 1.2 Elementary & Singularity Signals
content["1.2 Elementary & Singularity Signals"] = r"""
### 1.2 Elementary & Singularity Signals

#### Elementary Signals
1. **Exponential**: \(x(t)=A e^{a t}\)  
   - Grows if \(a>0\), decays if \(a<0\).

2. **Sinusoid**: \(x(t)=A\cos(2\pi f_0t+\theta)\)  
   - Period \(T_0=\tfrac1{f_0}\), RMS \(=\tfrac A{\sqrt2}\).

3. **Complex Exponential**: \(x(t)=A e^{j(2\pi f_0t+\phi)}\)

#### Singularity Signals
1. **Dirac Delta**:  
   \[
     \delta(t)=\begin{cases}
       \infty,&t=0\\
       0,&t\neq0
     \end{cases},\quad
     \int_{-\infty}^\infty\delta(t)\,dt=1
   \]

2. **Unit Step**:  
   \[
     u(t)=\begin{cases}
       1,&t\ge0\\
       0,&t<0
     \end{cases}
   \]

3. **Signum**:  
   \[
     \mathrm{sgn}(t)=\begin{cases}
       1,&t>0\\
       0,&t=0\\
       -1,&t<0
     \end{cases}
   \]

4. **Rectangular**:  
   \[
     \mathrm{rect}\Bigl(\tfrac tT\Bigr)
     =\begin{cases}
       1,&|t|\le\tfrac T2\\
       0,&\text{otherwise}
     \end{cases}
   \]

5. **Sinc**: \(\displaystyle\sinc(t)=\frac{\sin(\pi t)}{\pi t}\)

---

**Example 2**  
Sample \(x(t)=5\,\sinc(t)\) at \(T_s=0.5\) s:  
\[
x_s(t)=\sum_{n=-\infty}^\infty x(nT_s)\,\delta(t-nT_s).
\]
"""

# 1.3 Operations on Signals
content["1.3 Operations on Signals"] = r"""
### 1.3 Operations on Signals

- **Amplitude Scaling**: \(y(t)=a\,x(t)\)  
- **Time Shifting**: \(y(t)=x(t-T)\)  
- **Time Reversal**: \(y(t)=x(-t)\)  
- **Time Scaling**: \(y(t)=x(a\,t)\), compresses if \(|a|>1\), inverts if \(a<0\)

---

**Example 3**  
If \(x(t)=0.5\,\mathrm{rect}(\tfrac t4)\), find  
\(y(t)=2\,x(2-t)\).  

> **Solution:**  
> \(y(t)=2\cdot0.5\,\mathrm{rect}\bigl(\tfrac{2-t}4\bigr).\)
"""

# 1.4 Properties of Systems
content["1.4 Properties of Systems"] = r"""
### 1.4 Properties of Systems

1. **BIBO Stability**: Bounded input ⇒ bounded output  
2. **Memory**: Output depends on past/future input  
3. **Causality**: No dependence on future inputs  
4. **Linearity**: Superposition holds \(\to y=ax_1+bx_2\)  
5. **Time Invariance**: Delay input ⇒ same delay in output

---

**Example 4**  
\(y[n]=\tfrac13[x(n)+x(n-1)+x(n-2)]\) is LTI and causal.
"""

# 2.1 LTI Systems
content["2.1 Discrete‑Time & Continuous‑Time LTI"] = r"""
### 2.1 Discrete‑Time & Continuous‑Time LTI Systems

- **Impulse Response**: \(h[n]\) or \(h(t)\)  
- **Convolution Sum**:  
  \[
    y[n]=x[n]*h[n]=\sum_{m=-\infty}^{\infty}x[m]\,h[n-m]
  \]
- **Convolution Integral**:  
  \[
    y(t)=x(t)*h(t)=\int_{-\infty}^\infty x(\tau)\,h(t-\tau)\,d\tau.
  \]

---

**Example 5**  
Compute \(y[n]=\{1,2,1\}*\{1,-1\}\) by hand.
"""

# 2.2 Convolution
content["2.2 Convolution"] = r"""
### 2.2 Convolution (Graphical Method)

1. Flip one sequence: \(h[-m]\)  
2. Shift: \(h[n-m]\)  
3. Multiply pointwise with \(x[m]\)  
4. Sum over \(m\)

*(See standard graphical convolution illustration.)*
"""

# 2.3 Fourier Series
content["2.3 Fourier Series (Trigonometric, Amplitude‑Phase, Complex)"] = r"""
### 2.3 Fourier Series

#### (a) Trigonometric Form  
\[
x(t)=a_0
+\sum_{n=1}^{\infty}\bigl[a_n\cos(2\pi n f_0t)+b_n\sin(2\pi n f_0t)\bigr]
\]
\[
a_n=\frac{2}{T_0}\int_{0}^{T_0}x(t)\cos(2\pi n f_0t)\,dt,\quad
b_n=\frac{2}{T_0}\int_{0}^{T_0}x(t)\sin(2\pi n f_0t)\,dt
\]

#### (b) Amplitude‑Phase Form  
\[
x(t)=A_0+\sum_{n=1}^\infty A_n\cos\bigl(2\pi n f_0t+\phi_n\bigr),
\]
\[
A_n=\sqrt{a_n^2+b_n^2},\quad
\phi_n=\tan^{-1}\!\bigl(-b_n/a_n\bigr)
\]

#### (c) Complex Exponential Form  
\[
x(t)=\sum_{k=-\infty}^\infty c_k\,e^{j2\pi kf_0t},\quad
c_k=\frac1{T_0}\int_0^{T_0}x(t)e^{-j2\pi kf_0t}\,dt
\]

---

**Example 6**  
Rectangular pulse train (\(\tau/T_0=1/4\)):  
\[
a_n=\frac{2A}{n\pi}\sin\!\Bigl(n\pi\frac{\tau}{T_0}\Bigr),\quad b_n=0.
\]
"""

# 2.4 Parseval’s Theorem
content["2.4 Parseval’s Theorem"] = r"""
### 2.4 Parseval’s Power Theorem

For periodic \(x(t)\) with FS coefficients \(c_k\):
\[
P=\frac1{T_0}\int_0^{T_0}|x(t)|^2dt
=\sum_{k=-\infty}^\infty |c_k|^2.
\]
"""

# 3.1 Derivation of FT
content["3.1 Derivation of FT"] = r"""
### 3.1 Derivation of the Fourier Transform

From FS as \(T_0\to\infty\), we get the continuous pair:

\[
X(f)=\int_{-\infty}^\infty x(t)\,e^{-j2\pi f t}\,dt,
\quad
x(t)=\int_{-\infty}^\infty X(f)\,e^{j2\pi f t}\,df.
\]
"""

# 3.2 FT Pair & Inversion
content["3.2 FT Pair & Inversion"] = r"""
### 3.2 Fourier Transform Pair

\[
x(t)\ \longleftrightarrow\ X(f)
\]
where
\[
X(f)=\int_{-\infty}^\infty x(t)e^{-j2\pi f t}dt,
\quad
x(t)=\int_{-\infty}^\infty X(f)e^{j2\pi f t}df.
\]
*(Zero‑frequency term \(X(0)=\int x(t)dt\) gives area.)*
"""

# 3.3 FT Properties
content["3.3 FT Properties"] = r"""
### 3.3 Key Properties of the FT

1. **Linearity**: \(a\,x_1+b\,x_2\to aX_1+bX_2\).  
2. **Time Shift**: \(x(t-t_0)\to X(f)e^{-j2\pi f t_0}\).  
3. **Time Scaling**: \(x(at)\to\frac1{|a|}X(f/a)\).  
4. **Duality**: \(X(t)\to x(-f)\).  
5. **Convolution**: \(x*y\to X\cdot Y\).  
6. **Modulation**: \(x(t)e^{j2\pi f_0t}\to X(f-f_0)\).
"""

# 4.1 Sinusoidal Signal Representation
content["4.1 Sinusoidal Signal Representation"] = r"""
### 4.1 Sinusoidal Signal Representation

A general CT sinusoid:
\[
x(t)=A\cos(2\pi f_0t+\theta).
\]
- **Amplitude** \(A>0\)  
- **Frequency** \(f_0\ge0\) (Hz), period \(T_0=1/f_0\)  
- **Phase** \(\theta\in[-\pi,\pi]\)  

**Average power** \(P=\frac{A^2}{2}\).  
**RMS** \(A/\sqrt2\).
"""

# 4.2 Phasor & Line Spectrum
content["4.2 Phasor & Line Spectrum"] = r"""
### 4.2 Phasor & Line Spectrum

Write \(x(t)=\Re\{Ae^{j(2\pi f_0t+\theta)}\}\).  
**One‑sided line spectrum** at \(f=f_0\):  
- Amplitude:  \(A\)  
- Phase:      \(\theta\)  
- (Implicit: at \(-f_0\) its complex conjugate)
"""

# 4.3 Addition & Multiplication of Sinusoids
content["4.3 Addition & Multiplication of Sinusoids"] = r"""
### 4.3 Combining Sinusoids

1. **Addition, same frequency**:  
   \(\sum A_k\cos(2\pi f_0t+\theta_k)=A\cos(2\pi f_0t+\theta)\)  
   via phasor sum \(A e^{j\theta}=\sum A_ke^{j\theta_k}\).

2. **Addition, different freq.**:  
   generally aperiodic or periodic only if freq. ratio is rational.

3. **Multiplication**:  
\[
\cos(2\pi f_1t+\theta_1)\cos(2\pi f_2t+\theta_2)
=\tfrac12\cos[2\pi(f_1-f_2)t+\theta_1-\theta_2]
+\tfrac12\cos[2\pi(f_1+f_2)t+\theta_1+\theta_2].
\]
"""

# 5.1 Types of Modulation
content["5.1 Types of Modulation"] = r"""
### 5.1 Types of Modulation

1. **AM** (Amplitude Modulation):
   \[
     x_{AM}(t)=\bigl[1+k_a m(t)\bigr]\cos(2\pi f_c t).
   \]

2. **FM** (Frequency Modulation):
   \[
     x_{FM}(t)=\cos\!\Bigl(2\pi f_c t
     +k_f\int^t m(\tau)d\tau\Bigr).
   \]

3. **PM** (Phase Modulation):
   \[
     x_{PM}(t)=\cos\!\bigl[2\pi f_c t+k_p m(t)\bigr].
   \]
"""

# 5.2 AM Theory
content["5.2 Amplitude Modulation Theory"] = r"""
### 5.2 AM Theory

- **Modulation index**: \(\mu=k_a A_m\).  
- **Under‑modulation**: \(\mu<1\).  
- **Over‑modulation**: \(\mu>1\).

**Spectrum**:
\[
X_{AM}(f)
=\tfrac{A_c}2\bigl[\delta(f-f_c)+\delta(f+f_c)\bigr]
+\tfrac{A_c\mu}4\bigl[\delta(f-f_c-f_m)+\delta(f-f_c+f_m)+\dots\bigr].
\]

**Power efficiency**:
\[
\eta=\frac{\text{sideband power}}{\text{total power}}
=\frac{\mu^2}{2+\mu^2}.
\]
"""

# 5.3 AM Generation & Demodulation
content["5.3 AM Generation & Demodulation"] = r"""
### 5.3 AM Generation & Demodulation

**Generation**: Multiply \(m(t)+\tfrac1{k_a}\) by carrier.  
**Envelope detector** for demodulation: simple diode + RC filter.

---

**Example 7**  
For \(m(t)=A_m\cos(2\pi f_mt)\), 
\(\mu=k_aA_m\). Then
\[
x_{AM}(t)=A_c\bigl[1+\mu\cos(2\pi f_mt)\bigr]\cos(2\pi f_ct).
\]
Carrier amplitude \(A_c\), sideband amplitude \(A_c\mu/2\).
"""

# --- Render the selected content ---
st.markdown(content[topic], unsafe_allow_html=True)
