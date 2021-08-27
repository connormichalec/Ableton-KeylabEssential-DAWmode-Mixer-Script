![image](https://user-images.githubusercontent.com/35946564/131079986-c325c6cf-5632-4de7-904b-4e59ecd1a3c5.png)





# What is this
  A convenient feature that does not seem to be intergrated very well in a lot of MIDI controllers is Automapping/Device control in ableton; each track automatically assigns midi input to a specific parameter(when used in conjunction with instrument rack macros this leave a practically hands free ableton experience.) As an arturia keylab essential user, I have found it frustrating that the default DAW mode does not support this feature, while it is possible to create a custom User control script.txt such as this one: https://github.com/gaw1ik/Tuturial-Ableton-Blue-Hand-Device-Control-Using-Arturia-Keylab. While this does work, you have to switch the midi map to user mode, instead of using the DAW mode. The downside to this is that you will lose the ability to control ableton's session view like you can in DAW mode, which means switching back and forth between daw and user 1 when I want to select a track, then control it's parameters. The source of this issue is that Arturia's remote MIDI mapping python scripts were built this way, so there is no solution. However, thanks to the help of python's decompilable nature and github user gluon I have slightly edited these midi remote scripts to achieve what I am looking for. 

# What it does

Essentially the modified python scripts will now allow the encoders to act as device automap knobs(similar to what would happen in "device mode" on other controllers) I was also able to get this to work with the faders but have not figured out how to get them both to work in conjunction, so I have it so the faders still will control the mix levels in DAW mode. This is fine for me because all I want to use for parameters are the encoders, and 8 parameters+mod wheel is plenty per instrument, however feel free to check out the messy commented code if you would like get the faders working as well(plz pull request if u figure it out). 

# How

Unlike regular user scripts you will have to install decompiled and edited python scripts.

To do this navigate to your MIDI Remote Scripts directory. 
For me it's C:/User/blah/ProgramData\Ableton\Live poor version\Resources\MIDI Remote Scripts\Keylab_Essential

![image](https://user-images.githubusercontent.com/35946564/131079360-00e636bb-f8aa-48dc-9663-dcdcf56db3a6.png)


Make sure ableton is closed

Now (first download the .pys from this repo) for each .py that needs to be replaced, locate the default keylab_essential.pyc version of that file and replace it with the modified version. Make sure to delete the .pyc because I think python will use this as a dependency instead of the .py. Copy device.py,and device_parametres.py, they don't have a corresponding .pyc because are defaulty there.

reopen ableton, 
You should NOT have to select a new control surface, as you are just replacing the current one, however make sure the Keylab essential control surface is selected:

![image](https://user-images.githubusercontent.com/35946564/131077875-d6db1881-b4ce-4fc6-8846-313222031f31.png)

msg me on discord or create an issue or something if something doesnt work...


# Helpful things

Thanks to gaw1ik for creating the inspiration:
https://github.com/gaw1ik/Tuturial-Ableton-Blue-Hand-Device-Control-Using-Arturia-Keylab

Some things that I found helpful trying to do this:
https://github.com/gluon/AbletonLive10.1_MIDIRemoteScripts (The akai force MPC .py's were especially helpful because it is uses the classes i had to integrate)

https://stackoverflow.com/questions/4020027/debugging-python-within-ableton-live

https://github.com/CJmusic/MPK_CZ and his original video: https://youtu.be/uGUI_lbPTaE

https://anotherproducer.com/online-tools-for-musicians/midi-cc-list/ mainly to understand that arturia does not know how to make a midi device with a clean midi data layout

Absue the shit out of google

# Another thing

I commented out some modifications you can do and ugly annotations in the .py files so check those out if u want to modify the files further.
If you would like to change the sensitivity of the encoders, I believe in device.py you can just modify the param: default_encoder_sensitivity=1.0 


