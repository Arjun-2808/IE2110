import streamlit as st
import requests
from streamlit_lottie import st_lottie

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

# Sidebar navigation using radio for direct visibility
parts = [
    "Part I: Signals, Systems & Fourier",
    "Part II: Sampling & Sinusoids",
    "Part III: Modulation"
]
part = st.sidebar.radio("Select Slide Part", parts)
st.sidebar.markdown("---")

# Title and Lottie animation
st.title("IE2110: Signals & Systems Master Review")
if lottie:
    st_lottie(lottie, height=150)

# Helper for equations
def show_eq(equations):
    for eq in equations:
        st.latex(eq)

# Display full content for each part
if part == "Part I: Signals, Systems & Fourier":
    st.header(part)
    st.subheader("1.1 Classification of Signals")
    st.markdown(
        "**Key Types:** Continuous vs Discrete, Deterministic vs Random, "
        "Periodic vs Aperiodic, Even vs Odd, Energy vs Power."
    )
    show_eq([
        r"x_e(t)=\tfrac12[x(t)+x(-t)]",
        r"x_o(t)=\tfrac12[x(t)-x(-t)]",
        r"E=\int_{-\infty}^{\infty}x^2(t)dt,\ P=\lim_{T\to\infty}\tfrac1T\int_{-T/2}^{T/2}x^2(t)dt"
    ])
    st.markdown("**Example:** Show $x(t)=t^3\cos^3(10t)$ is odd, hence $\int_{-T}^T x(t)dt=0$. Solution: $x(-t)=-x(t)$, integral over symmetric limits is zero.")

    st.subheader("1.2 System Properties & LTI")
    st.markdown(
        "- **Linearity**: $T\{ax_1 + bx_2\} = aT\{x_1\} + bT\{x_2\}$  "
        "- **Time-Invariance**: Input shift ⇒ output shift  "
        "- **Causality**: Depends only on present/past inputs  "
        "- **BIBO Stability**: Bounded input ⇒ bounded output"
    )
    st.markdown("**Example:** For $y[n]=(x[n]+x[n-1]+x[n-2])/3$, convolution form (LTI), depends only on past (causal).")

    st.subheader("1.3 Convolution")
    show_eq([
        r"y[n]=\sum_{m=-\infty}^{\infty}x[m]h[n-m]",
        r"y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau"
    ])
    st.markdown("**Example:** Convolve $x[n]=[1,2,1]$ with $h[n]=[1,-1]$: flip, shift, multiply, sum.")

    st.subheader("1.4 Fourier Series & Transform")
    st.markdown("**Fourier Series** (periodic):")
    show_eq([
        r"x(t)=a_0+\sum_{k=1}^\infty[a_k\cos(2\pi kf_0t)+b_k\sin(2\pi kf_0t)]",
        r"c_k=\tfrac1{T_0}\int_0^{T_0}x(t)e^{-j2\pi kf_0t}dt"
    ])
    st.markdown("**Fourier Transform** (aperiodic):")
    show_eq([
        r"X(f)=\int_{-\infty}^{\infty}x(t)e^{-j2\pi ft}dt",
        r"x(t)=\int_{-\infty}^{\infty}X(f)e^{j2\pi ft}df"
    ])

elif part == "Part II: Sampling & Sinusoids":
    st.header(part)
    st.subheader("2.1 Sampling Theorem & Aliasing")
    st.markdown(
        "Sampling at rate $f_s$ ⇒ $x[n]=x(nT)$ with $T=1/f_s$.  "
        "To avoid aliasing, require $f_s>2f_{max}$ (Nyquist)."
    )
    st.markdown("**Example:** If $f_s<2f_0$, spectral copies overlap ⇒ aliasing.")

    st.subheader("2.2 Sinusoidal Signals & Phasors")
    st.markdown(
        "$x(t)=A\cos(2\pi f_0t+\theta)$ as phasor $Ae^{j\theta}$.  "
        "Avg. power $=A^2/2$, RMS $=A/\sqrt2$."
    )
    show_eq([
        r"x(t)=\Re\{Ae^{j(2\pi f_0t+\theta)}\}",
        r"A e^{j\theta}=A(\cos\theta+j\sin\theta)"
    ])
    st.markdown("**Example:** Sum phasors 2∠45° and 3∠-30° via complex addition.")

else:
    st.header(part)
    st.subheader("3.1 Amplitude Modulation (AM)")
    st.markdown(
        "$x_{AM}(t)=A_c[1+\mu m(t)]\cos(2\pi f_c t)$,  "
        "$\mu=k_a A_m$, under $\mu<1$, over $\mu>1$."
    )
    show_eq([
        r"\mu=\max|k_a m(t)|",
        r"X_{AM}(f)=\tfrac{A_c}{2}[\delta(f-f_c)+\delta(f+f_c)]+\tfrac{A_c\mu}{4}[\delta(f-(f_c±f_m))]"
    ])
    st.markdown(
        "**Example:** For $m(t)=A_m\cos(2\pi f_mt)$, carrier power $P_c=A_c^2/2$, sidebands $=A_c^2\mu^2/4$, efficiency = $\mu^2/(2+\mu^2)$."
    )
    st.subheader("3.2 FM & PM")
    st.markdown(
        "FM: $x_{FM}(t)=\cos(2\pi f_ct + k_f\int m(\tau)d\tau)$  "
        "PM: $x_{PM}(t)=\cos(2\pi f_ct + k_p m(t))$."
    )
    st.markdown("**Demodulation:** FM via PLL/discriminator; PM via PLL.")
    st.subheader("3.3 Envelope Detector")
    st.markdown(
        "Diode + RC low-pass tracks envelope of $x_{AM}(t)$ to recover $m(t)$."
    )
