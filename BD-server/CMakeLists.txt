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


if(WIN32)

	target_include_directories(BD-server PUBLIC "D:/MyCode/CppLibs/include")
	target_link_libraries(BD-server "lib/sockpp-static_d")
endif(WIN32)
if(UNIX)
	find_library(sockpp_location sockpp)
	message("sockpp is at: ${sockpp_location}")
	target_link_libraries(BD-server "${sockpp_location}")
endif(UNIX)
