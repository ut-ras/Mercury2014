#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def talker():
    pub = rospy.Publisher('keypress', String)

    rospy.init_node('keyboard_driver')
    getch = _GetchUnix()

    while not rospy.is_shutdown():
        str = getch()
	if ord(str) == 3 : break;
	print str
        pub.publish(str)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
