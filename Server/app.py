from concurrent import futures
import logging

import grpc
import Users_pb2
import Users_pb2_grpc


class Users(Users_pb2_grpc.UserOperationServicer):
    
    def GetUsers(self, request, context):
        return Users_pb2.GetUserResponse(users=[
            Users_pb2.User(
                id='1',
                name='manoj',
                password='1234'
            )
        ])
    def SendData(self, request, context):
        print(request.users)
        return Users_pb2.GetUserResponse(users=[Users_pb2.User()])
    
def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Users_pb2_grpc.add_UserOperationServicer_to_server(Users(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
