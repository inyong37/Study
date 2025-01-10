import streamlit as st

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Select a page:",
    ["Page 1", "Page 2", "Page 3", "Page 4", "Page 5", "Page 6"]
)

# Content for each page
if page == "Page 1":
    st.title("Page 1")
    st.write("Content for Page 1")
    
elif page == "Page 2":
    st.title("Page 2")
    st.write("Content for Page 2")
    
elif page == "Page 3":
    st.title("Page 3")
    st.write("Content for Page 3")
    
elif page == "Page 4":
    st.title("Page 4")
    st.write("Content for Page 4")
    
elif page == "Page 5":
    st.title("Page 5")
    st.write("Content for Page 5")
    
elif page == "Page 6":
    st.title("Page 6")
    st.write("Content for Page 6")
