import customtkinter as ctk
import os
from PIL import Image
import sqlite3
import subprocess 
import sys

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("ReciclaFacil")
        self.geometry("700x450")
        self.resizable(False, False)  # Desabilita o redimensionamento da janela
        self.iconbitmap(r"c:\Users\Israel\Downloads\RECICLAFACIL COM BD\ReciclaFacilPY\images\logo.ico")
        
        # Config de Grid 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=2)
        
        # Pegando as imagens
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "logoee.png")), size=(26, 26))
        
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                       dark_image=Image.open(os.path.join(image_path, "home_lightsss.png")), size=(20, 20))
        
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                       dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        
        self.cliente_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "ranking_dark.png")),
                                          dark_image=Image.open(os.path.join(image_path, "ranking_light.png")), size=(20, 20))

        self.conta_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "account_dark.png")).resize((32, 32)),
                                         dark_image=Image.open(os.path.join(image_path, "account_light.png")).resize((32, 32)), size=(20, 20))
        
        self.reciclagem_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "recycle_dark.png")),
                                              dark_image=Image.open(os.path.join(image_path, "recycle_light.png")), size=(20, 20))
        
        # Frame botoes de navegação
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1) 

        self.nav_frame_label = ctk.CTkLabel(self.navigation_frame, text="Gestão de Perfil", image=self.logo_image,
                                            compound="left", font=ctk.CTkFont(size=15, weight='bold'))
        self.nav_frame_label.grid(row=0, column=0, pady=20, padx=20)
        
        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="Inicio", fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"), image=self.home_image, anchor="w",
                                         command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        
        self.chat_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="Premiação", fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"), image=self.chat_image, anchor="w",
                                         command=self.chat_button_event)
        self.chat_button.grid(row=2, column=0, sticky="ew")
        
        self.rank_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="Ver Rankings", fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"), image=self.cliente_image, anchor="w",
                                         command=self.rank_button_event)
        self.rank_button.grid(row=3, column=0, sticky="ew")
       
        self.conta_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                           text="Conta", fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"), image=self.conta_image, anchor="w",
                                           command=self.conta_button_event)
        self.conta_button.grid(row=4, column=0, sticky="ew")

        self.reciclagem_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                text="Reciclagem", fg_color="transparent", text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"), image=self.reciclagem_image, anchor="w",
                                                command=self.reciclagem_button_event)
        self.reciclagem_button.grid(row=5, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["light", "dark", "system"],
                                                     command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, pady=20, padx=20, sticky="s")
        
        # Frames
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.chat_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.rank_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.conta_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")  
        self.reciclagem_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")  
        
        # Widgets nos Frames
        self.title_home = ctk.CTkLabel(self.home_frame, text="Bem-vindo ao ReciclaFacil", font=("confortaa bold", 36), text_color="green")
        self.title_home.grid(row=0, column=0, padx=20, pady=10)
        
        # Descrição do projeto no frame "home"
        self.description_home = ctk.CTkLabel(
            self.home_frame,
            text=( 
                "O ReciclaFacil é uma iniciativa dedicada à sustentabilidade e ao impacto social. "
                "Nosso objetivo é facilitar a coleta de resíduos recicláveis em áreas periféricas e favelas, "
                "gerando créditos verdes e promovendo a inclusão social através da reciclagem. "
                "Com o uso de lixeiras especializadas e tecnologia inovadora, queremos criar uma solução acessível "
                "e eficiente para uma coleta mais organizada e econômica. Junte-se a nós para transformar "
                "o futuro com atitudes conscientes!"
            ),
            font=("confortaa bold", 20),
            wraplength=460,  # Define a largura do texto
            justify="center"
        )
        self.description_home.grid(row=1, column=0, padx=20, pady=20)
        
        self.chat_home = ctk.CTkLabel(self.chat_frame, text="Premiações", font=("Arial bold", 36))
        self.chat_home.grid(row=0, column=0, padx=20, pady=10)
        
        self.rank_home = ctk.CTkLabel(self.rank_frame, text="Top 10 Rankings", font=("Arial bold", 36))
        self.rank_home.grid(row=0, column=0, padx=20, pady=10)




   



        # Campos para adicionar nome, quantidade de lixo reciclado e rank
        self.rank_name_label = ctk.CTkLabel(self.rank_frame, text="Nome:", font=("Arial", 16))
        self.rank_name_label.grid(row=1, column=0, padx=20, pady=15, sticky="w")
        
        self.rank_name_entry = ctk.CTkEntry(self.rank_frame, font=("Arial", 16))
        self.rank_name_entry.grid(row=1, column=1, padx=20, pady=5)
        
        self.lixo_reciclado_label = ctk.CTkLabel(self.rank_frame, text="Quantidade de Lixo Reciclado (kg):", font=("Arial", 16))
        self.lixo_reciclado_label.grid(row=2, column=0, padx=20, pady=15, sticky="w")
        
        self.lixo_reciclado_entry = ctk.CTkEntry(self.rank_frame, font=("Arial", 16))
        self.lixo_reciclado_entry.grid(row=2, column=1, padx=20, pady=5)
        
        self.rank_button_add = ctk.CTkButton(self.rank_frame, text="Adicionar ao Ranking", font=("Arial", 16), command=self.add_to_ranking)
        self.rank_button_add.grid(row=3, column=0, columnspan=2, pady=25)
        
        # Mostrar os Rankings
        self.rank_list_frame = ctk.CTkFrame(self.rank_frame)
        self.rank_list_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
        
        self.load_ranking()
        
        
         # Texto para atualização de conta
        self.login_label = ctk.CTkLabel(self.conta_frame, text="Atualizar credenciais", font=("Arial", 24))
        self.login_label.grid(row=1, column=0, padx=20, pady=10, columnspan=2)

        # Campos de atualização de conta
        self.email_label = ctk.CTkLabel(self.conta_frame, text="Email:", font=("Arial", 16))
        self.email_label.grid(row=2, column=0, padx=20, pady=15, sticky="w")
        
        self.email_entry = ctk.CTkEntry(self.conta_frame, font=("Arial", 16))
        self.email_entry.grid(row=2, column=1, padx=10, pady=15)
        
        self.senha_label = ctk.CTkLabel(self.conta_frame, text="Senha:", font=("Arial", 16))
        self.senha_label.grid(row=3, column=0, padx=20, pady=15, sticky="w")
        
        self.senha_entry = ctk.CTkEntry(self.conta_frame, font=("Arial", 16), show="*")
        self.senha_entry.grid(row=3, column=1, padx=10, pady=15)
        
        self.pix_label = ctk.CTkLabel(self.conta_frame, text="Pix:", font=("Arial", 16))
        self.pix_label.grid(row=4, column=0, padx=20, pady=15, sticky="w")
        
        self.pix_entry = ctk.CTkEntry(self.conta_frame, font=("Arial", 16))
        self.pix_entry.grid(row=4, column=1, padx=10, pady=15)

        # Botões
        self.update_button = ctk.CTkButton(self.conta_frame, text="Atualizar Conta", font=("Arial", 16), command=self.update_account)
        self.update_button.grid(row=5, column=1, columnspan=2, pady=20)
        
        self.logout_button = ctk.CTkButton(self.conta_frame, text="Sair da Conta", font=("Arial", 16), command=self.logout)
        self.logout_button.grid(row=6, column=1, columnspan=2, pady=20)

        # Mensagens de status
        self.status_label = ctk.CTkLabel(self.conta_frame, text="", font=("Arial", 14), fg_color="transparent", text_color="red")
        self.status_label.grid(row=7, column=0, columnspan=2, pady=10)
        
        
        # Widgets no Frame Reciclagem
        self.reciclagem_label = ctk.CTkLabel(self.reciclagem_frame, text="Adicionar Informações de Reciclagem", font=("Arial bold", 24))
        self.reciclagem_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        # Campo para Local
        self.local_label = ctk.CTkLabel(self.reciclagem_frame, text="Local:", font=("Arial", 16))
        self.local_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.local_entry = ctk.CTkEntry(self.reciclagem_frame, font=("Arial", 16))
        self.local_entry.grid(row=1, column=1, padx=20, pady=10)

        # Campo para Status
        self.status_label = ctk.CTkLabel(self.reciclagem_frame, text="Status:", font=("Arial", 16))
        self.status_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.status_entry = ctk.CTkEntry(self.reciclagem_frame, font=("Arial", 16))
        self.status_entry.grid(row=2, column=1, padx=20, pady=10)

        # Botão para salvar Local e Status no banco de dados
        self.save_button = ctk.CTkButton(self.reciclagem_frame, text="Salvar Informações", font=("Arial", 16), command=self.save_recycling_info)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=20)

    # Método para salvar informações no banco de dados
    def save_recycling_info(self):
        local = self.local_entry.get()
        status = self.status_entry.get()
        
        if local and status:
            try:
                conn = sqlite3.connect("chamados.db")
                c = conn.cursor()
                c.execute("INSERT INTO reciclagem (local, status) VALUES (?, ?)", (local, status))
                conn.commit()
                conn.close()
                self.local_entry.delete(0, "end")
                self.status_entry.delete(0, "end")
                print("Informações de reciclagem salvas com sucesso!")
            except sqlite3.Error as e:
                print(f"Erro ao salvar as informações: {e}")
        else:
            print("Por favor, preencha todos os campos!")
        
    
    

    def update_account(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        pix = self.pix_entry.get()

        # Verifica se os campos foram preenchidos
        if email and senha and pix:
            try:
                conn = sqlite3.connect("Sistema.db")
                c = conn.cursor()
                c.execute("UPDATE users SET email=?, senha=?, pix=? WHERE id=1", (email, senha, pix))
                conn.commit()
                conn.close()
                
                # Mensagem de sucesso
                self.status_label.configure(text="Conta atualizada com sucesso!", fg_color="transparent", text_color="green")
            except sqlite3.Error as e:
                # Mensagem de erro
                self.status_label.configure(text=f"Erro ao atualizar a conta: {e}", fg_color="transparent", text_color="red")
        else:
            # Mensagem de campos vazios
            self.status_label.configure(text="Por favor, preencha todos os campos!", fg_color="transparent", text_color="red")

    def logout(self):
        self.quit()
        self.destroy()
        subprocess.Popen([sys.executable, "C:\\Users\\Israel\\Downloads\\RECICLAFACIL COM BD\\ReciclaFacilPY\\login.py"])
        

    def add_to_ranking(self):
        nome = self.rank_name_entry.get()
        lixo_reciclado = self.lixo_reciclado_entry.get()
        
        if nome and lixo_reciclado:
            try:
                conn = sqlite3.connect("ranking.db")
                c = conn.cursor()
                c.execute("INSERT INTO ranking (nome, pontuacao) VALUES (?, ?)", (nome, lixo_reciclado))
                conn.commit()
                conn.close()
                self.rank_name_entry.delete(0, "end")
                self.lixo_reciclado_entry.delete(0, "end")
                self.load_ranking()  # Atualizar o ranking após adicionar o novo registro
            except sqlite3.Error as e:
                print(f"Erro ao adicionar dados ao banco: {e}")
        else:
            print("Por favor, preencha todos os campos!")

    
    
    
    
    
   
   
   
    def load_ranking(self):
        # Limpar a lista atual de rankings
        for widget in self.rank_list_frame.winfo_children():
            widget.destroy()

        try:
            conn = sqlite3.connect("ranking.db")
            c = conn.cursor()
            c.execute("SELECT nome, pontuacao FROM ranking ORDER BY pontuacao DESC LIMIT 10")
            records = c.fetchall()
            
            row = 1  
            for record in records:
                nome, pontuacao = record
                ctk.CTkLabel(self.rank_list_frame, text=f"{row}. {nome} - {pontuacao} kg", font=("Arial", 16)).grid(row=row, column=0, padx=20, pady=5)
                row += 1

            conn.close()
        except sqlite3.Error as e:
            print("Erro ao carregar o ranking:", e)
            
            
            
             # Botões de premiações
        self.voucher_button = ctk.CTkButton(self.chat_frame, text="Voucher", font=("Arial", 16), command=self.voucher_button_event)
        self.voucher_button.grid(row=2, column=0, padx=155, pady=15, sticky="ew")
        
        self.dinheiro_button = ctk.CTkButton(self.chat_frame, text="Dinheiro", font=("Arial", 16), command=self.dinheiro_button_event)
        self.dinheiro_button.grid(row=3, column=0, padx=155, pady=15, sticky="ew")
        
        self.eletronicos_button = ctk.CTkButton(self.chat_frame, text="Eletrônicos", font=("Arial", 16), command=self.eletronicos_button_event)
        self.eletronicos_button.grid(row=4, column=0, padx=155, pady=15, sticky="ew")
        
    
        


    # Funções de ação para cada tipo de premiação
    
    def voucher_button_event(self):
        print("Voucher selecionado")
        
        
    def dinheiro_button_event(self):
        print("Dinheiro selecionado")
        
        
    def eletronicos_button_event(self):
        print("Eletrônicos selecionados")
        
            
    
  
            
 
            
            
            

    def select_frame_by_name(self, name):
        # Configuração das cores de destaque para os botões
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.chat_button.configure(fg_color=("gray75", "gray25") if name == "chat" else "transparent")
        self.rank_button.configure(fg_color=("gray75", "gray25") if name == "rank" else "transparent")
        self.conta_button.configure(fg_color=("gray75", "gray25") if name == "conta" else "transparent")
        self.reciclagem_button.configure(fg_color=("gray75", "gray25") if name == "reciclagem" else "transparent")

        # Gerenciamento de exibição de frames
        self.home_frame.grid_forget()
        self.chat_frame.grid_forget()
        self.rank_frame.grid_forget()
        self.conta_frame.grid_forget()
        self.reciclagem_frame.grid_forget()
        
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        elif name == "chat":
            self.chat_frame.grid(row=0, column=1, sticky="nsew")
        elif name == "rank":
            self.rank_frame.grid(row=0, column=1, sticky="nsew")
        elif name == "conta":
            self.conta_frame.grid(row=0, column=1, sticky="nsew")
        elif name == "reciclagem":
            self.reciclagem_frame.grid(row=0, column=1, sticky="nsew")

    # Botões de navegação
    def home_button_event(self):
        self.select_frame_by_name("home")
        
    def chat_button_event(self):
        self.select_frame_by_name("chat")
        
    def rank_button_event(self):
        self.select_frame_by_name("rank")
        
    def conta_button_event(self):
        self.select_frame_by_name("conta")
        
    def reciclagem_button_event(self):
        self.select_frame_by_name("reciclagem")
    
    def change_appearance_mode_event(self, new_mode):
        ctk.set_appearance_mode(new_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
