#include "pawn.hpp"

simulations::Pawn::Pawn(): Actor(0.0f, 0.0f)
{
	this->dv_x = 0.0f;
	this->dv_y = 0.0f;
}

simulations::Pawn::Pawn(float x, float y): Actor(x, y)
{
	this->dv_x = 0.0f;
	this->dv_y = 0.0f;
}

simulations::Pawn::Pawn(float x, float y, float dx, float dy) : Actor(x, y)
{
	this->dv_x = dx;
	this->dv_y = dy;
}

void simulations::Pawn::update(float dt)
{
	this->x_pos = this->dv_x * dt;
	this->y_pos = this->dv_y * dt;
}