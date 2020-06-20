import pygame, random, time, webbrowser, os #modules required in here
pygame.init()#Initialising pygame window
clock = pygame.time.Clock()#Initialising clock
image = pygame.image.load('background.jpg')#Initialising the blue background
image2 = pygame.image.load('cap.jpg')#Initialising Captain America image
screen = pygame.display.set_mode((626, 417))#Setting the length and width of the pygame window
white = (255, 255, 255)#Initialising the colours used here
black = (0, 0, 0)
red = (255, 0, 0)
myFont = pygame.font.SysFont("Times New Roman", 25)#Initialising the font
music = [#Making a list of the music used later for relaxing
'https://www.youtube.com/watch?v=pAgnJDJN4VA',#BACK IN BLACK by AC/DC
'https://www.youtube.com/watch?v=LOZuxwVk7TU',#TOXIC by Britney Spears
'https://www.youtube.com/watch?v=Ihjx3mX75y8',#IMMIGRANT SONG by Led Zeppelin
'https://www.youtube.com/watch?v=7wtfhZwyrcc',#BELIEVER by Imagine Dragons
'https://www.youtube.com/watch?v=JGwWNGJdvx8',#SHAPE OF YOU by Ed Sheeran
'https://www.youtube.com/watch?v=60ItHLz5WEA',#FADED by Alan Walker
'https://www.youtube.com/watch?v=pRpeEdMmmQ0',#WAKA WAKA by Shakira
'https://www.youtube.com/watch?v=ttwJbTLLyXI']#SENORITA by Donald Trump
def clrscr():#A function which gets rid of everything and just gives us the blue background
    screen.blit(image,(0,0))
    pygame.display.update()
def studytime():#THE MAIN FUNCTION
    clrscr()#TO FILL THE BACKGROUND WITH THE COLOUR
    studytext = myFont.render(str('What\'s your productivity goal?'), 1, white)#Renders the text within quotes in the window
    screen.blit(studytext,(100,100))#Displays the above text
    pygame.display.update()#To refresh the screen
    study = float(input("Enter in Minutes"))#To get input from user in command prompt/terminal
    seconda = study * 60#converts the input into seconds
    clrscr()#Again clearing the screen to get rid of the question
    time.sleep(seconda)#This is a function to halt the program for the given number of seconds in brackets
    print('Time is up!')#This is here in case of any lags
    clrscr()#Again clearing the screen jusst in case
    screen.blit(image2, (0, 0))#Displaying CAPTAIN AMERICA
    captext1 = myFont.render(str('So, you have finished being productive.'), 10, red)#Rendering Cap's speech
    captext2 = myFont.render(str('You wanna relax.'), 2, red)
    captext3 = myFont.render(str('Believe me, I know how it feels'), 2, red)
    captext4 = myFont.render(str('Here\'s a song for you!'), 2, red)
    screen.blit(captext1, (1, 10))#displaying Cap's speech
    screen.blit(captext2,(1, 40))
    screen.blit(captext3,(1, 70))
    screen.blit(captext4,(1, 100))
    pygame.display.update()#updating the display because we have made changes
    x = random.choice(music)#the random.choice(music)assigns any one of the above links to x
    webbrowser.open(x, new=2)#Opening the browser and opening the link in x
    time.sleep(270)#Waits until the song is over
    browserExe = "chrome.exe"#Closes the browser using os module
    os.system("taskkill /f /im "+browserExe)
run = True
while run:#The infinite loop of this life/this project
    studytime()
    pygame.display.update()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#If we press X button, it gets closed!
            run = False
