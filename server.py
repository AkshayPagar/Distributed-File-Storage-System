from concurrent import futures
import time
import logging
from activeNodes import activeNodes
from threading import Thread
import sys
import grpc
from NodePing import Heartbeat
from FileOperations import FileService
sys.path.append('./Gen')
import heartbeat_pb2
import heartbeat_pb2_grpc
import fileService_pb2
import fileService_pb2_grpc
from leaderbackground import TestObj

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
activeNodeObj= activeNodes()

"""
Thread function to check Leader
"""
mainLeader = None
def threaded_function(a):
    global mainLeader
    print("Argument",a)
    port = ""
    partners = ["127.0.0.1:2000","127.0.0.1:2100"]
    self_node = '127.0.0.1:2200'
    o = TestObj(self_node, partners)
    n = 0
    old_value = -1
    while True:
        
        #print('Current Counter value:', old_value)
        print(" is Leader : ",mainLeader)
        time.sleep(0.5)
        if o.getCounter() != old_value:
            old_value = o.getCounter()
            print('Current Counter value:', old_value)
        if o._getLeader() is None:
            mainLeader = self_node
            continue
        
        # if n < 2000:
        if n < 20: 
            if (port == 2000):
                o.addValue(10, n)
        n += 1
        #if n % 20 == 0:
        print("thread function-----"+o._getLeader())
        mainLeader = o._getLeader()



def serve():
    global mainLeader
    cmd_host = "127.0.0.1"
    serverAddress= cmd_host+':'+sys.argv[1]
    print("Server started on" +  sys.argv[1])
    
    leader=None
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000))
    if mainLeader is not None and cmd_host==mainLeader.split(":")[0]:
        leader=True
    else:
        leader=False
    # if sys.argv[1] != str(3000):
    #     leader=False
    
    heartbeat_pb2_grpc.add_HearBeatServicer_to_server(Heartbeat(), server)
    fileService_pb2_grpc.add_FileserviceServicer_to_server(FileService(leader, serverAddress, activeNodeObj), server)
    server.add_insecure_port('127.0.0.1:'+sys.argv[1])
    #time.sleep(30)
    print("Current leader is ",mainLeader)
    server.start()
    thread = Thread(target = threaded_function, args = (sys.argv[1], ))
    print("System args",sys.argv[1])
    thread.start()
    #thread.join()
    try:
        while True:
            
            time.sleep(_ONE_DAY_IN_SECONDS)

            #if mainLeader:
            #    print("Current Main leader is ",mainLeader)
            #else:
            #    print("not up")
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print("Mian start here")
    serve()

# from concurrent import futures
# import time
# import logging
# from activeNodes import activeNodes
# import threading
# import sys
# import grpc
# from NodePing import Heartbeat
# from FileOperations import FileService
# sys.path.append('./Gen')
# import heartbeat_pb2
# import heartbeat_pb2_grpc
# import fileService_pb2
# import fileService_pb2_grpc

# _ONE_DAY_IN_SECONDS = 60 * 60 * 24
# activeNodeObj= activeNodes()

# def serve():
#     leader=True
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000))
#     if sys.argv[1] != str(3000):
#         leader=False
#     serverAddress= '127.0.0.1:'+sys.argv[1]
#     print("Server started on" +  sys.argv[1])
#     heartbeat_pb2_grpc.add_HearBeatServicer_to_server(Heartbeat(), server)
#     fileService_pb2_grpc.add_FileserviceServicer_to_server(FileService(leader, serverAddress, activeNodeObj), server)
#     server.add_insecure_port('127.0.0.1:'+sys.argv[1])
#     server.start()
#     try:
#         while True:
#             time.sleep(_ONE_DAY_IN_SECONDS)
#     except KeyboardInterrupt:
#         server.stop(0)


# if __name__ == '__main__':
#     serve()
