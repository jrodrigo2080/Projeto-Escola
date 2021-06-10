from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3 as sqlite
from tkinter import messagebox



#----------------FUNÇÕES-BOTÕES-------------------------
class Funcs_btn():
    def conecta_bd(self):
        self.conn = sqlite.connect("./DADOS/Dados.db")
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def bt_cadastrar(self):
        global con
        self.media = (float(self.entry_n1.get()) + float(self.entry_n2.get()) + float(self.entry_n3.get()))/3

        turma = self.entry_turma.get()
        turno = self.entry_turno.get()
        disciplina = self.entry_disc.get()


        if (self.media>6):
            self.situacao='Aprovado'
        else:
            self.situacao='Reprovado'
        try:
            if (turno == "SELECIONE" or turma == "SELECIONE" or disciplina == "SELECIONE"):
                messagebox.showerror("Error", "Você esta tentando inserir dados invalidos, verifique novamente!")
            else:
                con = sqlite.connect("./DADOS/Dados.db")
                cursor = con.cursor()
                comando = '''INSERT INTO TBALUNO(matricula, nome, nota1, nota2, nota3, media, turno, turma, disciplina, situacao) VALUES (
                            :matricula, :nome, :nota1, :nota2, :nota3, :media, :turno, :turma, :disciplina, :situacao); '''
                cursor.execute(comando, {"matricula": int(self.entry_mat.get()),
                                         "nome": str(self.entry_nome.get()),
                                         "nota1": float(self.entry_n1.get()),
                                         "nota2": float(self.entry_n2.get()),
                                         "nota3": float(self.entry_n3.get()),
                                         "media": (f'{self.media:.1f}'),
                                         "turno": str(self.entry_turno.get()),
                                         "turma": str(self.entry_turma.get()),
                                         "disciplina": str(self.entry_disc.get()),
                                         "situacao": self.situacao})


                con.commit()
                con.close()
                print("Aluno salvo com sucesso!")
                messagebox.showinfo("Salvo com sucesso!", "Salvo com sucesso!")
                self.bt_limpar()
        except sqlite.DatabaseError as e:
            print('Erro ao adicionar aluno ->', e)
            con.close()
            messagebox.showinfo("Error ao salvar!", "erro ao salvar verifique se a matricula já esta cadastrada!")
        finally:
            con.close()
    #----------------------------------------------
    def bt_limpar(self):
        self.entry_mat.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_disc.set("SELECIONE")
        self.entry_n1.delete(0, END)
        self.entry_n2.delete(0, END)
        self.entry_n3.delete(0, END)
        self.entry_turno.set("SELECIONE")
        self.entry_turma.set("SELECIONE")
    #---------------------------------------------------
    def bt_cadastro(self):
        self.jnl_inicio.destroy()
        Cadastro()
    #----------------------------------------
    def bt_voltar_lista(self):
        self.jnl_lista.destroy()
        Inicio()
    def bt_voltar_cadastro(self):
        self.jnl_cadastro.destroy()
        Inicio()
    #-----------------------------
    def bt_lista(self):
        self.jnl_inicio.destroy()
        Lista()
#----------------FRONT-INICIO-------------------------
class Inicio(Funcs_btn):
    def __init__(self):
        self.jnl_inicio = Tk()
        self.tela()
        self.imagem()
        self.botoes()
        self.label()
        self.jnl_inicio.mainloop()
    def tela(self):
        self.jnl_inicio.title("Inicio")
        self.jnl_inicio.configure(bg='#296182')
        self.jnl_inicio.geometry("700x700+450+50")
        self.jnl_inicio.resizable(False, False)
    def imagem(self):
        self.img_inicio = ImageTk.PhotoImage(Image.open('./Imagens/inicio.png'))
        self.lb_img = Label(self.jnl_inicio, image=self.img_inicio)
        self.lb_img.place(x=-120,y=0)
    def label(self):
        self.lb_inicio = Label(text="Bem-vindos, escolham\numa das opções abaixo:", font=('verdana', 28), fg='White', bg='#296182')
        self.lb_inicio.place(relx=0.18, rely=0.62)
    def botoes(self):
        self.btn_cadastro = Button(self.jnl_inicio, text="Cadastro", bg='#f85955', fg='White', font=('verdana', 18, 'bold'), bd=3
                                   , activebackground='#f85955', activeforeground='white', command=self.bt_cadastro)
        self.btn_cadastro.place(relx= 0.11, rely=0.8, relwidth=0.3, relheight=0.1)
        self.btn_lista = Button(self.jnl_inicio, text="Lista", bg='#f85955', fg='White', font=('verdana', 18, 'bold'), bd=3
                                 , activebackground='#f85955', activeforeground='white', command=self.bt_lista)
        self.btn_lista.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)
#----------------FRONT-CADASTRO-------------------------
class Cadastro(Funcs_btn):
    def __init__(self):
        self.jnl_cadastro = Tk()
        self.tela()
        self.botoes()
        self.labels_entrys()
        self.jnl_cadastro.mainloop()

    def tela(self):
        self.jnl_cadastro.title("Cadastro")
        self.jnl_cadastro.configure(bg='#296182')
        self.jnl_cadastro.geometry("700x700+450+50")
        self.jnl_cadastro.resizable(False, False)

    def botoes(self):
        self.btn_cadastrar = Button(self.jnl_cadastro, text="Cadastrar", bg='#f85955', fg='White', font=('verdana', 18, 'bold'),
                                    bd=3, activebackground='#f85955', activeforeground='white', command=self.bt_cadastrar)

        self.btn_cadastrar.place(relx=0.11, rely=0.8, relwidth=0.3, relheight=0.1)

        self.btn_voltar = Button(self.jnl_cadastro, text="Voltar", bg='#f85955', fg='White', font=('verdana', 18, 'bold'),
                                 bd=3, activebackground='#f85955', activeforeground='white', command=self.bt_voltar_cadastro)
        self.btn_voltar.place(relx=0.6, rely=0.8, relwidth=0.3, relheight=0.1)
        self.btn_limpar = Button(self.jnl_cadastro, text="Limpar", bg='#f85955', fg='White', font=('verdana', 18, 'bold'),
                                 bd=3, activebackground='#f85955', activeforeground='white', command=self.bt_limpar)
        self.btn_limpar.place(relx=0.6, rely=0.6, relwidth=0.3, relheight=0.1)

    def labels_entrys(self):
        # Matricula
        self.lb_mat = Label(self.jnl_cadastro, text='Matrícula:', font=('verdana', 22, 'bold'), bg='#296182', fg='White')
        self.lb_mat.place(x=60, y=30)
        self.entry_mat = Entry(self.jnl_cadastro, font=('verdana', 18))
        self.entry_mat.place(x=65, y=70, width=170, height=50)
        # Nome
        self.lb_nome = Label(self.jnl_cadastro, text='Nome:', font=('verdana', 22, 'bold'), bg='#296182', fg='White')
        self.lb_nome.place(x=250, y=30)
        self.entry_nome = Entry(self.jnl_cadastro, font=('verdana', 18))
        self.entry_nome.place(x=255, y=70, width=400, height=50)
        # Disciplina
        self.lb_disc = Label(self.jnl_cadastro, text='Disciplina:', font=('verdana', 22, 'bold'), bg='#296182', fg='White')
        self.lb_disc.place(x=250, y=150)
        self.entry_disc = ttk.Combobox(self.jnl_cadastro, font=('verdana', 18), state='readonly',
                            values=["Sistemas Operacionais",
                                    "Python",
                                    "Engenharia de Software",
                                    "Estrutua de dados"])
        self.entry_disc.place(x=255, y=190, width=400, height=50)
        self.entry_disc.set('SELECIONE')
        # Turno
        self.lb_turno = Label(self.jnl_cadastro, text='Turno:', font=('verdana', 22, 'bold'), bg='#296182', fg='White')
        self.lb_turno.place(x=250, y=270)
        self.entry_turno = ttk.Combobox(self.jnl_cadastro, font=('verdana', 18), state='readonly',
                            values=["Manhã",
                                    "Tarde",
                                    "Noite"])
        self.entry_turno.place(x=255, y=310, width=168, height=50)
        self.entry_turno.set('SELECIONE')
        # Turma
        self.lb_turma = Label(self.jnl_cadastro, text='Turma:', font=('verdana', 22, 'bold'), bg='#296182', fg='White')
        self.lb_turma.place(x=500, y=270)
        self.entry_turma = ttk.Combobox(self.jnl_cadastro, font=('verdana', 18), state='readonly',
                            values=["A",
                                    "B",
                                    "C",
                                    "D"])
        self.entry_turma.place(x=505, y=310, width=168, height=50)
        self.entry_turma.set('SELECIONE')
        # Nota 1
        self.lb_n1 = Label(self.jnl_cadastro, text='1° Nota:', font=('verdana', 22, 'bold'), bg='#296182', fg='White')
        self.lb_n1.place(x=60, y=150)
        self.entry_n1 = Entry(self.jnl_cadastro, font=('verdana', 18))
        self.entry_n1.place(x=65, y=190, width=140, height=50)
        # Nota 2
        self.lb_n2 = Label(self.jnl_cadastro, text='2° Nota:', font=('verdana', 22, 'bold'), bg='#296182', fg='White')
        self.lb_n2.place(x=60, y=270)
        self.entry_n2 = Entry(self.jnl_cadastro, font=('verdana', 18))
        self.entry_n2.place(x=65, y=310, width=140, height=50)
        # Nota 3
        self.lb_n3 = Label(self.jnl_cadastro, text='3° Nota:', font=('verdana', 22, 'bold'), bg='#296182', fg='White')
        self.lb_n3.place(x=60, y=390)
        self.entry_n3 = Entry(self.jnl_cadastro, font=('verdana', 18))
        self.entry_n3.place(x=65, y=430, width=140, height=50)
#----------------FRONT-LISTA-------------------------
class Lista(Funcs_btn):
    def __init__(self):
        self.jnl_lista = Tk()
        self.tela()
        self.botoes()
        self.lista_dados()
        self.select_lista()
        self.jnl_lista.mainloop()

    def tela(self):
        self.jnl_lista.title("Listagem")
        self.jnl_lista.configure(bg='#296182')
        self.jnl_lista.geometry("900x500+300+150")
        self.jnl_lista.resizable(False, False)
    def botoes(self):
        self.btn_voltar = Button(self.jnl_lista, text="Voltar", bg='#f85955', fg='White',
                                    font=('verdana', 18, 'bold'), bd=3
                                    , activebackground='#f85955', activeforeground='white', command=self.bt_voltar_lista)
        self.btn_voltar.place(x=25, y=25)
    def lista_dados(self):
        self.list_dados = ttk.Treeview(self.jnl_lista, height=3, column=('col1', 'col2', 'col3', 'col4', 'col5'), )
        self.list_dados.heading('#0', text='')
        self.list_dados.heading('#1', text='Matrícula')
        self.list_dados.heading('#2', text='Nome')
        self.list_dados.heading('#3', text='Disciplina')
        self.list_dados.heading('#4', text='Média')
        self.list_dados.heading('#5', text='Situação')

        self.list_dados.column('#0', width=-50)
        self.list_dados.column('#1', width=35)
        self.list_dados.column('#2', width=125)
        self.list_dados.column('#3', width=125)
        self.list_dados.column('#4', width=25)
        self.list_dados.column('#5', width=80)


        self.scrool_lista = Scrollbar(self.jnl_lista,orient='vertical')
        self.list_dados.configure(yscroll=self.scrool_lista.set)


        self.list_dados.place(x=25,y=85, height=400, width=850)
        self.scrool_lista.place(x=855,y=85, width=20, height=400)
    def select_lista(self):
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT matricula, nome, disciplina, media, situacao FROM TBALUNO 
                                        ORDER BY matricula ASC;""")
        for i in lista:
            self.list_dados.insert('', END, values=i)
        self.desconecta_bd()

Inicio()

