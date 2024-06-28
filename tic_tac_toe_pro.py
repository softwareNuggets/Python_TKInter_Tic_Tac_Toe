
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
        self.master.geometry("280x420")
        self.defaultFontName = 'Helvetica'
        self.playerX = ('X', "Player X's turn", "Orange",'Player X is the winner')
        self.playerO = ('O', "Player O's turn", "lightGreen",'Player O is the winner')

        #create IntVar() object... has .get() and .set()
        self.play_against_computer_var = tk.IntVar()
        self.current_play_computer = self.playerX[0]

        self.game_over = False
        
        #setup menu bar and attach to app
        self.setup_menubar()

        #attach score card to display
        self.attach_score_card()

        #let random pic user
        self.pick_random_player()
        #print(f'init.29:CurrentPlayer={self.current_player}')

        #show current user in score card section
        self.switch_current_user_on_score_card()

        #reset score and re-show
        self.reset_win_losses()

        #add function to add buttons to form
        self.setup_board()
        
        #add reset board and play computer
        self.setup_bottom_section()

    def pick_random_player(self):
        #let random pic user
        if (random.randint(13,143) % 2) ==  0:
            self.current_player = self.playerX[0]
        else:
            self.current_player = self.playerO[0]

    def setup_menubar(self):
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

    def attach_score_card(self):

        self.scoreboard = tk.Frame(self.master, borderwidth=2, relief="groove")
        self.scoreboard.rowconfigure(2, {'minsize': 30, 'weight': 1})
        self.scoreboard.grid(row=0, column=0, rowspan=2, columnspan="3", sticky='news')

        # Create the labels to display the counts
        self.my_win_label = tk.Label(self.scoreboard, text="Player X: 0", font=(self.defaultFontName, 16), 
                                            fg="white",background="black", width=12)
        self.my_win_label.grid(row=1, column=0)

        self.their_win_label = tk.Label(self.scoreboard, text="Player O: 0", font=(self.defaultFontName, 16))
        self.their_win_label.grid(row=1, column=2)

        self.status_label = tk.Label(self.scoreboard, width=22,
                                            text=self.playerX[1], background=self.playerX[2],
                                            font=(self.defaultFontName, 16))
        self.status_label.grid(row=2, column=0, columnspan=4, sticky='news')        

    def switch_current_user_on_score_card(self):
        if self.current_player == 'X':
            self.status_label.config(text=self.playerX[1],background=self.playerX[2])
            #print(f'switch:current={self.current_player}:MenuBar={self.playerX[1]}')
        else:
            self.status_label.config(text=self.playerO[1],background=self.playerO[2])        
            #print(f'switch:current={self.current_player}:MenuBar={self.playerO[1]}')
 
    def reset_win_losses(self):
        self.my_win_count  = 0
        self.their_win_count = 0
        self.update_scoreboard()

    def setup_board(self):
        #print(f'setup_board:103:current_player={self.current_player}')
        # tic-tac-toe board area
        self.board_frame = tk.Frame(self.master, borderwidth=2, relief="ridge")
        self.board_frame.grid(row=2, column=0, rowspan=3)

        #create empty 3x3 board
        #self.board = [["" for _ in range(3)] for _ in range(3)]
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        
        
        #create None valued 3x3
        #self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]
        
        
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.board_frame, text="", 
                                    font=(self.defaultFontName, 20), width=5, height=2,
                                    command=lambda i=i, j=j: self.play(i, j))
                button.grid(row=i, column=j)
                
                #created object above with None placeholder
                self.buttons[i][j] = button        

    def setup_bottom_section(self):
        
        self.restart_button = tk.Button(self.board_frame, text="Restart", 
                                font=(self.defaultFontName, 16), 
                                command=self.restart)
        self.restart_button.grid(row=4, column=0, columnspan=3)

        
        self.computer_checkbox = tk.Checkbutton(self.board_frame, text="Play against computer",
                                                variable=self.play_against_computer_var, 
                                                command=self.toggle_computer)
        self.computer_checkbox.grid(row=5, column=0, columnspan=3)  

    def update_scoreboard(self):
        self.my_win_label.config(text=f"PlayerX: {self.my_win_count}")
        self.their_win_label.config(text=f"PlayerO: {self.their_win_count}")
 
    def reset_buttons(self):
        #clean up all the button, set the text property to emtpy string
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.board[i][j]=''

    def restart(self):

        #create empty 3x3 board
        #self.board = [["" for _ in range(3)] for _ in range(3)]
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]

        self.reset_buttons()
        
        self.game_over = False

        #let's take turns going first
        if self.play_against_computer_var.get():
            if(self.current_play_computer == self.playerX[0]):
                self.current_player = self.playerO[0]
            else:
                self.current_player = self.playerX[0]
        else:
            self.pick_random_player()


        self.current_play_computer = self.current_player;
        
        self.switch_current_user_on_score_card()

        if self.play_against_computer_var.get():

            if(self.current_player == self.playerO[0]):
                self.status_label.config(text=self.playerO[1], background=self.playerO[2])
            else:
                self.current_player = self.playerX[0]
                self.status_label.config(text=self.playerX[1], background=self.playerX[2])

            self.play_computer()

    def toggle_computer(self):

        self.reset_buttons()
        self.game_over=False

        self.want2playComputer = self.play_against_computer_var.get()

        if self.want2playComputer == True:
            self.pick_random_player()

            #print(f'toggle_computer:CurrentPlayer={self.current_player}')

            self.switch_current_user_on_score_card()
            
            #if(self.current_player == self.playerO[0]):
            self.play_computer()

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

    def show_about(self):
        about_window = tk.Toplevel(self.master)
        about_window.title("About")

        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()
        parent_x = self.master.winfo_rootx()
        parent_y = self.master.winfo_rooty()
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

    def play(self, i, j):
        #print(f'play255:current_player={self.current_player}')
        
        if self.board[i][j] != "":
            self.buttons[i][j].config(text=self.current_player)
            
        if self.game_over == True or self.board[i][j] != "":
            return

        self.board[i][j] = self.current_player
        self.buttons[i][j].config(text=self.current_player)
        
        

        #print(f'269:buttons[i={i}][j={j}]=current_player={self.current_player}')
        
        #self.aa = self.board[0]
        #self.bb = self.board[0].count("X")
        #self.torf = (bool)(self.board[0].count("X") == 2)
        #self.test = (bool)((self.board[0].count("X") ==2) and ("" in self.board[0]))

        if self.check_win():
            self.game_over = True
            if self.current_player == 'X':
                self.status_label.config(text=self.playerX[3],background=self.playerX[2])
                self.my_win_count += 1
            else: 
                self.status_label.config(text=self.playerO[3],background=self.playerO[2])
                self.their_win_count += 1

            self.update_scoreboard()
            return

        #check for draw
        if self.check_draw():
            self.game_over = True
            self.status_label.config(text="It's a draw!",background="Orange")
            return

        #print(f'play291:current_player={self.current_player}')
        #swap current player
        if self.current_player == 'O':
            self.current_player = 'X'
        else:
            self.current_player = 'O'
           
        #update the score card
        self.switch_current_user_on_score_card()    

        #print(f'play297:current_player={self.current_player}')
        

        if self.play_against_computer_var.get() and self.current_player == self.playerO[0]:
            self.play_computer()

    def play_computer(self):
        #print(f'play_computer:305:current_player={self.current_player}')
        if(self.current_player != 'O'):
            return
        
        # let's check the center if available, this is where we start
        if self.board[1][1] == "":
            self.board[1][1] = "O"
            self.buttons[1][1].config(text=self.playerO[0])
            if self.check_win():
                self.game_over = True
                self.their_win_count += 1
                self.update_scoreboard()
                self.status_label.config(text="Computer wins!", background=self.playerO[2])
            elif self.check_draw():
                self.game_over = True
                self.status_label.config(text="It's a draw!",background="Orange")
            else:
                self.current_player = self.playerX[0]
                self.status_label.config(text="Player X's turn",background=self.playerX[2])
            return

        for i in range(3):
            if self.board[i].count("X") == 2 and "" in self.board[i]:
                j = self.board[i].index("")
                #print(f'play_computer:330:[{i}][{j}]=[{self.board[i][j]}]:current_player={self.current_player}')
                self.board[i][j] = self.playerO[0]
                self.buttons[i][j].config(text=self.playerO[0])
                #print(f'play_computer:333:[{i}][{j}]=[{self.board[i][j]}]:current_player={self.current_player}')
                if self.check_win():
                    self.game_over = True
                    self.their_win_count += 1
                    self.update_scoreboard()
                    self.status_label.config(text="Computer wins!",background=self.playerO[2])
                elif self.check_draw():
                    self.game_over = True
                    self.status_label.config(text="It's a draw!",background="Orange")
                else:
                    self.current_player = self.playerX[0]
                    self.status_label.config(text="Player X's turn",background=self.playerX[2])
                return

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.playerO[0]
                    #print(f'play_computer:351:[{i}][{j}]=[{self.board[i][j]}]:current_player={self.current_player}')
                    if self.check_win():
                        self.buttons[i][j].config(text=self.playerO[0])
                        self.game_over = True
                        self.their_win_count += 1
                        self.update_scoreboard()
                        self.status_label.config(text=self.playerO[3],background=self.playerO[2])
                        return
                    self.board[i][j] = ""
                    #print(f'play_computer:reset:359:[{i}][{j}]=[{self.board[i][j]}]:current_player={self.current_player}')

        for j in range(3):
            for i in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.playerO[0]
                    #print(f'play_computer:366:[{i}][{j}]=[{self.board[i][j]}]:current_player={self.current_player}')
                    if self.check_win():
                        self.buttons[i][j].config(text=self.playerO[0])
                        self.game_over = True
                        self.their_win_count += 1
                        self.update_scoreboard()
                        self.status_label.config(text=self.playerO[3],background=self.playerO[2])
                        return
                    self.board[i][j] = ""
                    #print(f'play_computer:reset:374:[{i}][{j}]=[{self.board[i][j]}]:current_player={self.current_player}')
                    
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if self.board[i][j] == "":
                self.board[i][j] = self.playerO[0]
                self.buttons[i][j].config(text=self.playerO[0])

                if self.check_win():
                    self.game_over = True
                    self.their_win_count += 1
                    self.update_scoreboard()                    
                    self.status_label.config(text="Computer wins!",background=self.playerO[2])
                elif self.check_draw():
                    self.game_over = True
                    self.status_label.config(text="It's a draw!",background="Orange")
                else:
                    self.current_player = self.playerX[0]
                    self.status_label.config(text="Player X's turn",background=self.playerX[2])
                return

if __name__ == '__main__':
    
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.mainloop()
