# Registro de datos en MySQL desde una GUI en TkInter
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

from tkinter import Entry, Label, Frame, Tk, Button,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END



class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='navy')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='black')
        self.frame4.grid(column=0, row=2)
        self.frame5 = Frame(master)
        self.frame5.grid(column=0, row=3)

        self.codigo = StringVar()
        self.nombre = StringVar()
        self.modelo = StringVar()
        self.precio = StringVar()
        self.cantidad = StringVar()
        self.buscar = StringVar()

        self.create_wietgs()

    def create_wietgs(self):
        Label(self.frame1, text = 'G E S T O R   D E   I N V E N T A R I O',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        Label(self.frame2, text = 'PRODUCTO',fg='white', bg ='navy', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'Codigo',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'Nombre',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = 'Modelo',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame2, text = 'Precio', fg='white',bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = 'Cantidad',fg='white', bg ='navy', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)

        self.entry_codigo = Entry(self.frame2, textvariable=self.codigo, font=('Arial', 12))
        self.entry_codigo.grid(column=1, row=1, padx=5)

        self.entry_nombre = Entry(self.frame2, textvariable=self.nombre, font=('Arial', 12))
        self.entry_nombre.grid(column=1, row=2)
        self.entry_nombre.config(state='disabled')

        self.entry_modelo = Entry(self.frame2, textvariable=self.modelo, font=('Arial', 12))
        self.entry_modelo.grid(column=1, row=3)
        self.entry_modelo.config(state='disabled')

        self.entry_precio = Entry(self.frame2, textvariable=self.precio, font=('Arial', 12))
        self.entry_precio.grid(column=1, row=4)
        self.entry_precio.config(state='disabled')

        self.entry_cantidad = Entry(self.frame2, textvariable=self.cantidad, font=('Arial', 12))
        self.entry_cantidad.grid(column=1, row=5)


       
        Label(self.frame4, text = 'Control',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)
        Button(self.frame4, text='BUSCAR', font=('Arial',10,'bold'), bg='magenta2').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame4, text='MODIFICAR', font=('Arial',10,'bold'), bg='orange red').grid(column=1,row=1, padx=10)
        Button(self.frame4, text='ELIMINAR', font=('Arial',10,'bold'), bg='yellow').grid(column=2,row=1, padx=4)
        Button(self.frame5, text='GENERAR ORDEN DE COMPRA', font=('Arial', 10, 'bold'), bg='red').grid(column=2, row=1, padx=4)

        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        self.tabla['columns'] = ('Nombre', 'Modelo', 'Precio', 'Cantidad')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=130 , anchor='center')
        self.tabla.column('Modelo', minwidth=100, width=120, anchor='center' )
        self.tabla.column('Precio', minwidth=100, width=120 , anchor='center')
        self.tabla.column('Cantidad', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='Codigo', anchor ='center')
        self.tabla.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla.heading('Modelo', text='Modelo', anchor ='center')
        self.tabla.heading('Precio', text='Precio', anchor ='center')
        self.tabla.heading('Cantidad', text='Cantidad', anchor ='center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        


def main():
    ventana = Tk()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('900x530')
    ventana.resizable(0,0)
    app = Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()        


