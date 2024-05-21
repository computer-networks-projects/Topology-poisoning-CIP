#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

from mininet.topo import Topo

class Japan( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        s6 = self.addSwitch('s6', cls=OVSKernelSwitch)
        s9 = self.addSwitch('s9', cls=OVSKernelSwitch)
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch)
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch)
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch)
        s11 = self.addSwitch('s11', cls=OVSKernelSwitch)
        s8 = self.addSwitch('s8', cls=OVSKernelSwitch)
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
        s5 = self.addSwitch('s5', cls=OVSKernelSwitch)
        s10 = self.addSwitch('s10', cls=OVSKernelSwitch)
        s7 = self.addSwitch('s7', cls=OVSKernelSwitch)

        info( '*** Add hosts\n')
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)

        info( '*** Add links\n')
        self.addLink(s1, s6)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s3, s4)
        self.addLink(s1, s5)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s8, s9)
        self.addLink(s9, s10)
        self.addLink(s7, s11)
        self.addLink(s10, h1)
        self.addLink(s11, h1)
        self.addLink(s3, h2)
        self.addLink(s5, h2)

topos = { 'japan': ( lambda: Japan() ) }


