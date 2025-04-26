import streamlit as st

# ────────────────────────────────────────────────────────────────────────────────
# IE2110 Exam-Focused Cheat-Sheet
# Minimal theory; only high-leverage hacks + detailed past-paper examples
# Streamlit 1.30+; uses only st.latex and raw st.markdown
# ────────────────────────────────────────────────────────────────────────────────

# Must be the first Streamlit command
st.set_page_config(page_title="IE2110 Exam Hacks", layout="wide")

# Title
st.title("IE2110 · Signals & Systems — Exam-Focused Hacks")

# Sidebar navigation
section = st.sidebar.selectbox(
    "Navigate to topic:",
    [
        "1. Convolution (Past-Paper Q3)",
        "2. Fourier Mag & Phase (Past-Paper Q4)",
        "3. Sampling & Aliasing (Past-Paper Q5)",
        "4. LTI System Tests (Past-Paper Q2)",
        "5. Amplitude Modulation (Past-Paper Q6)"
    ]
)

# Horizontal rule HTML snippet
hr = "<hr style='margin:1em 0'>"

# ────────────────────────────────────────────────────────────────────────────────
# 1. Convolution — Past-Paper Q3
# ────────────────────────────────────────────────────────────────────────────────
if section.startswith("1"):
    st.header("1. Convolution — Past-Paper Q3")
    st.latex(r"y(t)=\int_{-\infty}^{\infty}x(\tau)\,h(t-\tau)\,d\tau")
    st.markdown(r"""
**🔑 Core Formula**

Flip the impulse response h, shift by t, multiply with x, integrate over overlap.

**⚡ Speed Hack**
1. Draw supports: [a,b] for x, [c,d] for h.  
2. Overlap for output non-zero: t ∈ [a+c, b+d].  
3. For simple shapes (rectangles, triangles), compute output amplitude via base×height formulas instead of full integral.

**🛠️ Worked Example**
**Past-Paper Q3:**
Let x(t)=u(t)-u(t-1), h(t)=u(t)-u(t-2). Sketch y(t)=x*h.

Piecewise result:
- 0≤t<1: overlap length = t ⇒ y(t)=t
- 1≤t<2: full 1s overlap ⇒ y(t)=1
- 2≤t<3: overlap length = 3−t ⇒ y(t)=3−t
- otherwise y(t)=0
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# 2. Fourier Magnitude & Phase — Past-Paper Q4
# ────────────────────────────────────────────────────────────────────────────────
elif section.startswith("2"):
    st.header("2. Fourier Magnitude & Phase — Past-Paper Q4")
    st.latex(r"X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi f t}dt")
    st.markdown(r"""
**🔑 Key Rules**
- Real even x(t) ⇒ X(f) real & even; phase = 0 or π.
- Real odd x(t) ⇒ X(f) imaginary & odd; phase = ±π/2.
- Time shift t0 ⇒ multiply spectrum by e^{−j2πft0} (linear phase).

**⚡ Sketch Hack**
Decompose x(t) into elementary shapes: rect, tri, impulses. Use known transforms and apply time shifts/multiplications.

**🛠️ Worked Example**
**Past-Paper Q4:**
$$x(t)=\operatorname{rect}(t/2)+\operatorname{rect}((t-3)/2).$$
Then:
$$X(f)=2\,\mathrm{sinc}(2f)e^{-j3\pi f}\cos(3\pi f).$$
- Magnitude: |X(f)| = 2 |\mathrm{sinc}(2f)| · |\cos(3πf)|.  
- Phase: arg X = −3πf + arg[cos(3πf)] (0 or π inside lobes).
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# 3. Sampling & Aliasing — Past-Paper Q5
# ────────────────────────────────────────────────────────────────────────────────
elif section.startswith("3"):
    st.header("3. Sampling & Aliasing — Past-Paper Q5")
    st.latex(r"x_s(t)=x(t)\sum_{n=-\infty}^{\infty}\delta(t-nT_s),\quad f_s=1/T_s")
    st.markdown(r"""
**🔑 Spectrum Replication**
$$X_s(f)=\frac1{T_s}\sum_{k=-\infty}^{\infty}X(f - kf_s).$$
Spectral replicas at multiples of f_s.

**⚡ Nyquist Hack**
f_s must satisfy f_s ≥ 2B to avoid aliasing.  
Sketch center lobe ±B, then replicas at ±kf_s.

**🛠️ Worked Example**
**Past-Paper Q5:**
Signal band-limited to B=5 kHz. Choose f_s=12 kHz.
Draw X_s(f): central copy from −5 to +5 kHz, then copies centered at ±12, ±24 kHz.
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# 4. LTI System Tests — Past-Paper Q2
# ────────────────────────────────────────────────────────────────────────────────
elif section.startswith("4"):
    st.header("4. LTI System Tests — Past-Paper Q2")
    st.markdown(r"""
**🔑 Quick Checklist**
1. **Linearity**: superposition for two arbitrary inputs.
2. **Time-Invariance**: shift input ⇒ same shift in output.
3. **Causality**: h(t)=0 for t<0.
4. **BIBO Stability**: ∫|h(t)|dt<∞ (CT) or ∑|h[n]|<∞ (DT).
5. **Memoryless**: depends only on x(t), not delayed samples.
""", unsafe_allow_html=True)
    st.markdown(r"""
**🛠️ Worked Example**
**Past-Paper Q2:**
$$y(t)=3x(t) - 2\frac{d}{dt}x(t) + x(t-1).$$
- Linearity: Yes.  
- Time-Invariance: Yes.  
- Causality: Yes (x(t-1) uses past).  
- Stability: Differentiation amplifies high-frequency noise ⇒ not BIBO stable.
""", unsafe_allow_html=True)

# ────────────────────────────────────────────────────────────────────────────────
# 5. Amplitude Modulation — Past-Paper Q6
# ────────────────────────────────────────────────────────────────────────────────
else:
    st.header("5. Amplitude Modulation — Past-Paper Q6")
    st.latex(r"x_{AM}(t)=[1+\mu m(t)]\cos(2\pi f_c t),\quad \mu=\frac{\Delta A}{A_c}")
    st.markdown(r"""
**🔑 Spectrum Layout**
Carrier at ±f_c with amplitude A_c/2. Sidebands at f_c±f_m with amplitude (μA_c/4)·M.
Bandwidth = 2B of m(t).

**⚡ Efficiency Hack**
Power efficiency = μ²/(2+μ²). Maximum at μ=1 → 33.3%.

**🛠️ Worked Example**
**Past-Paper Q6:**
$$m(t)=4\cos(2\pi 0.5t)+2\cos(2\pi1.5t), A_c=5, f_c=100\text{kHz}.$$  
m_max=4+2=6 → choose μ=0.6.  
Sidebands at 100±0.5 kHz & 100±1.5 kHz.
Line amplitudes: (μA_c/2)*{4,2} = { (0.6*5/2)*4, (0.6*5/2)*2 } = {6,3 }.
""", unsafe_allow_html=True)

# Footer info
st.sidebar.success("All set for the exam — good luck!")
