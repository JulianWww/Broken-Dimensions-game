# CMakeList.txt : CMake project for BD-server, include source and define
# project specific logic here.
#
project("BrokenDimsServer")
cmake_minimum_required (VERSION 3.8)

file(GLOB sims
	"include/sims/*"
	"include/sims/agents/*"
	"include/server/*"
)

# Add source to this project's executable.
add_executable (BD-server "BD-server.cpp" "BD-server.h" ${sims})

target_include_directories(BD-server PUBLIC "${CMAKE_SOURCE_DIR}/include")

find_library(sockpp_location sockpp)
message("sockpp is at: ${sockpp_location}")
target_link_libraries(BD-server "${sockpp_location}")
