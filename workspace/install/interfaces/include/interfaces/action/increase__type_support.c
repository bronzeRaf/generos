// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interfaces:action/Increase.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
#include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interfaces/action/increase__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Increase_Goal__rosidl_typesupport_introspection_c__Increase_Goal_message_member_array[2] = {
  {
    "start",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_Goal, start),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stop",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_Goal, stop),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Increase_Goal__rosidl_typesupport_introspection_c__Increase_Goal_message_members = {
  "interfaces__action",  // message namespace
  "Increase_Goal",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Increase_Goal),
  Increase_Goal__rosidl_typesupport_introspection_c__Increase_Goal_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Increase_Goal__rosidl_typesupport_introspection_c__Increase_Goal_message_type_support_handle = {
  0,
  &Increase_Goal__rosidl_typesupport_introspection_c__Increase_Goal_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_Goal)() {
  if (!Increase_Goal__rosidl_typesupport_introspection_c__Increase_Goal_message_type_support_handle.typesupport_identifier) {
    Increase_Goal__rosidl_typesupport_introspection_c__Increase_Goal_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Increase_Goal__rosidl_typesupport_introspection_c__Increase_Goal_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/increase__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Increase_Result__rosidl_typesupport_introspection_c__Increase_Result_message_member_array[1] = {
  {
    "resus",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_Result, resus),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Increase_Result__rosidl_typesupport_introspection_c__Increase_Result_message_members = {
  "interfaces__action",  // message namespace
  "Increase_Result",  // message name
  1,  // number of fields
  sizeof(interfaces__action__Increase_Result),
  Increase_Result__rosidl_typesupport_introspection_c__Increase_Result_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Increase_Result__rosidl_typesupport_introspection_c__Increase_Result_message_type_support_handle = {
  0,
  &Increase_Result__rosidl_typesupport_introspection_c__Increase_Result_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_Result)() {
  if (!Increase_Result__rosidl_typesupport_introspection_c__Increase_Result_message_type_support_handle.typesupport_identifier) {
    Increase_Result__rosidl_typesupport_introspection_c__Increase_Result_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Increase_Result__rosidl_typesupport_introspection_c__Increase_Result_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/increase__struct.h"


// Include directives for member types
// Member `h`
#include "std_msgs/msg/header.h"
// Member `h`
#include "std_msgs/msg/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_member_array[2] = {
  {
    "h",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_Feedback, h),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "z",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_Feedback, z),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_members = {
  "interfaces__action",  // message namespace
  "Increase_Feedback",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Increase_Feedback),
  Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_type_support_handle = {
  0,
  &Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_Feedback)() {
  Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_type_support_handle.typesupport_identifier) {
    Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Increase_Feedback__rosidl_typesupport_introspection_c__Increase_Feedback_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/increase__struct.h"


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid__rosidl_typesupport_introspection_c.h"
// Member `goal`
#include "interfaces/action/increase.h"
// Member `goal`
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_SendGoal_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "goal",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_SendGoal_Request, goal),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_members = {
  "interfaces__action",  // message namespace
  "Increase_SendGoal_Request",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Increase_SendGoal_Request),
  Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_type_support_handle = {
  0,
  &Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_SendGoal_Request)() {
  Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_Goal)();
  if (!Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_type_support_handle.typesupport_identifier) {
    Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Increase_SendGoal_Request__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/increase__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_member_array[2] = {
  {
    "accepted",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_SendGoal_Response, accepted),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_SendGoal_Response, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_members = {
  "interfaces__action",  // message namespace
  "Increase_SendGoal_Response",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Increase_SendGoal_Response),
  Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_type_support_handle = {
  0,
  &Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_SendGoal_Response)() {
  Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_type_support_handle.typesupport_identifier) {
    Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Increase_SendGoal_Response__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_generator_c/service_type_support_struct.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_service_members = {
  "interfaces__action",  // service namespace
  "Increase_SendGoal",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_Request_message_type_support_handle,
  NULL  // response message
  // interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_Response_message_type_support_handle
};

static rosidl_service_type_support_t interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_service_type_support_handle = {
  0,
  &interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_SendGoal_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_SendGoal_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_SendGoal)() {
  if (!interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_service_type_support_handle.typesupport_identifier) {
    interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_SendGoal_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_SendGoal_Response)()->data;
  }

  return &interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_SendGoal_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/increase__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_member_array[1] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_GetResult_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_members = {
  "interfaces__action",  // message namespace
  "Increase_GetResult_Request",  // message name
  1,  // number of fields
  sizeof(interfaces__action__Increase_GetResult_Request),
  Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_type_support_handle = {
  0,
  &Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_GetResult_Request)() {
  Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  if (!Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_type_support_handle.typesupport_identifier) {
    Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Increase_GetResult_Request__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/increase__struct.h"


// Include directives for member types
// Member `result`
// already included above
// #include "interfaces/action/increase.h"
// Member `result`
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_member_array[2] = {
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_GetResult_Response, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "result",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_GetResult_Response, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_members = {
  "interfaces__action",  // message namespace
  "Increase_GetResult_Response",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Increase_GetResult_Response),
  Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_type_support_handle = {
  0,
  &Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_GetResult_Response)() {
  Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_Result)();
  if (!Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_type_support_handle.typesupport_identifier) {
    Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Increase_GetResult_Response__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_generator_c/service_type_support_struct.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_service_members = {
  "interfaces__action",  // service namespace
  "Increase_GetResult",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_Request_message_type_support_handle,
  NULL  // response message
  // interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_Response_message_type_support_handle
};

static rosidl_service_type_support_t interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_service_type_support_handle = {
  0,
  &interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_GetResult_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_GetResult_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_GetResult)() {
  if (!interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_service_type_support_handle.typesupport_identifier) {
    interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_GetResult_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_GetResult_Response)()->data;
  }

  return &interfaces__action__increase__rosidl_typesupport_introspection_c__Increase_GetResult_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/increase__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid__rosidl_typesupport_introspection_c.h"
// Member `feedback`
// already included above
// #include "interfaces/action/increase.h"
// Member `feedback`
// already included above
// #include "interfaces/action/increase__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_FeedbackMessage, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "feedback",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Increase_FeedbackMessage, feedback),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_members = {
  "interfaces__action",  // message namespace
  "Increase_FeedbackMessage",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Increase_FeedbackMessage),
  Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_type_support_handle = {
  0,
  &Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_FeedbackMessage)() {
  Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Increase_Feedback)();
  if (!Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_type_support_handle.typesupport_identifier) {
    Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Increase_FeedbackMessage__rosidl_typesupport_introspection_c__Increase_FeedbackMessage_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
