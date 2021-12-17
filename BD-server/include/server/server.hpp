#include <sockpp/tcp_acceptor.h>
#include <mutex>
#include <sims/agents/pawn.hpp>

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
	private: sockpp::tcp_socket sock;
	public: ClientConnection(acceptor* acc);
	};
}