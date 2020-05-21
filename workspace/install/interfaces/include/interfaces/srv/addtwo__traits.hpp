// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/Addtwo.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__ADDTWO__TRAITS_HPP_
#define INTERFACES__SRV__ADDTWO__TRAITS_HPP_

#include "interfaces/srv/addtwo__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::Addtwo_Request>()
{
  return "interfaces::srv::Addtwo_Request";
}

template<>
struct has_fixed_size<interfaces::srv::Addtwo_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::Addtwo_Request>
  : std::integral_constant<bool, true> {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'h'
#include "std_msgs/msg/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::Addtwo_Response>()
{
  return "interfaces::srv::Addtwo_Response";
}

template<>
struct has_fixed_size<interfaces::srv::Addtwo_Response>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<interfaces::srv::Addtwo_Response>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::Addtwo>()
{
  return "interfaces::srv::Addtwo";
}

template<>
struct has_fixed_size<interfaces::srv::Addtwo>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::Addtwo_Request>::value &&
    has_fixed_size<interfaces::srv::Addtwo_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::Addtwo>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::Addtwo_Request>::value &&
    has_bounded_size<interfaces::srv::Addtwo_Response>::value
  >
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__ADDTWO__TRAITS_HPP_
