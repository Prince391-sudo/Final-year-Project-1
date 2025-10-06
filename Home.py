import streamlit as st
import random
from datetime import datetime

# 🧭 Page Configuration
st.set_page_config(page_title="MSME BI App", page_icon="💼", layout="wide")

# 🎨 Styling
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

# ✨ LOGIN PAGE
if not st.session_state["authenticated"]:
    st.markdown("<h1 class='main-title'>💼 MSME BI Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Empowering Small Businesses with Data-driven Insights</p>", unsafe_allow_html=True)

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

    quotes = [
        "“Small businesses are the backbone of innovation.”",
        "“Empowering MSMEs means empowering the future.”",
        "“Every big idea starts small — and data helps it grow.”"
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
                <h3>🤖 AI Predictive</h3>
                <p>Upload your MSME datasets and clean them for analysis.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Upload Page"):
            st.switch_page("pages/Upload.py")

    with col2:
        st.markdown("""
            <div class='card'>
                <h3>📊 Explore Dashboard</h3>
                <p>Visualize trends and gain insights using interactive charts.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Dashboard"):
            st.switch_page("pages/Dashboard.py")

    with col3:
        st.markdown("""
            <div class='card'>
                <h3>📑 Reports & Export</h3>
                <p>Generate professional PDF reports and download insights easily.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Reports"):
            st.switch_page("pages/Reports.py")

    st.markdown("---")

    st.markdown("""
        <div class='card'>
            <h3>🧭 Admin Panel</h3>
            <p>Manage users and monitor analytics performance.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Admin Page"):
        st.switch_page("pages/Admin.py")

    # 🕒 Footer Section
    st.markdown(f"""
        <footer>
            <hr>
            <p>© 2025 MSME BI Dashboard | Empowering Small Businesses with Smart Data Insights</p>
            <p>Last Login: {datetime.now().strftime("%B %d, %Y %H:%M:%S")}</p>
        </footer>
    """, unsafe_allow_html=True)

    if st.button("Logout"):
        st.session_state.clear()
        st.rerun()

    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = ""
        st.rerun()
