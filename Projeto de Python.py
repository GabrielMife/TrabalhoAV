from os import path
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as msb
import sqlite3


root = Tk()
root.title("Programa de Acompanhamento de Nota")
width = 1250
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.iconbitmap("icons/Estacio.ico")
root.config(bg="#B0E2FF")
# ----- Variaveis ------

nome = StringVar()
matricula = IntVar()
disciplina = StringVar()
professor = StringVar()
av1 = DoubleVar()
av2 = DoubleVar()
av3 = DoubleVar()
avd = DoubleVar()
avds = DoubleVar()
av = DoubleVar()
avs = DoubleVar()
cd = DoubleVar()
id = None
janela = None

# ----- Forma ------

def database():
    conn = sqlite3.connect("Registro.db")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'cadastro' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT, matricula INT, disciplina TEXT, professor TEXT, av1 DOUBLE, av2 DOUBLE, av3 DOUBLE, avd DOUBLE, avds DOUBLE, av DOUBLE, avs DOUBLE, cd DOUBLE) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'cadastro' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def submitData():
    if nome.get() == "" or matricula.get() == "" or disciplina.get() == "" or professor.get() == "" or av1.get() == "" or av2.get() == "" or av3.get() == "" or avd.get() == "" or avds.get() == "" or av.get() == '' or avs.get() == '' or cd.get() == '':
        resultado = tk.showwarning("", "Por favor, digite todos os  campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("Registro.db")
        cursor = conn.cursor()
        query = """INSERT INTO 'cadastro' (nome, matricula, disciplina, professor, av1, av2, av3, avd, avds, av, avs, cd) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), int(matricula.get()), str(disciplina.get()), str(professor.get()), float(av1.get()), float(av2.get()), float(av3.get()), float(avd.get()), float(avds.get()), float(av.get()), float(avs.get()), float(cd.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'cadastro' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        matricula.set("")
        disciplina.set("")
        professor.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")
        av.set("")
        avs.set("")
        cd.set("")
        janela.destroy()

def addData():
    global janela
    nome.set("")
    matricula.set("")
    disciplina.set("")
    professor.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    av.set("")
    avs.set("")
    cd.set("")

# ----------- FRAMES - INCLUIR ----------------

    janela = Toplevel()
    janela.title("Cadastro")
    formTitle = Frame(janela)
    formTitle.pack(side=TOP)
    formContact = Frame(janela)
    formContact.pack(side=TOP, pady=10)
    width = 500
    height = 500
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    janela.geometry("%dx%d+%d+%d" % (width, height, x, y))
    janela.resizable(0, 0)
    janela.iconbitmap("icons/Estacio.ico")


# ----------- LABELS - INCLUIR ----------------

    lbl_title = Label(formTitle, text="Cadastro de Disciplina",
                      font=('Times New Roman', 18), bg='#A4D3EE', width=300)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContact, text='Nome', font=('Times New Roman', 15))
    lbl_nome.grid(row=0, sticky=W)
    lbl_matricula = Label(formContact, text='Matricula', font=('Times New Roman', 15))
    lbl_matricula.grid(row=1, sticky=W)
    lbl_disciplina = Label(formContact, text='Disciplina', font=('Times New Roman', 15))
    lbl_disciplina.grid(row=2, sticky=W)
    lbl_professor = Label(formContact, text='Professor', font=('Times New Roman', 15))
    lbl_professor.grid(row=3, sticky=W)
    lbl_av1 = Label(formContact, text='AV1', font=('Times New Roman', 15))
    lbl_av1.grid(row=4, sticky=W)
    lbl_av2 = Label(formContact, text='AV2', font=('Times New Roman', 15))
    lbl_av2.grid(row=5, sticky=W)
    lbl_av3 = Label(formContact, text='AV3', font=('Times New Roman', 15))
    lbl_av3.grid(row=6, sticky=W)
    lbl_avd = Label(formContact, text='AVD', font=('Times New Roman', 15))
    lbl_avd.grid(row=7, sticky=W)
    lbl_avds = Label(formContact, text='AVDS', font=('Times New Roman', 15))
    lbl_avds.grid(row=8, sticky=W)
    lbl_av = Label(formContact, text='AV', font=('Times New Roman', 15))
    lbl_av.grid(row=9, sticky=W)
    lbl_avs = Label(formContact, text='AVS', font=('Times New Roman', 15))
    lbl_avs.grid(row=10, sticky=W)
    lbl_cd = Label(formContact, text='Credito Digital', font=('Times New Roman', 15))
    lbl_cd.grid(row=11, sticky=W)

# ----------- ENTRY - INCLUIR ----------------#

    nomeEntry = Entry(formContact, textvariable=nome, font=('Times New Roman', 15))
    nomeEntry.grid(row=0, column=1)
    matriculaEntry = Entry(formContact, textvariable=matricula, font=('Times New Roman', 15))
    matriculaEntry.grid(row=1, column=1)
    disciplinaEntry = Entry(formContact, textvariable=disciplina, font=('Times New Roman', 15))
    disciplinaEntry.grid(row=2, column=1)
    professorEntry = Entry(formContact, textvariable=professor, font=('Times New Roman', 15))
    professorEntry.grid(row=3, column=1)
    av1Entry = Entry(formContact, textvariable=av1, font=('Times New Roman', 15))
    av1Entry.grid(row=4, column=1)
    av2Entry = Entry(formContact, textvariable=av2, font=('Times New Roman', 15))
    av2Entry.grid(row=5, column=1)
    av3Entry = Entry(formContact, textvariable=av3, font=('Times New Roman', 15))
    av3Entry.grid(row=6, column=1)
    avdEntry = Entry(formContact, textvariable=avd, font=('Times New Roman', 15))
    avdEntry.grid(row=7, column=1)
    avdsEntry = Entry(formContact, textvariable=avds, font=('Times New Roman', 15))
    avdsEntry.grid(row=8, column=1)
    avEntry = Entry(formContact, textvariable=av, font=('Times New Roman', 15))
    avEntry.grid(row=9, column=1)
    avsEntry = Entry(formContact, textvariable=avs, font=('Times New Roman', 15))
    avsEntry.grid(row=10, column=1)
    cdEntry = Entry(formContact, textvariable=cd, font=('Times New Roman', 15))
    cdEntry.grid(row=11, column=1)


# ----------- BOTÃO - INCLUIR ---------------

    btn_includecom = Button(formContact, text="Finalizar Cadastro",
                            font=('Times New Roman', 18), bg='#7EC0EE', width=30, command=submitData)
    btn_includecom.grid(row=50, columnspan=5, pady=50)

# ----------- FRAME PRINCIPAL -----------------

top = Frame(root, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg="#B0E2FF")
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT, pady=20)
midleftPadding = Frame(mid, width=350, bg="#FF0000")
bottom = Frame(root, width=200)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=500)
tableMargin.pack(side=TOP)

# ----------- LABEL PRINCIPAL -----------------

lbl_title = Label(top, text="Bem-Vindo ao nosso sistema de acompanhamento de nota! ☺", font=('Times New Roman', 18), bg='#7EC0EE', width=500)
lbl_title.pack(fill=X)



# ----------- BUTTONS PRINCIPAL ----------------

bttn_add = Button(midleft, text="Cadastrar Disciplina",
                 font=('Times New Roman', 15), bg="#8DB6CD", command=addData)
bttn_add.pack()



# ----------- TABELAS - TREEVIEW ----------------

scrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
scrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("ID", "Nome", "Matricula", "Disciplina", "Professor", "AV1", "AV2", "AV3", "AVD", "AVDS", "AV", "AVS", "CD"), 
                    height=25, selectmode="extended", yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
scrollbarX.config(command=tree.xview)
scrollbarX.pack(side=BOTTOM, fill=X)
scrollbarY.config(command=tree.yview)
scrollbarY.pack(side=RIGHT, fill=Y)

tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Matricula", text="Matricula", anchor=W)
tree.heading("Disciplina", text="Disciplina", anchor=W)
tree.heading("Professor", text="Professor", anchor=W)
tree.heading("AV1", text="AV1", anchor=W)
tree.heading("AV2", text="AV2", anchor=W)
tree.heading("AV3", text="AV3", anchor=W)
tree.heading("AVD", text="AVD", anchor=W)
tree.heading("AVDS", text="AVDS", anchor=W)
tree.heading("AV", text="AV", anchor=W)
tree.heading("AVS", text="AVS", anchor=W)
tree.heading("CD", text="CD", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=45)
tree.column('#6', stretch=NO, minwidth=0, width=45)
tree.column('#7', stretch=NO, minwidth=0, width=45)
tree.column('#8', stretch=NO, minwidth=0, width=45)
tree.column('#9', stretch=NO, minwidth=0, width=45)
tree.column('#10', stretch=NO, minwidth=0, width=45)
tree.column('#11', stretch=NO, minwidth=0, width=45)
tree.column('#12', stretch=NO, minwidth=0, width=45)
tree.column('#13', stretch=NO, minwidth=0, width=45)
tree.pack()

# ---------- INICIAR -------------
if __name__ == '__main__':
    database()
    root.mainloop()