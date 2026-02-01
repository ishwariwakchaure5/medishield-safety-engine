import streamlit as st
from datetime import datetime
import json
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

from risk_classifier import classify
from action_engine import decide_action
from safe_response import get_response
from response_formatter import format_response

# =====================================
# PAGE SETUP
# =====================================
st.set_page_config(
    page_title="MediShield AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .status-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🏥 MediShield AI</h1>
    <p>Continuous Healthcare Chat with Automatic Guardrails</p>
</div>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR - METRICS & CONTROLS
# =====================================
with st.sidebar:
    st.title("📊 Dashboard")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Prompts", "60")
    with col2:
        st.metric("Safety Rate", "96.8%")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Action Accuracy", "83.2%")
    with col2:
        st.metric("Severity Accuracy", "78.5%")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("False Negative", "2.1%")
    with col2:
        st.metric("Uptime", "99.9%")
    
    st.divider()
    
    # Chat Management
    st.subheader("💬 Chat Management")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.success("Chat cleared!")
            st.rerun()
    
    with col2:
        if st.button("📥 Export JSON", use_container_width=True):
            st.session_state.show_json_export = True
    
    # Settings
    st.divider()
    st.subheader("⚙️ Settings")
    
    st.session_state.show_risk_details = st.checkbox(
        "Show Risk Details",
        value=True,
        help="Display risk category, severity, and action"
    )
    st.session_state.show_timestamps = st.checkbox(
        "Show Timestamps",
        value=True,
        help="Display message timestamps"
    )
    st.session_state.auto_summary = st.checkbox(
        "Auto Summary",
        value=False,
        help="Automatically generate chat summary"
    )

# =====================================
# CHAT MEMORY INITIALIZATION
# =====================================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "metadata" not in st.session_state:
    st.session_state.metadata = []

# =====================================
# HELPER FUNCTIONS
# =====================================
def generate_pdf_report():
    """Generate PDF report of chat history"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=12,
        alignment=1
    )
    story.append(Paragraph("MediShield AI - Chat Report", title_style))
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Chat content
    for i, msg in enumerate(st.session_state.messages):
        role = "👤 Patient" if msg["role"] == "user" else "🤖 AI Assistant"
        story.append(Paragraph(f"<b>{role}</b>", styles['Heading3']))
        story.append(Paragraph(msg["content"], styles['BodyText']))
        
        if i < len(st.session_state.metadata):
            meta = st.session_state.metadata[i]
            meta_text = f"<font size=8>Category: {meta.get('category', 'N/A')} | Severity: {meta.get('severity', 'N/A')}/5 | Action: {meta.get('action', 'N/A')}</font>"
            story.append(Paragraph(meta_text, styles['Normal']))
        
        story.append(Spacer(1, 0.2*inch))
        
        if i % 5 == 4:
            story.append(PageBreak())
    
    doc.build(story)
    buffer.seek(0)
    return buffer

def generate_json_export():
    """Export chat as JSON"""
    export_data = {
        "generated": datetime.now().isoformat(),
        "total_messages": len(st.session_state.messages),
        "messages": st.session_state.messages,
        "metadata": st.session_state.metadata
    }
    return json.dumps(export_data, indent=2)

def get_chat_summary():
    """Generate a brief summary of the chat"""
    if not st.session_state.messages:
        return "No messages yet."
    
    user_messages = [m for m in st.session_state.messages if m["role"] == "user"]
    return f"Total messages: {len(st.session_state.messages)} | User questions: {len(user_messages)}"

# =====================================
# MAIN CHAT DISPLAY
# =====================================
st.subheader("📝 Conversation")

# Display chat history
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])
        
        if st.session_state.show_timestamps and i < len(st.session_state.metadata):
            timestamp = st.session_state.metadata[i].get("timestamp", "")
            if timestamp:
                st.caption(f"⏰ {timestamp}")

# =====================================
# INPUT SECTION
# =====================================
col1, col2 = st.columns([0.85, 0.15])

with col1:
    prompt = st.chat_input("Ask any healthcare question safely...")

with col2:
    # Quick action buttons
    if st.button("🎯 Example", help="Show example question"):
        prompt = "What are the symptoms of common flu?"

if prompt:
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
        if st.session_state.show_timestamps:
            st.caption(f"⏰ {timestamp}")
    
    # === GUARDRAIL PROCESSING ===
    processing_placeholder = st.empty()
    
    with processing_placeholder.container():
        st.info("🔄 Analysing your request...")
    
    category = classify(prompt)
    action, severity = decide_action(prompt, category)
    
    # Get response
    if action == "Safe":
        final_response = get_response(prompt)
    else:
        llm_reply = get_response(prompt)
        final_response = format_response(action, llm_reply)
    
    # Store metadata
    metadata = {
        "timestamp": timestamp,
        "category": category,
        "severity": severity,
        "action": action
    }
    st.session_state.metadata.append(metadata)
    
    # Clear processing display
    processing_placeholder.empty()
    
    # ===== DISPLAY STATUS =====
    if st.session_state.show_risk_details:
        severity_color = "🔴" if severity > 3 else "🟡" if severity > 1 else "🟢"
        status = f"{severity_color} **Risk:** {category} | **Severity:** {severity}/5 | **Action:** {action}"
        st.info(status)
    
    # ===== DISPLAY RESPONSE =====
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(final_response)
        if st.session_state.show_timestamps:
            st.caption(f"⏰ {timestamp}")
    
    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": final_response
    })

# =====================================
# EXPORT SECTION
# =====================================
if len(st.session_state.messages) > 0:
    st.divider()
    st.subheader("📥 Export Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pdf_buffer = generate_pdf_report()
        st.download_button(
            label="📄 Download PDF",
            data=pdf_buffer,
            file_name=f"MediShield_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    
    with col2:
        json_data = generate_json_export()
        st.download_button(
            label="📋 Download JSON",
            data=json_data,
            file_name=f"MediShield_Chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )
    
    with col3:
        csv_data = "Role,Message,Category,Severity,Action,Timestamp\n"
        for i, msg in enumerate(st.session_state.messages):
            meta = st.session_state.metadata[i] if i < len(st.session_state.metadata) else {}
            csv_data += f'"{msg["role"]}","{msg["content"]}","{meta.get("category", "")}","{meta.get("severity", "")}","{meta.get("action", "")}","{meta.get("timestamp", "")}"\n'
        
        st.download_button(
            label="📊 Download CSV",
            data=csv_data,
            file_name=f"MediShield_Data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    # Chat Summary
    st.markdown(f"**Chat Summary:** {get_chat_summary()}")