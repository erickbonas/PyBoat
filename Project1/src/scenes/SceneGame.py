from Scene import *
from Scene2 import *
from PySFML import *

class SceneGame (Scene):
    """
     

    :version:
    :author: boni
    """
    
    def create( self, game ):        
        """
         

        @return  :
        @author
        """
        self._game = game;
        self.text = sf.String("Hello")
        self.text.SetPosition( 0,0 )

    def update( self ):
        """
         

        @return  :
        @author
        """
        if self._game.get_window().GetInput().IsKeyDown(sf.Key.A):            
            self._game.change_scene(Scene2())
            return
        self._game.get_window().Clear()
        self._game.get_window().Draw( self.text )
        self._game.get_window().Display()
    #update()
        

    def destroy( self ):
        """
         

        @return  :
        @author
        """
        print("pinto")
        pass

    def notify_close(self):
        """
        Notifica a cena que ela foi fechada
        @return: void
        """
        self._game.change_scene( None )
