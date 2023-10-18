
class User:
    name = "default"
    player_choice = 'Stone'
    def __init__(self, name, player_choices):
        self.name = name
        self.player_choice = player_choices

    def set(self, name):
        self.name = name
        
def WhoWin(fPlayer, sPlayer):
    if fPlayer.player_choice == sPlayer.player_choice:
        print("draw")
        print(fPlayer.player_choice, " ", sPlayer.player_choice)
    else:
        list = []
        list.append(fPlayer.player_choice)
        list.append(sPlayer.player_choice)
        papper = False
        stone = False
        scissors = False
        for l in list:
            if l == "papper":
                papper = True
            elif l == "stone":
                stone = True
            elif l == "scissors":
                scissors = True
            if(papper and stone):
                if(fPlayer.player_choice == "papper"):
                    print("Win: ", fPlayer.name)
                else:
                    print("Win: ", sPlayer.name)
            elif(papper and scissors):
                if(fPlayer.player_choice == "scissors"):
                    print("Win: ", fPlayer.name)
                else:
                    print("Win: ", sPlayer.name)
            elif(scissors and stone):
                if(fPlayer.player_choice == "stone"):
                    print("Win: ", fPlayer.name)
                else:
                    print("Win: ", sPlayer.name) 
    
 