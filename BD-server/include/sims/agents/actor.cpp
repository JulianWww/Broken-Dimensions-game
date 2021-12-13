#include "actor.hpp"

unsigned int id_counter = 0;

inline simulations::Actor::Actor()
{
	this->initID();
	this->x_pos = 0.0f;
	this->y_pos = 0.0f;
}

simulations::Actor::Actor(float _x_pos, float _y_pos)
{
	this->initID();
	this->x_pos = _x_pos;
	this->y_pos = _y_pos;
}
