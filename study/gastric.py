# En el archivo gastric.py
import streamlit as st

def app(patient_data):
    if patient_data is not None:
        st.title("Gastric Protocol")
        st.markdown("## Patient Information")
        
        col1, col2 = st.columns(2)

        with col1:
            st.write(f"Name: {patient_data['name']}")
            st.write(f"Gender: {patient_data['gender']}")
            st.write(f"DNI: {patient_data['dni']}")

        with col2:
            st.write(f"Last Name: {patient_data['last_names']}")
            st.write(f"Age: {patient_data['age']}")
            st.write(f"City: {patient_data['city']}")

        # Aquí puedes añadir más código para el protocolo gastric
        st.sidebar.markdown("## Gastric Protocol")
        st.sidebar.markdown("## Patient Data")
        st.sidebar.write(f"**Name:**      {patient_data['name']}")
        st.sidebar.write(f"**Last Name:** {patient_data['last_names']}")
        st.sidebar.write(f"**Gender:** {patient_data['gender']}")
        st.sidebar.write(f"**Age:** {patient_data['age']}")
        st.sidebar.write(f"**DNI:** {patient_data['dni']}")
        st.sidebar.write(f"**City:**  {patient_data['city']}")
                  
        
        dictionary = {
            "LOCATION": ["ANTRO", "BODY", "ANTROCORPORAL"],
            "CHRONIC INFLAMMATION": ["ABSENT", "MILD", "MODERATE", "SEVERE"],
            "ACTIVITY": ["ABSENT", "MILD", "MODERATE", "SEVERE"],
            "DYSPLASIA": ["ABSENT", "LOW GRADE", "HIGH GRADE"],
            "INTESTINAL METAPLASIA": ["ABSENT", "COMPLETE INTESTINAL METAPLASIA", "INCOMPLETE INTESTINAL METAPLASIA", "COMPLETE AND INCOMPLETE INTESTINAL METAPLASIA"],
            "ATROPHY": ["ABSENT", "MILD ATROPHY", "MODERATE ATROPHY", "SEVERE ATROPHY"]
            }
        col1, col2 = st.columns(2)

        with col1:
            location = st.selectbox('Location', dictionary["LOCATION"])
            activity = st.selectbox('Activity', dictionary["ACTIVITY"])
            intestinal_metaplasia = st.selectbox('Intestinal metaplasia', dictionary["INTESTINAL METAPLASIA"])

        with col2:
            chronic_inflammation = st.selectbox('Chronic inflammation', dictionary["CHRONIC INFLAMMATION"])
            dysplasia = st.selectbox('Dysplasia', dictionary["DYSPLASIA"])
            atrophy = st.selectbox('atrophy', dictionary["ATROPHY"])

        
        
        st.sidebar.write(f"**Location:**      {location}")
        st.sidebar.write(f"**Chronic inflammation:** {chronic_inflammation}")
        st.sidebar.write(f"**Activity:** {activity}")
        st.sidebar.write(f"**Dysplasia:** {dysplasia}")
        st.sidebar.write(f"**Intestinal metaplasia:** {intestinal_metaplasia}")
        st.sidebar.write(f"**Atrophy:** {atrophy}")
        
        

        
        
        
        
    else:
        st.error("No patient data available.")
