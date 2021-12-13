# CMakeList.txt : CMake project for BD-server, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

file(GLOB sims
	"include/sims/*.cpp"
	"include/sims/agents/*.cpp"
)

# Add source to this project's executable.
add_executable (BD-server "BD-server.cpp" "BD-server.h" ${sims})

if(win32)
	target_include_directories(BD-server PUBLIC "D:/MyCode/CppLibs/include")

	target_link_libraries(BC-server "lib/sockpp-static_d")
endif(win32)

# TODO: Add tests and install targets if needed.
