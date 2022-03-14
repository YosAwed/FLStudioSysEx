# FLStudioSysEx
How to send System Exclusive command by using FL Studio
<img width="1920" alt="fl4" src="https://user-images.githubusercontent.com/4214168/158175316-37ef37cb-4ae0-4d72-8f8e-d6c6127bf046.png">

Basically I aligned with https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm

Please read "The basics of working with Script Files:"
According to this explanation, I made device_CASIO CTSV1000.py and put into \\Documents\Image-Line\FL Studio\Settings\Hardware\CASIO CTS1000V\

The Script set OnInit() for initialization. I put change Lylic Play Mode of CTS-1000V to "NOTE" from "Phrase(default)"

You may want to send SysEX every play cycle. For that purpose, it can use onUpdateBeatIndicator(), this can call every beat while playing.
