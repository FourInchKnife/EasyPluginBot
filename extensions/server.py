from serverutils import TCPServer
from serverutils import Protocol_HTTP
from serverutils import URISterilizer
from serverutils import IncrediblySimpleWebSend

cogs=[] ## No cogs here.

class TheBotServer(TCPServer):
    def httprecieve(self,incoming): ## Here we can listen in on http messages, and be very very good at being very very good at things.
        print(incoming.rqstdt)

def run(host,port,uristerilizerconfig=None,websendconfig=None):
    server=TheBotServer(host,port,blocking=True)
    print("Made a server")
    http=Protocol_HTTP()
    print("Made an http")
    server.addProtocol(http)
    print("Added an http")
    uristerilizer=URISterilizer(config=uristerilizerconfig)
    print("Made a uristerilizer")
    websend=IncrediblySimpleWebSend(config=websendconfig)
    print("Made a websend")
    server.addExtension(uristerilizer) ## Because of "hooks", this must be first. Consult Tyler Clarke (LinuxRocks2000, some may know him on Discord as weird_pusheen) for more information.
    print("Added the uristerilizer")
    server.addExtension(websend) ## Websender.
    print("Added the websender")
    server.start() ## Prime the server for run.
    print("Primed server")
    while 1:
        server.iterate()
        print("Iterated server once")
