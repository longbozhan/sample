cmake_minimum_required(VERSION 3.20)
project(hook_exception)

set(CMAKE_CXX_STANDARD 14)

add_executable(hook_exception main.cpp)
target_link_libraries(hook_exception pthread)