// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:msg/ValueString.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__VALUE_STRING__TRAITS_HPP_
#define INTERFACES__MSG__VALUE_STRING__TRAITS_HPP_

#include "interfaces/msg/value_string__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::msg::ValueString>()
{
  return "interfaces::msg::ValueString";
}

template<>
struct has_fixed_size<interfaces::msg::ValueString>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces::msg::ValueString>
  : std::integral_constant<bool, false> {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__MSG__VALUE_STRING__TRAITS_HPP_
