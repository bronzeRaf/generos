// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:msg/ValueInt.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__VALUE_INT__STRUCT_H_
#define INTERFACES__MSG__VALUE_INT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/header__struct.h"

// Struct defined in msg/ValueInt in the package interfaces.
typedef struct interfaces__msg__ValueInt
{
  std_msgs__msg__Header header;
  int8_t x;
} interfaces__msg__ValueInt;

// Struct for a sequence of interfaces__msg__ValueInt.
typedef struct interfaces__msg__ValueInt__Sequence
{
  interfaces__msg__ValueInt * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interfaces__msg__ValueInt__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__MSG__VALUE_INT__STRUCT_H_
