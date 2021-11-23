cmake_minimum_required(VERSION 3.1.0)
project(gtest)

configure_file(CMakeLists.txt.in googletest-download/CMakeLists.txt) # 复制CMakeLists.txt.in到googletest-download，这个命令还有替换关键字的功能
#执行cmake，把结果放到${CMAKE_CURRENT_BINARY_DIR}/googletest-download
execute_process(COMMAND ${CMAKE_COMMAND} -G "${CMAKE_GENERATOR}" .
        RESULT_VARIABLE result
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/googletest-download )
if(result)
    message(FATAL_ERROR "CMake step for googletest failed: ${result}")
endif()

#对google test进行build
execute_process(COMMAND ${CMAKE_COMMAND} --build .
        RESULT_VARIABLE result
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/googletest-download )
if(result)
    message(FATAL_ERROR "Build step for googletest failed: ${result}")
endif()

# Prevent overriding the parent project's compiler/linker
# settings on Windows
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Add googletest directly to our build. This defines
# the gtest and gtest_main targets.
add_subdirectory(${CMAKE_CURRENT_BINARY_DIR}/googletest-src
        ${CMAKE_CURRENT_BINARY_DIR}/googletest-build
        EXCLUDE_FROM_ALL)

# The gtest/gtest_main targets carry header search path
# dependencies automatically when using CMake 2.8.11 or
# later. Otherwise we have to add them here ourselves.
if (CMAKE_VERSION VERSION_LESS 2.8.11)
    include_directories("${gtest_SOURCE_DIR}/include")
endif()

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/envtest)
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/suittest)
add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/casetest)