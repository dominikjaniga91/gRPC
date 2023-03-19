package epam;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

/**
 * @author Dominik_Janiga
 */
class Main {

    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder.forTarget("localhost:50051")
                .usePlaintext()
                .build();

        PingPongClient client = new PingPongClient(channel);
        for (int i = 0; i < 10; i++) {
            client.sendMessage();
        }
    }
}
