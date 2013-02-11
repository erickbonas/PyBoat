'''
Created on 28/12/2012

@author: boni
'''
import os
#from PySFML import *
from Game import Game
import scenes
from scenes import SceneGame
'''
#Create the main window
window = sf.RenderWindow( sf.VideoMode( 800, 600 ), "ThunderBoat" )

#Create a graphical string to display
text = sf.String("Hello")
text.SetPosition( 0,0 )

thunder_boat_file_name = os.path.join("img","barco.png")

thunder_boat_image = sf.Image()
thunder_boat_image.LoadFromFile( thunder_boat_file_name )

thunder_boat = sf.Sprite( thunder_boat_image )

thunder_boat.SetPosition(400, 300)
thunder_boat.SetSubRect(sf.IntRect(192, 0, 288, 96))
thunder_boat.SetScale( 1, 1 )
elapsed_time = window.GetFrameTime()

# Start the game loop
running = True
while running:    
    event = sf.Event()
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False 
    
    
    if window.GetInput().IsKeyDown(sf.Key.A):
        thunder_boat.SetSubRect(sf.IntRect(96, 0,192, 96))
        thunder_boat.Move( -5, 0 )
        
    if window.GetInput().IsKeyDown(sf.Key.D):
        thunder_boat.SetSubRect(sf.IntRect(0, 0,96, 96))
        thunder_boat.Move( 5, 0)
        callable
    if window.GetInput().IsKeyDown(sf.Key.W):
        thunder_boat.SetSubRect(sf.IntRect(192, 0,288, 96))
        thunder_boat.Move( 0, -5 )
        
    if window.GetInput().IsKeyDown(sf.Key.S):
        thunder_boat.SetSubRect(sf.IntRect(288, 0,384, 96))
        thunder_boat.Move( 0, 5 )
   
    window.Clear()
    #window.Draw( text )
    window.Draw( thunder_boat )
    window.Display()  
''' 



def main():
    game  = Game()
    scene = SceneGame()
    game.change_scene( scene )
    game.loop()
# main()
    

if __name__ == '__main__':
    main()