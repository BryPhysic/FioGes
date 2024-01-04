import streamlit as st
from study import gastric, page3

class EstadoSesion:
    def __init__(self, **kwargs):
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)

def principal():
    # Inicializa patient_data en st.session_state si aún no existe
    if 'patient_data' not in st.session_state:
        st.session_state.patient_data = None

    st.sidebar.title("Protocolo")
    seleccion = st.sidebar.selectbox(
        'Por favor, seleccione un protocolo a continuación:',
        ['Datos del Paciente', 'Gástrico', 'Cáncer de Mama', 'Cáncer de Pulmón']
    )

    if seleccion == "Datos del Paciente":
        st.session_state.patient_data = pagina_principal(st.session_state.patient_data)
    elif seleccion == "Gástrico":
        if st.session_state.patient_data is not None:
            gastric.app(st.session_state.patient_data)
        else:
            st.warning("Por favor, ingrese primero los datos del paciente.")
    elif seleccion == "Cáncer de Mama":
        page3.app()

def pagina_principal(patient_data):
    st.markdown("# Datos del Paciente")
    col1, col2 = st.columns(2)
    opciones_genero = ['Masculino', 'Femenino']

    with col1:
        nombre = st.text_input("Nombre", key="name")
        edad = st.slider("Edad", key="age")
        ciudad = st.text_input("Ciudad", key="city")
        muestra = st.text_input("N Muestra", key="sample")
        entidad = st.text_input("Entidad", key="enti")

    with col2:
        apellidos = st.text_input("Apellidos", key="last_names")
        genero_seleccionado = st.radio('Seleccionar Género', opciones_genero)
        dni = st.text_input("DNI", key="dni")
        codigo = st.text_input("Historia", key="code")
        doctor = st.text_input('Doctor:', key='doc')

    procedencia = st.text_input('Procedencia:', key='Pro')
    
    col3, col4 = st.columns(2)
    
    with col3:
        fecha_obtencion = st.date_input("Fecha de Obtención", key="date_get")

    with col4:
        fecha_salida = st.date_input("Fecha de Salida", key="date_out")

    st.write("### Vista Previa de la Información del Paciente:")
    st.write(f"**Código:** {codigo}")
    st.write(f"**Nombre:** {nombre}")
    st.write(f"**Apellidos:** {apellidos}")
    st.write(f"**Género:** {genero_seleccionado}")
    st.write(f"**Edad:** {edad}")
    st.write(f"**DNI:** {dni}")
    st.write(f"**Ciudad:** {ciudad}")

    # Botón para guardar los datos
    if st.button("Guardar Datos del Paciente"):
        patient_data = {
            'muestra': muestra,
            'entidad': entidad,
            'codigo': codigo,
            'nombre': nombre,
            'apellidos': apellidos,
            'genero': genero_seleccionado,
            'edad': edad,
            'dni': dni,
            'ciudad': ciudad,
            'Doctor': doctor,
            'Procedencia': procedencia,
            'fecha_obtencion': fecha_obtencion,
            'fecha_salida': fecha_salida
        }
        st.sidebar.markdown("## Datos del Paciente Guardados 🎉")
        st.sidebar.write(f"**Código:**      {patient_data['codigo']}")
        st.sidebar.write(f"**Nombre:**      {patient_data['nombre']}")
        st.sidebar.write(f"**Apellidos:** {patient_data['apellidos']}")
        st.sidebar.write(f"**Género:**    {patient_data['genero']}")
        st.sidebar.write(f"**Edad:**.      {patient_data['edad']}")
        st.sidebar.write(f"**DNI:**       {patient_data['dni']}")
        st.sidebar.write(f"**Ciudad:**      {patient_data['ciudad']}")
        print(patient_data)
    return patient_data

if __name__ == "__main__":
    principal()
