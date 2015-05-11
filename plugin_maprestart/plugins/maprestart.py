# Plugin for BigBrotherBot(B3) (www.bigbrotherbot.com)
# Copyright (C) 2009 Wright
# phenke@ku.edu
# www.eliteclangaming.com
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
#=============================================================================
#
# Objective: 
#
# The goal of this plugin is to automatically restart a map once the
# last client on the server disconnects. The main reason for this plugin is as 
# a work around for a glitch in Call of Duty 1's PAM mod v1.0.8 that results in
# the server getting stuck in loop where it cannot restart the map after players
# reconnect and the game timer has reached 0. The intent of this plugin is to 
# restart the map before this loop happens, placing it in ready-up mode where
# there is no danger of the loop occurring.
#
# Changelog:
#
# 12/04/2009 - 0.1.1 - Wright
# > First attempt
#
# 12/05/2009 - 0.1.2 - Wright
# > Incorporated code suggestion by Bakes.
# > Fixed tab issue that was resulting in crash.
#
# 12/06/2009 - 0.1.3 - Wright
# > Corrected the class name.
# > Added debug comments.
# > Added [requiresConfigFile = False] to the class since the plugin has no config and should not
# >> look for one.
# 
# 12/06/2009 - 0.2.0 - Wright
# > New minor version since it actually starts without crashing!
# > Removed an extra argument from the onStartup() function that was resulting in an infinite loop.
#
# 12/07/2009 - 1.0.0 - Wright
# > First public version released.
#
# 12/07/09 - 1.0.1 - Wright
# > Corrected spelling errors.
#

__version__ = '1.0.1'
__author__  = 'Wright'

import b3, thread, time, string
import b3 
import b3.events
import b3.plugin

#--------------------------------------------------------------------------------------------------

class MaprestartPlugin(b3.plugin.Plugin):
	requiresConfigFile = False

	def onStartup(self):
		self.registerEvent(b3.events.EVT_CLIENT_DISCONNECT)
		self.debug('Now monitoring the server for stalls...')

	def onEvent(self, event):
		if event.type == b3.events.EVT_CLIENT_DISCONNECT:
			if len(self.console.clients.getList()) == 0:
				self.console.say('Round in progress with no clients present. Restarting map...')
				time.sleep(1)
				self.console.write('map_rotate')
				self.debug('Server stall was imminent... the map was restarted.')

