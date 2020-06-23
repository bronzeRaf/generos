// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:msg/M1.idl
// generated code does not contain a copyright notice
#include "interfaces/msg/m1__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `h`
#include "std_msgs/msg/header__functions.h"
// Member `s`
#include "rosidl_generator_c/string_functions.h"

bool
interfaces__msg__M1__init(interfaces__msg__M1 * msg)
{
  if (!msg) {
    return false;
  }
  // a
  // b
  // c
  // h
  if (!std_msgs__msg__Header__init(&msg->h)) {
    interfaces__msg__M1__fini(msg);
    return false;
  }
  // s
  if (!rosidl_generator_c__String__init(&msg->s)) {
    interfaces__msg__M1__fini(msg);
    return false;
  }
  // y
  return true;
}

void
interfaces__msg__M1__fini(interfaces__msg__M1 * msg)
{
  if (!msg) {
    return;
  }
  // a
  // b
  // c
  // h
  std_msgs__msg__Header__fini(&msg->h);
  // s
  rosidl_generator_c__String__fini(&msg->s);
  // y
}

interfaces__msg__M1 *
interfaces__msg__M1__create()
{
  interfaces__msg__M1 * msg = (interfaces__msg__M1 *)malloc(sizeof(interfaces__msg__M1));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__msg__M1));
  bool success = interfaces__msg__M1__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__msg__M1__destroy(interfaces__msg__M1 * msg)
{
  if (msg) {
    interfaces__msg__M1__fini(msg);
  }
  free(msg);
}


bool
interfaces__msg__M1__Sequence__init(interfaces__msg__M1__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__msg__M1 * data = NULL;
  if (size) {
    data = (interfaces__msg__M1 *)calloc(size, sizeof(interfaces__msg__M1));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__msg__M1__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__msg__M1__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interfaces__msg__M1__Sequence__fini(interfaces__msg__M1__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__msg__M1__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interfaces__msg__M1__Sequence *
interfaces__msg__M1__Sequence__create(size_t size)
{
  interfaces__msg__M1__Sequence * array = (interfaces__msg__M1__Sequence *)malloc(sizeof(interfaces__msg__M1__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__msg__M1__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__msg__M1__Sequence__destroy(interfaces__msg__M1__Sequence * array)
{
  if (array) {
    interfaces__msg__M1__Sequence__fini(array);
  }
  free(array);
}
