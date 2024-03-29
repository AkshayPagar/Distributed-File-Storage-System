from concurrent import futures
import time
import logging
import threading
import grpc
import sys
sys.path.append('./Gen')
import fileService_pb2
import fileService_pb2_grpc
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

CHUNK_SIZE= 1024*1024

def get_file_chunks(filename):
    with open(filename, 'rb') as f:
        while True:
            piece = f.read(CHUNK_SIZE);
            if len(piece) == 0:
                return
            yield fileService_pb2.FileData(username='akshay', filename= filename,data=piece)

def save_chunks(chunks, filename):
    i=0
    for chunk in chunks:
        with open(filename+str(i), 'wb') as f:
            if data.get(filename,None)==None:
                data[filename]=[0]*2
            data[filename][0]+=1
            i=i+1
            f.write(chunk.data)
    args= (1, filename, i)
    mycursor.execute("Insert into chunk_data VALUES(%d , '%s',  %d)" %(1, filename, i))
    cnx.commit()
    cnx.close()
    

def save_chunks_to_file(chunks, filename):
    with open(filename, 'wb') as f:
        for chunk in chunks:
            f.write(chunk.data)

def client():
    while True: 
        choice= int(input("What operation: 1. Upload 2. Download 3. Search 4. List File : "))
        if choice==1:
            channel = grpc.insecure_channel('127.0.0.1:3000')
            fileName=input("FileName to be uploaded: ")
            chunk_generator= get_file_chunks(fileName)
            stub = fileService_pb2_grpc.FileserviceStub(channel)
            response = stub.UploadFile(chunk_generator)
            print(response)
        elif choice==2:
            channel = grpc.insecure_channel('127.0.0.1:3000')
            name= input("Name of file to download")
            stub = fileService_pb2_grpc.FileserviceStub(channel)
            response = stub.DownloadFile(fileService_pb2.FileInfo(username="akshay", filename=name))
            save_chunks_to_file(response, "downloads/own.pdf")
            print("File downloaded. ")
        elif choice==3:
            channel = grpc.insecure_channel('127.0.0.1:3000')
            name= input("Name of file to Search")
            stub = fileService_pb2_grpc.FileserviceStub(channel)
            response = stub.FileSearch(fileService_pb2.FileInfo(username="akshay", filename=name))
            print(response)
        elif choice==4:
            channel = grpc.insecure_channel('127.0.0.1:3000')
            name= input("Enter username: ")
            stub = fileService_pb2_grpc.FileserviceStub(channel)
            fileList = stub.FileList(fileService_pb2.UserInfo(username=name))
            # response = stub.DownloadFile(fileService_pb2.FileInfo(username="akshay", filename=name))
            print("File List. ", fileList)
        


if __name__ == '__main__':
    t3 = threading.Thread(target=client)
    t3.start()
    t3.join()
