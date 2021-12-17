// BD-server.cpp : Defines the entry point for the application.
//

#include "BD-server.h"
#include <sims/world.hpp>
#include <server/server.hpp>

using namespace std;

int main()
{
	/*simulations::world wld(1.0f, 1.0f);
	wld.actors.push_back(std::make_unique<simulations::Pawn>(0.0, 0.0, 0.0, 1.0));
	wld.mainLoop();*/

	server::acceptor acc(PORT);
	server::ClientConnection client1(&acc);

	return 1;
}
