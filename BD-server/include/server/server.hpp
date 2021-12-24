#include <sockpp/tcp_acceptor.h>
#include <mutex>
#include <sims/agents/pawn.hpp>
#include <sims/world.hpp>
#include <thread>
#include <condition_variable>

namespace server
{
	class acceptor
	{
	private: sockpp::socket_initializer sockInit;
	private: sockpp::tcp_acceptor acc;
	private: std::mutex acceptionLock;
	public: std::condition_variable holder;

	public: acceptor(int16_t port);
	public: sockpp::tcp_socket accept();
	};

	class ClientConnection: public simulations::Pawn
	{
	private: std::thread* mainLoopThread;
	private: sockpp::tcp_socket sock;
	private: simulations::world* world;
	private: unsigned int lastMessageId = -1;
	private: bool isActive = true;

	public: ClientConnection(acceptor* acc, simulations::world* world);
	public: ~ClientConnection();

	public: static void _mainLoop(ClientConnection* conn);
	public: void mainLoop();
	public: void recv();

	private: bool checkMessageValidity();
	};
}

inline void server::ClientConnection::_mainLoop(ClientConnection* conn)
{
	conn->mainLoop();
}

inline bool server::ClientConnection::checkMessageValidity()
{
	unsigned int msgId[1];
	this->sock.read(msgId, sizeof(msgId));
	if (msgId[0] != this->lastMessageId)
	{
		this->lastMessageId = msgId[0];
		std::cout << "msg Id is: " << this->lastMessageId << std::endl;
		return true;
	}
	return false;
}
