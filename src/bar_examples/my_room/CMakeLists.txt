cmake_minimum_required(VERSION 3.8)
project(my_room)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_auto REQUIRED)

ament_auto_find_build_dependencies()


ament_auto_package(
  INSTALL_TO_SHARE     
    models
    worlds
)


install(DIRECTORY
  DESTINATION
  share/${PROJECT_NAME}/models/${PROJECT_NAME}
)



