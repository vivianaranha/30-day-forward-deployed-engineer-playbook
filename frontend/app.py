import requests
import streamlit as st
st.set_page_config(page_title="FDE Support Triage",layout="wide")
st.title("Support Ticket Triage")
st.caption("Forward Deployed Engineer capstone prototype")
api=st.sidebar.text_input("API URL","http://localhost:8000")
ticket_id=st.text_input("Ticket ID","T-1001")
subject=st.text_input("Subject","Production login outage")
description=st.text_area("Description","All users cannot access the production application after the authentication change.")
customer_tier=st.selectbox("Customer tier",["standard","gold","platinum"])
if st.button("Analyze Ticket"):
    response=requests.post(f"{api}/analyze",json={"ticket_id":ticket_id,"subject":subject,"description":description,"customer_tier":customer_tier},timeout=10)
    if response.ok:
        result=response.json(); st.session_state["analysis"]=result
        c1,c2,c3=st.columns(3); c1.metric("Category",result["category"]); c2.metric("Priority",result["priority"]); c3.metric("Confidence",f"{result['confidence']:.0%}")
        st.subheader("Summary"); st.write(result["summary"])
        st.subheader("Recommended Team"); st.write(result["recommended_team"])
        st.subheader("Why"); st.write(result["explanation"])
    else: st.error(response.text)
if "analysis" in st.session_state:
    st.divider(); st.subheader("Pilot Feedback")
    accepted=st.radio("Was this recommendation useful?",["Yes","No"],horizontal=True)
    comment=st.text_input("Comment")
    if st.button("Submit Feedback"):
        requests.post(f"{api}/feedback",json={"ticket_id":st.session_state["analysis"]["ticket_id"],"accepted":accepted=="Yes","comment":comment},timeout=10)
        st.success("Feedback recorded")
