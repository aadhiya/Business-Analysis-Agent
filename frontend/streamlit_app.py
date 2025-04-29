# frontend/streamlit_app.py

import streamlit as st
import requests

def main():
   st.title("Business Analysis Agent")
   uploaded_file = st.file_uploader("Upload your Business PDF Document", type=["pdf"])

   if uploaded_file is not None:
        if st.button("Analyze"):
            with st.spinner("Processing document... 🚀 Please wait..."):
                files = {"file": uploaded_file.getvalue()}
                response = requests.post("http://localhost:8000/analyze/", files=files)

                if response.status_code == 200:
                    report = response.json()["result"]
                    st.success("✅ Analysis Complete!")
                    st.text_area("Generated Business Analysis Report:", value=report, height=500)
                else:
                    st.error(f"❌ Error: {response.text}")

if __name__ == "__main__":
    main()
