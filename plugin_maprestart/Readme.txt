Maprestart Plugin (v1.0.1) for BigBrotherBot(B3) (www.bigbrotherbot.com)

Copyright (C) 2009 Wright
phenke@ku.edu (mailto:phenke@ku.edu)

www.eliteclangaming.com

=============================================================================
This program is free software and licensed under the terms of
the GNU General Public License (GPL), version 2.

(http://www.gnu.org/copyleft/gpl.html)
=============================================================================
DESCRIPTION:

The goal of this plugin is to automatically restart a map once the last 

client on the server disconnects. The main reason for this plugin is as a

work around for a glitch in Call of Duty 1's PAM mod v1.0.8 that results in

the server getting stuck in loop where it cannot restart the map after

players reconnect and the game timer has reached 0. The intent of this plugin

is to restart the map before this loop happens, placing it in ready-up mode

where there is no danger of the loop occurring. It can probably be adapted to

handle similar issues in other games/mods.

=============================================================================
REQUIREMENTS:

This plugin most likely works in most circumstances but it has only been
tested for Call of Duty(1.5b) with B3(v1.2.1). As long as the game reports

disconnects in the log, it should work.
=============================================================================

INSTALLATION:

1. Place maprestart.py in the plugins folder. (.../b3/plugins/)
2. Open the B3.xml file (.../b3/conf/b3.xml) and add the following line to
the <plugins> section of the file:
<plugin name="pingkicker" priority="10"/>
3. Restart B3 and it should begin monitoring the server for round stalls.


Note: The priority number can be set to anything you wish although I would

recommend using the highest unused priority number.
=============================================================================

CHANGELOG:


12/04/2009 - 0.1.1 - Wright

> First attempt

12/05/2009 - 0.1.2 - Wright

> Incorporated code suggestion by Bakes.

> Fixed tab issue that was resulting in crash.



12/06/2009 - 0.1.3 - Wright

> Corrected the class name.

> Added debug comments.

> Added [requiresConfigFile = False] to the class since the plugin has no 
>>config and should not look for one.
 


12/06/2009 - 0.2.0 - Wright

> New minor version since it actually starts without crashing!

> Removed an extra argument from the onStartup() function that was resulting
in an infinite loop.

12/07/2009 - 1.0.0 - Wright
> First public version released.



12/07/09 - 1.0.1 - Wright

> Corrected spelling errors.

=============================================================================