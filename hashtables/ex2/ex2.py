class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
# dictionary
d = {}
# recursive helper func
def link(arr):
    # next = lass source added to arr's destination
    next = str(d[arr[-1]])
    # if that destination is 'NONE' return
    if next == 'NONE': return arr + [next]
    # else keep looping
    else: return link(arr + [next])
# main func    
def reconstruct_trip(tickets, length):
    # for src and destination create a key, value pair in dict
    for i in tickets: d.update( {str(i.source) : str(i.destination)} )
    # return the linked pairs starting at src 'NONE'
    return link([d['NONE']])