import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("APIKEY")
model_name = os.getenv("model_name")
# Function to generate restaurant name, slogan, and menu items
def generate_cuisine_name_and_items(cuisine):
    llm = ChatGroq(
        model_name=model_name,
        api_key=api_key
    )

    # Step 1: Restaurant Name
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="Suggest a fancy restaurant name for {cuisine} cuisine. Only return the name, no any other text please, just plain name"
    )
    name_chain = name_prompt | llm
    name_response = name_chain.invoke({"cuisine": cuisine})
    restaurant_name = name_response.content.strip()

    # Step 2: Slogan
    slogan_prompt = PromptTemplate(
        input_variables=["name"],
        template="Create a catchy slogan for a restaurant named {name}. Only return the slogan, no any other text please, just plain slogan."
    )
    slogan_chain = slogan_prompt | llm
    slogan_response = slogan_chain.invoke({"name": restaurant_name})
    slogan = slogan_response.content.strip()

    # Step 3: Menu Items
    menu_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="List 10 unique and fancy dish names for {cuisine} cuisine. Only return the items separated by commas. IMPORTANT: Don't add any other text other than menu items please."
    )
    menu_chain = menu_prompt | llm
    menu_response = menu_chain.invoke({"cuisine": cuisine})
    menu_items = menu_response.content.strip()

    return {
        "restaurant_name": restaurant_name,
        "slogan": slogan,
        "menu_items": menu_items
    }


# Streamlit UI
st.title("🍽️ Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Sindhi", "Pakistani", "Arabic", "Mexican", "Italian"))

if cuisine:
    with st.spinner("Generating your restaurant concept..."):
        response = generate_cuisine_name_and_items(cuisine)

    st.header(response['restaurant_name'])
    st.subheader(response['slogan'])

    menu_items = [item.strip() for item in response['menu_items'].split(",")]

    st.write("### Menu Items")
    for item in menu_items:
        st.write(f"- {item}")
