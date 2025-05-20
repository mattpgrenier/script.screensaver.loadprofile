import xbmc
import xbmcaddon
#import xbmcgui

# Get the addon instance
addon = xbmcaddon.Addon(id='script.screensaver.loadprofile')

#Read the porifle name setting
profilename = addon.getSetting('profilename')

def loadprofile():
    if profilename:
        xbmc.executebuiltin(f'LoadProfile({profilename})')

if not xbmc.Player().isPlaying():
	loadprofile()
