// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/M1.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__M1__TRAITS_HPP_
#define INTERFACES__MSG__M1__TRAITS_HPP_

#include "interfaces/msg/m1__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'h'
#include "std_msgs/msg/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::msg::M1>()
{
  return "interfaces::msg::M1";
}

template<>
struct has_fixed_size<interfaces::msg::M1>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces::msg::M1>
  : std::integral_constant<bool, false> {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__M1__TRAITS_HPP_
