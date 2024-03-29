# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import fileService_pb2 as fileService__pb2


class FileserviceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UploadFile = channel.stream_unary(
        '/Fileservice/UploadFile',
        request_serializer=fileService__pb2.FileData.SerializeToString,
        response_deserializer=fileService__pb2.ack.FromString,
        )
    self.DownloadFile = channel.unary_stream(
        '/Fileservice/DownloadFile',
        request_serializer=fileService__pb2.FileInfo.SerializeToString,
        response_deserializer=fileService__pb2.FileData.FromString,
        )
    self.FileSearch = channel.unary_unary(
        '/Fileservice/FileSearch',
        request_serializer=fileService__pb2.FileInfo.SerializeToString,
        response_deserializer=fileService__pb2.ack.FromString,
        )
    self.ReplicateFile = channel.stream_unary(
        '/Fileservice/ReplicateFile',
        request_serializer=fileService__pb2.FileData.SerializeToString,
        response_deserializer=fileService__pb2.ack.FromString,
        )
    self.FileList = channel.unary_unary(
        '/Fileservice/FileList',
        request_serializer=fileService__pb2.UserInfo.SerializeToString,
        response_deserializer=fileService__pb2.FileListResponse.FromString,
        )
    self.FileDelete = channel.unary_unary(
        '/Fileservice/FileDelete',
        request_serializer=fileService__pb2.FileInfo.SerializeToString,
        response_deserializer=fileService__pb2.ack.FromString,
        )
    self.UpdateFile = channel.stream_unary(
        '/Fileservice/UpdateFile',
        request_serializer=fileService__pb2.FileData.SerializeToString,
        response_deserializer=fileService__pb2.ack.FromString,
        )
    self.metadataUpdate = channel.unary_unary(
        '/Fileservice/metadataUpdate',
        request_serializer=fileService__pb2.metadataInfo.SerializeToString,
        response_deserializer=fileService__pb2.ack.FromString,
        )


class FileserviceServicer(object):

  def UploadFile(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DownloadFile(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FileSearch(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplicateFile(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FileList(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FileDelete(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateFile(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def metadataUpdate(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FileserviceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UploadFile': grpc.stream_unary_rpc_method_handler(
          servicer.UploadFile,
          request_deserializer=fileService__pb2.FileData.FromString,
          response_serializer=fileService__pb2.ack.SerializeToString,
      ),
      'DownloadFile': grpc.unary_stream_rpc_method_handler(
          servicer.DownloadFile,
          request_deserializer=fileService__pb2.FileInfo.FromString,
          response_serializer=fileService__pb2.FileData.SerializeToString,
      ),
      'FileSearch': grpc.unary_unary_rpc_method_handler(
          servicer.FileSearch,
          request_deserializer=fileService__pb2.FileInfo.FromString,
          response_serializer=fileService__pb2.ack.SerializeToString,
      ),
      'ReplicateFile': grpc.stream_unary_rpc_method_handler(
          servicer.ReplicateFile,
          request_deserializer=fileService__pb2.FileData.FromString,
          response_serializer=fileService__pb2.ack.SerializeToString,
      ),
      'FileList': grpc.unary_unary_rpc_method_handler(
          servicer.FileList,
          request_deserializer=fileService__pb2.UserInfo.FromString,
          response_serializer=fileService__pb2.FileListResponse.SerializeToString,
      ),
      'FileDelete': grpc.unary_unary_rpc_method_handler(
          servicer.FileDelete,
          request_deserializer=fileService__pb2.FileInfo.FromString,
          response_serializer=fileService__pb2.ack.SerializeToString,
      ),
      'UpdateFile': grpc.stream_unary_rpc_method_handler(
          servicer.UpdateFile,
          request_deserializer=fileService__pb2.FileData.FromString,
          response_serializer=fileService__pb2.ack.SerializeToString,
      ),
      'metadataUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.metadataUpdate,
          request_deserializer=fileService__pb2.metadataInfo.FromString,
          response_serializer=fileService__pb2.ack.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Fileservice', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
