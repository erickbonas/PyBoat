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
    
    _position_x    = None   #posição x do objeto
    _position_y    = None   #posição y do objeto
    _direction     = None   #direção do objeto
    _speed         = None   #velocidade do objeto
    _object_sprite = None   #imagem do objeto
    
    def __init__( self, image ):
        '''
        Inicializa um objeto dentro do jogo
        '''
        self._position_x = 0
        self._position_y = 0
        self._object_sprite = sf.Sprite( image )
        
    #__init()__        
    
    
    def set_position( self, position ):
        """
        Seta a posição do objeto
        """
        self.SetPosition( position )
    #set_position()