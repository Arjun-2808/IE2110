import streamlit as st

"""
IE2110 – **Exam‑Focused** Cheat‑Sheet (Streamlit)
================================================
Only the high‑value tricks you actually need for the paper – no fluffy “what is
an exponential” notes.  Each tab holds:
• 🔑 Core formula / method  • ⚡ Quick hack  • 🛠️ Worked example.
Built for Streamlit ≥1.30; uses only `st.latex`, no extra packages.
"""

st.set_page_config(page_title="IE2110 Exam Hacks", layout="wide")

st.title("IE2110 · Signals & Systems — Last‑Minute Exam Hacks")

page = st.sidebar.radio(
    "Select topic",
    [
        "1. Convolution Sketching",
        "2. Fourier Magnitude & Phase",
        "3. Sampling & Aliasing",
        "4. LTI System Quick Tests",
        "5. Amplitude Modulation"
    ],
)

hr = "<hr style='margin:1em 0'>"

# ───────────────────────────────── 1 — Convolution
if page.startswith("1"):
    st.header("1. Convolution — Draw in Seconds")

    st.latex(r"y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau")

    st.markdown(r"""### 🔑 Core Idea
Flip‐then‐shift method; overlap area drives output.
""", unsafe_allow_html=True)

    st.markdown(r"""### ⚡ Speed Hack
1. Pre‑label **supports** (non‑zero spans) of x and h.  
2. Compute start and end of overlap only – the shape inside rarely matters:  
&nbsp;&nbsp;`t_start = start_x + start_h`  
&nbsp;&nbsp;`t_end   = end_x + end_h`.  
3. For simple rectangles/triangles integrate **area = base × height** instead of full integral.
""", unsafe_allow_html=True)

    st.markdown(r"""### 🛠️ Example (2019 Q3c)
Rect pulse width 2 s convolved with itself.
*Support* 0–2 s ⇒ overlap length = \(L(t)=\max(0,2-|t-2|)\). Result is triangle of base 4 s and peak 2 s.
""", unsafe_allow_html=True)

# ───────────────────────────────── 2 — Fourier
elif page.startswith("2"):
    st.header("2. Fourier — Magnitude & Phase in One Look")

    st.latex(r"X(f)=\int x(t)\,e^{-j2\pi f t} dt")

    st.markdown(r"""### 🔑 Core Rules
* Even real ⇒ X is real & even (phase 0 or π).  
* Odd real  ⇒ X is imag & odd (phase ±π/2).  
* Time‑shift T ⇒ linear phase  \(-2\pi f T\).
""", unsafe_allow_html=True)

    st.markdown(r"""### ⚡ Sketch Hack
1. Decompose signal into scaled/shifted **rect** & **tri** pieces; use table of transforms.  
2. Plot impulses for periodic lines, lobe shape for sinc.
""", unsafe_allow_html=True)

    st.markdown(r"""### 🛠️ Example (Sample Paper Q2b)
Signal  $$x(t)=\operatorname{rect}(t/2)+\operatorname{rect}((t-3)/2).$$  Two identical rects: spectrum is
$$X(f)=2\,\operatorname{sinc}(2f)\,e^{-j3\pi f}\cos(3\pi f).$$  Magnitude = $|2\,\operatorname{sinc}(2f)|$; phase is π‑step from the exponential.
""", unsafe_allow_html=True)

# ───────────────────────────────── 3 — Sampling
elif page.startswith("3"):
    st.header("3. Sampling & Aliasing")

    st.latex(r"x_s(t)=x(t)\sum_{n=-\infty}^{\infty}\!\delta(t-nT_s)\,,\qquad f_s=1/T_s")

    st.markdown(r"""### 🔑 Spectrum Replication
$$X_s(f)=\frac{1}{T_s}\sum_{k=-\infty}^{\infty} X(f-kf_s).$$  Aliasing if replicas overlap.
""", unsafe_allow_html=True)

    st.markdown(r"""### ⚡ Minimum f_s Hack
Always choose $f_s \ge 2B$ (Nyquist).  For exam, quote “anti‑alias LPF width B”.
""", unsafe_allow_html=True)

    st.markdown(r"""### 🛠️ Example (2022 Q4)
Low‑pass  B = 5 kHz.  Choose \$f_s=12\text{ kHz}\$. Show sketch: main lobe −5…5 kHz, replicas at ±12 kHz.
""", unsafe_allow_html=True)

# ───────────────────────────────── 4 — LTI Quick Tests
elif page.startswith("4"):
    st.header("4. LTI System Quick Tests")

    st.markdown(r"""### 🔑 Check List
* **Linearity**  → superposition with two δ inputs.  
* **Time‑invariance**  → replace \(t\to t-t_0\) and compare.  
* **BIBO stable**     → CT: \(\int |h(t)|dt\lt\infty\);  DT: Σ|h[n]|<∞.  
* **Causal**          → h(t)=0 for t<0.
""", unsafe_allow_html=True)

    st.markdown(r"""### ⚡ Memoryless Hack
If output depends **only** on present input: h(t)=k δ(t). Any delay term means memory.
""", unsafe_allow_html=True)

    st.markdown(r"""### 🛠️ Example (Past paper Q1d)
System:  $$y(t)=x(t)+3x(t-2).$$  Test:
* Linear ✓ (sum of scaled inputs)
* Time‑variant ✗?  shift test shows **causal** (t<0 section zero), **not memoryless** (depends on past).
""", unsafe_allow_html=True)

# ───────────────────────────────── 5 — AM
else:
    st.header("5. Amplitude Modulation (DSB‑TC)")

    st.latex(r"x_{AM}(t)=[1+\mu m(t)]\cos(2\pi f_c t)\,,\qquad \mu=k_a m_{max}")

    st.markdown(r"""### 🔑 Spectrum Layout
Carrier at ±f_c (power $$P_C=A^2/2R$$) and sidebands at f_c±f_m.  Bandwidth = 2B.
""", unsafe_allow_html=True)

    st.markdown(r"""### ⚡ Efficiency Hack
Maximum power transfer at μ = 1 ⇒ efficiency 33.3 %.  Anything higher ⇒ over‑modulation (envelope crosses zero).
""", unsafe_allow_html=True)

    st.markdown(r"""### 🛠️ Example (Exam Q3)
Message \$m(t)=0.6\cos(2\pi1\,\text{kHz} t)\$, carrier 100 kHz.
* μ = 0.6 < 1 (safe).  Output frequencies: 100 kHz carrier + sidebands 99 kHz and 101 kHz.
* Draw magnitude: carrier spike height \$A/2\$; each sideband \$0.3A/2\$.
""", unsafe_allow_html=True)


st.sidebar.info("Good luck – nail the paper!")
