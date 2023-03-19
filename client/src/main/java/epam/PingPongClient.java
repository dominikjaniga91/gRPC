package epam;

import io.grpc.Channel;

import java.util.logging.Logger;

/**
 * @author Dominik_Janiga
 */
class PingPongClient {

    private static final Logger LOGGER = Logger.getLogger(PingPongClient.class.getName());

    private final PingPongServerGrpc.PingPongServerBlockingStub stub;

    public PingPongClient(Channel channel) {
        this.stub = PingPongServerGrpc.newBlockingStub(channel);
    }

    public void sendMessage() {
        PingRequest message = PingRequest.newBuilder()
                .setMessage("Ping from Java client")
                .build();

        PongResponse pongResponse = this.stub.pingPong(message);
        LOGGER.info("Received response: " + pongResponse.getMessage());
    }
}
