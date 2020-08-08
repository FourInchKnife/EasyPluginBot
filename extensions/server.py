from serverutils import TCPServer
from serverutils import Protocol_HTTP
from serverutils import URISterilizer
from serverutils import IncrediblySimpleWebSend

cogs=[] ## No cogs here.

class TheBotServer(TCPServer):
    def httprecieve(self,incoming): ## Here we can listen in on http messages, and be very very good at being very very good at things.
        print(incoming.rqstdt)

def run(host,port,uristerilizerconfig=None,websendconfig=None):
    server=None
    position=0
    while True:
        try:
            server=TheBotServer(host,port[position],blocking=False) ## Blocking only works in VERY specific use cases, ie, ones in which you want to make any other coders on the team lose several hours of sleep over this weird issue that keeps happening :)
            break
        except OSError:
            position+=1
    print("Server exists on port:",port[position])
    http=Protocol_HTTP()
    server.addProtocol(http)
    uristerilizer=URISterilizer(config=uristerilizerconfig)
    websend=IncrediblySimpleWebSend(config=websendconfig)
    server.addExtension(uristerilizer) ## Because of "hooks", this must be first. Consult Tyler Clarke (LinuxRocks2000, some may know him on Discord as weird_pusheen) for more information.
    server.addExtension(websend) ## Websender.
    server.start() ## Prime the server for run.
    while 1:
        server.iterate()
