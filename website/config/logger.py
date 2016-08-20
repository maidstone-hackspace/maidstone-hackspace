import os 
import logging

log = logging.getLogger('Maidstone Hackspace')
log.setLevel(logging.DEBUG)
#~ log.propagate = False
if os.path.exists('/tmp/maidstone_hackspace.log'):
    ch = logging.FileHandler('/tmp/maidstone_hackspace.log')
    ch.setLevel(logging.DEBUG)
    log.addHandler(ch)
