# -*- coding: utf-8 -*-
from PySFML import *

class Game(object):

    """
     

    :version: 2.0
    :author: Boni
    """

    """ ATTRIBUTES

     

    cena_atual  (private)

    """
    
    def __init__( self ):
        self._current_scene = None
        #Create the main window
        self._window = sf.RenderWindow( sf.VideoMode( 800, 600 ), "ThunderBoat" )
    #__init()__
        
    def get_window( self ):
        """
        Método responsável por pegar a janela do game
        """
        return self._window
    
    
    def change_scene( self, new_scene ):
        """
        Muda a cena do jogo
        @param Scene new_scene : Nova Cena a ser criada
        @return  :
        @author
        """
        self._current_scene = new_scene
    #change_scene()
    
    
    def loop( self ):
        """
         
        Loop principal do jogo
        @return  :
        @author
        """
        while ( self._current_scene != None ):
            self._current_scene.create( self )
            scene = self._current_scene
            while ( scene == self._current_scene ):
                self._current_scene.update()
                event = sf.Event()
                while self._window.GetEvent(event):
                    if event.Type == sf.Event.Closed:                        
                        self._current_scene.notify_close()
            scene.destroy()
    #loop()



