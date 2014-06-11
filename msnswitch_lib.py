# Copyright (C) 2014 by Ralph Bearpark.
# Contact: <http://www.bearpark.ch/who/ralph/>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
MSNSwitch Power Switcher
========================

:Author: Ralph Bearpark
:Contact: mailto:ralph@bearpark.ch
:Version: 1.0
:Copyright: |copy| 2014 by Ralph Bearpark

This class provides an API to the MSNSwitch internet-connected 
remote-control power socket. ( http://www.brack.ch/remote-control-switch-191491 )
"""

import urllib2, base64
from xml.dom import minidom


class msnswitch:

    def __init__( self, ipaddr, username, password ):
        self.ipaddr = ipaddr
        self.username = username
        self.password = password
        self.authstr = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

    def sendCommand( self, outlet, command ):
        """ Sends a command for the given socket

        :param outlet: 0 for all outlets; 1 for socket #1; 2 for socket #2
        :type outlet: int
        :param command: 0 for OFF; 1 for ON; 2 for switching; 3 for reset; 4 for UIS ON; 5 for UIS OFF
        :type command: int
        
        :returns: status of switch as a whole, and of outlet1 and outlet2
        :rtype: tuple of ints

        Example Usage::

            import msnswitch_lib
            m=msnswitch_lib.msnswitch("1.2.3.4","admin","1234")
            m.sendCommand(1,1)
            =>
            (0, 1, 0)
        """
        request = urllib2.Request("http://%s/outlet2.cgi?user=%s&password=%s&outlet=%s&command=%s"
                                   % (self.ipaddr, self.username, self.password, outlet, command ) )
        request.add_header("Authorization", "Basic %s" % self.authstr)
        result = urllib2.urlopen(request)
        xmldoc = minidom.parseString(result.read())
        outlet1_status = int(xmldoc.getElementsByTagName('outlet1_status')[0].childNodes[0].data)
        outlet2_status = int(xmldoc.getElementsByTagName('outlet2_status')[0].childNodes[0].data)
        uis_status     = int(xmldoc.getElementsByTagName('uis_status')[0].childNodes[0].data)
        return ( uis_status, outlet1_status, outlet2_status )

    def setOutlet( self, outlet, state ):
        """ Set the given outlet to the desired state

        :param outlet: 1 for socket #1; 2 for socket #2
        :type outlet: int
        :param state: 0 for OFF; 1 for ON
        :type state: int

        :returns: True if the desired state was reached; otherwise False
        :rtype: bool

        Example Usage::
        
            import msnswitch_lib
            m=msnswitch_lib.msnswitch("1.2.3.4","admin","1234")
            m.setOutlet(1,1)
            =>
            True
        """

        retval = False
        if (outlet in (1,2)) and (state in (0,1)):
            response=self.sendCommand( outlet, state )
            if response[outlet] == state:
                retval = True
        return retval

    def setOutletOn( self, outlet ):
        """ Switch the given outlet ON

        :param outlet: 1 for socket #1; 2 for socket #2
        :type outlet: int

        :returns: True if the outlet was switched on successfully; otherwise False
        :rtype: bool

        Example Usage::

            import msnswitch_lib
            m=msnswitch_lib.msnswitch("1.2.3.4","admin","1234")
            m.setOutletOn(1)
            =>
            True
        """
        return self.setOutlet( outlet, 1 )

    def setOutletOff( self, outlet ):
        """ Switch the given outlet OFF

        :param outlet: 1 for socket #1; 2 for socket #2
        :type outlet: int 

        :returns: True if the outlet was switched off successfully; otherwise False
        :rtype: bool

        Example Usage::

            import msnswitch_lib
            m=msnswitch_lib.msnswitch("1.2.3.4","admin","1234")
            m.setOutletOff(1)
            =>
            True
        """
        return self.setOutlet( outlet, 0 )
