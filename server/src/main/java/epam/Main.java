package epam;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.ServerServiceDefinition;

import java.io.IOException;
import java.util.List;

/**
 * @author Dominik_Janiga
 */
class Main {
    public static void main(String[] args) throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(50051)
                .addService(new PingPongServer())
                .build();
        server.start();
        server.awaitTermination();

        List<ServerServiceDefinition> services = server.getServices();
        System.out.println("services " + services);
    }
}
