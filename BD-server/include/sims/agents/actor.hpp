#pragma once

extern unsigned int id_counter;

namespace simulations
{
	class Actor
	{
	public: float x_pos;
	public: float y_pos;
	public: int id;
	
	public: Actor();
	public: Actor(float x_pos, float y_pos);

	public: virtual void update(float dt) = 0;

	private: void initID();
	};
}

inline void simulations::Actor::initID()
{
	this->id = id_counter;
	id_counter++;
}