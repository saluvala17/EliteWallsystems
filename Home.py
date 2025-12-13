"""
Elite Wall Systems - Job Costing Application
Main entry point - Google Sheets Version
"""
import streamlit as st
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

# Check if Google Sheets is configured, otherwise use demo mode
import os

DEMO_MODE = True  # Default to demo

# Check for Streamlit secrets or credentials file
try:
    if hasattr(st, 'secrets') and 'SPREADSHEET_ID' in st.secrets:
        from google_sheets import get_all_jobs, get_all_customers, get_job_cost_totals, initialize_sheets
        DEMO_MODE = False
    elif os.path.exists(os.path.join(os.path.dirname(__file__), 'credentials.json')):
        from google_sheets import get_all_jobs, get_all_customers, get_job_cost_totals, initialize_sheets
        DEMO_MODE = False
except:
    pass

if DEMO_MODE:
    from demo_data import get_all_jobs, get_all_customers, get_job_cost_totals, initialize_sheets
from utils import format_currency, get_status_color

# Page configuration
st.set_page_config(
    page_title="Elite Wall Systems",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Elite Wall Systems Brand Colors
BRAND_GREEN = "#7AB930"
BRAND_GREEN_DARK = "#5A9020"
BRAND_GRAY = "#2D2D2D"
BRAND_LIGHT_GREEN = "#E8F5D9"

# Custom CSS with Elite Wall Systems Branding
st.markdown(f"""
<style>
    /* Import clean font */
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
    
    /* Global styles */
    .stApp {{
        font-family: 'Open Sans', sans-serif;
    }}
    
    /* Logo and Header */
    .brand-header {{
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 1rem;
        padding: 1rem 0;
    }}
    
    .logo-container {{
        display: flex;
        flex-direction: column;
        gap: 3px;
    }}
    
    .logo-chevron {{
        width: 40px;
        height: 8px;
        background: linear-gradient(90deg, {BRAND_GREEN} 0%, {BRAND_GREEN_DARK} 100%);
        clip-path: polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%, 15% 50%);
    }}
    
    .brand-title {{
        font-size: 2.2rem;
        font-weight: 300;
        color: {BRAND_GRAY};
        letter-spacing: -0.5px;
    }}
    
    .brand-title-bold {{
        font-weight: 700;
        color: {BRAND_GREEN};
    }}
    
    .sub-header {{
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 2rem;
        font-weight: 400;
    }}
    
    /* Sidebar styling - Light Theme */
    section[data-testid="stSidebar"] {{
        background-color: #F5F9F0;
    }}
    
    section[data-testid="stSidebar"] .stMarkdown {{
        color: {BRAND_GRAY};
    }}
    
    section[data-testid="stSidebar"] h2 {{
        color: {BRAND_GREEN} !important;
    }}
    
    section[data-testid="stSidebar"] hr {{
        border-color: #D4E8C4;
    }}
    
    /* Hide default page navigation */
    section[data-testid="stSidebar"] > div > div > div > div > ul {{
        display: none;
    }}
    
    /* Style page links */
    section[data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"] {{
        color: {BRAND_GRAY} !important;
        background-color: transparent;
        padding: 0.5rem 0.75rem;
        border-radius: 6px;
        margin: 2px 0;
        display: block;
        text-decoration: none;
        transition: background-color 0.2s;
    }}
    
    section[data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"]:hover {{
        background-color: rgba(122, 185, 48, 0.2);
        color: {BRAND_GRAY} !important;
    }}
    
    section[data-testid="stSidebar"] a[data-testid="stPageLink-NavLink"][aria-current="page"] {{
        background-color: {BRAND_GREEN};
        color: white !important;
        font-weight: 600;
    }}
    
    /* Metric cards */
    div[data-testid="metric-container"] {{
        background-color: #FAFAFA;
        border: 1px solid #E0E0E0;
        border-radius: 8px;
        padding: 1rem;
        border-left: 4px solid {BRAND_GREEN};
    }}
    
    div[data-testid="metric-container"] label {{
        color: {BRAND_GRAY} !important;
    }}
    
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] {{
        color: {BRAND_GREEN} !important;
    }}
    
    /* Buttons */
    .stButton > button {{
        background-color: {BRAND_GREEN};
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        background-color: {BRAND_GREEN_DARK};
        color: white;
        border: none;
    }}
    
    /* Section headers */
    .section-header {{
        color: {BRAND_GRAY};
        font-size: 1.3rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid {BRAND_GREEN};
    }}
    
    /* DataFrames */
    .stDataFrame {{
        border-radius: 8px;
        overflow: hidden;
    }}
    
    /* Expanders */
    .streamlit-expanderHeader {{
        background-color: {BRAND_LIGHT_GREEN};
        border-radius: 6px;
    }}
    
    /* Success/Info boxes */
    .stSuccess {{
        background-color: {BRAND_LIGHT_GREEN};
        border-left-color: {BRAND_GREEN};
    }}
    
    /* Demo mode badge */
    .demo-badge {{
        background-color: {BRAND_GREEN};
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
    }}
    
    /* Footer */
    .footer {{
        text-align: center;
        color: #888;
        padding: 2rem 0 1rem 0;
        font-size: 0.85rem;
    }}
    
    .footer-brand {{
        color: {BRAND_GREEN};
        font-weight: 600;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Sidebar Logo
    st.markdown(f"""
    <div style="padding: 0.5rem 0 1rem 0; margin-top: -1rem;">
        <div class="logo-container">
            <div class="logo-chevron"></div>
            <div class="logo-chevron"></div>
            <div class="logo-chevron"></div>
        </div>
        <div style="margin-top: 10px;">
            <span style="color: {BRAND_GREEN}; font-size: 1.4rem; font-weight: 700;">Elite</span>
            <span style="color: {BRAND_GRAY}; font-size: 1.4rem; font-weight: 300;"> Wall Systems</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if DEMO_MODE:
        st.markdown('<div class="demo-badge">🎮 DEMO MODE</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation with actual page links
    st.page_link("Home.py", label="🏠 Home", icon=None)
    st.page_link("pages/1_Dashboard.py", label="📊 Dashboard", icon=None)
    st.page_link("pages/2_Jobs.py", label="📋 Jobs", icon=None)
    st.page_link("pages/3_Cost_Entry.py", label="💰 Cost Entry", icon=None)
    st.page_link("pages/4_Customers.py", label="👥 Customers", icon=None)
    st.page_link("pages/5_Vendors.py", label="🏪 Vendors", icon=None)
    st.page_link("pages/6_Reports.py", label="📈 Reports", icon=None)
    
    st.markdown("---")
    st.caption("v1.0 | Job Costing System")
    
    if not DEMO_MODE:
        if st.button("🔄 Initialize Sheets"):
            with st.spinner("Setting up sheets..."):
                initialize_sheets()
                st.success("Sheets initialized!")
                st.rerun()

# Main content - Brand Header
st.markdown(f"""
<div class="brand-header">
    <div class="logo-container">
        <div class="logo-chevron"></div>
        <div class="logo-chevron"></div>
        <div class="logo-chevron"></div>
    </div>
    <div>
        <div class="brand-title">
            <span class="brand-title-bold">Elite</span> Wall Systems
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="sub-header">Job Costing Dashboard</p>', unsafe_allow_html=True)

# Load data
try:
    jobs = get_all_jobs()
    customers = get_all_customers()
except Exception as e:
    st.error(f"⚠️ Error loading data: {e}")
    st.stop()

# Calculate metrics
active_jobs = [j for j in jobs if j.get("status") == "active"]
total_contract_value = sum(float(j.get("contract_amount", 0) or 0) for j in active_jobs)
total_approved_cos = sum(float(j.get("approved_change_orders", 0) or 0) for j in active_jobs)

# Calculate total costs across all active jobs
total_costs = 0
over_budget_jobs = 0
for job in active_jobs:
    totals = get_job_cost_totals(job["id"])
    job_cost = totals.get("total", 0)
    total_costs += job_cost
    
    job_budget = sum([
        float(job.get("budget_insurance", 0) or 0),
        float(job.get("budget_labor", 0) or 0),
        float(job.get("budget_stamps", 0) or 0),
        float(job.get("budget_material", 0) or 0),
        float(job.get("budget_subs_bond", 0) or 0),
        float(job.get("budget_equipment", 0) or 0),
    ])
    if job_budget > 0 and job_cost > job_budget:
        over_budget_jobs += 1

# KPI Cards
st.markdown('<div class="section-header">📊 Key Metrics</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Active Jobs",
        value=len(active_jobs),
        delta=f"{len(jobs)} total"
    )

with col2:
    st.metric(
        label="Total Contract Value",
        value=format_currency(total_contract_value),
        delta=format_currency(total_approved_cos) + " in COs"
    )

with col3:
    st.metric(
        label="Total Costs (Active)",
        value=format_currency(total_costs)
    )

with col4:
    st.metric(
        label="Over Budget Jobs",
        value=over_budget_jobs,
        delta="attention needed" if over_budget_jobs > 0 else "all on track",
        delta_color="inverse" if over_budget_jobs > 0 else "normal"
    )

st.markdown("---")

# Active Jobs Table
st.markdown('<div class="section-header">📋 Active Jobs</div>', unsafe_allow_html=True)

if active_jobs:
    job_data = []
    for job in active_jobs:
        customer_name = job.get("customers", {}).get("name", "N/A") if job.get("customers") else "N/A"
        totals = get_job_cost_totals(job["id"])
        total_revenue = float(job.get("contract_amount", 0) or 0) + float(job.get("approved_change_orders", 0) or 0)
        total_budget = sum([
            float(job.get("budget_insurance", 0) or 0),
            float(job.get("budget_labor", 0) or 0),
            float(job.get("budget_stamps", 0) or 0),
            float(job.get("budget_material", 0) or 0),
            float(job.get("budget_subs_bond", 0) or 0),
            float(job.get("budget_equipment", 0) or 0),
        ])
        total_cost = totals.get("total", 0)
        
        profit = total_revenue - total_cost if total_revenue > 0 else 0
        profit_pct = (profit / total_revenue * 100) if total_revenue > 0 else 0
        budget_pct = (total_cost / total_budget * 100) if total_budget > 0 else 0
        status_indicator = "🟢" if budget_pct <= 90 else ("🟡" if budget_pct <= 100 else "🔴")
        
        job_data.append({
            "Status": status_indicator,
            "Job #": job.get("job_number"),
            "Job Name": job.get("job_name"),
            "Customer": customer_name,
            "Contract": format_currency(job.get("contract_amount", 0)),
            "Total Revenue": format_currency(total_revenue),
            "Total Cost": format_currency(total_cost),
            "Budget Used": f"{budget_pct:.0f}%",
            "Profit": format_currency(profit),
            "Margin": f"{profit_pct:.1f}%"
        })
    
    st.dataframe(job_data, use_container_width=True, hide_index=True)
else:
    st.info("No active jobs found. Go to **Jobs** to create your first job.")

st.markdown("---")

# Quick Actions
st.markdown('<div class="section-header">⚡ Quick Actions</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➕ New Job", use_container_width=True):
        st.switch_page("pages/2_Jobs.py")

with col2:
    if st.button("💰 Enter Costs", use_container_width=True):
        st.switch_page("pages/3_Cost_Entry.py")

with col3:
    if st.button("📈 View Reports", use_container_width=True):
        st.switch_page("pages/6_Reports.py")

# Footer
st.markdown(f"""
<div class="footer">
    <span class="footer-brand">Elite Wall Systems</span> Job Costing System<br>
    <span style="font-size: 0.75rem;">Anil Pachunuri, PE LEED AP | Chief Estimator</span>
</div>
""", unsafe_allow_html=True)