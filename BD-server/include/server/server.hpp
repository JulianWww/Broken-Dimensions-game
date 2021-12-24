#include <sockpp/tcp_acceptor.h>
#include <mutex>
#include <sims/agents/pawn.hpp>
#include <sims/world.hpp>
#include <thread>

namespace server
{
	class acceptor
	{
	private: sockpp::socket_initializer sockInit;
	private: sockpp::tcp_acceptor acc;
	private: std::mutex acceptionLock;

	public: acceptor(int16_t port);
	public: sockpp::tcp_socket accept();
	};

	class ClientConnection: public simulations::Pawn
	{
	private: std::thread mainLoopThread;
	private: sockpp::tcp_socket sock;
	private: simulations::world* world;
	private: bool isActive = true;
	public: ClientConnection(acceptor* acc, simulations::world* world);

	public: static void _mainLoop(ClientConnection* conn);
	public: void mainLoop();
	public: void recv();
	};
}

inline void server::ClientConnection::_mainLoop(ClientConnection* conn)
{
	conn->mainLoop();
}
