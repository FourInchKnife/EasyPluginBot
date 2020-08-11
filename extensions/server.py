from serverutils import TCPServer
from serverutils import Protocol_HTTP
from serverutils import URISterilizer
from serverutils import IncrediblySimpleWebSend
from serverutils import SimpleGzipper
from serverutils import PyHP


cogs=[]

class TheBotServer(TCPServer):
    def inittasks(self):
        self.authed="<!DOCTYPE html><html>Visit <a href='auth'>here</a> to add a name!</html>"
    def httprecieve(self,incoming): ## Here we can listen in on http messages, and be very very good at being very very good at things.
        print(incoming.rqstdt)

def run(host,port,serveron,run,eventualport,uristerilizerconfig=None,websendconfig=None):
    server=None
    position=0
    while True:
        try:
            server=TheBotServer(host,port[position],blocking=False) ## Blocking only works in VERY specific use cases, ie, ones in which you want to make any other coders on the team lose several hours of sleep over this weird issue that keeps happening :)
            break
        except OSError:
            position+=1
    print("Server exists on port:",port[position])
    eventualport.value=port[position]
    http=Protocol_HTTP()
    server.addProtocol(http)
    uristerilizer=URISterilizer(config=uristerilizerconfig)
    pyhp=PyHP(config={})
    websend=IncrediblySimpleWebSend(config=websendconfig)
    gzipper=SimpleGzipper()
    server.addExtension(uristerilizer) ## Because of "hooks", this must be first. Consult Tyler Clarke (LinuxRocks2000, some may know him on Discord as weird_pusheen) for more information.
    server.addExtension(gzipper) ## This will probably break if you add it before uristerilizer, because it uses the sterilized URI's. For more information on this logic, console Tyler Clarke (read the comment one line up)
    server.addExtension(pyhp) ## Python pHP. (Acronym). As usual, this one requires sterilized URI's, and Gzipper messes up PyHP messages, because it tries to index them and then edits the uri - so the python reader craps up.
    server.addExtension(websend) ## Websender.
    server.start() ## Ready the server for running. Although nothing serious (I think) requires this, its still a really good idea to do this.
    serveron.value=1
    try:
        while run.value:
            server.iterate()
    except:
        pass
    finally:
        serveron.value=0
