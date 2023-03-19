import grpc
import epam.ping_pong_pb2_grpc as pb2_grpc
import epam.ping_pong_pb2 as pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.PingPongServerStub(channel)
        response = stub.pingPong(pb2.PingRequest(message='Ping from Python client'))
    print("Python client received: " + response.message)


if __name__ == '__main__':
    run()
