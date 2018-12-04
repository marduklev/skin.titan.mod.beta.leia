## -*- coding: utf-8 -*-
import xbmc
import xbmcvfs

trailerfilenamemp4 =  xbmc.getInfoLabel( "listitem.path" ) + xbmc.getInfoLabel( "listitem.FolderName" ) + "-trailer" + ".mp4"

if xbmcvfs.exists(trailerfilenamemp4):
    xbmc.executebuiltin( "SetProperty(trailer_avail,true,home)" )
else:
    pass