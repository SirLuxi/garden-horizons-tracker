import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Garden Horizons Tracker", page_icon="🌱")

st.title("🌱 Garden Horizons Live Stock")
st.write("Real-time updates for seeds and gear.")

# Create a connection to your Google Sheet
conn = st.connection("gsheets", type=GSheetsConnection)

# Read the data (we'll set the URL in the next step)
df = conn.read(ttl="1m") # Updates every 1 minute

# Display Seeds
st.header("🛒 Current Seeds")
seeds = df[df['Category'] == 'Seed']
st.table(seeds)

# Display Gear
st.header("🛠️ Current Gear")
gear = df[df['Category'] == 'Gear']
st.table(gear)

st.info("Next global refresh in: Check Discord for exact timers.")
