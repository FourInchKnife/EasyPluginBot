from serverutils import TCPServer
from serverutils import Protocol_HTTP
from serverutils import URISterilizer
from serverutils import IncrediblySimpleWebSend

cogs=[] ## No cogs here.

def run(host,port,uristerilizerconfig,websendconfig):
    server=TCPServer(host,port)
    http=Protocol_HTTP()
    server.addProtocol(http)
    uristerilizer=URISterilizer(config=uristerilizerconfig)
    websend=IncrediblySimpleWebSend(config=websendconfig)
    server.addExtension(uristerilizer) ## Because of "hooks", this must be first. Consult Tyler Clarke (LinuxRocks2000, some may know him on Discord as weird_pusheen) for more information.
    server.addExtension(websend) ## Websender.
    server.start() ## Prime the server for run.
    while 1:
        server.iterate()
