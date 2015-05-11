#
# ASCII KICK Plugin for BigBrotherBot(B3) (www.bigbrotherbot.net)
# Copyright (C) 2011 Dr_Z
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
# ***** Special Note *****
# ***** Please Read  *****
#	Requierments: Python v2.7+ and B3 v1.4+
#	This Plugin may work with older versions of Python but it has not been tested.
#	ASCIIkick Plugin was built and tested in a Windows OS evironment for a dedicated
#	COD6 (MW2) Game Server.
#
# Changelog:
#
# 06-12-2011 v1.0.1
#   Fixed redundancy of code and added global variables
#
# 06-09-2011 v1.0.0
#	First Release
#
# 06-04-2011 v0.8b
#	Added support for B3 v1.6
#	Added ASCIIkick logging path variable to config settings
#	The log file name is 'asciikick.log' and it is Disabled by default. 
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
#   Built a python Regular Expression to search a Player's name for Unicode characters.
#

__author__	= 'Dr_Z'
__version__	= '1.0.1'
__date__	= '2011-06-12'

import b3, re, time, sys
import b3.events
import b3.plugin

timekick = time.asctime(time.localtime(time.time()))

class AsciikickPlugin(b3.plugin.Plugin):
    def onStartup(self):        

        # Get the admin plugin so we can register commands
	    # ** This is for future updates
        self._adminPlugin = self.console.getPlugin('admin')
 
        if not self._adminPlugin:
            # something is wrong, can't start without admin plugin
            self.error('Could not find admin plugin')
            return

        # Register events on client's connection
        self.verbose('Registering events')
        self.registerEvent(b3.events.EVT_CLIENT_CONNECT)

    def onLoadConfig(self):
        # Loading config file vars
        self.verbose('Loading config')
        try:
            self.kicknick = self.config.get('settings', 'kicknick') 
        except:
            self.kicknick = 0
            self.debug('Default value (%i) for settings::kicknick', self.kicknick)

        try:
            self.announce = self.config.get('settings', 'announce') 
        except:
            self.announce = 0
            self.debug('Default value (%i) for settings::announce', self.announce)

        try:
            self.logpath = self.config.get('settings', 'logpath')
        except:
            self.logpath = 0
            self.debug('Logging Disabled')

        return

    def onEvent(self, event):
        if (event.type == b3.events.EVT_CLIENT_CONNECT):
            isName = event.client.exactName
            isFound = '0'
	        # RegExp Search for Non Printable Ascii and Unicode Characters in Client's Name
            isFound = re.search('[\x80-\xff]', isName)

	        # If Client Name returns NULL :  Just Kick Them
            if (isName == ""):
                isName = 'NULL'
                admin_name = 'SYSTEM'
                reason2kick = '^2 NO NAME VALUE'
                #event.client.kick(reason=reason2kick, silent=True)
                self.console.kick(event.client.cid, reason2kick, None, True)

                # If Logging is Enabled, Make/Append Log File 'asciikick.log'
                if (self.logpath > 0):
                    # Log all Illegal Client Names sence B3 database can't handle Non printable ASCII and Unicode characters
                    #
                    filelog = ('%s%s' % tuple([self.logpath, 'asciikick.log']))
                    self.debug('opening asciikick.log file')
                    f = open(filelog, "a")
                    f.write('%s :: Admin: %s :: Player Kicked: %s :: Player IP: %s :: CLient guid: %s \n' % tuple([timekick, admin_name, isName, event.client.ip, event.client.guid]))
                    f.close()
                    #
                    # END Logging of Kicked Player
                    return
                return
	    
            if (self.kicknick and isFound != None):
                # Non Printable ASCII / Unicode Characters Found in Clients Name
                # Kick Client Command in process
                reason2kick = '^2 ILLEGAL ASCII-Unicode Characters in Name'
                event.client.kick(reason=reason2kick, silent=True)
		
                if len(self.announce)  > 0:
                    # Variables passed to the config file for useage
                    # **  Needs Work to fire Config file to Announce what happend to Client **
                    admin_name = 'SYSTEM'
                    variables = {
                                'name' : isName,
                                'ip' : event.client.ip,
                                'id' : event.client.id,
                                'guid' : event.client.guid,
                                'pbid' : event.client.pbid,
                                'adminname' : admin_name,
                                'reason' : reason2kick
                     }
                message = b3.functions.vars2printf(self.announce)

                # If Logging is Enabled, Make/Append Log File 'asciikick.log'
                if (self.logpath > 0):
                    # Log all Illegal Client Names sence B3 database can't handle Non printable ASCII and Unicode characters
                    #
                    filelog = ('%s%s' % tuple([self.logpath, 'asciikick.log']))
                    self.debug('opening asciikick.log file')
                    f = open(filelog, "a")
                    f.write('%s :: Admin: %s :: Player Kicked: %s :: Player IP: %s :: CLient guid: %s \n' % tuple([timekick, admin_name, isName, event.client.ip, event.client.guid]))
                    f.close()
                    #
                    # END Logging of Kicked Player
                    return
                return
    	    else:
                # No attributes to dump onEvent -- Just return to b3 #
                return
        else:
	        return
        return