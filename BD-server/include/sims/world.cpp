#include "world.hpp"

simulations::world::world(const float _x_size, const float _y_size) : x_size(_x_size), y_size(_y_size) 
{
}

void simulations::world::update(float dt)
{
	for (auto& actor : this->actors)
	{
		actor->update(dt);
	}
}

void simulations::world::mainLoop()
{
	double dt = 0.0;
	while (true)
	{
		auto t_start = std::chrono::high_resolution_clock::now();
		this->update(dt);
		auto t_stop = std::chrono::high_resolution_clock::now();
		dt = std::chrono::duration<double, std::ratio<1>>(t_stop - t_start).count();
	}
}
