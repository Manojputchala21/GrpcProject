
from __future__ import print_function

import logging

import grpc
import Users_pb2
import Users_pb2_grpc


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = Users_pb2_grpc.UserOperationStub(channel)
        # response = stub.GetUsers(Users_pb2.GetUserRequest())
        req=Users_pb2.SendDataToServer(users=Users_pb2.User(
            id='2',
            name='test',
            password='weew'
        ))
        response= stub.SendData(req)
    print(response)


if __name__ == "__main__":
    run()
