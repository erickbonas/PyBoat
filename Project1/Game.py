# -*- coding: utf-8 _*_
'''
Created on 29/12/2012

@author: boni
'''
from PySFML import *
from cache import Cache

class Game:
    '''
    Classe responsável pelos eventos principais do jogo
    '''
    _window      = None
    _window_size = None
    _running     = None
    _cache_image = None
    
    def __init__( self, size, name ):
        '''
        Constructor
        '''
        self._window = sf.RenderWindow( sf.VideoMode( size[0], size[1] ), name )
        self._running = True
    #__init()__    
    
    def _handle_event(self):
        '''
        Tratas os eventos do jogo
        '''
        event = sf.Event()
        while self._window.GetEvent(event):
            if event.Type == sf.Event.Closed:
                self._running = False 
    #handle_event()
    
    def _objects_draw(self):
        pass
    
    def game_loop(self):
        '''
        Laço principal do jogo 
        '''
        
        #Cria o personagen
        while self._running:
            
            self._handle_event()
            
            self._window.Clear()
            self._window.Display()        
    
        
        
    
    