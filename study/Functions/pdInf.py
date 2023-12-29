from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("imgs/Inf Pat.png", 0, 0, 210, 297)

    def patient_data(self,code, name, last_names, selected_gender, age, dni, city):
        x,y = 20,70
        self.set_xy(x, y)
        self.set_font("Arial", size=12)
        # Añadir celdas para los datos del paciente
        self.cell(90, 8, txt=f"Code: {code}", border=1,ln=1)
        self.set_x(x)
        self.cell(90, 8, txt=f"Name: {name}", border=1)
        self.cell(90, 8, txt=f"Last Name: {last_names}", border=1, ln=1)
        self.set_x(x)
        self.cell(90, 8, txt=f"Gender: {selected_gender}", border=1) 
        self.cell(90, 8, txt=f"Age: {age}", border=1, ln=1)
        self.set_x(x)
        self.cell(90, 8, txt=f"DNI: {dni}", border=1)
        self.cell(90, 8, txt=f"City: {city}", border=1, ln=1)

    def variables(self, data_dict):
        x,y = 20,155
        self.set_xy(x,y)
        self.set_font("Arial", size=12)
        for key, value in data_dict.items():
            self.set_x(x)
            self.cell(60, 8, txt=f"{key}: ", border=1)
            self.cell(90, 8, txt=f"{value}", border=1, ln=1)  # Celda vacía para alineación
    
    def add_space(self, height=None):
        if height is None:
            height = 10
        self.ln(height)\
            
    def add_image(self, image_path, x, y, w=0, h=0):
        self.image(image_path, x, y, w, h)

# Datos del paciente
code="0001"
name = "Nombre"
last_names = "Apellidos"
selected_gender = "Género"
age = "Edad"
dni = "DNI"
city = "Ciudad"

# Datos adicionales en forma de diccionario
variables_dict = {
    'LOCATION': 'location',
    'CHRONIC INFLAMMATION': 'chronic_inflammation',
    'ACTIVITY': 'activity',
    'DYSPLASIA': 'dysplasia',
    'INTESTINAL METAPLASIA': 'intestinal_metaplasia',
    'ATROPHY': 'atrophy'
}

# Crear una instancia de la clase PDF
def create_pdf(code,name, last_names, selected_gender, age, dni, city,variables_dict): 
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    #pdf.add_image('/Users/bryphy/Proyectos/FioGes/imgs/LogoPD.png',10,10)
    # Añadir datos del paciente y variables adicionales
    #pdf.set_xy(15, 10)
    pdf.patient_data(code,name, last_names, selected_gender, age, dni, city)
    pdf.add_space(5)
    pdf.variables(variables_dict)

    # Guardar el PDF
    ruta = f"temp/report_{name+' '+last_names}_{code}.pdf"
    pdf.output(ruta)
    return ruta
    
#create_pdf(code,name, last_names, selected_gender, age, dni, city,variables_dict) temp/report_dfs sdfs_gg.pdf