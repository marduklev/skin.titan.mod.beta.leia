## -*- coding: utf-8 -*-
import xbmc
import xbmcvfs
import xbmcgui

addon =  "current used skin script"
path =  xbmc.getInfoLabel( "listitem.path" )
name =  xbmc.getInfoLabel( "listitem.FolderName" )
trailer =  "-trailer"
extmp4 =  ".mp4"
filextnotmatter =  ".*"
# extesion =  ".mp4 | .avi | .mov | .mkv" - no idea how check diff filetypes atm,if even possible without extend the script
# windowprop = "trailer_avail"
##no name set need
test =  xbmc.getInfoLabel( "listitem.path" ) + xbmc.getInfoLabel( "listitem.FolderName" ) + "-trailer." + filextnotmatter
## use set name
trailerfilenameext = path + name + trailer + extmp4

#if xbmcvfs.exists(trailerfilename):
if xbmcvfs.exists(test):
    xbmc.executebuiltin( "SetProperty(trailer_avail,true,home)" )
else:
    pass