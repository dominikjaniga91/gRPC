package epam;

import io.grpc.stub.StreamObserver;

import java.util.logging.Logger;

/**
 * @author Dominik_Janiga
 */
class PingPongServer extends PingPongServerGrpc.PingPongServerImplBase {

    private static final Logger LOGGER = Logger.getLogger(PingPongServer.class.getName());

    @Override
    public void pingPong(PingRequest request, StreamObserver<PongResponse> responseObserver) {

        LOGGER.info("Received message: " + request.getMessage());
        PongResponse response = PongResponse.newBuilder()
                .setMessage("Pong from server")
                .build();
        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
