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

server::ClientConnection::ClientConnection(acceptor* acc, simulations::world* _world)
{
	this->world = _world;
	sock = acc->accept();
	std::cout << this->id << std::endl;
	int _id[1] = { this->id };

	sock.write_n(_id, sizeof(_id));
	std::cout << "sent id" << std::endl;

	this->mainLoopThread = new std::thread(server::ClientConnection::_mainLoop, this);
}

server::ClientConnection::~ClientConnection()
{
	delete this->mainLoopThread;
}

void server::ClientConnection::mainLoop()
{
	fd_set rfd;
	FD_ZERO(&rfd);
	FD_SET(this->sock.handle(), &rfd);

	while (this->isActive)
	{
		if (this->checkMessageValidity())
			this->recv();

		std::cout << select(1, &rfd, NULL, NULL, 0);
	}
}

void server::ClientConnection::recv()
{
	char action[1];
	this->sock.read(action, sizeof(action));
	int action_i = (int)action[0];
	std::cout << action_i << std::endl;
	return;
}
