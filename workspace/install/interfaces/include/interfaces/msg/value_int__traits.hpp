// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/ValueInt.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__VALUE_INT__TRAITS_HPP_
#define INTERFACES__MSG__VALUE_INT__TRAITS_HPP_

#include "interfaces/msg/value_int__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::msg::ValueInt>()
{
  return "interfaces::msg::ValueInt";
}

template<>
struct has_fixed_size<interfaces::msg::ValueInt>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<interfaces::msg::ValueInt>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__VALUE_INT__TRAITS_HPP_
