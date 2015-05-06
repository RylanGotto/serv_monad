#!/usr/local/bin/python
import sendgrid
import socket
import time
import os





TEST_SERVER = "www.google.com"
HOME_SERVER = ""
def is_connected(server):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(server)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False



if __name__ == '__main__':
  os.system('terminal-notifier -title "Server Monitor Script" -message "Server status: Server monad is up and running, captian!"')
  sg = sendgrid.SendGridClient('', '')
  message = sendgrid.Mail(to='@gmail.com', subject='Server is down', html='', text='Server is down', from_email='@gmail.com')
  time.sleep(10)
  while True:
    if is_connected(TEST_SERVER):
      if not is_connected(HOME_SERVER):
        status, msg = sg.send(message)
        os.system('terminal-notifier -title "Server Monitor Script" -message "Server status: NO CONNECTION"')
      else:
        os.system('terminal-notifier -title "Server Monitor Script" -message "Server status: All systems are go, captian!"')
    time.sleep(300)
