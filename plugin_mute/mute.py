#Set the command level on line 21. Should be fairly obvious.

__version__ = '1.0'
__author__  = 'Spoon'

import b3
import b3.events
# Import the necessary libaries you need here, for example, I need random for the randomization of answers part of it.

#--------------------------------------------------------------------------------------------------
#This lot doesn't need to be changed for simple commands, it gets the admin plugin and registers commands.
class MutePlugin(b3.plugin.Plugin):
    _adminPlugin = None
    requiresConfigFile = False

    def onStartup(self):  
        self._adminPlugin = self.console.getPlugin('admin')  
        if not self._adminPlugin:  
            return False  
        #SET COMMAND LEVEL HERE
        self._adminPlugin.registerCommand(self, 'mute', 100, self.cmd_mute)
        self.registerEvent(b3.events.EVT_CLIENT_SAY)  
        self.registerEvent(b3.events.EVT_CLIENT_TEAM_SAY)  
        self.registerEvent(b3.events.EVT_CLIENT_AUTH)  
  
    def onEvent(self, event):  
        if event.type == b3.events.EVT_CLIENT_AUTH:  
            event.client.setvar(self, 'muted', 0)
        elif event.type == b3.events.EVT_CLIENT_SAY or event.type == b3.events.EVT_CLIENT_TEAM_SAY:  
            if event.client.var(self, 'muted', 0).value == 1:  
                self._adminPlugin.warnClient(event.client, 'You are not allowed to talk', None, False, '', 1)  
            else:  
                return False

    def cmd_mute(self, data, client=None, cmd=None):
        """\
        <player> <on/off> - mute/unmute a player
        """
        # this will split the player name and the message
        input = self._adminPlugin.parseUserCmd(data)
        if input:
            # input[0] is the player id
            sclient = self._adminPlugin.findClientPrompt(input[0], client)
            if not sclient:
                # a player matchin the name was not found, a list of closest matches will be displayed
                # we can exit here and the user will retry with a more specific player
                return False
        else:
            client.message('^7Invalid data, try !help mute')
            return False
    
        if not len(input[1]):
            client.message('^7Missing data, try !help mute')
            return False
        
        m = input[1]
        if m in ('on','1'):
            sclient.message('^3You are now muted, shut up!')
            client.message('^3%s ^1MUTED^3!' % sclient.exactName)
            sclient.var(self, 'muted', 0).value = 1
        elif m in ('off', '0'):
            sclient.message('^3You have been unmuted!')
            client.message('^3%s ^2UNMUTED^3!' % sclient.exactName)
            sclient.var(self, 'muted', 0).value = 0
        else:
            client.message('^7Invalid or missing data, try !help mute')