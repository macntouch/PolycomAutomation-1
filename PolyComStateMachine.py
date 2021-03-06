#!/usr/bin/env python
###############################################################################
# This program is free software; you can redistribute it and/or modify it 
# under the terms of the GNU public license as published by the Free Software
# Foundation.
# 
# This program is distributed in the hopes that it will be useful but without 
# any warranty, even implied, of merchantability or fitness for a particular
# purpose.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Author Jeffrey McAnarney from U.S. 7/18/2013
###############################################################################


"""
VVX 400 Series
from active call:
    sk1=hold
        hold===>
            sk1=resume
            sk2=NewCall
            sk3=xfer
            sk4=more
                more===>
                sk1=conference
    sk2=end call
    sk3=xfer
        xfer===>
            sk2=cancel
            sk3=URL  (NOT SUPPORTED)
            sk4=more
                more===>
                    sk1=blind
                    sk2=directory
        sk1=conference
    sk4=more
        more===>
            sk1=conference
    
        



"""
"""
EXAMPLES OF STATES:
LineKeyNum : 1
LineDirNum : 5551111
LineState : Active
CallReference : dffd38
CallState : Connected
CallType : Outgoing
UIAppearanceIndex : 1*
CalledPartyName : 5552112
CalledPartyDirNum : sip:5552112@10.17.220.6
CallingPartyName : 5551111
CallingPartyDirNum : sip:5551111@10.17.220.6
CallDuration : 16
 
 
LineKeyNum : 1
LineDirNum : 5551112
LineState : Active
CallReference : 411cb1a0
CallState : Offering
CallType : Incoming
UIAppearanceIndex : 1*
CalledPartyName : 5551112
CalledPartyDirNum : sip:5551112@10.17.220.6
CallingPartyName : Maynard Keenan
CallingPartyDirNum : sip:5551111@10.17.220.6
CallDuration : 0
 
 
LineKeyNum : 1
LineDirNum : 5551111
LineState : Active
CallReference : dffd38
CallState : CallConfHold
CallType : Outgoing
UIAppearanceIndex : 0
CalledPartyName : 5552112
CalledPartyDirNum : sip:5552112@10.17.220.6
CallingPartyName : 5551111
CallingPartyDirNum : sip:5551111@10.17.220.6
CallDuration : 179
CallReference : e029c8
CallState : RingBack
CallType : Outgoing
UIAppearanceIndex : 1*
CalledPartyName : 5551112
CalledPartyDirNum : sip:5551112@10.17.220.6
CallingPartyName : 5551111
CallingPartyDirNum : sip:5551111@10.17.220.6
CallDuration : 0
 
 
LineKeyNum : 1
LineDirNum : 5551111
LineState : Active
CallReference : dffd38
CallState : CallConference
CallType : Outgoing
UIAppearanceIndex : 0
CalledPartyName : 5552112
CalledPartyDirNum : sip:5552112@10.17.220.6
CallingPartyName : 5551111
CallingPartyDirNum : sip:5551111@10.17.220.6
CallDuration : 198
CallReference : e029c8
CallState : CallConference
CallType : Outgoing
UIAppearanceIndex : 1*
CalledPartyName : 5551112
CalledPartyDirNum : sip:5551112@10.17.220.6
CallingPartyName : 5551111
CallingPartyDirNum : sip:5551111@10.17.220.6
CallDuration : 16
"""