# Daebrion Hopwood
# March 28th 2018
# Re-visit/Re-factor


# Purpose: Dice rollin game. Roll the dice to accumulate points. First to reach the preset amount wins.
# Pre-conditions: Players must click when prompted.
# Post-conditions: Winner is declared once point amount is reached. 


from graphics import *
from random import *

#-------------------------------------------------------------------------------
# function in_box
'''
Purpose: Determine if the user click is within the boxes.
Parameters: Three point objects; assumes the first point is on the left, and the second point is on the right.
Output: True if user_click is within the box formed by corner1 & corner2. False otherwise. 
'''

def in_box(corner1, corner2, user_click):
    corner1_x = corner1.getX()
    corner1_y = corner1.getY()
    
    corner2_x = corner2.getX()
    corner2_y = corner2.getY()
    
    user_click_x = user_click.getX()
    user_click_y = user_click.getY()
    
    if corner1_x < user_click_x < corner2_x and corner1_y < user_click_y < corner2_y:
        return_value = True
    else:
        return_value = False
        
    return return_value

#-------------------------------------------------------------------------------
# function draw_die
'''
Purpose: To draw a die face from a gif file at the location on the graphics window provided.
Preconditions (parameters): Need die number, location (x, y), and the graphics window.
Postconditions (outputs/results): Draws the gif on the graphics window, returns the image object that was drawn.
'''

def draw_die(die_number, image_x, image_y, win):
    
    dice_roll = Image(Point(image_x, image_y), str(die_number) + ".gif" )
    dice_roll.draw(win)

    return dice_roll
def click_yes_or_no(playernumber, win):
    
    instructions = Text(Point(400, 350), "Roll again, Player " + str(playernumber) + "?")
    instructions.setSize(25)
    instructions.setStyle("bold")
    instructions.setFace("times roman")
    instructions.setTextColor("black")
    instructions.draw(win)
    
    square_yes = Rectangle(Point(50, 160), Point(150, 260))
    square_yes.draw(win)
    
    square_yes_txt = Text(Point(100, 210), "Yes")
    square_yes_txt.setSize(30)
    square_yes_txt.setFace("times roman")
    square_yes_txt.setStyle("bold")
    square_yes_txt.draw(win)
    
    square_no = Rectangle(Point(50, 300), Point(150, 400))
    square_no.draw(win)
    
    square_no_txt = Text(Point(100, 350), "No")
    square_no_txt.setSize(30)
    square_no_txt.setFace("times roman")
    square_no_txt.setStyle("bold")  
    square_no_txt.draw(win)    
    
    click = win.getMouse()
    
    while not in_box(Point(50, 160), Point(150, 260), click) and not in_box(Point(50, 300), Point(150, 400), click):
        click = win.getMouse()
        
    if in_box(Point(50, 160), Point(150, 260), click):
        return_value = True
    else:
        return_value = False
        
    instructions.undraw()
    square_yes.undraw()
    square_yes_txt.undraw()
    square_no.undraw()
    square_no_txt.undraw()
        
    return return_value

#-------------------------------------------------------------------------------
# function play_a_round
'''
Purpose: Play a round of the game for one player, using the graphics window provided and the player number for the prompts.
Preconditions (parameters): Need the current player number and the graphics window. Will also check the function click_yes_or_no to dictate continuing that round for that user.
Postconditions (outputs/results): Updates and outputs the players score for that round. Outputs players total score after the round is over.
'''

def play_a_round(playernumber, win):
    
    player_score = 0
    roll_again = True
    
    die_roll = randrange(1, 7)
    
    while roll_again and die_roll != 1:
        player_score += die_roll
        dice_image = draw_die(die_roll, 400, 200, win)
        
        score_display = Text(Point(650, 210), "Player " + str(playernumber) + " score for this round " + str(player_score))
        score_display.setStyle("bold")
        score_display.draw(win)
        
        instructions = Text(Point(400, 80), "Round for Player " + str(playernumber))
        instructions.setSize(24)
        instructions.setStyle("bold")
        instructions.draw(win)
        
        line = Rectangle(Point(355,90), Point(435, 100))
        line.setFill("blue")
        line.setOutline("blue")
        line.draw(win)
               
        roll_again = click_yes_or_no(playernumber, win)
        if roll_again:
            die_roll = randrange(1, 7)
            
        dice_image.undraw()
        score_display.undraw()
        instructions.undraw()
        line.undraw()
    
    if die_roll == 1:
        player_score = 0
        dice_image = draw_die(die_roll, 400, 200, win)
        result = Text(Point(400, 520), "You rolled a one and left with 0")
        instructions = Text(Point(400,540), "End of round for " + str(playernumber))
        exit = Text(Point(400, 560), "Click to exit")
        result.setSize(20)
        instructions.setSize(20)
        exit.setSize(20)
    
    else:
        result = Text(Point(400, 520), "You left with " +str(player_score) + " points")
        instructions = Text(Point(400,540), "End of round for " + str(playernumber))
        exit = Text(Point(400, 560), "Click to exit")        
        result.setSize(20)
        instructions.setSize(20)
        exit.setSize(20)        
        
    result.draw(win)
    instructions.draw(win)
    exit.draw(win)
    
    win.getMouse()
    result.undraw()
    instructions.undraw()
    exit.undraw()
    
    if die_roll ==1:
        dice_image.undraw()
        
    return player_score

#-------------------------------------------------------------------------------
# function instructions
'''
Purpose: To display the instructions for the game, let the user click and close the window
Preconditions: None
Postconditions: Instructions have been displayed and then the window closed. No return value.
'''

def instructions():
    win = GraphWin("Instructions for Don't Roll One!", 800, 600)
    win.setBackground("yellow")
    
    greeting = Text(Point(400, 100), "Instructions for Don't Roll ONE!")
    greeting.setSize(32)
    greeting.setStyle("bold")
    greeting.setFace("times roman")
    greeting.setTextColor("blue")
    greeting.draw(win)
    
    instructions_1 = Text(Point(400, 140), "Player 1 goes first")
    instructions_1.setSize(25)
    instructions_1.setFace("times roman")
    instructions_1.setTextColor("black")
    instructions_1.draw(win)    
    
    instructions_2 = Text(Point(400, 170), "Player 2 goes second")
    instructions_2.setSize(25)
    instructions_2.setFace("times roman")
    instructions_2.setTextColor("black")
    instructions_2.draw(win)
    
    instructions_3 = Text(Point(400, 220), "The player rolls a die and gets points as long as they don't roll a ONE!")
    instructions_3.setSize(25)
    instructions_3.setFace("times roman")
    instructions_3.setTextColor("black")
    instructions_3.draw(win)
    
    instructions_4 = Text(Point(400, 260), "They can stop rolling any time after the first roll")
    instructions_4.setSize(25)
    instructions_4.setFace("times roman")
    instructions_4.setTextColor("black")
    instructions_4.draw(win)   
    
    instructions_5 = Text(Point(400, 300), "If they roll a ONE, they lose all the points in that round.")
    instructions_5.setSize(25)
    instructions_5.setFace("times roman")
    instructions_5.setTextColor("black")
    instructions_5.draw(win)    
    
    instructions_6 = Text(Point(400, 350), "First player to reach 100 wins!!")
    instructions_6.setSize(35)
    instructions_6.setStyle("bold")
    instructions_6.setFace("times roman")
    instructions_6.setTextColor("black")
    instructions_6.draw(win)    
    
    instructions_7 = Text(Point(400, 500), "Click to continue")
    instructions_7.setSize(25)
    instructions_7.setFace("times roman")
    instructions_7.setTextColor("black")
    instructions_7.draw(win)    
    
    win.getMouse()    
    win.close()
    
#-------------------------------------------------------------------------------
# function main

def main():
    player1_score = 0
    player2_score = 0
    
    win = GraphWin("Don't Roll ONE!", 800, 600)
    win.setBackground("Orange")
    
    instructions_1_1 = Text(Point(400, 50), "Don't Roll ONE!")
    instructions_1_1.setSize(36)
    instructions_1_1.setStyle("bold")
    instructions_1_1.setFace("times roman")
    instructions_1_1.setTextColor("blue")
    instructions_1_1.draw(win)
    
    instructions()
    
    score_board = Rectangle(Point(550, 130), Point(750, 200))
    score_board.draw(win)
        
    player1points = Text(Point(650, 150), "Player 1 Points: " + str(player1_score))
    player1points.setSize(20)
    player1points.setFace("times roman")
    player1points.setTextColor("black")
    player1points.draw(win)
    
    player2points = Text(Point(650, 170), "Player 2 Points: " + str(player2_score))
    player2points.setSize(20)
    player2points.setFace("times roman")
    player2points.setTextColor("black")
    player2points.draw(win)
    
    
    while player1_score < 100 and player2_score < 100:
        player1_score += play_a_round(1, win)
        player1points.setText("Player 1 Points: " + str(player1_score))
        win.getMouse()
        if player1_score < 100:
            player2_score += play_a_round(2, win)
            player2points.setText("Player 2 Points: " + str(player2_score))
            win.getMouse()
            
    game_over = Text(Point(400, 300), "GAME OVER")
    game_over.setSize(36)
    game_over.setStyle("bold")
    game_over.draw(win)
    
    if player1_score >= 100:
        winner = Text(Point(400, 350), "Player 1 won with a score of " +str(player1_score))
    else:
        winner = Text(Point(400, 350), "Player 2 won with a score of " +str(player2_score))
    
    winner.setSize(25)
    winner.draw(win)
    
    exit = Text(Point(400, 500), "Click to close")
    exit.setStyle("bold")
    exit.draw(win)
    
    
    win.getMouse()
    win.close()

main()
        
        
    