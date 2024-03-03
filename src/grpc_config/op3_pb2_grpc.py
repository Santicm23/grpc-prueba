# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import op3_pb2 as op3__pb2


class Op3Stub(object):
    """servicio op3
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Operation3 = channel.unary_unary(
                '/op3.Op3/Operation3',
                request_serializer=op3__pb2.Op3Request.SerializeToString,
                response_deserializer=op3__pb2.Op3Reply.FromString,
                )


class Op3Servicer(object):
    """servicio op3
    """

    def Operation3(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Op3Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Operation3': grpc.unary_unary_rpc_method_handler(
                    servicer.Operation3,
                    request_deserializer=op3__pb2.Op3Request.FromString,
                    response_serializer=op3__pb2.Op3Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'op3.Op3', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Op3(object):
    """servicio op3
    """

    @staticmethod
    def Operation3(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/op3.Op3/Operation3',
            op3__pb2.Op3Request.SerializeToString,
            op3__pb2.Op3Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
