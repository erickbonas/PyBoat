'''
Created on 29/12/2012

@author: boni
'''
from PySFML import *


class Game:
    '''
    Classe responsável pelos eventos principais do jogo
    '''
    _window      = None
    _window_size = None
    _running     = None
    
    def __init__( self, size, name ):
        '''
        Constructor
        '''
        self._window = sf.RenderWindow( sf.VideoMode( size ), name )
        self._running = True
    #__init()__    
    
    def _handle_event(self):
        '''
        Tratas os eventos do jogo
        '''
        
        event = sf.Event()
        while event.Type == sf.Event.Closed:
            return False
    #handle_event
    def _objects_draw(self):
        pass
    
    def game_loop(self):
        '''
        Laço principal do jogo 
        '''
        while self._running:
            
            self.handle_event()
            
            self._window.Clear()
            self._window.Display()        
    
        
        
    
    