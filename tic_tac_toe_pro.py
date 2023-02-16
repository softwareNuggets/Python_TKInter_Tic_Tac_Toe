#https://www.youtube.com/softwareNuggets
#https://github.com/softwareNuggets/Python_TKInter_Tic_Tac_Toe
import tkinter as tk
import random
from PIL import Image, ImageTk

#Install the Pillow package
#pip install Pillow

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.geometry("300x420")
        

        #create IntVar() object... has .get() and .set()
        self.play_against_computer_var = tk.IntVar()
        
        self.current_player = playerX[0]
        self.game_over = False

        
        self.scoreboard = tk.Frame(self.master, borderwidth=2, relief="groove")
        self.scoreboard.rowconfigure(2, {'minsize': 30, 'weight': 1})
        self.scoreboard.grid(row=0, column=0, rowspan=2, columnspan="3", sticky='news')

        # Create the labels to display the counts
        self.wins_label = tk.Label(self.scoreboard, text="Wins: 0", font=(defaultFontName, 16), 
                                            fg="white",background="black", width=12)
        self.wins_label.grid(row=1, column=0)

        self.losses_label = tk.Label(self.scoreboard, text="Losses: 0", font=(defaultFontName, 16))
        self.losses_label.grid(row=1, column=2)

        self.status_label = tk.Label(self.scoreboard, width=22,
                                            text=playerX[1], background=playerX[2],
                                            font=(defaultFontName, 16))
        self.status_label.grid(row=2, column=0, columnspan=4, sticky='news')

        # set the background color of the second row to red
        

        #reset score and re-show
        self.reset_win_losses()

        # Create the menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Create the file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New Game", command=self.restart)
        self.file_menu.add_command(label="Reset Score Board", command=self.reset_win_losses)
        self.file_menu.add_command(label="About", command=self.show_about)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)


        # tic-tac-toe board area
        self.board_frame = tk.Frame(self.master, borderwidth=2, relief="ridge")
        self.board_frame.grid(row=2, column=0, rowspan=3)

        #create empty 3x3 board
        #[['', '', ''], ['', '', ''], ['', '', '']]
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        #create None valued 3x3
        #[[None, None, None], [None, None, None], [None, None, None]]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.board_frame, text="", 
                                    font=(defaultFontName, 20), width=5, height=2,
                                    command=lambda i=i, j=j: self.play(i, j))
                button.grid(row=i, column=j)
                
                #created object above with None placeholder
                self.buttons[i][j] = button


        
        self.restart_button = tk.Button(self.board_frame, text="Restart", 
                                font=(defaultFontName, 16), 
                                command=self.restart)
        self.restart_button.grid(row=4, column=0, columnspan=3)

        
        self.computer_checkbox = tk.Checkbutton(self.board_frame, text="Play against computer",
                                                variable=self.play_against_computer_var, 
                                                command=self.toggle_computer)
        self.computer_checkbox.grid(row=5, column=0, columnspan=3)        
        
    def reset_win_losses(self):
        self.wins = 0
        self.losses = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.wins_label.config(text=f"Wins: {self.wins}")
        self.losses_label.config(text=f"Losses: {self.losses}")



    def play(self, i, j):
        if self.game_over or self.board[i][j] != "":
            return

        self.board[i][j] = self.current_player
        self.buttons[i][j].config(text=self.current_player)

        if self.check_win():
            self.game_over = True
            if(self.current_player == playerX[0]):
                self.status_label.config(text=playerX[4],background=playerX[2])
                self.wins = self.wins + 1
                self.update_scoreboard()
            elif(self.current_player == playerO[0]):
                self.status_label.config(text=playerO[4],background=playerO[2])
                self.losses = self.losses + 1
                self.update_scoreboard()
            return

        if self.check_draw():
            self.game_over = True
            self.status_label.config(text="It's a draw!")
            return

        if self.current_player == playerX[0]:
            self.current_player = playerO[0]
            self.status_label.config(text=playerO[1], background=playerO[2])
        else:
            self.current_player = playerX[0]
            self.status_label.config(text=playerX[1], background=playerX[2])

        if self.play_against_computer_var.get() and self.current_player == playerO[0]:
            self.play_computer()

    def play_computer(self):
        # Look for a winning move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = playerO[0]
                    if self.check_win():
                        self.buttons[i][j].config(text=playerO[0])
                        self.game_over = True
                        self.status_label.config(text="Computer wins!")
                        return
                    self.board[i][j] = ""

        # Look for a blocking move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = playerX[0]
                    if self.check_win():
                        self.board[i][j] = playerO[0]
                        self.buttons[i][j].config(text=playerO[0])
                        self.current_player = playerX[0]
                        self.status_label.config(text=playerX[1])
                        return
                    self.board[i][j] = ""

        # Choose a random move
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if self.board[i][j] == "":
                self.board[i][j] = playerO[0]
                self.buttons[i][j].config(text=playerO[0])
                if self.check_win():
                    self.game_over = True
                    self.status_label.config(text="Computer wins!")
                    self.update_scoreboard()
                elif self.check_draw():
                    self.game_over = True
                    self.status_label.config(text="It's a draw!")
                else:
                    self.current_player = playerX[0]
                    self.status_label.config(text=playerX[1])

                
                return

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False


    def check_draw(self):
        #check to see if any positions are open
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True
        

    def toggle_computer(self):
        if self.play_against_computer_var.get():
            self.current_player = playerX[0]
            self.status_label.config(text=playerX[1])
            self.play_computer()

    def restart(self):
        self.current_player = playerX[0]
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.status_label.config(text=playerX[1],background=playerX[2])

    def show_about(self):
                
        about_window = tk.Toplevel(self.master)
        about_window.title("About")

        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()
        parent_x = self.master.winfo_rootx()
        parent_y = self.master.winfo_rooty()
        #child_width = about_window.winfo_reqwidth()
        #child_height = about_window.winfo_reqheight()
        child_width = 500
        child_height = 300

        x = parent_x + (parent_width - child_width) // 2
        y = parent_y + (parent_height - child_height) // 2
        about_window.geometry('{}x{}+{}+{}'.format(child_width, child_height,x, y))
        about_window.grab_set();

        # Read the Image
        image = Image.open(r"c:\youtube\python\tictactoe\sn_slate.png")
        # Resize the image using resize() method
        resize_image1 = image.resize((250, 250))
        img1 = ImageTk.PhotoImage(resize_image1)
        # create label and add resize image
        label1 = tk.Label(about_window,image=img1)
        label1.image = img1
        label1.place(x=0, y=0)

        about_label = tk.Label(about_window, text="Software is available at GitHub/SoftwareNuggets")
        about_label.pack()
        about_window.focus_set()
        about_window.grab_set()
        about_window.wait_window()


if __name__ == '__main__':
    defaultFontName = 'Helvetica'
    playerX = ('X', "Player X's turn", "lightSkyBlue",1, 'Player X is winner')
    playerO = ('O', "Player O's turn", "lightGreen",2, 'Player O is winner')
 
    root = tk.Tk()
    
    tic_tac_toe = TicTacToe(root)
    root.mainloop()