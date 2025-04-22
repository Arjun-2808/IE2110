import streamlit as st
import requests
from streamlit_lottie import st_lottie

# -------------------------------
# IE2110 Signals & Systems Review
# -------------------------------
# This Streamlit app strictly follows the IE2110 slides content.
# Only slide material is included—no external topics.

# Load Lottie animation for header flair
def load_lottie_url(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie = load_lottie_url(
    "https://assets2.lottiefiles.com/packages/lf20_zr4ozr87.json"
)

# App configuration
st.set_page_config(
    page_title="IE2110 Master Review",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
parts = [
    "Part I: Signals, Systems & Fourier",
    "Part II: Sampling & Sinusoids",
    "Part III: Modulation"
]
part = st.sidebar.radio("Select Slide Part", parts)
st.sidebar.markdown("---")

# Title and header animation
st.title("IE2110: Signals & Systems Master Review")
if lottie:
    st_lottie(lottie, height=150)

# Utility to render LaTeX equations

def show_eq(eqs):
    for eq in eqs:
        st.latex(eq)

# -------------------------------------------
# Part I: Signals, Systems & Fourier
# -------------------------------------------
if part == "Part I: Signals, Systems & Fourier":
    st.header(part)

    # 1.1 Classification of Signals
    st.subheader("1.1 Classification of Signals")
    st.write(
        "Classification determines which mathematical tools apply: whether to use Fourier series or transforms, "
        "and simplifies computations by exploiting symmetry or energy/power properties."
    )
    st.markdown("**Types:** Continuous vs Discrete, Deterministic vs Random, Periodic vs Aperiodic, Even vs Odd, Energy vs Power.")
    show_eq([
        r"x_e(t)=\frac12\bigl[x(t)+x(-t)\bigr]",
        r"x_o(t)=\frac12\bigl[x(t)-x(-t)\bigr]",
        r"E=\int_{-\infty}^{\infty}x^2(t)dt,\quad P=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}x^2(t)dt"
    ])
    st.markdown("**Example 1:** Show $x(t)=t^3\cos^3(10t)$ is odd ⇒ $\int_{-T}^{T}x(t)dt=0$.\n" 
                "**Solution:** $x(-t)=(-t)^3\cos^3(10(-t))=-t^3\cos^3(10t)=-x(t)$; odd ⇒ integral zero.")

    # Additional classification examples from slides
    st.markdown("**Example 2:** Sketch continuous-time signal $x(t)=t$ and discrete-time signal $x[n]=n$.\n" 
                "These illustrate continuous vs discrete domain.")
    st.markdown("**Example 3:** Determine if $x[n]=(-1)^n$ is continuous- or discrete-value.\n" 
                "Answer: Discrete-value since it only takes ±1.")

    # Even/Odd decomposition example
    st.markdown("**Example 4:** Decompose $x(t)=\cos t + \sin t\cos t$ into even and odd components.\n" 
                "**Solution:** Use $x_e=(x(t)+x(-t))/2$, $x_o=(x(t)-x(-t))/2$. Simplify to get $x_e=\cos t$, $x_o=\sin t\cos t$." )
    show_eq([
        r"x_e(t)=\frac{\cos t+\cos(-t)}{2}=\cos t",
        r"x_o(t)=\frac{\sin t\cos t-\sin(-t)\cos(-t)}{2}=\sin t\cos t"
    ])

    # Energy vs Power example
    st.markdown("**Example 5:** Determine energy and power of $x(t)=A\cos(2\pi f_0 t)$.\n" 
                "**Solution:** Energy $E=\int_{-\infty}^{\infty}A^2\cos^2(...)dt=\infty$ (periodic ⇒ infinite energy).\n" 
                "Power $P=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}A^2\cos^2(...)dt=A^2/2$." )

    # 1.2 Elementary & Singularity Signals
    st.subheader("1.2 Elementary & Singularity Signals")
    st.write("Basic building blocks: exponentials, sinusoids, complex exponentials; singularities: delta and step.")
    st.markdown("**Exponential:** $x(t)=Ae^{at}$ (growth/decay).\n" 
                "**Sinusoid:** $x(t)=A\cos(2\pi f_0t+\theta)$.\n" 
                "**Complex exponential:** $Ae^{j(2\pi f_0t+\theta)}$.\n" 
                "**Delta:** $\delta(t)$ unit area.\n" 
                "**Step:** $u(t)$ switches at t=0.")
    show_eq([
        r"x(t)=Ae^{at}, \quad x(t)=A\cos(2\pi f_0t+\theta)",
        r"\delta(t):\int_{-\infty}^{\infty}\delta(t)dt=1, \quad u(t)=\begin{cases}1,&t\ge0\\0,&t<0\end{cases}"
    ])
    st.markdown("**Example 6:** Represent sampling: $x_s(t)=\sum_{n=-\infty}^{\infty}x(nT)\delta(t-nT)$.")

    # 1.3 Operations on Signals
    st.subheader("1.3 Operations on Signals")
    st.write("Time-shifting, scaling, reversal, and amplitude operations modify how a signal is displayed or processed.")
    show_eq([
        r"y(t)=x(t-t_0)",
        r"y(t)=x(at)",
        r"y(t)=x(-t)",
        r"y(t)=a\,x(t)"
    ])
    st.markdown("**Example 7:** If $y(t)=x(2-t)$, rewrite as $x(-(t-2))$. This is a time reversal followed by a delay of 2 units.")

    # 1.4 System Properties
    st.subheader("1.4 Properties of Systems")
    st.write("Key LTI system properties: linearity, time-invariance, causality, and stability.")
    st.markdown("- **Linearity:** $T\{a x_1 + b x_2\}=aT\{x_1\}+bT\{x_2\}$.\n" 
                "- **Time-Invariance:** Input shift ⇒ same output shift.\n" 
                "- **Causality:** Dependence only on present/past.\n" 
                "- **BIBO Stability:** Bounded input yields bounded output.")
    st.markdown("**Example 8:** For $y[n]=x[n]+2x[n-1]$, h[n]=[1,2] ⇒ LTI, uses only n,n-1 ⇒ causal. Stable since sum|h[n]|<∞.")

# -------------------------------------------
# Part II: Sampling & Sinusoids
# -------------------------------------------
elif part == "Part II: Sampling & Sinusoids":
    st.header(part)

    # 2.1 Sampling Theorem & Aliasing
    st.subheader("2.1 Sampling Theorem & Aliasing")
    st.write("Sampling at rate $f_s$ yields discrete-time samples x[n]=x(nT).\n" 
             "To avoid aliasing, f_s>2f_{max}. This ensures no spectral overlap.")
    show_eq([r"f_s>2f_{\max}\quad(\text{Nyquist criterion})"])
    st.markdown("**Example 9:** Sampling x(t)=sin(2π10t) at f_s=15Hz. Since f_s<20Hz, the discrete-time frequency alias to 5Hz (|10-15|).")

    # 2.2 Sinusoidal Signals & Phasors
    st.subheader("2.2 Sinusoidal Signals & Phasor Representation")
    st.write(
        "A sinusoid x(t)=A cos(2πf0t+θ) has amplitude A, freq f0, phase θ. "
        "As a phasor, Ae^{jθ} rotates at f0 in complex plane."
    )
    show_eq([
        r"x(t)=\Re\{Ae^{j(2\pi f_0t+\theta)}\}",
        r"Ae^{j\theta}=A(\cos\theta+j\sin\theta)"
    ])
    st.markdown("**Example 10:** Sum phasors 1∠30° and 2∠-45°. Convert: 1e^{jπ/6}+2e^{-jπ/4}, add, find magnitude and angle.")

# -------------------------------------------
# Part III: Modulation Techniques
# -------------------------------------------
else:
    st.header(part)

    # 3.1 Amplitude Modulation (AM)
    st.subheader("3.1 Amplitude Modulation (AM)")
    st.write(
        "AM: carrier multiplied by [1+ka m(t)]. Sidebands appear at f_c±f_m."
    )
    show_eq([
        r"x_{AM}(t)=A_c[1+k_a m(t)]\cos(2\pi f_c t)",
        r"\mu=k_aA_m=\max|k_a m(t)|"
    ])
    st.markdown("**Example 11:** Given envelope peak A_{max}=5V and minimum A_{min}=3V, modulation index \mu=(A_{max}-A_{min})/(A_{max}+A_{min})=(5-3)/(5+3)=0.25.")
    st.markdown("**Example 12:** For m(t)=cos(2πf_mt), expand x_{AM}(t) to show carrier and two sidebands:\n" )
    st.latex(
        r"x_{AM}(t)=A_c\cos(2\pi f_c t)+\frac{A_c\mu}{2}\cos(2\pi(f_c+f_m)t)+\frac{A_c\mu}{2}\cos(2\pi(f_c-f_m)t)"
    )

    # 3.2 Frequency & Phase Modulation (FM/PM)
    st.subheader("3.2 Frequency & Phase Modulation (FM/PM)")
    st.write(
        "FM: instantaneous frequency deviates by k_f m(t). PM: instantaneous phase deviates by k_p m(t)."
    )
    show_eq([
        r"x_{FM}(t)=\cos\bigl(2\pi f_c t + k_f\int m(τ)dτ\bigr)",
        r"x_{PM}(t)=\cos\bigl(2\pi f_c t + k_p m(t)\bigr)"
    ])
    st.markdown("**Example 13:** For m(t)=sin(2πf_mt), instantaneous frequency = f_c + (k_f/2π)sin(2πf_mt).  ")

    # 3.3 Envelope Detector
    st.subheader("3.3 Envelope Detector for AM")
    st.write(
        "Circuit uses diode + RC. Diode charges capacitor at peaks; resistor discharges between. "
        "Output approximates envelope if RC time constant >> 1/f_c but << 1/f_m."
    )
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3c/Envelope_detector_circuit.svg",
        use_column_width=True
    )
