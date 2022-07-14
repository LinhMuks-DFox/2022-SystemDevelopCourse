cmake_minimum_required(VERSION 3.20)
project(mbf)

set(CMAKE_CXX_STANDARD 17)

add_executable(mbf main.cpp CommandLineParser.hpp)
