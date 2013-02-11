from Scene import *
from PySFML import *
from SceneGame import *

class Scene2 (Scene):
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
        self.text = sf.String("Hello2")
        self.text.SetPosition( 0,0 )

    def update( self ):
        """
         

        @return  :
        @author
        """
        if self._game.get_window().GetInput().IsKeyDown(sf.Key.S):            
            self._game.change_scene( SceneGame() )
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
        pass

    def notify_close(self):
        """
        Notifica a cena que ela foi fechada
        @return: void
        """
        self._game.change_scene( None )
