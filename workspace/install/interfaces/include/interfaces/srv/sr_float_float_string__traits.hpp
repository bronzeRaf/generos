// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:srv/SrFloatFloatString.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__TRAITS_HPP_
#define INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__TRAITS_HPP_

#include "interfaces/srv/sr_float_float_string__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::SrFloatFloatString_Request>()
{
  return "interfaces::srv::SrFloatFloatString_Request";
}

template<>
struct has_fixed_size<interfaces::srv::SrFloatFloatString_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::srv::SrFloatFloatString_Request>
  : std::integral_constant<bool, true> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::SrFloatFloatString_Response>()
{
  return "interfaces::srv::SrFloatFloatString_Response";
}

template<>
struct has_fixed_size<interfaces::srv::SrFloatFloatString_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<interfaces::srv::SrFloatFloatString_Response>
  : std::integral_constant<bool, false> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::srv::SrFloatFloatString>()
{
  return "interfaces::srv::SrFloatFloatString";
}

template<>
struct has_fixed_size<interfaces::srv::SrFloatFloatString>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::srv::SrFloatFloatString_Request>::value &&
    has_fixed_size<interfaces::srv::SrFloatFloatString_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::srv::SrFloatFloatString>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::srv::SrFloatFloatString_Request>::value &&
    has_bounded_size<interfaces::srv::SrFloatFloatString_Response>::value
  >
{
};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__TRAITS_HPP_
