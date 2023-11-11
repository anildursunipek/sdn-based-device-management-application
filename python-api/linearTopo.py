from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.topo import Topo, LinearTopo
from mininet.node import RemoteController
from mininet.log import setLogLevel
from mininet.cli import CLI

global net

def startNetwork(numberOfSwitches, numberOfHostsPerSwitch):
    global net
    topo = LinearTopo(numberOfSwitches,numberOfHostsPerSwitch)
    net = Mininet(topo=topo, build=False)

    remoteControllerIp = "127.0.0.1"
    # Adding floodlight controller here
    net.addController("c1", controller=RemoteController,switch=OVSSwitch, ip=remoteControllerIp, port=6653)

    net.build()
    net.start()
    print(net.hosts)
    print(type(net.hosts[0]))
    h1, h2 = net.getNodeByName('h1s1', 'h2s1')
    print(h1.IP())
    print(h1.MAC())
    print(h1.name)

    # result = net.iperf((h1,h2), l4Type='UDP')
    # print("sonuclar yazdi")
    # print(result)

    hosts = net.hosts
    print("TEST ---------> hostlar yazdirildi")
    result2 = net.iperf((hosts[0], hosts[1]), l4Type='UDP')
    print(result2)
    CLI(net)
    

def stopNetwork():
    global net
    net.stop()

if __name__ == "__main__":
    setLogLevel('info')
    startNetwork(1,2)
    stopNetwork()