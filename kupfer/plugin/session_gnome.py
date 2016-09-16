__kupfer_name__ = _("GNOME Session Management")
__kupfer_sources__ = ("GnomeItemsSource", )
__description__ = _("Special items and actions for GNOME environment")
__version__ = "2009-12-05"
__author__ = "Ulrik Sverdrup <ulrik.sverdrup@gmail.com>"

from kupfer.plugin import session_support as support
import os
import pwd

username = pwd.getpwuid(os.getuid())[0]
# sequences of argument lists
LOGOUT_CMD = (["gnome-session-quit --logout --no-prompt"])

SHUTDOWN_CMD_OLD = (["/home/" + username + "/scripts/shutdown2.sh"])
SHUTDOWN_CMD = (["/home/" + username + "/scripts/shutdown.sh"])

SUSPEND_CMD_OLD = (["/home/" + username + "/scripts/suspend.sh"])
SUSPEND_CMD = (["/home/" + username + "/scripts/suspend.sh"])

LOCKSCREEN_CMD = (["/home/" + username + "/scripts/lockscreen.sh"])

HIBERNATE_CMD = (["/home/" + username + "/scripts/hibernate.sh"])

REBOOT_CMD_OLD = (["/home/" + username + "/scripts/reboot.sh"])
REBOOT_CMD = (["/home/" + username + "/scripts/reboot.sh"])

class GnomeItemsSource (support.CommonSource):
	def __init__(self):
		support.CommonSource.__init__(self, _("GNOME Session Management"))
	def get_items(self):
		return (
			support.Logout(LOGOUT_CMD),
			support.LockScreen(LOCKSCREEN_CMD),
			support.Shutdown(SHUTDOWN_CMD),
			support.Hibernate(HIBERNATE_CMD),
			support.Suspend(SUSPEND_CMD),
			support.Reboot(REBOOT_CMD),
			support.Restart(REBOOT_CMD),
		)

