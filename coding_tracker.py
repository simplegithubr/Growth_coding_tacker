import streamlit as st
import json
import os
import datetime  
import matplotlib.pyplot as plt

#File to short data
Data_File = "coding_data.json"

#Load existing data
def load_data():
    if os.path.exists(Data_File):
        with open(Data_File, "r") as file:
            return json.load(file)
    return{}
    #save data

def save_data(data):
        with open(Data_File, "w") as file:
            json.dump(data , file, indent=4)
            
#initialize data
data =load_data()

#streamlit ui
st.title("🚀 Daily Coding Growth Tracker")
st.write("Track your daily coding hours and see your progress!")
#input section
date = st.date_input("📅 Select Date", datetime.date.today())
hours = st.number_input("⏳ Hours Coded", min_value=0.0, max_value=24.0 , step=0.5 )

if st.button("Save Entry"):
    date_str = str(date)
    data[date_str] = hours
    save_data(data)
    st.success(f"✅ Saved {hours} hours for {date_str}")

#Display progress
if data:
    dates = list(data.keys())
    hours_coded = list(data.values())

#plot
    fig , ax = plt.subplots()
    ax.plot(dates, hours_coded, marker='o', linestyle='-', color="blue" )
    ax.set_xlabel("Date")
    ax.set_ylabel("Hours Coded")
    ax.set_title("📈 Coding Progress Over Time")
    plt.xticks(rotation=45)
    st.pyplot(fig)

