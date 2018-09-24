from twisted.internet import reactor

def gotIP(ip):
    print("IP of 'example.com' is", ip)
    reactor.callLater(3, reactor.stop)

reactor.resolve('example.com').addCallback(gotIP)
reactor.run()