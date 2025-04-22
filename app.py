import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve
from streamlit_lottie import st_lottie
import requests

# Load Lottie animation

def load_lottie_url(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_zr4ozr87.json")

# App configuration
st.set_page_config(
    page_title="IE2110 Master Review",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Sidebar for Parts ---
parts = [
    "Part I: Signals, Systems & Fourier",
    "Part II: Sampling & Sinusoids",
    "Part III: Modulation"
]
part = st.sidebar.selectbox("Select Slide Part", parts)
st.sidebar.markdown("---")

# Title and animation
st.title("IE2110: Signals & Systems Master Review")
if lottie:
    st_lottie(lottie, height=150)

# Helper functions

def show_eq(equations):
    for eq in equations:
        st.latex(eq)


def plot_signal(x, y, title):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(title)
    ax.grid(True)
    st.pyplot(fig)

# --- Part I Content ---
if part == "Part I: Signals, Systems & Fourier":
    st.header(part)

    # 1.1 Classification
    st.subheader("1.1 Classification of Signals")
    st.markdown("**Key Types:** Continuous vs Discrete, Deterministic vs Random, Periodic vs Aperiodic, Even vs Odd, Energy vs Power.")
    show_eq([
        r"x_e(t)=\tfrac12[x(t)+x(-t)]",
        r"x_o(t)=\tfrac12[x(t)-x(-t)]",
        r"E=\int_{-\infty}^{\infty}x^2(t)dt,\quad P=\lim_{T\to\infty}\tfrac1T\int_{-T/2}^{T/2}x^2(t)dt"
    ])
    with st.expander("Example: Odd Function Integration"):
        st.write("Show $x(t)=t^3\cos^3(10t)$ is odd, so $\int_{-T}^T x(t)dt=0$.")
        show_eq([
            r"x(-t)=(-t)^3\cos^3(10(-t))=-t^3\cos^3(10t)=-x(t)",
            r"\int_{-T}^T x(t)dt = 0"
        ])

    # 1.2 System Properties & LTI
    st.subheader("1.2 System Properties & LTI")
    st.markdown(
        "- **Linearity**, **Time-Invariance**, **Causality**, **BIBO Stability**"
    )
    with st.expander("Example: Check LTI & Causality"):
        st.write(
            "For $y[n]=\frac{1}{3}[x[n]+x[n-1]+x[n-2]]$, it's in convolution form ⇒ LTI, and depends only on present/past ⇒ causal."
        )

    # 1.3 Convolution
    st.subheader("1.3 Convolution (Discrete & Continuous)")
    show_eq([
        r"y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]",
        r"y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau"
    ])
    with st.expander("Interactive Discrete Convolution"):
        x_in = st.text_input("Enter x[n] (comma-separated)", "1,2,1")
        h_in = st.text_input("Enter h[n] (comma-separated)", "1,-1")
        if st.button("Compute Convolution y[n]"):
            x = np.fromstring(x_in, sep=',')
            h = np.fromstring(h_in, sep=',')
            y = np.convolve(x, h)
            st.write("**x[n]:**", x)
            st.write("**h[n]:**", h)
            st.write("**y[n] = x*h:**", y)
            n_idx = np.arange(len(y))
            plot_signal(n_idx, y, "Convolution Output y[n]")

    # 1.4 Fourier Series & Transform
    st.subheader("1.4 Fourier Series & Transform")
    st.write("**Fourier Series** (Periodic Signals)")
    show_eq([
        r"x(t)=a_0+\sum_{k=1}^\infty[a_k\cos(2\pi kf_0t)+b_k\sin(2\pi kf_0t)]",
        r"c_k=\tfrac{1}{T_0}\int_0^{T_0}x(t)e^{-j2\pi kf_0t}dt"
    ])
    st.write("**Fourier Transform** (Aperiodic Signals)")
    show_eq([
        r"X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}dt",
        r"x(t)=\int_{-\infty}^{\infty}X(f)e^{j2\pi ft}df"
    ])

# --- Part II Content ---
elif part == "Part II: Sampling & Sinusoids":
    st.header(part)

    # 2.1 Sampling & Aliasing
    st.subheader("2.1 Sampling Theorem & Aliasing")
    fs = st.slider("Sampling Rate f_s (Hz)", 1.0, 100.0, 20.0)
    f0 = st.slider("Signal Frequency f0 (Hz)", 0.1, 50.0, 5.0)
    t = np.linspace(0, 1, 1000)
    x = np.sin(2 * np.pi * f0 * t)
    n = np.arange(0, 1, 1/fs)
    xs = np.sin(2 * np.pi * f0 * n)
    plot_signal(t, x, "Continuous Signal x(t)")
    plot_signal(n, xs, "Sampled Signal x[n]")
    st.markdown("**Note:** Aliasing occurs if $f_s < 2f_0$. Nyquist rate = 2f_0.")

    # 2.2 Sinusoidal Signals & Phasors
    st.subheader("2.2 Sinusoidal Signals & Phasor Representation")
    A = st.slider("Amplitude A", 0.1, 5.0, 1.0)
    f_sin = st.slider("Frequency f0 (Hz)", 0.1, 10.0, 2.0)
    phi = st.slider("Phase (rad)", -np.pi, np.pi, 0.0)
    x_sin = A * np.cos(2 * np.pi * f_sin * t + phi)
    plot_signal(t, x_sin, "Time-Domain Sinusoid x(t)")
    st.latex(r"x(t)=A\cos(2\pi f_0t+\phi)=\Re\{Ae^{j(2\pi f_0t+\phi)}\}")
    with st.expander("Example: Phasor Addition"):
        z1 = 2 * np.exp(1j * np.pi/4)
        z2 = 3 * np.exp(-1j * np.pi/6)
        z_sum = z1 + z2
        st.write(f"Phasor 1: 2∠45°, Phasor 2: 3∠-30°")
        st.write(f"Resulting magnitude = {abs(z_sum):.2f}, angle = {np.angle(z_sum):.2f} rad")

# --- Part III Content ---
else:
    st.header(part)

    # 3.1 Amplitude Modulation (AM)
    st.subheader("3.1 Amplitude Modulation (AM)")
    Ac = st.slider("Carrier Amplitude A_c", 0.1, 5.0, 2.0)
    Am = st.slider("Message Amplitude A_m", 0.1, 2.0, 1.0)
    fm = st.slider("Message Frequency f_m (Hz)", 0.1, 10.0, 1.0)
    fc = st.slider("Carrier Frequency f_c (Hz)", 5.0, 100.0, 20.0)
    mu = Am / Ac
    t = np.linspace(0, 1, 1000)
    m = Am * np.cos(2 * np.pi * fm * t)
    x_am = Ac * (1 + mu * np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * fc * t)
    plot_signal(t, x_am, "AM Signal x_AM(t)")
    show_eq([r"\mu=\frac{A_m}{A_c}", r"x_{AM}(t)=A_c[1+\mu\cos(2\pi f_mt)]\cos(2\pi f_ct)"])
    st.markdown(f"Modulation index μ = {mu:.2f}")

    # 3.2 FM & PM (Overview)
    st.subheader("3.2 Frequency & Phase Modulation (FM/PM)")
    st.latex(r"x_{FM}(t)=\cos\bigl(2\pi f_ct + k_f\int m(\tau)d\tau\bigr)")
    st.latex(r"x_{PM}(t)=\cos\bigl(2\pi f_ct + k_p m(t)\bigr)")
    with st.expander("Envelope Detector Circuit"):
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/3c/Envelope_detector_circuit.svg",
            use_column_width=True
        )
        st.write("A diode followed by an RC low-pass filter tracks the envelope of the AM wave to recover the message signal.")
