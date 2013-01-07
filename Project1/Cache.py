'''
Created on 07/01/2013

@author: boni
'''
from PySFML import *


class Cache(object):
    '''
    classdocs
    '''
    _boat    = sf.Image()  #imagem do heroi
    _inimigo = sf.Image()  #imagem do inimigo 

    def __init__( self ):
        '''
        Constructor
        '''
        self._boat.LoadFromFile( "data/img/barco.png" )
        
    #__init()__
        