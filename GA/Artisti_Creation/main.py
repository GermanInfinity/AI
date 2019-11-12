#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 05:06:18 2019

@author: ugoslight

GA - Artist optimizer
"""

from Create_artist import Create_artist
from Display import Display

if __name__ == "__main__":
    
    
    """Create Artist"""
    artist_name = "Segun"
    ad = Create_artist(artist_name)
    
    """Display and assess creation"""
    a = Display.Display(artist_name, ad.script)

    #run_artist #See/Run the script produced