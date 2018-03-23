project(jwasm C)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(TRMEM 0) # Memory tracker

file(GLOB sources RELATIVE ${CMAKE_SOURCE_DIR} "*.c")

set(defs $<$<CONFIG:Debug>:DEBUG_OUT>$<$<CONFIG:Release>:NDEBUG>)
if(TRMEM AND WIN32)
  list(APPEND defs TRMEM FASTMEM=0)
else()
  list(REMOVE_ITEM sources trmem.c)
endif()
if(WIN32)
  list(APPEND defs __NT__)
else()
  list(APPEND defs __UNIX__)
endif()

add_executable(${PROJECT_NAME} ${sources})
target_include_directories(${PROJECT_NAME} PRIVATE H)
set_target_properties(${PROJECT_NAME} PROPERTIES COMPILE_DEFINITIONS "${defs}")
if(NOT WIN32)
  target_link_libraries(${PROJECT_NAME} -static)
endif()
