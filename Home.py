import streamlit as st
import random
from datetime import datetime

# 🧭 Page Configuration
st.set_page_config(page_title="MSME BI App", page_icon="💼", layout="wide")

# 🎨 Enhanced Styling
st.markdown("""
    <style>
        body { font-family: 'Segoe UI', Roboto, sans-serif; background: #0b0c10; color: #f8f9fa; }
        h1, h2, h3, h4 { color: #66fcf1 !important; }
        .main-title { text-align: center; font-size: 38px; font-weight: 800; margin-top: 10px; }
        .sub-title { text-align: center; font-size: 20px; color: #c5c6c7; margin-bottom: 30px; }
        [data-testid="stSidebar"] { background-color: #1f2833 !important; }
        .card {
            background: linear-gradient(135deg, #1f2833 0%, #0b0c10 100%);
            padding: 30px; border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
            transition: transform 0.2s ease-in-out;
        }
        .card:hover { transform: translateY(-5px); }
        .stButton button {
            background: linear-gradient(90deg, #45a29e, #66fcf1);
            color: #0b0c10 !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            padding: 10px 25px !important;
            border: none !important;
        }
        .stButton button:hover { background: linear-gradient(90deg, #66fcf1, #45a29e); }
        .quote { text-align: center; color: #f1c40f; font-style: italic; margin-top: 40px; }
        footer { text-align: center; color: #c5c6c7; margin-top: 60px; font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# 🎯 Session State
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# ✨ LOGIN & SIGN-UP PAGE
if not st.session_state["authenticated"]:
    st.markdown("<h1 class='main-title'>💼 MSME BI Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Empowering Small Businesses with Data-driven Insights</p>", unsafe_allow_html=True)

    option = st.radio("Select an Option", ["Login", "Sign Up", "Google Login"])

    if option == "Login":
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        if st.button("Login"):
            if username and password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success(f"✅ Welcome, {username}!")
                st.rerun()
            else:
                st.error("❌ Please enter both username and password.")

    elif option == "Sign Up":
        new_user = st.text_input("👤 Choose Username")
        new_pass = st.text_input("🔑 Choose Password", type="password")
        confirm_pass = st.text_input("🔁 Confirm Password", type="password")
        if st.button("Create Account"):
            if new_user and new_pass == confirm_pass:
                st.success("✅ Account created successfully! You can now login.")
            else:
                st.error("❌ Please check your input fields.")

    elif option == "Google Login":
        st.markdown("👉 [Login with Google](https://accounts.google.com/signin) *(demo link)*")
        st.info("⚙️ Integrate Firebase or OAuth for real Google authentication.")

    # 🌟 Random Quote
    quotes = [
        "“Small businesses are the backbone of innovation.”",
        "“Empowering MSMEs means empowering the future.”",
        "“Every big idea starts small — and data helps it grow.”",
        "“Insight turns opportunity into success.”",
        "“Data-driven MSMEs outperform intuition-driven ones.”"
    ]
    st.markdown(f"<p class='quote'>{random.choice(quotes)}</p>", unsafe_allow_html=True)

# 🏠 MAIN DASHBOARD HOME
else:
    st.markdown(f"<h1 class='main-title'>Welcome, {st.session_state['username']} 👋</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Here’s your business intelligence workspace.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class='card'>
                <h3>AI Predictive</h3>
                <p>Upload your MSME datasets and clean them for analysis.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Go to Upload Page")

    with col2:
        st.markdown("""
            <div class='card'>
                <h3>📊 Explore Dashboard</h3>
                <p>Visualize trends and gain insights using interactive charts.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Go to Dashboard")

    with col3:
        st.markdown("""
            <div class='card'>
                <h3>📑 Reports & Export</h3>
                <p>Generate professional PDF reports and download insights easily.</p>
            </div>
        """, unsafe_allow_html=True)
        st.button("Go to Reports")

    # 🕒 Footer Section
    st.markdown("""
        <footer>
            <hr>
            <p>© 2025 MSME BI Dashboard | Empowering Small Businesses with Smart Data Insights</p>
            <p>Last Login: {}</p>
        </footer>
    """.format(datetime.now().strftime("%B %d, %Y %H:%M:%S")), unsafe_allow_html=True)

    # 🚪 Logout Button
    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = ""
        st.rerun()
