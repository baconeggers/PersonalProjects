""" D6 rolling program, inspired by RealPython.com | Charles M Eggers II"""

import random
import dice_art

def parse_input(input_string):
    """ return 'input_string' as an int between 1 and 6
        
        check if 'input_string' is between 1 and 6
        if so, return an int with the same value, otherwise 
        tell the user to enter a valid number and quit the program """
    if input_string.strip() in {"1","2","3","4","5","6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

def generate_dice_faces_diagram(dice_values):
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # generate header with the word 'RESULTS' centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

def _get_dice_faces(dice_values):
    # generate a list of dice faces from dice_art.DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(dice_art.DICE_ART[value])
    return dice_faces

def _generate_dice_faces_rows(dice_faces):
    # generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(dice_art.DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = dice_art.DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows
    


def roll_dice(num_dice):
    """ return a list of ints with length 'num_dice'
    
    each int in the returned list is a random number between 
    1 and 6, inclusive """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,6)
        roll_results.append(roll)
    return roll_results

# app's main code block

num_dice_input = input("How many dice would you like to roll? [1-6] ")
num_dice = parse_input(num_dice_input)

roll_results = roll_dice(num_dice)

dice_face_diagram = generate_dice_faces_diagram(roll_results)

print(f"\n{dice_face_diagram}")
