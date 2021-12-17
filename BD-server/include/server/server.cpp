#include "server.hpp"

server::acceptor::acceptor(int16_t port): acc(port)
{
	if (!acc)
	{
		std::cerr << "Failed to create acceptor: " << acc.last_error_str() << std::endl;
	}
	std::cout << "waiting for connections at: " << acc.address() << std::endl;
}
