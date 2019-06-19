# used for system commands. cls for clearing the screen mainly
import os
import pyperclip

# the function for converting the text into discord emoji text
def emojiconvert(textstring):
	
	emoji_dbs = {
	
	# Key names for emoji numbers 0-9
	"1": ":one:",
	"2": ":two:",
	"3": ":three:",
	"4": ":four:",
	"5": ":five:",
	"6": ":six:",
	"7": ":seven:",
	"8": ":eight:",
	"9": ":nine:",
	"0": ":zero:",
	
	# Key names for emoji alfabetical characters from a-z
	"a": ":regional_indicator_a:",
	"b": ":regional_indicator_b:",
	"c": ":regional_indicator_c:",
	"d": ":regional_indicator_d:",
	"e": ":regional_indicator_e:",
	"f": ":regional_indicator_f:",
	"g": ":regional_indicator_g:",
	"h": ":regional_indicator_h:",
	"i": ":regional_indicator_i:",
	"j": ":regional_indicator_j:",
	"k": ":regional_indicator_k:",
	"l": ":regional_indicator_l:",
	"m": ":regional_indicator_m:",
	"n": ":regional_indicator_n:",
	"o": ":regional_indicator_o:",
	"p": ":regional_indicator_p:",
	"q": ":regional_indicator_q:",
	"r": ":regional_indicator_r:",
	"s": ":regional_indicator_s:",
	"t": ":regional_indicator_t:",
	"u": ":regional_indicator_u:",
	"v": ":regional_indicator_v:",
	"w": ":regional_indicator_w:",
	"x": ":regional_indicator_x:",
	"y": ":regional_indicator_y:",
	"z": ":regional_indicator_z:",
	" ": "    ",
	
	# Key names for emoji special characters
	"!": ":exclamation:",
	"#": ":hash:",
	"$": ":heavy_dollar_sign:",
	"*": ":heavy_multiplication_x:",
	"-": ":heavy_minus_sign:",
	"+": ":heavy_plus_sign:",
	"/": ":heavy_division_sign:",
	"?": ":question:",
	",": ":comet:",
	".": ":octagonal_sign:"
	}
	
	# The list of characters or numbers are appended to a list
	input_list = []
	converted_text = ""
	
	for index in range(len(inputstring)):
		input_list.append(inputstring[index])
		
	for keyword in range(len(input_list)):	
		if input_list[keyword] in emoji_dbs:
			converted_text = converted_text + "".join(emoji_dbs[input_list[keyword]]) + " "
	
	# returns the output of text as discord emoji text
	return converted_text

# prints the tile screen
def title():
	print(f'''
  ___  _                   _                  _ _                  
 |   \(_)___ __ ___ _ _ __| |  ___ _ __  ___ (_|_)  __ ___ _ ___ __
 | |) | (_-</ _/ _ \ '_/ _` | / -_) '  \/ _ \| | | / _/ _ \ ' \ V /
 |___/|_/__/\__\___/_| \__,_|_\___|_|_|_\___// |_|_\__\___/_||_\_/ 
                           |___|           |__/ |___|              
------------------------------------------------------------------version_{ver}
Type the text you want, and the script will spit out the emoji text code.
After typing something, as soon as you press enter all output will be
copied to the clipboard.

when your done playing with emojis, you can exit by typing !!exit
''')


# shows the version of the script and displays a message on what to do
ver = "0.02"

title()

# user enters input which is then passed to the emojiconvert function and is returned as emoji text
inputstring = input("Enter some text.... ").lower()

# used for breaking the while loop
exitflag = 0
while exitflag != 1:
	
	# clears the screen
	# os.system("cls")
		
	# the emoji convert function is called and does its business
	discord_string = emojiconvert(inputstring)
	
	# prints the output to the screen
	print(discord_string)

	# copy text to clipboard
	pyperclip.copy(discord_string)
	
	# starts the loop again
	inputstring = input("> ").lower()
	
	# entering !!exit will end the loop
	# script will return with an empty string if empty string is given
	if inputstring == "!!exit":
		exitflag += 1
	elif inputstring == "":
		print("")
	
