import streamlit as st

st.title("Unit Converter App")
st.markdown("### Conversion of Length, weight & Time")
st.write("Select Category, Enter Value & get converted value")

category = st.selectbox("Select a category as:", ["Length", "Weight", "Time"])

def converts(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to miles":
            return value * 0.621371
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        
    # If no valid conversion is selected, return None
    return None

if category == "Length":
    unit = st.selectbox("Select Value", ["Kilometer to miles", "Miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Value", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Value", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours", "Hours to minutes", "Hours to days", "Days to Hours"])

value = st.number_input("Enter the value which you want to convert")

if st.button("Convert"):
    result = converts(category, value, unit)
    
    # Check if result is None before formatting
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion or no conversion selected.")
