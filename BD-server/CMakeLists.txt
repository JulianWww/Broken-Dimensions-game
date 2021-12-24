# CMakeList.txt : CMake project for BD-server, include source and define
# project specific logic here.
#
project("BrokenDimsServer")
set (CMAKE_CXX_STANDARD 17)
cmake_minimum_required (VERSION 3.8)
set(CMAKE_BUILD_TYPE Debug)

file(GLOB sims
	"include/sims/*"
	"include/sims/agents/*"
	"include/server/*"
)

# Add source to this project's executable.
add_executable (BD-server "BD-server.cpp" "BD-server.h" ${sims})
target_include_directories(BD-server PUBLIC "${CMAKE_SOURCE_DIR}/include")

target_compile_definitions(BD-server PUBLIC PORT=25600)

if(WIN32)

	target_include_directories(BD-server PUBLIC "D:/MyCode/CppLibs/include")
	target_link_libraries(BD-server "lib/sockpp-static_d")
endif(WIN32)
if(UNIX)
	find_library(sockpp_location sockpp)
	message("sockpp is at: ${sockpp_location}")
	target_link_libraries(BD-server "${sockpp_location}")

	find_package (Threads REQUIRED)
	target_link_libraries(BD-server
		${CMAKE_THREAD_LIBS_INIT}
	)
endif(UNIX)