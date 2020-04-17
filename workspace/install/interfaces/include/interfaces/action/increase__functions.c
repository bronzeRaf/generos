// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interfaces:action/Increase.idl
// generated code does not contain a copyright notice
#include "interfaces/action/increase__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `start`
// Member `goal`
#include "std_msgs/msg/int32__functions.h"

bool
interfaces__action__Increase_Goal__init(interfaces__action__Increase_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // start
  if (!std_msgs__msg__Int32__init(&msg->start)) {
    interfaces__action__Increase_Goal__destroy(msg);
    return false;
  }
  // goal
  if (!std_msgs__msg__Int32__init(&msg->goal)) {
    interfaces__action__Increase_Goal__destroy(msg);
    return false;
  }
  return true;
}

void
interfaces__action__Increase_Goal__fini(interfaces__action__Increase_Goal * msg)
{
  if (!msg) {
    return;
  }
  // start
  std_msgs__msg__Int32__fini(&msg->start);
  // goal
  std_msgs__msg__Int32__fini(&msg->goal);
}

interfaces__action__Increase_Goal *
interfaces__action__Increase_Goal__create()
{
  interfaces__action__Increase_Goal * msg = (interfaces__action__Increase_Goal *)malloc(sizeof(interfaces__action__Increase_Goal));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__Increase_Goal));
  bool success = interfaces__action__Increase_Goal__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__Increase_Goal__destroy(interfaces__action__Increase_Goal * msg)
{
  if (msg) {
    interfaces__action__Increase_Goal__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__Increase_Goal__Sequence__init(interfaces__action__Increase_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__Increase_Goal * data = NULL;
  if (size) {
    data = (interfaces__action__Increase_Goal *)calloc(size, sizeof(interfaces__action__Increase_Goal));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__Increase_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__Increase_Goal__fini(&data[i - 1]);
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
interfaces__action__Increase_Goal__Sequence__fini(interfaces__action__Increase_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__Increase_Goal__fini(&array->data[i]);
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

interfaces__action__Increase_Goal__Sequence *
interfaces__action__Increase_Goal__Sequence__create(size_t size)
{
  interfaces__action__Increase_Goal__Sequence * array = (interfaces__action__Increase_Goal__Sequence *)malloc(sizeof(interfaces__action__Increase_Goal__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__Increase_Goal__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__Increase_Goal__Sequence__destroy(interfaces__action__Increase_Goal__Sequence * array)
{
  if (array) {
    interfaces__action__Increase_Goal__Sequence__fini(array);
  }
  free(array);
}


bool
interfaces__action__Increase_Result__init(interfaces__action__Increase_Result * msg)
{
  if (!msg) {
    return false;
  }
  // a
  return true;
}

void
interfaces__action__Increase_Result__fini(interfaces__action__Increase_Result * msg)
{
  if (!msg) {
    return;
  }
  // a
}

interfaces__action__Increase_Result *
interfaces__action__Increase_Result__create()
{
  interfaces__action__Increase_Result * msg = (interfaces__action__Increase_Result *)malloc(sizeof(interfaces__action__Increase_Result));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__Increase_Result));
  bool success = interfaces__action__Increase_Result__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__Increase_Result__destroy(interfaces__action__Increase_Result * msg)
{
  if (msg) {
    interfaces__action__Increase_Result__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__Increase_Result__Sequence__init(interfaces__action__Increase_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__Increase_Result * data = NULL;
  if (size) {
    data = (interfaces__action__Increase_Result *)calloc(size, sizeof(interfaces__action__Increase_Result));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__Increase_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__Increase_Result__fini(&data[i - 1]);
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
interfaces__action__Increase_Result__Sequence__fini(interfaces__action__Increase_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__Increase_Result__fini(&array->data[i]);
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

interfaces__action__Increase_Result__Sequence *
interfaces__action__Increase_Result__Sequence__create(size_t size)
{
  interfaces__action__Increase_Result__Sequence * array = (interfaces__action__Increase_Result__Sequence *)malloc(sizeof(interfaces__action__Increase_Result__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__Increase_Result__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__Increase_Result__Sequence__destroy(interfaces__action__Increase_Result__Sequence * array)
{
  if (array) {
    interfaces__action__Increase_Result__Sequence__fini(array);
  }
  free(array);
}


bool
interfaces__action__Increase_Feedback__init(interfaces__action__Increase_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // update
  return true;
}

void
interfaces__action__Increase_Feedback__fini(interfaces__action__Increase_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // update
}

interfaces__action__Increase_Feedback *
interfaces__action__Increase_Feedback__create()
{
  interfaces__action__Increase_Feedback * msg = (interfaces__action__Increase_Feedback *)malloc(sizeof(interfaces__action__Increase_Feedback));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__Increase_Feedback));
  bool success = interfaces__action__Increase_Feedback__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__Increase_Feedback__destroy(interfaces__action__Increase_Feedback * msg)
{
  if (msg) {
    interfaces__action__Increase_Feedback__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__Increase_Feedback__Sequence__init(interfaces__action__Increase_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__Increase_Feedback * data = NULL;
  if (size) {
    data = (interfaces__action__Increase_Feedback *)calloc(size, sizeof(interfaces__action__Increase_Feedback));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__Increase_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__Increase_Feedback__fini(&data[i - 1]);
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
interfaces__action__Increase_Feedback__Sequence__fini(interfaces__action__Increase_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__Increase_Feedback__fini(&array->data[i]);
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

interfaces__action__Increase_Feedback__Sequence *
interfaces__action__Increase_Feedback__Sequence__create(size_t size)
{
  interfaces__action__Increase_Feedback__Sequence * array = (interfaces__action__Increase_Feedback__Sequence *)malloc(sizeof(interfaces__action__Increase_Feedback__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__Increase_Feedback__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__Increase_Feedback__Sequence__destroy(interfaces__action__Increase_Feedback__Sequence * array)
{
  if (array) {
    interfaces__action__Increase_Feedback__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid__functions.h"
// Member `goal`
// already included above
// #include "interfaces/action/increase__functions.h"

bool
interfaces__action__Increase_SendGoal_Request__init(interfaces__action__Increase_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    interfaces__action__Increase_SendGoal_Request__destroy(msg);
    return false;
  }
  // goal
  if (!interfaces__action__Increase_Goal__init(&msg->goal)) {
    interfaces__action__Increase_SendGoal_Request__destroy(msg);
    return false;
  }
  return true;
}

void
interfaces__action__Increase_SendGoal_Request__fini(interfaces__action__Increase_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  interfaces__action__Increase_Goal__fini(&msg->goal);
}

interfaces__action__Increase_SendGoal_Request *
interfaces__action__Increase_SendGoal_Request__create()
{
  interfaces__action__Increase_SendGoal_Request * msg = (interfaces__action__Increase_SendGoal_Request *)malloc(sizeof(interfaces__action__Increase_SendGoal_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__Increase_SendGoal_Request));
  bool success = interfaces__action__Increase_SendGoal_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__Increase_SendGoal_Request__destroy(interfaces__action__Increase_SendGoal_Request * msg)
{
  if (msg) {
    interfaces__action__Increase_SendGoal_Request__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__Increase_SendGoal_Request__Sequence__init(interfaces__action__Increase_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__Increase_SendGoal_Request * data = NULL;
  if (size) {
    data = (interfaces__action__Increase_SendGoal_Request *)calloc(size, sizeof(interfaces__action__Increase_SendGoal_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__Increase_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__Increase_SendGoal_Request__fini(&data[i - 1]);
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
interfaces__action__Increase_SendGoal_Request__Sequence__fini(interfaces__action__Increase_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__Increase_SendGoal_Request__fini(&array->data[i]);
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

interfaces__action__Increase_SendGoal_Request__Sequence *
interfaces__action__Increase_SendGoal_Request__Sequence__create(size_t size)
{
  interfaces__action__Increase_SendGoal_Request__Sequence * array = (interfaces__action__Increase_SendGoal_Request__Sequence *)malloc(sizeof(interfaces__action__Increase_SendGoal_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__Increase_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__Increase_SendGoal_Request__Sequence__destroy(interfaces__action__Increase_SendGoal_Request__Sequence * array)
{
  if (array) {
    interfaces__action__Increase_SendGoal_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time__functions.h"

bool
interfaces__action__Increase_SendGoal_Response__init(interfaces__action__Increase_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    interfaces__action__Increase_SendGoal_Response__destroy(msg);
    return false;
  }
  return true;
}

void
interfaces__action__Increase_SendGoal_Response__fini(interfaces__action__Increase_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

interfaces__action__Increase_SendGoal_Response *
interfaces__action__Increase_SendGoal_Response__create()
{
  interfaces__action__Increase_SendGoal_Response * msg = (interfaces__action__Increase_SendGoal_Response *)malloc(sizeof(interfaces__action__Increase_SendGoal_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__Increase_SendGoal_Response));
  bool success = interfaces__action__Increase_SendGoal_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__Increase_SendGoal_Response__destroy(interfaces__action__Increase_SendGoal_Response * msg)
{
  if (msg) {
    interfaces__action__Increase_SendGoal_Response__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__Increase_SendGoal_Response__Sequence__init(interfaces__action__Increase_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__Increase_SendGoal_Response * data = NULL;
  if (size) {
    data = (interfaces__action__Increase_SendGoal_Response *)calloc(size, sizeof(interfaces__action__Increase_SendGoal_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__Increase_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__Increase_SendGoal_Response__fini(&data[i - 1]);
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
interfaces__action__Increase_SendGoal_Response__Sequence__fini(interfaces__action__Increase_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__Increase_SendGoal_Response__fini(&array->data[i]);
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

interfaces__action__Increase_SendGoal_Response__Sequence *
interfaces__action__Increase_SendGoal_Response__Sequence__create(size_t size)
{
  interfaces__action__Increase_SendGoal_Response__Sequence * array = (interfaces__action__Increase_SendGoal_Response__Sequence *)malloc(sizeof(interfaces__action__Increase_SendGoal_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__Increase_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__Increase_SendGoal_Response__Sequence__destroy(interfaces__action__Increase_SendGoal_Response__Sequence * array)
{
  if (array) {
    interfaces__action__Increase_SendGoal_Response__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid__functions.h"

bool
interfaces__action__Increase_GetResult_Request__init(interfaces__action__Increase_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    interfaces__action__Increase_GetResult_Request__destroy(msg);
    return false;
  }
  return true;
}

void
interfaces__action__Increase_GetResult_Request__fini(interfaces__action__Increase_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

interfaces__action__Increase_GetResult_Request *
interfaces__action__Increase_GetResult_Request__create()
{
  interfaces__action__Increase_GetResult_Request * msg = (interfaces__action__Increase_GetResult_Request *)malloc(sizeof(interfaces__action__Increase_GetResult_Request));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__Increase_GetResult_Request));
  bool success = interfaces__action__Increase_GetResult_Request__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__Increase_GetResult_Request__destroy(interfaces__action__Increase_GetResult_Request * msg)
{
  if (msg) {
    interfaces__action__Increase_GetResult_Request__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__Increase_GetResult_Request__Sequence__init(interfaces__action__Increase_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__Increase_GetResult_Request * data = NULL;
  if (size) {
    data = (interfaces__action__Increase_GetResult_Request *)calloc(size, sizeof(interfaces__action__Increase_GetResult_Request));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__Increase_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__Increase_GetResult_Request__fini(&data[i - 1]);
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
interfaces__action__Increase_GetResult_Request__Sequence__fini(interfaces__action__Increase_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__Increase_GetResult_Request__fini(&array->data[i]);
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

interfaces__action__Increase_GetResult_Request__Sequence *
interfaces__action__Increase_GetResult_Request__Sequence__create(size_t size)
{
  interfaces__action__Increase_GetResult_Request__Sequence * array = (interfaces__action__Increase_GetResult_Request__Sequence *)malloc(sizeof(interfaces__action__Increase_GetResult_Request__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__Increase_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__Increase_GetResult_Request__Sequence__destroy(interfaces__action__Increase_GetResult_Request__Sequence * array)
{
  if (array) {
    interfaces__action__Increase_GetResult_Request__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `result`
// already included above
// #include "interfaces/action/increase__functions.h"

bool
interfaces__action__Increase_GetResult_Response__init(interfaces__action__Increase_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!interfaces__action__Increase_Result__init(&msg->result)) {
    interfaces__action__Increase_GetResult_Response__destroy(msg);
    return false;
  }
  return true;
}

void
interfaces__action__Increase_GetResult_Response__fini(interfaces__action__Increase_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  interfaces__action__Increase_Result__fini(&msg->result);
}

interfaces__action__Increase_GetResult_Response *
interfaces__action__Increase_GetResult_Response__create()
{
  interfaces__action__Increase_GetResult_Response * msg = (interfaces__action__Increase_GetResult_Response *)malloc(sizeof(interfaces__action__Increase_GetResult_Response));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__Increase_GetResult_Response));
  bool success = interfaces__action__Increase_GetResult_Response__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__Increase_GetResult_Response__destroy(interfaces__action__Increase_GetResult_Response * msg)
{
  if (msg) {
    interfaces__action__Increase_GetResult_Response__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__Increase_GetResult_Response__Sequence__init(interfaces__action__Increase_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__Increase_GetResult_Response * data = NULL;
  if (size) {
    data = (interfaces__action__Increase_GetResult_Response *)calloc(size, sizeof(interfaces__action__Increase_GetResult_Response));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__Increase_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__Increase_GetResult_Response__fini(&data[i - 1]);
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
interfaces__action__Increase_GetResult_Response__Sequence__fini(interfaces__action__Increase_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__Increase_GetResult_Response__fini(&array->data[i]);
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

interfaces__action__Increase_GetResult_Response__Sequence *
interfaces__action__Increase_GetResult_Response__Sequence__create(size_t size)
{
  interfaces__action__Increase_GetResult_Response__Sequence * array = (interfaces__action__Increase_GetResult_Response__Sequence *)malloc(sizeof(interfaces__action__Increase_GetResult_Response__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__Increase_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__Increase_GetResult_Response__Sequence__destroy(interfaces__action__Increase_GetResult_Response__Sequence * array)
{
  if (array) {
    interfaces__action__Increase_GetResult_Response__Sequence__fini(array);
  }
  free(array);
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid__functions.h"
// Member `feedback`
// already included above
// #include "interfaces/action/increase__functions.h"

bool
interfaces__action__Increase_FeedbackMessage__init(interfaces__action__Increase_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    interfaces__action__Increase_FeedbackMessage__destroy(msg);
    return false;
  }
  // feedback
  if (!interfaces__action__Increase_Feedback__init(&msg->feedback)) {
    interfaces__action__Increase_FeedbackMessage__destroy(msg);
    return false;
  }
  return true;
}

void
interfaces__action__Increase_FeedbackMessage__fini(interfaces__action__Increase_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  interfaces__action__Increase_Feedback__fini(&msg->feedback);
}

interfaces__action__Increase_FeedbackMessage *
interfaces__action__Increase_FeedbackMessage__create()
{
  interfaces__action__Increase_FeedbackMessage * msg = (interfaces__action__Increase_FeedbackMessage *)malloc(sizeof(interfaces__action__Increase_FeedbackMessage));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interfaces__action__Increase_FeedbackMessage));
  bool success = interfaces__action__Increase_FeedbackMessage__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
interfaces__action__Increase_FeedbackMessage__destroy(interfaces__action__Increase_FeedbackMessage * msg)
{
  if (msg) {
    interfaces__action__Increase_FeedbackMessage__fini(msg);
  }
  free(msg);
}


bool
interfaces__action__Increase_FeedbackMessage__Sequence__init(interfaces__action__Increase_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  interfaces__action__Increase_FeedbackMessage * data = NULL;
  if (size) {
    data = (interfaces__action__Increase_FeedbackMessage *)calloc(size, sizeof(interfaces__action__Increase_FeedbackMessage));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interfaces__action__Increase_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interfaces__action__Increase_FeedbackMessage__fini(&data[i - 1]);
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
interfaces__action__Increase_FeedbackMessage__Sequence__fini(interfaces__action__Increase_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interfaces__action__Increase_FeedbackMessage__fini(&array->data[i]);
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

interfaces__action__Increase_FeedbackMessage__Sequence *
interfaces__action__Increase_FeedbackMessage__Sequence__create(size_t size)
{
  interfaces__action__Increase_FeedbackMessage__Sequence * array = (interfaces__action__Increase_FeedbackMessage__Sequence *)malloc(sizeof(interfaces__action__Increase_FeedbackMessage__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = interfaces__action__Increase_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
interfaces__action__Increase_FeedbackMessage__Sequence__destroy(interfaces__action__Increase_FeedbackMessage__Sequence * array)
{
  if (array) {
    interfaces__action__Increase_FeedbackMessage__Sequence__fini(array);
  }
  free(array);
}
