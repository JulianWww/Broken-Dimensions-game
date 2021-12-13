#pragma once

#include "actor.hpp"


namespace simulations
{
	class Pawn : public Actor
	{
	public: float dv_x;
	public: float dv_y;

	public: Pawn();
	public: Pawn(float x, float y);
	public: Pawn(float x, float y, float dx, float dy);

	public: virtual void update(float dt);
	};
}