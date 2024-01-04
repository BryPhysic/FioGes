import sys
import os
import shutil
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
sys.path.append('study')
from .Functions.pdInf import create_pdf
from .Functions.inference import predict

# En el archivo gastric.py
import streamlit as st
import study.Functions.pdInf as pdf

def app(patient_data):
    if patient_data is not None:
        st.title("Protocolo Gástrico")
        st.markdown("# Información del Paciente")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"Nombre: {patient_data['nombre']}")
            st.write(f"Código: {patient_data['codigo']}")
            st.write(f"Entidad: {patient_data['entidad']}")

        with col2:
            st.write(f"Apellidos: {patient_data['apellidos']}")
            st.write(f"Edad: {patient_data['edad']}")
            st.write(f"Doctor: {patient_data['Doctor']}")

        st.sidebar.markdown("## Protocolo Gástrico")
        st.sidebar.markdown("## Datos del Paciente")
        st.sidebar.write(f"**Nombre:**      {patient_data['nombre']}")
        st.sidebar.write(f"**Apellidos:** {patient_data['apellidos']}")
        st.sidebar.write(f"**Género:** {patient_data['genero']}")
        st.sidebar.write(f"**Edad:** {patient_data['edad']}")
        st.sidebar.write(f"**DNI:** {patient_data['dni']}")
        st.sidebar.write(f"**Ciudad:**  {patient_data['ciudad']}")

        st.markdown("# HISTOLOGÍA")
        st.markdown("## ESTUDIO MACROSCÓPICO (H)")

        # Estudio macroscópico
        variable_macro = {
            'ÓRGANO': None,
            'MUESTRA': None,
            'CALIDAD DE MUESTRA': None,
            'OBSERVACIONES': None
        }
        col1, col2 = st.columns(2)
        
        with col1:
            variable_macro["ÓRGANO"] = st.text_input('Órgano', key='organ')
            variable_macro["MUESTRA"] = st.text_input('Muestra', key='sample')
            
        with col2:
            variable_macro["CALIDAD DE MUESTRA"] = st.text_input('Calidad de muestra', key='sample_quality')
            variable_macro["OBSERVACIONES"] = st.text_input('Observaciones', key='observations')

        # Estudio microscópico
        diccionario = {
            "LOCALIZACIÓN": ["ANTRO", "CUERPO", "ANTROCORPORAL"],
            "INFLAMACIÓN CRÓNICA": ["AUSENTE", "LEVE", "MODERADA", "SEVERA"],
            "ACTIVIDAD": ["AUSENTE", "LEVE", "MODERADA", "SEVERA"],
            "DISPLASIA": ["AUSENTE", "GRADO BAJO", "GRADO ALTO"],
            "METAPLASIA INTESTINAL": ["AUSENTE", "METAPLASIA INTESTINAL COMPLETA", "METAPLASIA INTESTINAL INCOMPLETA", "METAPLASIA INTESTINAL COMPLETA E INCOMPLETA"],
            "ATROFIA": ["AUSENTE", "ATROFIA LEVE", "ATROFIA MODERADA", "ATROFIA SEVERA"],
            "HELICOBACTER PYLORI": ["AUSENTE", "PRESENTE (+/+++)","PRESENTE (++/+++)", "PRESENTE (+++/+++)"],
        }
        st.markdown("## ESTUDIO MICROSCÓPICO (H)")
        col3, col4 = st.columns(2)
        
        with col3:
            localizacion = st.selectbox('Localización', diccionario["LOCALIZACIÓN"])
            actividad = st.selectbox('Actividad', diccionario["ACTIVIDAD"])
            metaplasia_intestinal = st.selectbox('Metaplasia intestinal', diccionario["METAPLASIA INTESTINAL"])
            
        with col4:
            inflamacion_cronica = st.selectbox('Inflamación crónica', diccionario["INFLAMACIÓN CRÓNICA"])
            displasia = st.selectbox('Displasia', diccionario["DISPLASIA"])
            atrofia = st.selectbox('Atrofia', diccionario["ATROFIA"])

        helico = st.selectbox('Helicobacter pylori', diccionario["HELICOBACTER PYLORI"])
        st.markdown("## CONCLUSIONES")
        conclusiones = st.text_area('Conclusiones', key='conclusions')
        st.sidebar.write(f"**Localización:**      {localizacion}")
        st.sidebar.write(f"**Inflamación crónica:** {inflamacion_cronica}")
        st.sidebar.write(f"**Actividad:** {actividad}")
        st.sidebar.write(f"**Displasia:** {displasia}")
        st.sidebar.write(f"**Metaplasia intestinal:** {metaplasia_intestinal}")
        st.sidebar.write(f"**Atrofia:** {atrofia}")
        st.sidebar.write(f"**Helicobacter pylori:** {helico}")

        # Variables microscópicas
        variable_micro = {
            'LOCALIZACIÓN': localizacion,
            'INFLAMACIÓN CRÓNICA': inflamacion_cronica,
            'ACTIVIDAD': actividad,
            'DISPLASIA': displasia,
            'METAPLASIA INTESTINAL': metaplasia_intestinal,
            'ATROFIA': atrofia,
            'HELICOBACTER PYLORI': helico
        }

        

        def vaciar_temp(ruta_carpeta):
            # Verifica si la carpeta existe
            if not os.path.exists(ruta_carpeta):
                print("La carpeta no existe.")
                return

            # Elimina cada archivo y subcarpeta dentro de la carpeta
            for nombre in os.listdir(ruta_carpeta):
                ruta_completa = os.path.join(ruta_carpeta, nombre)
                if os.path.isfile(ruta_completa):
                    os.remove(ruta_completa)
                elif os.path.isdir(ruta_completa):
                    shutil.rmtree(ruta_completa)
        # Subir imagen a stramlit
        st.markdown("# Imagen")
        st.markdown("## Subir imagen")
        uploaded_file = st.file_uploader("Choose a image file", type=['png', 'jpg', 'jpeg'])
        #print(uploaded_file)
        umbral = st.slider('Umbral de confianza', 0.0, 1.0, 0.5)
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            #st.image(image, caption='Uploaded Image.', use_column_width=True)
            col1, col2 = st.columns(2)
            image = Image.open(uploaded_file)
            results = predict(image, conf=umbral)
            with col1:
                st.image(image, caption='Imagen', use_column_width=True)
            with col2:
        
                st.image(results, caption='Imagen analisada', use_column_width=True)
    
            
        def generar_y_guardar_reporte():
            ruta = create_pdf(
                code=patient_data['codigo'],
              name=patient_data['nombre'],
              last_names=patient_data['apellidos'],
              selected_gender=patient_data['genero'],
                age=patient_data['edad'],
                dni=patient_data['dni'],
                muestra=patient_data['muestra'],
                entidad=patient_data['entidad'],
                doctor=patient_data['Doctor'],
                procedencia=patient_data['Procedencia'],
                fecha1=patient_data['fecha_obtencion'],
                fecha2=patient_data['fecha_salida'],
                city=patient_data['ciudad'],
                variables_macro=variable_macro,
                variables_micro=variable_micro,
                conclusion=conclusiones,
                ImageI=image,
                ImageO=results
            )
            st.write("Reporte generado y guardado con éxito.")
            return ruta
            
            #st.image(results, caption='Uploaded Image.', use_column_width=True)
    
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
                        file_name=f"reporte-{patient_data['nombre']+' '+patient_data['apellidos']}.pdf",
                        mime="application/pdf",)
                vaciar_temp('temp')
            else:
                st.write("El reporte no se ha generado correctamente.")
    else:
        st.error("No hay datos del paciente disponibles.")

