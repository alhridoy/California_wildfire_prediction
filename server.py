import streamlit as st
from app import (
    inference, model_variables, overview, model_details,
    dataset_introduction, performance, wildfire_data_insights,
    temperature_data_insights, training_data_insights
)

# Define page categories and their corresponding pages
PAGES = {
    "Project Overview": overview,
    "Used Datasets": dataset_introduction,
    "Wildfire Data Insights": wildfire_data_insights,
    "Temperature Data Insights": temperature_data_insights,
    "Training Data Insights": training_data_insights,
    "Used Variables": model_variables,
    "Model Details": model_details,
    "Prediction": inference,
    "Evaluation": performance
}

CATEGORIES = {
    "Overview": list(PAGES.keys())[:2],
    "Data Analysis": list(PAGES.keys())[2:5],
    "Pipeline Details": list(PAGES.keys())[5:7],
    "Runtime": list(PAGES.keys())[7:]
}

def main():
    # Set up the sidebar
    try:
        st.sidebar.image("app/media/wildfire_logo.png", width=285)
    except:
        st.sidebar.title("California Wildfire Prediction")

    st.sidebar.markdown("## Navigation")
    st.sidebar.markdown("Select a category and then choose a page to view.")

    # Category selection
    cat_selection = st.sidebar.radio("Select Category:", list(CATEGORIES.keys()))
    
    # Page selection based on category
    available_pages = CATEGORIES[cat_selection]
    selection = st.sidebar.radio("Select Page:", available_pages)

    # Display selected page
    try:
        page = PAGES[selection]
        page.app()
    except Exception as e:
        st.error(f"Error loading page: {str(e)}")
        st.info("Please try selecting a different page or refresh the application.")

if __name__ == "__main__":
    main()
