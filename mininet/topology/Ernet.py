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

class Ernet( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        s7 = self.addSwitch('s7', cls=OVSKernelSwitch)
        s5 = self.addSwitch('s5', cls=OVSKernelSwitch)
        s10 = self.addSwitch('s10', cls=OVSKernelSwitch)
        s6 = self.addSwitch('s6', cls=OVSKernelSwitch)
        s8 = self.addSwitch('s8', cls=OVSKernelSwitch)
        s15 = self.addSwitch('s15', cls=OVSKernelSwitch)
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch)
        s16 = self.addSwitch('s16', cls=OVSKernelSwitch)
        s14 = self.addSwitch('s14', cls=OVSKernelSwitch)
        s9 = self.addSwitch('s9', cls=OVSKernelSwitch)
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch)
        s13 = self.addSwitch('s13', cls=OVSKernelSwitch)
        s11 = self.addSwitch('s11', cls=OVSKernelSwitch)
        s12 = self.addSwitch('s12', cls=OVSKernelSwitch)
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch)

        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)

        self.addLink(s2, s1)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s4, s5)
        self.addLink(s3, s6)
        self.addLink(s1, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s9)
        self.addLink(s9, s10)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s10, s12)
        self.addLink(s1, s10)
        self.addLink(s10, s13)
        self.addLink(s11, s14)
        self.addLink(s14, s16)
        self.addLink(s14, s15)
        self.addLink(s1, s14)
        self.addLink(h1, s6)
        self.addLink(h1, s2)
        self.addLink(s15, h2)
        self.addLink(s12, h2)
        self.addLink(s7, h3)
        self.addLink(h3, s13)

topos = { 'ernet': ( lambda: Ernet() ) }
