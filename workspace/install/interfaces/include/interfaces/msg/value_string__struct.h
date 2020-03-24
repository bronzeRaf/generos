// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/ValueString.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__VALUE_STRING__STRUCT_H_
#define INTERFACES__MSG__VALUE_STRING__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'x'
#include "rosidl_generator_c/string.h"

// Struct defined in msg/ValueString in the package interfaces.
typedef struct interfaces__msg__ValueString
{
  rosidl_generator_c__String x;
} interfaces__msg__ValueString;

// Struct for a sequence of interfaces__msg__ValueString.
typedef struct interfaces__msg__ValueString__Sequence
{
  interfaces__msg__ValueString * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__ValueString__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__VALUE_STRING__STRUCT_H_
