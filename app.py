import streamlit as st

"""
IE2110 • Signals & Systems — Comprehensive Exam Cheat-Sheet
Includes essential theory from slides + high-impact hacks + worked examples.
Streamlit 1.30+ only. All math via st.latex in raw strings.
"""
# Must be first
st.set_page_config(page_title="IE2110 Comprehensive Cheat-Sheet", layout="wide")

st.title("IE2110 · Signals & Systems — Comprehensive Exam Cheat-Sheet")

# Improved sidebar navigation
section = st.sidebar.radio(
    "Choose Section:",
    [
        "1. Signal Classification",
        "2. Elementary & Operations",
        "3. LTI Systems Theory",
        "4. Fourier & Line Spectra",
        "5. Sampling & Aliasing",
        "6. Modulation & Demodulation"
    ]
)

# Horizontal rule
hr = "<hr style='margin:1em 0'>"

# 1. Signal Classification
if section == "1. Signal Classification":
    st.header("1. Signal Classification")

    st.subheader("Continuous vs Discrete Time")
    st.latex(r"""x(t)\quad(t\in\mathbb R)
\quad\text{vs}\quad x[n]\quad(n\in\mathbb Z)""")
    st.markdown(r"""
**Theory:** Continuous-time signals defined ∀ real t; discrete-time only at integer n.  
**Hack:** Parentheses vs brackets notation.  
**Example:** x[n]={1,2,3} only at n=0,1,2 ⇒ discrete-time.
""", unsafe_allow_html=True)
    st.markdown(hr, unsafe_allow_html=True)

    st.subheader("Even & Odd Decomposition")
    st.latex(r"""x_e(t)=\tfrac12[x(t)+x(-t)],
\quad x_o(t)=\tfrac12[x(t)-x(-t)]""")
    st.markdown(r"""
**Theory:** Any x(t)=x_e(t)+x_o(t).  
**Hack:** ∫_{-T}^{T} x_o(t) dt = 0.  
**Example:** t^3 cos t odd ⇒ zero symmetric integral.
""", unsafe_allow_html=True)

# 2. Elementary & Operations
elif section == "2. Elementary & Operations":
    st.header("2. Elementary Signals & Operations")

    st.subheader("Basic Signals")
    st.markdown(r"""
• **Unit Impulse:** δ(t), ∫δ(t)dt=1, δ(t−t0) sampling.  
• **Step:** u(t)=1(t≥0), derivative = δ(t).  
• **Rectangular/Pulse:** rect(t/T)=u(t+T/2)−u(t−T/2).  
""", unsafe_allow_html=True)

    st.subheader("Common Operations")
    st.markdown(r"""
• **Time Shift:** y(t)=x(t−t0) ⇒ X(f)e^{-j2π f t0}.  
• **Scaling:** y(t)=x(at) ⇒ (1/|a|)X(f/a).  
• **Amplitude:** y(t)=A x(t).  
""", unsafe_allow_html=True)
    st.markdown(r"""
**Example Hack:** For shift + scale, plot support endpoints and transform accordingly.
""", unsafe_allow_html=True)

# 3. LTI Systems Theory
elif section == "3. LTI Systems Theory":
    st.header("3. Linear Time-Invariant (LTI) Systems")

    st.subheader("Impulse Response & Convolution")
    st.latex(r"y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(τ)h(t−τ)dτ")
    st.markdown(r"""
**Theory:** Impulse response h(t) fully characterizes LTI.  
**Hack:** Identify supports of x/h, overlap region yields non-zero y(t).
""", unsafe_allow_html=True)
    st.markdown(hr, unsafe_allow_html=True)

    st.subheader("System Properties")
    st.markdown(r"""
• **Stability:** ∫|h(t)|dt<∞.  
• **Causality:** h(t)=0 for t<0.  
• **Memoryless:** h(t)=k δ(t).  
• **Linearity & Time-Invariance:** check superposition & shift invariance.
""", unsafe_allow_html=True)

# 4. Fourier & Line Spectra
elif section == "4. Fourier & Line Spectra":
    st.header("4. Fourier & Line Spectra")

    st.subheader("Continuous-Time Fourier Transform")
    st.latex(r"""X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2πft}dt,
\quad x(t)=\int_{-\infty}^{\infty}X(f)e^{j2πft}df""")
    st.markdown(r"""
**Key:** Real even/odd, shift, and modulation properties.  
**Hack:** Use transform table: rect↔sinc, tri↔sinc^2, impulses for sinusoids.
""", unsafe_allow_html=True)
    st.markdown(hr, unsafe_allow_html=True)

    st.subheader("Line Spectra (Periodic Signals)")
    st.markdown(r"""
Periodic x(t)=Σ a_k e^{j2πk f0 t} ⇒ discrete lines at k f0 with weights a_k.
""", unsafe_allow_html=True)

# 5. Sampling & Aliasing
elif section == "5. Sampling & Aliasing":
    st.header("5. Sampling & Aliasing")

    st.subheader("Sampling Theorem")
    st.latex(r"""x_s(t)=x(t)\sum_{n}δ(t−nT_s),
\quad X_s(f)=\tfrac1{T_s}\sum_kX(f−k f_s)""")
    st.markdown(r"""
**Theory:** f_s≥2B avoids overlap.  Reconstruction via ideal LPF.  
**Hack:** Sketch replicas spaced f_s apart; avoid alias region.
""", unsafe_allow_html=True)

# 6. Modulation & Demodulation
else:
    st.header("6. Modulation & Demodulation")

    st.subheader("Amplitude Modulation (AM)")
    st.latex(r"""x_{AM}(t)=[1+μ m(t)]cos(2πf_ct),
\quad μ=k_a m_{max}""")
    st.markdown(r"""
**Theory:** Spectrum: carrier at ±f_c, sidebands at f_c±f_m.  BW=2B.  
**Hack:** Envelope detector requires μ<1.  
""", unsafe_allow_html=True)
    st.markdown(hr, unsafe_allow_html=True)

    st.subheader("Frequency/Phase Modulation (FM/PM)")
    st.markdown(r"""
• FM: f_inst = f_c + k_f m(t).  
• PM: phase = k_p m(t).  
**Hack:** FM spectrum via Bessel functions; use narrowband approx for small dev.
""", unsafe_allow_html=True)

# Footer
st.sidebar.success("Ready for exam — best of luck!")
