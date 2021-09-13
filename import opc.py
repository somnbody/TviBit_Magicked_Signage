import opc
import time
    # Create a client object
client = opc.Client('10.80.31.22:7890')
    # Test if it can connect (optional)
if client.can_connect():
        print('connected to %s' % '10.80.31.22')
else:
        # We could exit here, but instead let's just print a warning
        # and then keep trying to send pixels in case the server
        # appears later
         print('WARNING: could not connect to %s' % '10.80.31.22')
    # Send pixels forever at 30 frames per second
while True:
         my_pixels = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
         if client.put_pixels(my_pixels, channel=0):
             print('...')
         else:
              print('not connected')
         time.sleep(1/30.0)