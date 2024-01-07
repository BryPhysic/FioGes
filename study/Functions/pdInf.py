from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("imgs/Inf Pat (1).png", 0, 0, 210, 297)
  
    def add_image(self, image_path, x, y, w=0, h=0):
        self.image(image_path, x, y, w, h)
        
    def patient(self,code, name, last_names, selected_gender, age, dni,muestra,entidad,doctor,procedencia,fecha1, city,border=None):
        x,y = 20,70
        self.set_xy(x, y)
        if border is None:
            bord = 0
        self.set_font("Arial", size=15)
        self.cell(90, 8, txt=f"DATOS GENERALES", border=bord,ln=1)
        self.set_x(x)
        # Añadir celdas para los datos del paciente
        self.set_font("Arial", size=10)
        self.cell(90, 5, txt=f"Cdigo: {code}", border=bord) #code
        self.cell(90, 5, txt=f"Muestra:   {muestra}", border=bord, ln=1)
        self.set_x(x) 
        self.cell(90, 5, txt=f"Nombre: {name}", border=bord) #name
        self.cell(90, 5, txt=f"Apellidos: {last_names}", border=bord, ln=1) #apellidos
        self.set_x(x)
        self.cell(90, 5, txt=f"Genero: {selected_gender}", border=bord) # genero
        self.cell(90, 5, txt=f"Edad:       {age}", border=bord, ln=1) #edad
        self.set_x(x)
        self.cell(90, 5, txt=f"DNI: {dni}", border=bord) # dni
        self.cell(90, 5, txt=f"Ciudad:    {city}", border=bord, ln=1) # ciudad
        self.set_x(x)
        self.cell(90, 5, txt=f"Doctor: {doctor}", border=bord)
        self.cell(90, 5, txt=f"Entidad:   {entidad}", border=bord, ln=1)
        self.set_x(x)
        self.cell(90, 5, txt=f"Fecha de Entrada: {fecha1}", border=bord)
        self.cell(90, 5, txt=f"Procedencia: {procedencia}", border=bord)
        #self.cell(90, 5, txt=f"Fecha de Salida: {fecha2}", border=bord, ln=1)
        #self.set_x(x)
        #self.cell(90, 5, txt=f"Procedencia: {procedencia}", border=bord)
        
    def variables_rep(self, data_dict,border=None):
        if border is None:
            bord = 0
        x,y = 20,100
        #self.set_xy(x,y)
        self.set_x(x)
        self.set_font("Arial", size=15)
        self.cell(90, 8, txt=f"RECEPCIÓN", border=0,ln=1)
        self.set_font("Arial", size=12)
        
        for key, value in data_dict.items():
            self.set_x(x)
            self.cell(90, 5, txt=f"{key}: ", border=bord)
            self.cell(90, 5, txt=f"{value}", border=bord, ln=1)

    def variables_micro(self,data_dict,bord=None,x=None,y=None):
        if bord is None:
            bord = 0
            
        if x is None:
            x = 20
        if y is None:
            y = 150
        self.set_x(x)
        
        self.set_font("Arial", size=15)
        self.cell(90, 8, txt=f"ESTUDIO MICROSCOPICO", border=0,ln=1)
        for key, value in data_dict.items():
            self.set_x(x)
            self.set_font("Arial", size=12)
            self.cell(60, 5, txt=f"{key}: ", border=bord)
            self.cell(90, 5, txt=f"{value}", border=bord, ln=1)  # Celda vacía para alineación
    
    def add_space(self, height=None):
        if height is None:
            height = 10
        self.ln(height)\
            
    def add_image(self, image_path, x, y, w=0, h=0):
        self.image(image_path, x, y, w, h)
        
    

# Datos del paciente


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
def create_pdf(code, name, last_names, selected_gender, age, dni,muestra,entidad,doctor,procedencia,fecha1, city,recep,variables_micro,est_macro,conclusion,ImageI=None,ImageO=None): 
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    #----pagina 1
    pdf.add_page()
   
    #pdf.patient_data(code,name, last_names, selected_gender, age, dni, city)
    pdf.patient(code, name, last_names, selected_gender, age, dni,muestra,entidad,doctor,procedencia,fecha1, city)
    pdf.add_space(15)
    pdf.variables_rep(recep)
    
    pdf.add_space(15)
    pdf.set_x(20)
    pdf.set_font_size(15)
    pdf.cell(90, 8, txt="ESTUDIO MACRO", border=0,ln=1)
    
    pdf.set_x(20)
    pdf.set_font_size(12)
    pdf.multi_cell(0, 8, txt=f"{str(est_macro)}", border=0,ln=1)
    
    #----pagina 2
    pdf.add_page()
    pdf.patient(code, name, last_names, selected_gender, age, dni,muestra,entidad,doctor,procedencia,fecha1, city)
    
    pdf.add_space(15)
    pdf.variables_micro(variables_micro,x=20,bord=0)
    
    pdf.add_space(8)
    pdf.set_x(20)
    pdf.set_font_size(15)
    pdf.cell(90, 8, txt="CONCLUSIÓN", border=0,ln=1)
    pdf.set_x(20)
    pdf.set_font_size(12)
    pdf.multi_cell(0, 8, txt=f"{str(conclusion)}", border=0,ln=1)
    #pdf.multi_cell(0, 8, txt="IMAGENES", border=0,ln=1)
    #----pagina 3
    pdf.add_page()
    pdf.patient(code, name, last_names, selected_gender, age, dni,muestra,entidad,doctor,procedencia,fecha1, city)
    pdf.add_space(8)
    pdf.set_xy(20,120)
    pdf.multi_cell(0, 8, txt="ANALISIS DE IMAGENES", border=0,ln=1)
    if ImageI is not None:   
        pdf.add_image(ImageI, x=20, y=130, w=80, h=80)
    if ImageO is not None:   
        pdf.add_image(ImageO, x=110, y=130, w=80, h=80)
    # Guardar el PDF
    ruta = f"temp/report_{name+' '+last_names}_{code}.pdf"
    pdf.output(ruta)
    return ruta
   
#-------
patient_data = {
            'muestra': 'muestra',
            'entidad': 'entidad',
            'codigo': 'codigo',
            'nombre': 'nombre',
            'apellidos': 'apellidos',
            'genero': 'genero_seleccionad',
            'edad': 'edad',
            'dni': 'dni',
            'ciudad': 'ciudad',
            'Doctor': 'doctor',
            'Procedencia': 'procedencia',
            'fecha_obtencion': 'fecha_obtencion',
            'fecha_salida': 'fecha_salid'
        }
recepcion = {
    'organo': 'organo',
    'muestra': 'muestra',
    'observaciones': 'observaciones',
    'calidad': 'calidad',
}

variables_dict = {
    'Test': 'location',
    'CHRONIC INFLAMMATION': 'chronic_inflammation',
    'ACTIVITY': 'activity',
    'DYSPLASIA': 'dysplasia',
    'INTESTINAL METAPLASIA': 'intestinal_metaplasia',
    'ATROPHY': 'atrophy'
}
from PIL import Image
new_image = 'Testimages/Metaplasia_300.png'

pil = Image.open(new_image).convert('RGB')

create_pdf(code=patient_data['codigo'],
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
                #fecha2=patient_data['fecha_salida'],
                city=patient_data['ciudad'],
                recep=recepcion,
                est_macro="Esto es un estudio macroscopico ksjasdlakaldakljlsalasad",
                variables_micro=variables_dict,
                conclusion="Conclukajsdkaskjdlasdlkjhsdaksjdajlkdjaslkdjlkasion",
                ImageI=pil,
                ImageO=pil
                
           ) 



