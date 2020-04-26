// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:srv/SrFloatFloatString.idl
// generated code does not contain a copyright notice
#include "interfaces/srv/sr_float_float_string__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool
interfaces__srv__SrFloatFloatString_Request__init(interfaces__srv__SrFloatFloatString_Request * msg)
{
  if (!msg) {
    return false;
  }
  // x
  // y
  return true;
}

void
interfaces__srv__SrFloatFloatString_Request__fini(interfaces__srv__SrFloatFloatString_Request * msg)
{
  if (!msg) {
    return;
  }
  // x
  // y
}

interfaces__srv__SrFloatFloatString_Request *
interfaces__srv__SrFloatFloatString_Request__create()
{
  interfaces__srv__SrFloatFloatString_Request * msg = (interfaces__srv__SrFloatFloatString_Request *)malloc(sizeof(interfaces__srv__SrFloatFloatString_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__srv__SrFloatFloatString_Request));
  bool success = interfaces__srv__SrFloatFloatString_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__srv__SrFloatFloatString_Request__destroy(interfaces__srv__SrFloatFloatString_Request * msg)
{
  if (msg) {
    interfaces__srv__SrFloatFloatString_Request__fini(msg);
  }
  free(msg);
}


bool
interfaces__srv__SrFloatFloatString_Request__Sequence__init(interfaces__srv__SrFloatFloatString_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__srv__SrFloatFloatString_Request * data = NULL;
  if (size) {
    data = (interfaces__srv__SrFloatFloatString_Request *)calloc(size, sizeof(interfaces__srv__SrFloatFloatString_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__srv__SrFloatFloatString_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__srv__SrFloatFloatString_Request__fini(&data[i - 1]);
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
interfaces__srv__SrFloatFloatString_Request__Sequence__fini(interfaces__srv__SrFloatFloatString_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__srv__SrFloatFloatString_Request__fini(&array->data[i]);
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

interfaces__srv__SrFloatFloatString_Request__Sequence *
interfaces__srv__SrFloatFloatString_Request__Sequence__create(size_t size)
{
  interfaces__srv__SrFloatFloatString_Request__Sequence * array = (interfaces__srv__SrFloatFloatString_Request__Sequence *)malloc(sizeof(interfaces__srv__SrFloatFloatString_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__srv__SrFloatFloatString_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__srv__SrFloatFloatString_Request__Sequence__destroy(interfaces__srv__SrFloatFloatString_Request__Sequence * array)
{
  if (array) {
    interfaces__srv__SrFloatFloatString_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `z`
#include "rosidl_generator_c/string_functions.h"

bool
interfaces__srv__SrFloatFloatString_Response__init(interfaces__srv__SrFloatFloatString_Response * msg)
{
  if (!msg) {
    return false;
  }
  // z
  if (!rosidl_generator_c__String__init(&msg->z)) {
    interfaces__srv__SrFloatFloatString_Response__destroy(msg);
    return false;
  }
  return true;
}

void
interfaces__srv__SrFloatFloatString_Response__fini(interfaces__srv__SrFloatFloatString_Response * msg)
{
  if (!msg) {
    return;
  }
  // z
  rosidl_generator_c__String__fini(&msg->z);
}

interfaces__srv__SrFloatFloatString_Response *
interfaces__srv__SrFloatFloatString_Response__create()
{
  interfaces__srv__SrFloatFloatString_Response * msg = (interfaces__srv__SrFloatFloatString_Response *)malloc(sizeof(interfaces__srv__SrFloatFloatString_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__srv__SrFloatFloatString_Response));
  bool success = interfaces__srv__SrFloatFloatString_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__srv__SrFloatFloatString_Response__destroy(interfaces__srv__SrFloatFloatString_Response * msg)
{
  if (msg) {
    interfaces__srv__SrFloatFloatString_Response__fini(msg);
  }
  free(msg);
}


bool
interfaces__srv__SrFloatFloatString_Response__Sequence__init(interfaces__srv__SrFloatFloatString_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__srv__SrFloatFloatString_Response * data = NULL;
  if (size) {
    data = (interfaces__srv__SrFloatFloatString_Response *)calloc(size, sizeof(interfaces__srv__SrFloatFloatString_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__srv__SrFloatFloatString_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__srv__SrFloatFloatString_Response__fini(&data[i - 1]);
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
interfaces__srv__SrFloatFloatString_Response__Sequence__fini(interfaces__srv__SrFloatFloatString_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__srv__SrFloatFloatString_Response__fini(&array->data[i]);
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

interfaces__srv__SrFloatFloatString_Response__Sequence *
interfaces__srv__SrFloatFloatString_Response__Sequence__create(size_t size)
{
  interfaces__srv__SrFloatFloatString_Response__Sequence * array = (interfaces__srv__SrFloatFloatString_Response__Sequence *)malloc(sizeof(interfaces__srv__SrFloatFloatString_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__srv__SrFloatFloatString_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__srv__SrFloatFloatString_Response__Sequence__destroy(interfaces__srv__SrFloatFloatString_Response__Sequence * array)
{
  if (array) {
    interfaces__srv__SrFloatFloatString_Response__Sequence__fini(array);
  }
  free(array);
}
