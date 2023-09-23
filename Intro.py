import streamlit as st

# Set a background color and text color for the page
def app():
    st.markdown(
        """
        <style>
        body {
            background-color: #F0F3F4;
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Add a title and subtitle
    st.title("Welcome to Recipe Generator!")
    st.subheader("Let's Cook Up Some Delicious Ideas")

    # Add an image related to cooking or food
    st.image("cooking.jpg", use_column_width=True)

    # Add an introduction paragraph
    st.write(
        "Are you looking for culinary inspiration? You've come to the right place! "
        "Recipe Generator is here to help you discover mouthwatering recipes tailored to your tastes and preferences."
    )

    # Explain what the app does
    st.write(
        "With Recipe Generator, you can:"
    )
    st.markdown(
        "- 🍽️ **Generate Recipes**: Simply tell us your preferred cuisine, ingredients, and dietary restrictions, and we'll generate unique recipes for you."
    )
    st.markdown(
        "- 📝 **Save Favorites**: Keep track of your favorite recipes by saving them to your profile."
    )
    st.markdown(
        "- 🧾 **Shopping List**: Generate a shopping list for any recipe with just a click, making grocery shopping a breeze."
    )

    # Invite users to get started
    st.write("Are you ready to embark on a culinary adventure?")
    st.button("Get Started")
