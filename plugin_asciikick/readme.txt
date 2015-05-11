################################################################################
#
#	ASCIIKick
#	Plugin for B3 (www.bigbrotherbot.com)
#	(c) 2011 Dr_Z and http://www.secondmethods.com
#
#	This program is free software and licensed under the terms of
#	the GNU General Public License (GPL), version 2.
#
#	http://www.gnu.org/copyleft/gpl.html
#
#	Please note that use of this plugin is subject to the 
#	terms and conditions set out in the warranty disclaimer.
#
################################################################################

ASCIIKick version 1.0.1

##############################

Plugin Discription:
------------------------------
	This B3 3rd Party Plugin checks for NON-Printable ASCII / Unicode 
	Characters in a Client's(Player's) name. If Found, Kicks Client from server.

	It was Built on a Windows 7 Dedicated COD6 (MW2) Gaming server.
	This pluging might work with other B3 supported Game Servers.

	This plugin has not been tested on a Linux Game server but can't
	see why it shouldn't.

##############################

Requirements:
------------------------------
	Python v2.7+
		(note: may work with older versions of Python but has not been 
		 tested. Python 2.7+ was properly compiled with encodings to 
		 handle Uicode strings )

	B3 Version 1.4+

##############################

Installation:
------------------------------
	1. Place the 'asciikick.py' file in your '@b3/extplugins' directory
	   Place the 'asciikick.xml' file in your '@b3/extplugins/conf' directory.

	2. Open the 'asciikick.xml' file with your favorite editor and modify the settings.

	3. Open your 'B3.xml' file found in '@b3/conf' and add the next line in the
	   <plugins> section of the file:

		<plugin config="@b3/extplugins/conf/asciikick.xml" name="asciikick" />

##############################
#
# Changelog:
#
# 06-12-2011 v1.0.1
#	Fixed redundancy of code and added global variables
#
# 06-09-2011 v1.0.0
#	First Release
#
# 06-04-2011 v0.8b
#	Added support for B3 v1.6
#	Added ASCIIkick logging path variable to config settings.
#	The log file name is 'asciikick.log' and it is Disabled. 
#	To Enable it, You have to Set the Directory path in the Config file asciikick.xml
#
# 05-29-2011 v0.6b
#	Added Logging of Players Kicked sence B3 Database dose not recognise
#	non printable ASCII / Unicode characters in a Client's name.
#
# 05-28-2011 v0.5b
#	Fixed non existing attributtes for dump.event
#	Plugin works. Need to work on Config Announcement
#
# The Begining: 05-25-2011 v0.1b
#	Built a python Regular Expression to search a Player's name for Unicode characters.
#
##############################

WARRANTY DISCLAIMER:
------------------------------
This Plugin is provided "as is" and '2M'(secondmethonds.com) and the author (Dr_Z) of the plugin
(collectively '2M') make no warranties, express or implied including merchantability, fitness
for a particular purpose, title, non-infringement or any other warranty, condition, guarantee
or representation whether verbal, written or in electronic form, including but not limited to, 
the integrity of the plugin, the existence of bugs, viruses or other disabling devices, 
or the accuracy or completeness of any information contained therein. Your use of the plugin
is entirely at your own risk. '2M' will not be responsible to you or any third parties for any
direct or indirect, consequential, special or punitive damages or losses you may incur in 
connection with the plugin, your use of the plugin or any data or other materials generated 
from use of the plugin, regardless of the type of claim or the nature of the cause of action, 
even if '2M' has been advised of the possibility of such damage or loss.