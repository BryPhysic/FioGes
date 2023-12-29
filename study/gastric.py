import sys
import os
sys.path.append('study')
from .Functions.pdInf import create_pdf

# En el archivo gastric.py
import streamlit as st
import  study.Functions.pdInf as pdf
def app(patient_data):
    if patient_data is not None:
        st.title("Gastric Protocol")
        st.markdown("## Patient Information")
        st.write(f"Code: {patient_data['code']}")
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
            "ATROPHY": ["ABSENT", "MILD ATROPHY", "MODERATE ATROPHY", "SEVERE ATROPHY"],
            "HELICOBACTER PYLORI": ["ABSENT", "PRESENT (+/+++)","PRESENT (++/+++)", "PRESENT (+++/+++)"],
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

        helico=st.selectbox('Helicobacter pylori', dictionary["HELICOBACTER PYLORI"])
        
        
        st.sidebar.write(f"**Location:**      {location}")
        st.sidebar.write(f"**Chronic inflammation:** {chronic_inflammation}")
        st.sidebar.write(f"**Activity:** {activity}")
        st.sidebar.write(f"**Dysplasia:** {dysplasia}")
        st.sidebar.write(f"**Intestinal metaplasia:** {intestinal_metaplasia}")
        st.sidebar.write(f"**Atrophy:** {atrophy}")
        st.sidebar.write(f"**Helicobacter pylori:** {helico}")
        varible={'LOCATION':location,
                 'CHRONIC INFLAMMATION':chronic_inflammation,
                 'ACTIVITY':activity,'DYSPLASIA':dysplasia,
                 'INTESTINAL METAPLASIA':intestinal_metaplasia,
                 'ATROPHY':atrophy,
                 'HELICOBACTER PYLORI':helico}
        

       
        
      
        def generar_y_guardar_reporte():
            ruta=create_pdf(patient_data['code'],
                            patient_data['name'], 
                            patient_data['last_names'],
                            patient_data['gender'],
                            patient_data['age'], 
                            patient_data['dni'], 
                            patient_data['city'],variables_dict=varible)
            
            st.write("Reporte generado y guardado con éxito.")
            return ruta
        import os
        import shutil

        def vaciar_temp(ruta_carpeta):
            # Verifica si la carpeta existe
            if not os.path.exists(ruta_carpeta):
                print("La carpeta no existe.")
                return

            # Elimina cada archivo y subcarpeta dentro de la carpeta
            for nombre in os.listdir(ruta_carpeta):
                ruta_completa = os.path.join(ruta_carpeta, nombre)
                # Verifica si es un archivo o una carpeta
                if os.path.isfile(ruta_completa):
                    os.remove(ruta_completa)
                elif os.path.isdir(ruta_completa):
                    shutil.rmtree(ruta_completa)
                    
        # Botón para generar y guardar el reporte
        st.title("Generador de Reportes")
        if st.button("Guardar y Generar Reporte"):
            vaciar_temp('temp')
            ruta = generar_y_guardar_reporte()
            st.success(f"Reporte correctamente generado: {ruta}")
            if os.path.exists(ruta):
                with open(ruta, "rb") as f:
                    st.download_button(
                        label="Descargar Reporte",
                        data=f,
                        file_name=f"reporte-{patient_data['name']+' '+patient_data['last_names']}.pdf",
                        mime="application/pdf",)
                vaciar_temp('temp')
            else:
                st.write("El reporte no se ha generado correctamente.")                  
    else:
        st.error("No patient data available.")
            
     
      
