// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:srv/SrFloatFloatString.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__STRUCT_H_
#define INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/SrFloatFloatString in the package interfaces.
typedef struct interfaces__srv__SrFloatFloatString_Request
{
  double x;
  float y;
} interfaces__srv__SrFloatFloatString_Request;

// Struct for a sequence of interfaces__srv__SrFloatFloatString_Request.
typedef struct interfaces__srv__SrFloatFloatString_Request__Sequence
{
  interfaces__srv__SrFloatFloatString_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__SrFloatFloatString_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'z'
#include "rosidl_generator_c/string.h"

// Struct defined in srv/SrFloatFloatString in the package interfaces.
typedef struct interfaces__srv__SrFloatFloatString_Response
{
  rosidl_generator_c__String z;
} interfaces__srv__SrFloatFloatString_Response;

// Struct for a sequence of interfaces__srv__SrFloatFloatString_Response.
typedef struct interfaces__srv__SrFloatFloatString_Response__Sequence
{
  interfaces__srv__SrFloatFloatString_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__srv__SrFloatFloatString_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__STRUCT_H_
