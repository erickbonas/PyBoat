

class Scene( object ):

    """
     

    :version:
    :author:
    """

    """ ATTRIBUTES

     

    game_pai  (private)

    """

    def __init__( self ):
        self._game = None
        
    
    
    def create( self, game ):        
        """
         

        @return  :
        @author
        """
        self._game = game
        pass

    def update( self ):
        """
         

        @return  :
        @author
        """
        pass

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
    

