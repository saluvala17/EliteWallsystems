"""
Elite Wall Systems - Brand Styles
Shared styling for all pages
"""

# Elite Wall Systems Brand Colors
BRAND_GREEN = "#7AB930"
BRAND_GREEN_DARK = "#5A9020"
BRAND_GRAY = "#2D2D2D"
BRAND_LIGHT_GREEN = "#E8F5D9"

def get_page_styling():
    """Return CSS for Elite Wall Systems branding"""
    return f"""
<style>
    /* Import clean font */
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap');
    
    /* Global styles */
    .stApp {{
        font-family: 'Open Sans', sans-serif;
    }}
    
    /* Page header */
    .page-header {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 0.5rem;
    }}
    
    .page-header-icon {{
        font-size: 2rem;
    }}
    
    .page-header-title {{
        font-size: 1.8rem;
        font-weight: 600;
        color: {BRAND_GRAY};
    }}
    
    .page-subtitle {{
        color: #666;
        margin-bottom: 1.5rem;
    }}
    
    /* Logo components */
    .logo-container {{
        display: flex;
        flex-direction: column;
        gap: 3px;
    }}
    
    .logo-chevron {{
        width: 35px;
        height: 7px;
        background: linear-gradient(90deg, {BRAND_GREEN} 0%, {BRAND_GREEN_DARK} 100%);
        clip-path: polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%, 15% 50%);
    }}
    
    .logo-chevron-sm {{
        width: 25px;
        height: 5px;
        background: linear-gradient(90deg, {BRAND_GREEN} 0%, {BRAND_GREEN_DARK} 100%);
        clip-path: polygon(0 0, 85% 0, 100% 50%, 85% 100%, 0 100%, 15% 50%);
    }}
    
    /* Sidebar styling - Light Theme */
    section[data-testid="stSidebar"] {{
        background-color: #F5F9F0;
    }}
    
    section[data-testid="stSidebar"] .stMarkdown {{
        color: {BRAND_GRAY};
    }}
    
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: {BRAND_GREEN} !important;
    }}
    
    section[data-testid="stSidebar"] hr {{
        border-color: #D4E8C4;
    }}
    
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stMultiSelect label {{
        color: {BRAND_GRAY} !important;
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
    
    .stButton > button[kind="secondary"] {{
        background-color: transparent;
        color: {BRAND_GRAY};
        border: 1px solid #DDD;
    }}
    
    .stButton > button[kind="secondary"]:hover {{
        background-color: #F5F5F5;
        color: {BRAND_GRAY};
    }}
    
    /* Form submit button */
    .stFormSubmitButton > button {{
        background-color: {BRAND_GREEN};
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 600;
    }}
    
    .stFormSubmitButton > button:hover {{
        background-color: {BRAND_GREEN_DARK};
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
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background-color: #F5F5F5;
        border-radius: 6px 6px 0 0;
        padding: 10px 20px;
        font-weight: 500;
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: {BRAND_GREEN} !important;
        color: white !important;
    }}
    
    /* Expanders */
    .streamlit-expanderHeader {{
        background-color: {BRAND_LIGHT_GREEN};
        border-radius: 6px;
        font-weight: 500;
    }}
    
    .streamlit-expanderHeader:hover {{
        background-color: #D4E8C4;
    }}
    
    /* DataFrames */
    .stDataFrame {{
        border-radius: 8px;
        overflow: hidden;
    }}
    
    /* Input fields focus */
    .stTextInput input:focus,
    .stNumberInput input:focus,
    .stTextArea textarea:focus {{
        border-color: {BRAND_GREEN} !important;
        box-shadow: 0 0 0 1px {BRAND_GREEN} !important;
    }}
    
    /* Success messages */
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
    
    /* Status badges */
    .status-active {{
        background-color: {BRAND_GREEN};
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }}
    
    .status-estimate {{
        background-color: #F4A460;
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }}
    
    .status-completed {{
        background-color: #4A90D9;
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }}
    
    /* Charts - Plotly colors */
    .js-plotly-plot .plotly .modebar {{
        right: 10px !important;
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
"""

def get_sidebar_logo():
    """Return HTML for sidebar logo"""
    return f"""
    <div style="padding: 0.5rem 0 1rem 0; margin-top: -1rem;">
        <div class="logo-container">
            <div class="logo-chevron-sm"></div>
            <div class="logo-chevron-sm"></div>
            <div class="logo-chevron-sm"></div>
        </div>
        <div style="margin-top: 8px;">
            <span style="color: {BRAND_GREEN}; font-size: 1.2rem; font-weight: 700;">Elite</span>
            <span style="color: {BRAND_GRAY}; font-size: 1.2rem; font-weight: 300;"> Wall Systems</span>
        </div>
    </div>
    """

def get_page_header(icon, title, subtitle=""):
    """Return HTML for page header"""
    html = f"""
    <div class="page-header">
        <span class="page-header-icon">{icon}</span>
        <span class="page-header-title">{title}</span>
    </div>
    """
    if subtitle:
        html += f'<p class="page-subtitle">{subtitle}</p>'
    return html