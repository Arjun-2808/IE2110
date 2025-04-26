import streamlit as st

# First command must be set_page_config
st.set_page_config(page_title="IE2110 Exam Hacks", layout="wide")

# Title
st.title("IE2110 · Signals & Systems — Exam-Focused Hacks")

# Sidebar navigation
page = st.sidebar.radio(
    "Select topic",
    [
        "1. Convolution",
        "2. Fourier Magnitude & Phase",
        "3. Sampling & Aliasing",
        "4. LTI System Tests",
        "5. Amplitude Modulation"
    ],
)

# Horizontal rule HTML
hr = "<hr style='margin:1em 0'>"

# 1. Convolution
if page == "1. Convolution":
    st.header("1. Convolution — Fast Sketching")
    st.latex(r"y(t)=\int_{-\infty}^{\infty}x(\tau)\,h(t-\tau)\,d\tau")
    st.markdown(r"""
**🔑 Core:** flip h, shift by t, overlap with x, integrate product.
**⚡ Hack:** only track start/end of overlap; for rectangles use area=base×height.

**🛠️ Example:** Rect(0–2) * Rect(0–2) ⇒ triangle of width 4, peak 2.
""", unsafe_allow_html=True)

# 2. Fourier Magnitude & Phase
elif page == "2. Fourier Magnitude & Phase":
    st.header("2. Fourier — Magnitude & Phase")
    st.latex(r"X(f)=\int_{-\infty}^{\infty}x(t) e^{-j2\pi f t}dt")
    st.markdown(r"""
**🔑 Rules:**  
- Even real x ⇒ X real & even (phase 0 or π).  
- Odd real x ⇒ X imaginary & odd (phase ±π/2).  
- Time shift t0 ⇒ linear phase −2πf t0.

**⚡ Sketch:** decompose into known shapes (rect, tri, impulses); plot magnitude, then phase.

**🛠️ Example:** cos(2πf0t) ⇒ |X|=½δ(f−f0)+½δ(f+f0), phase 0.
""", unsafe_allow_html=True)

# 3. Sampling & Aliasing
elif page == "3. Sampling & Aliasing":
    st.header("3. Sampling & Aliasing")
    st.latex(r"x_s(t)=x(t)\sum_{n=-\infty}^{\infty}\delta(t-nT_s),\quad f_s=1/T_s")
    st.markdown(r"""
**🔑 Spectrum:**  
X_s(f)= (1/T_s)ΣX(f−k f_s).  Replicas at k·f_s.

**⚡ Hack:** choose f_s≥2B, sketch main lobe ±B, replicas at ±f_s.

**🛠️ Example:** B=5kHz ⇒ f_s=12kHz ⇒ replicas at 0±12kHz.
""", unsafe_allow_html=True)

# 4. LTI System Tests
elif page == "4. LTI System Tests":
    st.header("4. LTI System Quick Tests")
    st.markdown(r"""
**🔑 BIBO Stability:** ∫|h(t)|dt<∞ (CT), Σ|h[n]|<∞ (DT).
**🔑 Causality:** h(t)=0 for t<0.
**🔑 Memoryless:** output y(t)=k x(t) ⇒ h(t)=kδ(t).
**🔑 Linearity:** superposition with δ inputs.
**🔑 Time-invariant:** shift input⇒same shift output.
""", unsafe_allow_html=True)
    st.markdown(r"""
**🛠️ Example:** y(t)=x(t)+3x(t−2) is linear, causal, has memory, but time-invariant.
""", unsafe_allow_html=True)

# 5. Amplitude Modulation
else:
    st.header("5. Amplitude Modulation (DSB-TC)")
    st.latex(r"x_{AM}(t)=[1+\mu\,m(t)]\cos(2\pi f_c t),\quad \mu=\text{modulation index}")
    st.markdown(r"""
**🔑 Spectrum:** carrier at ±f_c plus sidebands at f_c±f_m.  BW=2B.
**⚡ Efficiency:** max at μ=1 ⇒ η=μ²/(2+μ²)=1/3≈33%.

**🛠️ Example:** m(t)=0.6cos(2π·1kHz t), f_c=100kHz ⇒ sidebands at 99kHz,101kHz, μ=0.6 safe.
""", unsafe_allow_html=True)

st.sidebar.info("Good luck on your exam!")
