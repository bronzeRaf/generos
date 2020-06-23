// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/M1.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__M1__STRUCT_H_
#define INTERFACES__MSG__M1__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'h'
#include "std_msgs/msg/header__struct.h"
// Member 's'
#include "rosidl_generator_c/string.h"

// Struct defined in msg/M1 in the package interfaces.
typedef struct interfaces__msg__M1
{
  int64_t a;
  bool b;
  bool c;
  std_msgs__msg__Header h;
  rosidl_generator_c__String s;
  float y;
} interfaces__msg__M1;

// Struct for a sequence of interfaces__msg__M1.
typedef struct interfaces__msg__M1__Sequence
{
  interfaces__msg__M1 * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__M1__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__M1__STRUCT_H_
