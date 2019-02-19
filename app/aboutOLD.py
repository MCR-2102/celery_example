import os
import grp
import datetime

__all__ = ['__version__', 'major', 'minor', 'patch', 'pre', '__version_string__']

major = 0
minor = 0
patch = 26

pre = '.1'

local = ''
primary_group = grp.getgrgid(os.getgid()).gr_name
if primary_group == 'progr':
	now = int(datetime.datetime.now().timestamp())
	local = '+build.{}'.format(now)

__author__ = 'your name'
__version__ = '{major}.{minor}.{patch}{pre}{local}'.format(**locals())

__version_string__ = str(major) + '.' + str(minor) + '.' + str(patch)
