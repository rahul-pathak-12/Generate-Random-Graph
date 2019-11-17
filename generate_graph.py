from collections import defaultdict
import random

class rdgraph():
    node_conn = defaultdict( list )
    connections = []
    coordinates = []

    def __init__( self, minR=1, maxR=11, minE =1, maxE=1, total_node=7 ):
        self.minR=minR
        self.maxR=maxR
        self.minE =minE
        self.maxE=maxE
        self.total_node = total_node
        self.nodes = list(range(0, total_node))

    def generate_weight( self ):
        x = round( random.uniform(self.minR, self.maxR), 2 )
        y = round( random.uniform(self.minR, self.maxR), 2 )
        z = round( random.uniform(self.minR, self.maxR), 2 )
        return ( x, y, z )

    def generate_graph( self ):
        node_n = 0
        
        while( node_n < self.total_node ):
            node_list = []
            r_edges = random.randint( self.minE, self.maxE  )
            index = 0
            
            while(index< r_edges):
                random_weight = self.generate_weight()
                random_node = random.randint(0, self.total_node-1)

                if random_node not in node_list and self.nodes[node_n] != self.nodes[random_node]:
                    node_list.append( self.nodes[random_node] )
                    self.coordinates.append( random_weight )
                    self.connections.append( ( self.nodes[node_n], self.nodes[random_node] ) )
                    self.node_conn[ self.nodes[node_n]].append( self.nodes[random_node] )
                    index += 1
            node_n += 1

    def visualise( self ):
        for x in self.coordinates:
            print( str(x[0]) +","+ str(x[1]) +","+ str(x[2]) )
        for y in self.connections: 
            print( str(y[0]) +","+ str(y[1]) )
        print( self.node_conn )

x = rdgraph()
x.generate_graph()
print( x.visualise() )