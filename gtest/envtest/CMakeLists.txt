cmake_minimum_required(VERSION 3.1.0)
project(envtest)

# Now simply link against gtest or gtest_main as needed.
add_executable(envtest env_test.cpp)
target_link_libraries(envtest gtest_main)
enable_testing()