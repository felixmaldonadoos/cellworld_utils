#include "vr_server.h"

using namespace cell_world;
using namespace experiment;
using namespace agent_tracking;
using namespace vr_server;
using namespace tcp_messages;

bool Vr_server::prepare() {
    tracking_server.start(Tracking_service::get_port());
    auto &experiment_tracking_client = tracking_server.create_local_client<Experiment_tracking_client>();
    experiment_tracking_client.subscribe();
    experiment_server.set_tracking_client(experiment_tracking_client);
    experiment_server.start(Experiment_service::get_port());
    return true;
}

void Vr_server::stop() {
    experiment_server.stop();
    tracking_server.stop();

}

Vr_server::Vr_server() {

}

void vr_server::Vr_server::join() {
    experiment_server.join();
    tracking_server.join();
}

cell_world::Location_list vr_server::Vr_service::get_cell_locations() {
    auto configuration = Resources::from("world_configuration").key("hexagonal").get_resource<World_configuration>();
    auto implementation = Resources::from("world_implementation").key("hexagonal").key("canonical").get_resource<World_implementation>();
    auto world = World(configuration, implementation);
    cell_world::Location_list cell_locations;
    for (Cell &cell: world.cells){
        cell_locations.push_back(cell.location);
    }
    return cell_locations;
}

cell_world::Cell_group_builder vr_server::Vr_service::get_occlusions(std::string &occlusion_name) {
    return Resources::from("cell_group").key("hexagonal").key(occlusion_name).key("occlusions").get_resource<Cell_group_builder>();
}
