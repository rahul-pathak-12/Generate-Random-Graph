from collections import defaultdict, deque
import random

class rdgraph():
    node_conn = defaultdict( list ) # data { 0: [1,2] }
    connections = []    # coordinates  = [ (1.1, 2.2, 1.5) ]
    coordinates = []    # connections  = [ (0, 1) ]

    def __init__( self, minR=1, maxR=11, minE =1, maxE=1, total_node=7 ):
        self.minR=minR
        self.maxR=maxR
        self.minE =minE
        self.maxE=maxE
        self.total_node = total_node
        self.nodes = list(range(0, total_node)) # [ 0, 1, 2 ] if total nodes = 3

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
            
            while(index< r_edges): # generate random nodes up till max
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

    def bfs( self, vS, vE ): 
            # For this we need a dictionary which keeps track of the path that has been visited
            # a queue for the the search. 
            # essentially the nodes we have visited
            dist = { vS: [vS] } # Populate the dict with the initial node and its cnxions
            q = deque() 
            q.append(vS)    # Create a que with the vStart node

            while len(q):   # While the que is greater than 0
                at = q.popleft() # get the left elem of the que 

                # loop through the connections that we popped { 1 : [0, 2] }
                for next in self.node_conn[at]:
                    if next not in dist:    # If the connection is not in the dict 
                                    # we add that new node to the dict with that node conxns
                        dist[next] = [ dist[at], next ]
                # we appendthe initial node we followed and the next node to be explored. 
                        q.append( next )
            # This is repeated until all connections this node is connected to are explored. 

            #pp(dist)
            # vE is the 
            if vE in dist: 
                return dist[ vE ]
            else: 
                return "NO PATH FOUND" 

x = rdgraph()
x.generate_graph()
print( x.visualise() )

path = x.bfs( 0, 2 )
print( path )