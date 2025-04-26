import streamlit as st

"""
IE2110 — Signals & Systems: Exam-Focused Cheat-Sheet
• Minimal theory; only high-leverage hacks + detailed past-paper examples.
• Streamlit 1.30+ only; uses st.latex and st.markdown with raw strings.
"""

# must be first
st.set_page_config(page_title="IE2110 Exam Hacks", layout="wide")

st.title("IE2110 · Signals & Systems — Exam-Focused Hacks")

# improved sidebar with selectbox for clean nav
section = st.sidebar.selectbox(
    "Navigate to topic:",
    [
        "1. Convolution (Past-Paper Q3)",
        "2. Fourier Mag & Phase (Q4)",
        "3. Sampling & Aliasing (Q5)",
        "4. LTI System Tests (Q2)",
        "5. Amplitude Modulation (Q6)"
    ]
)

# thin horizontal rule html\hr = "<hr style='margin:1em 0'>"

# 1. Convolution
if section.startswith("1"):
    st.header("1 · Convolution — Detailed Past-Paper Example")
    st.latex(r"y(t)=\int_{-\infty}^{\infty}x(\tau)\,h(t-\tau)\,d\tau")
    st.markdown(r"""
**🔑 Core formula:** flip h, shift by t, overlap with x, integrate product.

**⚡ Hack:** Identify supports: start_x, end_x; start_h, end_h.  \
Compute overlap window [start_x+start_h, end_x+end_h]. For piecewise-linear kernels (rectangles, triangles), sketch output piecewise using simple area formulas.

**🛠️ Past-Paper Q3:**  
Let $$x(t)=u(t)-u(t-1), \quad h(t)=u(t)-u(t-2).$$  
Sketch $$y(t)=x*h.$$  
_Answer piecewise:_  
- For $0\le t<1$: overlap width = t, so $y(t)=t$.  
- For $1\le t<2$: full 1 s overlap ⇒ $y(t)=1$.  
- For $2\le t<3$: overlap shrinks: $y(t)=3 - t$.  
- Elsewhere $y(t)=0$.
""", unsafe_allow_html=True)

# 2. Fourier Magnitude & Phase
elif section.startswith("2"):
    st.header("2 · Fourier — Past-Paper Q4 Example")
    st.latex(r"X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi f t}dt")
    st.markdown(r"""
**🔑 Key rules:**  
- Real even x(t) → X(f) real, even; phase = 0 or π.  
- Real odd x(t) → X(f) imaginary, odd; phase = ±90°.  
- Time shift T → phase factor $e^{-j2\pi f T}$.

**🛠️ Past-Paper Q4:**  
$$x(t)=\operatorname{rect}(t/2)+\operatorname{rect}\bigl((t-3)/2\bigr).$$  
Then  
$$X(f)=2\,\mathrm{sinc}(2f)e^{-j3\pi f}\cos(3\pi f).$$  
- **Magnitude:** $|X| = 2|\mathrm{sinc}(2f)||\cos(3\pi f)|$.  
- **Phase:** $\arg X = -3\pi f + \arg[\cos(3\pi f)]$ (±0 inside lobes).
""", unsafe_allow_html=True)

# 3. Sampling & Aliasing
elif section.startswith("3"):
    st.header("3 · Sampling & Aliasing — Past-Paper Q5")
    st.latex(r"x_s(t)=x(t)\sum_{n=-\infty}^{\infty}\delta(t-nT_s),\quad f_s=1/T_s")
    st.markdown(r"""
**🔑 Spectrum replication:**  
$$X_s(f)=\frac{1}{T_s}\sum_{k=-\infty}^{\infty}X(f - k f_s).$$  
Replicas at multiples of $f_s$.

**⚡ Hack:** ensure $f_s\ge2B$ to avoid overlap (aliasing). Draw main lobe ±B, then replicas at k·f_s.

**🛠️ Past-Paper Q5:**  
Bandlimit B=5 kHz. Choose $f_s=12\,\text{kHz}$.  
Replica centers at ... -24, -12, 0, 12, 24 kHz. Draw magnitude of $X_s(f)$ accordingly.
""", unsafe_allow_html=True)

# 4. LTI System Tests
elif section.startswith("4"):
    st.header("4 · LTI System Tests — Past-Paper Q2")
    st.markdown(r"""
**🔑 Checklist:**
1. **Linearity:** test $x_1,x_2$ → output $y_1+y_2$.  
2. **Time-invariance:** delay input by $t_0$, see if output delays.  
3. **Causality:** $h(t)=0$ for $t<0$.  
4. **BIBO Stability:** ∫|h(t)|dt < ∞ (CT) or Σ|h[n]|<∞ (DT).  
5. **Memoryless:** dependence only on $x(t)$, no shifts.
""", unsafe_allow_html=True)
    st.markdown(r"""
**🛠️ Past-Paper Q2:**  
System: $$y(t)=3x(t)-2\frac{d}{dt}x(t)+x(t-1).$$  
- **Linear?** yes (sum of LTI ops).  
- **Time-invariant?** yes (all shifts).  
- **Causal?** yes ($x(t-1)$ uses past).  
- **Stable?** differentiation unbounded for high-frequency noise ⇒ not BIBO stable.
""", unsafe_allow_html=True)

# 5. Amplitude Modulation
else:
    st.header("5 · Amplitude Modulation — Past-Paper Q6")
    st.latex(r"x_{AM}(t)=[1+\mu m(t)]\cos(2\pi f_c t),\quad \mu=\frac{\Delta A}{A_c}")
    st.markdown(r"""
**🔑 Spectrum:** Carrier at ±f_c, sidebands at f_c ± f_m.  Bandwidth = 2B.
**⚡ Power Efficiency:** η = μ²/(2+μ²), peaks at μ=1 (33.3%).

**🛠️ Past-Paper Q6:**  
$$m(t)=4\cos(2\pi 0.5t)+2\cos(2\pi1.5t),\quad f_c=100\,	ext{kHz},\ A_c=5.$$  
- μ depends on max m → m_max=4+2=6; choose k_a=0.1 ⇒ μ=0.6.  
- Sidebands: at 99.5, 101.5 kHz (for 0.5 kHz tone) and 98.5, 102.5 kHz (1.5 kHz tone).  
- Amplitudes: each line amplitude = (μA_c/2)*(component amplitude).
""", unsafe_allow_html=True)

st.sidebar.success("Exam ready — go ace it!")
