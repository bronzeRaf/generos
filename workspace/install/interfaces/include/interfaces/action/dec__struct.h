// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:action/Dec.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__ACTION__DEC__STRUCT_H_
#define INTERFACES__ACTION__DEC__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in action/Dec in the package interfaces.
typedef struct interfaces__action__Dec_Goal
{
  int64_t x1;
  double x2;
} interfaces__action__Dec_Goal;

// Struct for a sequence of interfaces__action__Dec_Goal.
typedef struct interfaces__action__Dec_Goal__Sequence
{
  interfaces__action__Dec_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Dec_Goal__Sequence;


// Constants defined in the message

// Struct defined in action/Dec in the package interfaces.
typedef struct interfaces__action__Dec_Result
{
  double y;
} interfaces__action__Dec_Result;

// Struct for a sequence of interfaces__action__Dec_Result.
typedef struct interfaces__action__Dec_Result__Sequence
{
  interfaces__action__Dec_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Dec_Result__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'h'
#include "std_msgs/msg/header__struct.h"

// Struct defined in action/Dec in the package interfaces.
typedef struct interfaces__action__Dec_Feedback
{
  std_msgs__msg__Header h;
  double yt;
} interfaces__action__Dec_Feedback;

// Struct for a sequence of interfaces__action__Dec_Feedback.
typedef struct interfaces__action__Dec_Feedback__Sequence
{
  interfaces__action__Dec_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Dec_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/uuid__struct.h"
// Member 'goal'
#include "interfaces/action/dec__struct.h"

// Struct defined in action/Dec in the package interfaces.
typedef struct interfaces__action__Dec_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  interfaces__action__Dec_Goal goal;
} interfaces__action__Dec_SendGoal_Request;

// Struct for a sequence of interfaces__action__Dec_SendGoal_Request.
typedef struct interfaces__action__Dec_SendGoal_Request__Sequence
{
  interfaces__action__Dec_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Dec_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/time__struct.h"

// Struct defined in action/Dec in the package interfaces.
typedef struct interfaces__action__Dec_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} interfaces__action__Dec_SendGoal_Response;

// Struct for a sequence of interfaces__action__Dec_SendGoal_Response.
typedef struct interfaces__action__Dec_SendGoal_Response__Sequence
{
  interfaces__action__Dec_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Dec_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__struct.h"

// Struct defined in action/Dec in the package interfaces.
typedef struct interfaces__action__Dec_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} interfaces__action__Dec_GetResult_Request;

// Struct for a sequence of interfaces__action__Dec_GetResult_Request.
typedef struct interfaces__action__Dec_GetResult_Request__Sequence
{
  interfaces__action__Dec_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Dec_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "interfaces/action/dec__struct.h"

// Struct defined in action/Dec in the package interfaces.
typedef struct interfaces__action__Dec_GetResult_Response
{
  int8_t status;
  interfaces__action__Dec_Result result;
} interfaces__action__Dec_GetResult_Response;

// Struct for a sequence of interfaces__action__Dec_GetResult_Response.
typedef struct interfaces__action__Dec_GetResult_Response__Sequence
{
  interfaces__action__Dec_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Dec_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "interfaces/action/dec__struct.h"

// Struct defined in action/Dec in the package interfaces.
typedef struct interfaces__action__Dec_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  interfaces__action__Dec_Feedback feedback;
} interfaces__action__Dec_FeedbackMessage;

// Struct for a sequence of interfaces__action__Dec_FeedbackMessage.
typedef struct interfaces__action__Dec_FeedbackMessage__Sequence
{
  interfaces__action__Dec_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__action__Dec_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__ACTION__DEC__STRUCT_H_
