import os
from freeswitch import *

# HANGUP HOOK
#
# session is a session object
# what is "hangup" or "transfer"
# if you pass an extra arg to setInputCallback then append 'arg' to get that value
# 
# WARNING: known bugs with hangup hooks, use with extreme caution
def hangup_hook(session, what):

	consoleLog("info","hangup hook for %s!!\n\n" % what)
	return


# INPUT CALLBACK
#
# session is a session object
# what is "dtmf" or "event"
# obj is a dtmf object or an event object depending on the 'what' var.
# if you pass an extra arg to setInputCallback then append 'arg' to get that value
# def input_callback(session, what, obj, arg):
def input_callback(session, what, obj):

	if (what == "dtmf"):
		consoleLog("info", what + " " + obj.digit + "\n")
	else:
		consoleLog("info", what + " " + obj.serialize() + "\n")		
	return "pause"

# APPLICATION
#
# default name for apps is "handler" it can be overridden with <modname>::<function>
# session is a session object
# args is all the args passed after the module name
def handler(session, args):

	session.answer()
	session.setHangupHook(hangup_hook)
	session.setInputCallback(input_callback)
	session.execute("playback", session.getVariable("hold_music"))
