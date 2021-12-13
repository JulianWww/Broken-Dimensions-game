#pragma once

#include <list>
#include <memory>
#include "agents/actor.hpp"
#include "agents/pawn.hpp"
#include <chrono>

namespace simulations
{
	class world
	{
	public: const float x_size;
	public: const float y_size;

	public: std::list<std::unique_ptr<Actor>> actors;

	public: world(const float _x_size, const float _y_size);

	public: void update(float dt);

	public: void mainLoop();
	};
}