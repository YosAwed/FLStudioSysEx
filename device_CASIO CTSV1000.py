# name=CASIO CTS-1000V

"""
[[
	Surface:	CTS-1000V
	Developer:	CASIO
	Version:	Beta 1.0
	Date:		13/3/2022

]]
"""

import time
import midi
import ui
import sys
import mixer
import transport
import channels
import playlist
import patterns
import device

SYS_BEGIN=[0xF0,0x44,0x7E,0x7F,0x7F,0x06,0x00,0x00,0x00,0x01]
SYS_NOTE=[0x00]
SYS_PHASE=[0x01]
SYS_END=[0xF7]

#----------------------------------------------------------------------------------------

# Function called when FL Studio is starting

def OnInit():
    print('Loaded MIDI script for CASIO CTS-1000V')
    print('SysEx send')
    msg= SYS_BEGIN+SYS_NOTE+SYS_END #concat data to Note Mode
    device.midiOutSysex(bytes(msg)) #send sysex    
    print('SysEx send end')


# Handles the script when FL Studio closes

def OnDeInit():
    return
        
  
# Function called when Play/Pause button is ON

def OnUpdateBeatIndicator(value):
    print('SysEx send on Update')
#    msg= SYS_BEGIN+SYS_NOTE+SYS_END #concat data to Note Mode
#    device.midiOutSysex(bytes(msg)) #send sysex
