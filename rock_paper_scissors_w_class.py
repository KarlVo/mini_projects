import random
class Rock:

    def __init__(self, p_move, c_move, score_p, score_c):
        self.p_move = p_move
        self.c_move = c_move
        self.y = computer_choice()
        self.score_c = 0
        self.score_p = 0
        #self.winner = moves()


    def round_win(self, p_move, c_move, score_c, score_p):
            self.winner = self.moves(p_move, c_move)
            if self.winner == "Player wins":
                self.score_p = 1
                self.score_c = 0
                return self.score_p, self.score_c
                
                
            if self.winner == "Computer wins":
                self.score_c = 1
                self.score_p = 0
                return self.score_p, self.score_c
                
                    
            if self.winner == "No point":
                self.score_c = 0
                self.score_p = 0
                return self.score_p, self.score_c
                  
                
    
                
    def moves(self, p_move, c_move):
        if self.p_move == self.c_move:
            winner = "No point"
            
            return winner
        if self.p_move == "A" and self.c_move == "C":
            winner = "Player wins"
            return winner
            
        if self.p_move == "A" and self.c_move == "B":
            winner = "Computer wins"
           
            return winner
        if self.p_move == "B" and self.c_move =="A":
            winner = "Player wins"
            
            return winner
        if self.p_move == "B" and self.c_move == "C":
            winner = "Computer wins"
            
            return winner
        if self.p_move == "C" and self.c_move == "A":
            winner = "Computer wins"
         
            return winner
        if self.p_move == "C" and self.c_move == "B":
            winner = "Player wins"
           
            return winner

            
  
                

def intro():
    print("Welcome to the Rock, Paper, Scissors \nWrite your hand gesture as A (Rock), B (Paper) or C (Scissors)")


def check_input():
    ans = ["A","B","C"]
    while True:
        try:
            x = input("Your move! ")
            x.capitalize()#fixa
            for elem in ans:
                if elem == x:
                     z =1
            if z == 0:                     
                print("Error occured. Try again!")
                continue
            else:
                print("Your choice is: "+ x)
                break
        except:
            print("Error except. Try again!")
    return x

def num_rounds():
    while True:
        try:
            f = int(input("How many rounds do you want to play? "))
            if f == "":
                print("Error 1")
            else:
                break
        except:
            print("Error 2")
    return f
            
        
def computer_choice():
    y  = random.randrange(3)
    if y == 0:
        y = "A"
    elif y == 1:
        y = "B"
    else:
        y = "C"
    return y
        
          

def main():
    intro()
    round_winner = []
    score_player = 0
    score_computer = 0


   
    number_rounds = num_rounds()
    print("")
    while True:
        
        player_choice = check_input()
        comp_move = computer_choice()
        print("Computer choice is: "+ comp_move)
        round_Rock = Rock(player_choice, comp_move, score_player, score_computer)
    
        winner = round_Rock.moves(player_choice, comp_move)
        round_winner = round_Rock.round_win(player_choice, comp_move, score_player, score_computer)
        print(winner)
        score_player += round_winner[0]
        score_computer += round_winner[1]
        print("Your points: " + str(score_player)+ " Points Computer: "+ str(score_computer))
        print("")
        if  score_player == number_rounds or score_computer == number_rounds:
            break
    print("Game over")
    print("Final score \nYou: "+str(score_player) + " Computer: "+ str(score_computer))


main()
