'''
Created on 29/12/2012

@author: boni
'''
from PySFML import *
import os

class GameObject(sf.Sprite):
    '''
    Classe responsavel por todos os objetos dentro do jogo
    '''
    
    _image = None
    def __init__(self, image, position, speed = None ):
        '''
        Inicializa um objeto dentro do jogo
        '''
        
        thunder_boat_file_name = os.path.join("img","barco.png")
        
        self._image = sf.Image()
        self._image .LoadFromFile( thunder_boat_file_name )
        
        #thunder_boat = sf.Sprite( self._image )
        sf.Sprite.__init__( self._image )
        #thunder_boat.SetPosition(400, 300)
        #thunder_boat.SetSubRect(sf.IntRect(192, 0, 288, 96))
        #thunder_boat.SetScale( 1, 1 )
        
    def draw(self):
        pass
    
    def set_position(self, position ):
        """
        Seta a posição do objeto
        """
        self.SetPosition( position )
    #set_position()