import zmq

def create_zmq_context():
      return zmq.Context()
  
def create_socket(context, socket_type, bind_addr=None, connect_addr=None):
    socket = context.socket(socket_type)
    if bind_addr:
        socket.bind(bind_addr)
    if connect_addr:
        socket.connect(connect_addr)
    return socket