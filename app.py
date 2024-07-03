import streamlit as st



# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Simple Calculator", layout="wide")

# ---- HEADER SECTION ----
st.subheader("Hi, I am Aditya Raj  :wave:")
st.title("Welcome to my simple calculator")

st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")

    operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

# Display the result
    st.write("Result:", result)
