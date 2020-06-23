// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from interfaces:action/Increase.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__ACTION__INCREASE__TRAITS_HPP_
#define INTERFACES__ACTION__INCREASE__TRAITS_HPP_

#include "interfaces/action/increase__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_Goal>()
{
  return "interfaces::action::Increase_Goal";
}

template<>
struct has_fixed_size<interfaces::action::Increase_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::action::Increase_Goal>
  : std::integral_constant<bool, true> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_Result>()
{
  return "interfaces::action::Increase_Result";
}

template<>
struct has_fixed_size<interfaces::action::Increase_Result>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<interfaces::action::Increase_Result>
  : std::integral_constant<bool, true> {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'h'
#include "std_msgs/msg/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_Feedback>()
{
  return "interfaces::action::Increase_Feedback";
}

template<>
struct has_fixed_size<interfaces::action::Increase_Feedback>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<interfaces::action::Increase_Feedback>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/uuid__traits.hpp"
// Member 'goal'
#include "interfaces/action/increase__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_SendGoal_Request>()
{
  return "interfaces::action::Increase_SendGoal_Request";
}

template<>
struct has_fixed_size<interfaces::action::Increase_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<interfaces::action::Increase_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<interfaces::action::Increase_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<interfaces::action::Increase_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/time__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_SendGoal_Response>()
{
  return "interfaces::action::Increase_SendGoal_Response";
}

template<>
struct has_fixed_size<interfaces::action::Increase_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<interfaces::action::Increase_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_SendGoal>()
{
  return "interfaces::action::Increase_SendGoal";
}

template<>
struct has_fixed_size<interfaces::action::Increase_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::action::Increase_SendGoal_Request>::value &&
    has_fixed_size<interfaces::action::Increase_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::action::Increase_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::action::Increase_SendGoal_Request>::value &&
    has_bounded_size<interfaces::action::Increase_SendGoal_Response>::value
  >
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_GetResult_Request>()
{
  return "interfaces::action::Increase_GetResult_Request";
}

template<>
struct has_fixed_size<interfaces::action::Increase_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<interfaces::action::Increase_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "interfaces/action/increase__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_GetResult_Response>()
{
  return "interfaces::action::Increase_GetResult_Response";
}

template<>
struct has_fixed_size<interfaces::action::Increase_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<interfaces::action::Increase_Result>::value> {};

template<>
struct has_bounded_size<interfaces::action::Increase_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<interfaces::action::Increase_Result>::value> {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_GetResult>()
{
  return "interfaces::action::Increase_GetResult";
}

template<>
struct has_fixed_size<interfaces::action::Increase_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<interfaces::action::Increase_GetResult_Request>::value &&
    has_fixed_size<interfaces::action::Increase_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<interfaces::action::Increase_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<interfaces::action::Increase_GetResult_Request>::value &&
    has_bounded_size<interfaces::action::Increase_GetResult_Response>::value
  >
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "interfaces/action/increase__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<interfaces::action::Increase_FeedbackMessage>()
{
  return "interfaces::action::Increase_FeedbackMessage";
}

template<>
struct has_fixed_size<interfaces::action::Increase_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<interfaces::action::Increase_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<interfaces::action::Increase_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<interfaces::action::Increase_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

}  // namespace rosidl_generator_traits

#endif  // INTERFACES__ACTION__INCREASE__TRAITS_HPP_
