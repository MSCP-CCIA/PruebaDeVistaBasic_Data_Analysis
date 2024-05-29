from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.df = pd.DataFrame({
            'Codigo': ['001', '002', '003'],
            'Nombre': ['Producto1', 'Producto2', 'Producto3'],
            'Modelo': ['M1', 'M2', 'M3'],
            'Cantidad': [10, 20, 30]
        })
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0, row=0)
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
        self.cantidad = StringVar()
        self.buscar = StringVar()
        self.create_widgets()
        self.load_data()
    def create_widgets(self):
        Label(self.frame1, text='G E S T O R   D E   I N V E N T A R I O', bg='gray22', fg='white',
              font=('Orbitron', 15, 'bold')).grid(column=0, row=0)
        Label(self.frame2, text='PRODUCTO', fg='white', bg='navy', font=('Rockwell', 12, 'bold')).grid(columnspan=2,                                                                                      pady=5)
        Label(self.frame2, text='Codigo', fg='white', bg='navy', font=('Rockwell', 13, 'bold')).grid(column=0, row=1,
                                                                                                     pady=15)
        Label(self.frame2, text='Nombre', fg='white', bg='navy', font=('Rockwell', 13, 'bold')).grid(column=0, row=2,
                                                                                                     pady=15)
        Label(self.frame2, text='Modelo', fg='white', bg='navy', font=('Rockwell', 13, 'bold')).grid(column=0, row=3,
                                                                                                     pady=15)
        Label(self.frame2, text='Cantidad', fg='white', bg='navy', font=('Rockwell', 13, 'bold')).grid(column=0, row=4,
                                                                                                       pady=15)

        self.entry_codigo = Entry(self.frame2, textvariable=self.codigo, font=('Arial', 12))
        self.entry_codigo.grid(column=1, row=1, padx=5)

        self.entry_nombre = Entry(self.frame2, textvariable=self.nombre, font=('Arial', 12))
        self.entry_nombre.grid(column=1, row=2)
        self.entry_nombre.config(state='disabled')

        self.entry_modelo = Entry(self.frame2, textvariable=self.modelo, font=('Arial', 12))
        self.entry_modelo.grid(column=1, row=3)
        self.entry_modelo.config(state='disabled')

        self.entry_cantidad = Entry(self.frame2, textvariable=self.cantidad, font=('Arial', 12))
        self.entry_cantidad.grid(column=1, row=4)

        Label(self.frame4, text='Control', fg='white', bg='black', font=('Rockwell', 12, 'bold')).grid(columnspan=3,
                                                                                                       column=0, row=0,
                                                                                                       pady=1, padx=4)
        Button(self.frame4, text='BUSCAR', font=('Arial', 10, 'bold'), bg='magenta2',
               command=self.buscar_producto).grid(column=0, row=1, pady=10, padx=4)
        Button(self.frame4, text='MODIFICAR', font=('Arial', 10, 'bold'), bg='orange red',
               command=self.modificar_producto).grid(column=1, row=1, padx=10)
        Button(self.frame4, text='ELIMINAR', font=('Arial', 10, 'bold'), bg='yellow',
               command=self.eliminar_producto).grid(column=2, row=1, padx=4)
        Button(self.frame5, text='GENERAR ORDEN DE COMPRA', font=('Arial', 10, 'bold'), bg='red',
               command=self.generar_orden_de_compra).grid(column=2, row=1, padx=4)

        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient=HORIZONTAL, command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = Scrollbar(self.frame3, orient=VERTICAL, command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Nombre', 'Modelo', 'Cantidad')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=130, anchor='center')
        self.tabla.column('Modelo', minwidth=100, width=120, anchor='center')
        self.tabla.column('Cantidad', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='Codigo', anchor='center')
        self.tabla.heading('Nombre', text='Nombre', anchor='center')
        self.tabla.heading('Modelo', text='Modelo', anchor='center')
        self.tabla.heading('Cantidad', text='Cantidad', anchor='center')

        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt')
        estilo.configure(".", font=('Helvetica', 12, 'bold'), foreground='red2')
        estilo.configure("Treeview", font=('Helvetica', 10, 'bold'), foreground='black', background='white')
        estilo.map('Treeview', background=[('selected', 'green2')], foreground=[('selected', 'black')])

    def load_data(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)
        # Insertar filas del DataFrame en la tabla
        for index, row in self.df.iterrows():
            self.tabla.insert("", END, text=row['Codigo'],
                              values=(row['Nombre'], row['Modelo'], row['Cantidad']))

    def buscar_producto(self):
        codigo = self.codigo.get()
        producto = self.df[self.df['Codigo'] == codigo]
        if not producto.empty:
            self.nombre.set(producto.iloc[0]['Nombre'])
            self.modelo.set(producto.iloc[0]['Modelo'])
            self.cantidad.set(producto.iloc[0]['Cantidad'])
            self.entry_nombre.config(state='normal')
            self.entry_modelo.config(state='normal')
        else:
            self.nombre.set('')
            self.modelo.set('')
            self.cantidad.set('')
            self.entry_nombre.config(state='disabled')
            self.entry_modelo.config(state='disabled')

    def modificar_producto(self):
        codigo = self.codigo.get()
        if codigo in self.df['Codigo'].values:
            self.df.loc[self.df['Codigo'] == codigo, 'Nombre'] = self.nombre.get()
            self.df.loc[self.df['Codigo'] == codigo, 'Modelo'] = self.modelo.get()
            self.df.loc[self.df['Codigo'] == codigo, 'Cantidad'] = self.cantidad.get()
            self.load_data()
            self.limpiar_campos()

    def eliminar_producto(self):
        codigo = self.codigo.get()
        self.df = self.df[self.df['Codigo'] != codigo]
        self.load_data()
        self.limpiar_campos()

    def limpiar_campos(self):
        self.codigo.set('')
        self.nombre.set('')
        self.modelo.set('')
        self.cantidad.set('')
        self.entry_nombre.config(state='disabled')
        self.entry_modelo.config(state='disabled')

    def generar_orden_de_compra(self):
        c = canvas.Canvas("orden_de_compra.pdf", pagesize=letter)
        c.drawString(30, 750, "Orden de Compra")
        c.drawString(30, 735, "=================")

        data = self.df.to_dict('records')
        y = 700
        for item in data:
            c.drawString(30, y, f"Codigo: {item['Codigo']}, Nombre: {item['Nombre']}, Modelo: {item['Modelo']}, "
                                 f"Cantidad: {item['Cantidad']}")
            y -= 15
            if y < 30:
                c.showPage()
                y = 750

        c.save()


def main():
    ventana = Tk()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('900x530')
    ventana.resizable(0, 0)
    app = Registro(ventana)
    app.mainloop()


if __name__ == "__main__":
    main()

