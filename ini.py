import streamlit as st
from study import gastric, page3

class SessionState:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            
            
def main():
    # Inicializa patient_data en st.session_state si aún no existe
    if 'patient_data' not in st.session_state:
        st.session_state.patient_data = None

    st.sidebar.title("Protocol")
    selection = st.sidebar.selectbox(
        'Please select a protocol below:',
        ['Patient Data', 'Gastric', 'Breast Cancer','Lung Cancer']
    )

    if selection == "Patient Data":
        st.session_state.patient_data = main_page(st.session_state.patient_data)
        #main_page()
    elif selection == "Gastric":
        if st.session_state.patient_data is not None:
            gastric.app(st.session_state.patient_data)
        else:
            st.warning("Please enter patient data first.")
    elif selection == "Breast Cancer":
        page3.app()

        
def main_page(patient_data):
    
    st.markdown("# Patient Data ")
    
    col1, col2 = st.columns(2)
    gender_options = ['Male', 'Female'] 
   
    
    with col1:
        name = st.text_input("Name", key="name")
        age = st.slider("Age", key="age")
        city = st.text_input("City", key="city")
        sample = st.text_input("N Sample", key="sample")
        entity =st.text_input("Entity", key="enti") 

    with col2:
        last_names = st.text_input("Last name", key="last_names")
        selected_gender = st.radio('Select Gender', gender_options)
        dni = st.text_input("DNI", key="dni")
        code = st.text_input("History", key="code")
        doc = st.text_input('Doctor:', key='doc')
    
    prode = st.text_input('Prodence:', key='Pro')
    #email = 
   
    
    col3, col4 = st.columns(2)
    
    with col3:
        date_get = st.date_input("Date get", key="date_get")
        

    with col4:
        date_out = st.date_input("Date out", key="date_out")
        
        
    print(date_get)

    # Display the patient data dynamically as it is entered
    
    st.write("### Patient Information Preview:")
    st.write(f"**Code:** {code}")
    st.write(f"**Name:** {name}")
    st.write(f"**Last Name:** {last_names}")
    st.write(f"**Gender:** {selected_gender}")
    st.write(f"**Age:** {age}")
    st.write(f"**DNI:** {dni}")
    st.write(f"**City:** {city}")

    # Button to save the data
    if st.button("Save Patient Data"):
        patient_data = save_patient_data(code,name, last_names, selected_gender, age, dni, city)
        # Display the saved patient data in the sidebar
        st.sidebar.markdown("## Saved Patient Data 🎉")
        st.sidebar.write(f"**Code:**      {patient_data['code']}")
        st.sidebar.write(f"**Name:**      {patient_data['name']}")
        st.sidebar.write(f"**Last Name:** {patient_data['last_names']}")
        st.sidebar.write(f"**Gender:**    {patient_data['gender']}")
        st.sidebar.write(f"**Age:**.      {patient_data['age']}")
        st.sidebar.write(f"**DNI:**       {patient_data['dni']}")
        st.sidebar.write(f"**City:**      {patient_data['city']}")
    return patient_data

def save_patient_data(code,name, last_names, gender, age, dni, city):
   
    return {
        'code': code,
        'name': name,
        'last_names': last_names,
        'gender': gender,
        'age': age,
        'dni': dni,
        'city': city,
    }

if __name__ == "__main__":
    main()
