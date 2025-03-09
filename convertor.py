import streamlit as st

# Modern CSS Styling
st.markdown(
    """
    <style>
        /* Global Styles */
        body {
            background: #0d1117;
            color: #e6edf3;
            font-family: 'Poppins', sans-serif;
        }

        /* App Container */
        .stApp {
            background: #161b22;
            padding: 30px;
            border-radius: 15px;
            box-shadow: inset 5px 5px 10px #0a0c10, inset -5px -5px 10px #1a1f27;
        }

        /* Title */
        h1 {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #58a6ff;
            text-shadow: 2px 2px 10px rgba(88, 166, 255, 0.5);
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #161b22;
            padding: 20px;
            border-radius: 15px;
            transition: all 0.7s ease-in-out !important;
            box-shadow: inset 5px 5px 10px #0a0c10, inset -5px -5px 10px #1a1f27;
        }

        /* Sidebar Selectbox */
        .stSelectbox {
            border-radius: 10px !important;
        }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #1f6feb, #58a6ff);
            color: white;
            font-size: 18px;
            padding: 12px 24px;
            border: none;
            border-radius: 12px;
            transition: all 0.3s ease-in-out;
            box-shadow: 5px 5px 15px rgba(31, 111, 235, 0.3);
            cursor: pointer;
        }

        .stButton > button:hover {
            transform: translateY(-3px);
            background: linear-gradient(135deg, #58a6ff, #1f6feb);
            color: black;
            box-shadow: 5px 5px 20px rgba(88, 166, 255, 0.5);
        }

        /* Result Box */
        .result-box {
            font-size: 22px;
            font-weight: 600;
            text-align: center;
            background: #21262d;
            padding: 25px;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: inset 5px 5px 10px #0a0c10, inset -5px -5px 10px #1a1f27;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            font-weight: bold;
            color: #8b949e;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)
st.write("Effortlessly switch between units for length, weight, speed, time, and temperature.")

# Sidebar for Conversion Type
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature", "Speed", "Time"])
value = st.number_input("Enter Value", value=1.0, min_value=0.1, step=0.1)

col1, col2 = st.columns(2)

# Unit Options (with symbols)
length_units = ["Meters (m)", "Kilometers (km)", "Centimeters (cm)", "Millimeters (mm)", "Miles (mi)", "Yards (yd)", "Inches (in)", "Feet (ft)"]
weight_units = ["Kilograms (kg)", "Grams (g)", "Milligrams (mg)", "Pounds (lb)", "Ounces (oz)"]
temp_units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
speed_units = ["Meters per Second (m/s)", "Kilometers per Hour (km/h)", "Miles per Hour (mph)", "Feet per Second (ft/s)"]
time_units = ["Seconds (s)", "Minutes (min)", "Hours (h)", "Days (d)"]

# Dynamic Dropdowns
if conversion_type == "Length":
    with col1: from_unit = st.selectbox("From", length_units)
    with col2: to_unit = st.selectbox("To", length_units.__reversed__())
elif conversion_type == "Weight":
    with col1: from_unit = st.selectbox("From", weight_units)
    with col2: to_unit = st.selectbox("To", weight_units.__reversed__())
elif conversion_type == "Temperature":
    with col1: from_unit = st.selectbox("From", temp_units)
    with col2: to_unit = st.selectbox("To", temp_units.__reversed__())
elif conversion_type == "Speed":
    with col1: from_unit = st.selectbox("From", speed_units)
    with col2: to_unit = st.selectbox("To", speed_units.__reversed__())
elif conversion_type == "Time":
    with col1: from_unit = st.selectbox("From", time_units)
    with col2: to_unit = st.selectbox("To", time_units.__reversed__())

# Function to extract unit symbol
def extract_symbol(unit_string):
    return unit_string.split(" ")[-1][1:-1]  # Extracts the part inside parentheses

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    conversion = {"m": 1, "km": 0.001, "cm": 100, "mm": 1000, "mi": 0.000621371, "yd": 1.09361, "ft": 3.28084, "in": 39.3701}
    return (value / conversion[from_unit]) * conversion[to_unit]

def weight_converter(value, from_unit, to_unit):
    conversion = {"kg": 1, "g": 1000, "mg": 1000000, "lb": 2.20462, "oz": 35.274}
    return (value / conversion[from_unit]) * conversion[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == to_unit: return value
    if from_unit == "°C":
        return (value * 9/5 + 32) if to_unit == "°F" else value + 273.15
    if from_unit == "°F":
        return (value - 32) * 5/9 if to_unit == "°C" else (value - 32) * 5/9 + 273.15
    if from_unit == "K":
        return value - 273.15 if to_unit == "°C" else (value - 273.15) * 9/5 + 32
    return None

def speed_converter(value, from_unit, to_unit):
    conversion = {"m/s": 1, "km/h": 3.6, "mph": 2.23694, "ft/s": 3.28084}
    return (value / conversion[from_unit]) * conversion[to_unit]

def time_converter(value, from_unit, to_unit):
    conversion = {"s": 1, "min": 1/60, "h": 1/3600, "d": 1/86400}
    return (value / conversion[from_unit]) * conversion[to_unit]

# Convert Button
if st.button("Convert 🔄"):
    from_symbol = extract_symbol(from_unit)
    to_symbol = extract_symbol(to_unit)

    if conversion_type == "Length":
        result = length_converter(value, from_symbol, to_symbol)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_symbol, to_symbol)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_symbol, to_symbol)
    elif conversion_type == "Speed":
        result = speed_converter(value, from_symbol, to_symbol)
    elif conversion_type == "Time":
        result = time_converter(value, from_symbol, to_symbol)

    if result is not None:
        st.markdown(f'<div class="result-box">{value} {from_symbol} = {result:.4f} {to_symbol}</div>', unsafe_allow_html=True)
    else:
        st.error("Unsupported conversion.")

st.markdown('<div class="footer">Created with ❤️ by Sameed</div>', unsafe_allow_html=True)
