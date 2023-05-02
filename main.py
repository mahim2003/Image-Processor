# Yet Another Image Processor
# Mahim Chaudhary:301463607 & Ariel Tyson:301458219
# December 6th, 2021.
# Create an image processing software with functionalities in a nice stand-alone interface.
# Cmpt120:D300

# Imported modules
import cmpt120imageProjHelper as helper
import cmpt120imageManip as manip
import tkinter
import tkinter.filedialog
import pygame
pygame.init()


# Main system options in user interface :
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# Basic options for user interface :
basic = [
          "1: Apply Red Filter",
          "2: Apply Green Filter",
          "3: Apply Blue Filter",
          "4: Apply Sepia Filter",
          "5: Apply Warm Filter",
          "6: Apply Cold Filter",
          "7: Switch to Advanced Functions"
         ]


# Advanced options for user interface :
advanced = [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Double Size",
                "4: Half Size",
                "5: Locate Fish",
                "6: Switch to Basic Functions",
             ]


# A function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """

    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("")  # an empty line
    menuString.append("Choose the following options:")
    menuString.append("")  # an empty line
    menuString += system
    menuString.append("")  # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter Your Choice (Q/O/S/R or 1-7)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter Your Choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString


# a helper unction that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, mode attribute if the user switches mode)
def handleUserInput(state, image):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """

    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")

        elif userInput.lower() == "o":  # opens image
            tkinter.Tk().withdraw()
            open_filename = tkinter.filedialog.askopenfilename()
            state["lastOpenFilename"] = open_filename
            print(str(open_filename))
            image = helper.getImage(open_filename)
            helper.showInterface(image, "Open Image" + state['lastOpenFilename'],generateMenu(state))

        elif userInput.lower() == "s":   # To save image
            #tkinter.withdraw()
            save_filename = tkinter.filedialog.asksaveasfilename()
            state['lastSaveFilename'] = save_filename
            image = helper.saveImage(image, save_filename + ".jpg")
            helper.showInterface(image, state['lastOpenFilename'], generateMenu(state))

        elif userInput.lower() == "r":  # To Reload image
            image = helper.getImage(state['lastOpenFilename'])
            helper.showInterface(image, "Reload Image"+ state['lastOpenFilename'],generateMenu(state))

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)

        # When the mode is basic
        if state["mode"] == "basic":
            if userInput == "7":
                print("Log: Performing " + basic[int(userInput) - 1])
                state["mode"] = "advanced"
                helper.showInterface(image, "Advanced Mode" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "6":
                print("Log: Performing " + basic[int(userInput) - 1])
                image = manip.applyColdFilter(image)
                helper.showInterface(image, "Apply Cold Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "5":
                print("Log: Performing " + basic[int(userInput) - 1])
                image = manip.applyWarmFilter(image)
                helper.showInterface(image, "Apply Warm Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "4":
                print("Log: Performing " + basic[int(userInput) - 1])
                image = manip.applySepiaFilter(image)
                helper.showInterface(image, "Apply Sepia Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "3":
                print("Log: Performing " + basic[int(userInput) - 1])
                image = manip.applyBlueFilter(image)
                helper.showInterface(image, "Apply Blue Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "2":
                print("Log: Performing " + basic[int(userInput) - 1])
                image = manip.applyGreenFilter(image)
                helper.showInterface(image, "Apply Green Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "1":
                print("Log: Performing " + basic[int(userInput) - 1])
                image = manip.applyRedFilter(image)
                helper.showInterface(image, "Apply Red Filter" +
                                 state['lastOpenFilename'],generateMenu(state))

        else: # When the mode is advanced
            if userInput == "1":
                print("Log: Performing " + advanced[int(userInput) - 1])
                image = manip.rotateLeft(image)
                helper.showInterface(image, "Rotate Left" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "2":
                print("Log: Performing " + advanced[int(userInput) - 1])
                image = manip.rotateRight(image)
                helper.showInterface(image, "Rotate Right" +
                                 state['lastOpenFilename'], generateMenu(state))
            elif userInput == "3":
                print("Log: Performing " + advanced[int(userInput) - 1])
                image = manip.doubleSize(image)
                helper.showInterface(image, "Double Size" +
                                 state['lastOpenFilename'], generateMenu(state))
            elif userInput == "4":
                print("Log: Performing " + advanced[int(userInput) - 1])
                image = manip.halfSize(image)
                helper.showInterface(image, "Half Size" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "5":
                print("Log: Performing " + advanced[int(userInput) - 1])
                image = manip.locateFish(image)
                helper.showInterface(image, "Locate Fish" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "6":
                print("Log: Performing " + advanced[int(userInput) - 1])
                state["mode"] = "basic"
                helper.showInterface(image, "Basic Mode" +
                                 state['lastOpenFilename'],generateMenu(state))

    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)

    return image


# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = helper.getBlackImage(300, 200) # create a default 300 x 200 black image
helper.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")