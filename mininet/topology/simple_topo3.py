"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )

        # Add links
        #self.addLink( h1, s1,params1={'ip': '10.2/8'},params2={'ip': '10.3/8'} )
        #self.addLink( h1, s2, params1={'ip': '10.4/8'},params2={'ip': '10.5/8'})
        self.addLink( h1, s1 )
        self.addLink( h1, s2 )
        self.addLink( s3, s2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
