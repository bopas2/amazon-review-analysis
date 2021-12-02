import streamlit as st 
from pages import pyvis_network_app, welcome

class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        self.pages.append({
          
                "title": title, 
                "function": func
            })

    def run(self):
        # Dropdown to select the page to run  
        page = st.sidebar.selectbox(
            'App Navigation', 
            self.pages, 
            format_func=lambda page: page['title']
        )
        # run the app function 
        page['function']()


app = MultiPage()

st.title("Reviews Recommendation System")


app.add_page("Welcome", welcome.app)
app.add_page("Custom Queries", pyvis_network_app.app)

app.run()
