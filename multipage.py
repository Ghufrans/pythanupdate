import streamlit as st

# Define a function to set up session state
def setup_session_state():
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'

# Home page content
def home():
    st.title('Home Page')
    st.write('Welcome to the home page!')

# About page content
def about():
    st.title('About Page')
    st.write('This is the about page.')

# Contact page content
def contact():
    st.title('Contact Page')
    st.write('This is the contact page.')

# Sidebar navigation
def sidebar():
    st.sidebar.title('Navigation')
    pages = ['Home', 'About', 'Contact']
    st.session_state.page = st.sidebar.radio('Go to', pages, index=pages.index(st.session_state.page))

# Main function to run the app
def main():
    setup_session_state()
    sidebar()

    if st.session_state.page == 'Home':
        home()
    elif st.session_state.page == 'About':
        about()
    elif st.session_state.page == 'Contact':
        contact()

if __name__ == '__main__':
    main()
