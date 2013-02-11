'''
Created on 07/01/2013

@author: boni
'''

from GameObject import *
from PySFML import *
class Hero(GameObject):
    '''
    classdocs
    '''
    
    _image_name = "barco.png"

    def __init__( self, image, position, speed = None ):
        '''
        Constructor
        '''
        
        GameObject.__init__( self, image, position, speed = None )
        self.SetSubRect( sf.IntRect( 192, 0, 288, 96 ) )
        self.SetScale( 1, 1 )