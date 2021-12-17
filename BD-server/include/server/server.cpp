#include "server.hpp"

server::acceptor::acceptor(int16_t port): acc(port)
{
	if (!acc)
	{
		std::cerr << "Failed to create acceptor: " << acc.last_error_str() << std::endl;
	}
	std::cout << "waiting for connections at: " << acc.address() << std::endl;
}

sockpp::tcp_socket server::acceptor::accept()
{
	this->acceptionLock.lock();
	auto sock = this->acc.accept();
	this->acceptionLock.unlock();
	return sock;
}

server::ClientConnection::ClientConnection(acceptor* acc)
{
	sock = acc->accept();
	std::cout << this->id << std::endl;
	sock.write((void*)this->id, 4);
}
