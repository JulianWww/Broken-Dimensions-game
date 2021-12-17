#include <sockpp/tcp_acceptor.h>
#include <mutex>

namespace server
{
	class acceptor
	{
	private: sockpp::socket_initializer sockInit;
	private: sockpp::tcp_acceptor acc;
	private: std::mutex acceptionLock;

	public: acceptor(int16_t port);
	};
}