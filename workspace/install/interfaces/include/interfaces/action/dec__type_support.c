// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interfaces:action/Dec.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
#include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interfaces/action/dec__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Dec_Goal__rosidl_typesupport_introspection_c__Dec_Goal_message_member_array[2] = {
  {
    "x1",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_Goal, x1),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "x2",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_Goal, x2),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Dec_Goal__rosidl_typesupport_introspection_c__Dec_Goal_message_members = {
  "interfaces__action",  // message namespace
  "Dec_Goal",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Dec_Goal),
  Dec_Goal__rosidl_typesupport_introspection_c__Dec_Goal_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Dec_Goal__rosidl_typesupport_introspection_c__Dec_Goal_message_type_support_handle = {
  0,
  &Dec_Goal__rosidl_typesupport_introspection_c__Dec_Goal_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_Goal)() {
  if (!Dec_Goal__rosidl_typesupport_introspection_c__Dec_Goal_message_type_support_handle.typesupport_identifier) {
    Dec_Goal__rosidl_typesupport_introspection_c__Dec_Goal_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Dec_Goal__rosidl_typesupport_introspection_c__Dec_Goal_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/dec__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Dec_Result__rosidl_typesupport_introspection_c__Dec_Result_message_member_array[1] = {
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_Result, y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Dec_Result__rosidl_typesupport_introspection_c__Dec_Result_message_members = {
  "interfaces__action",  // message namespace
  "Dec_Result",  // message name
  1,  // number of fields
  sizeof(interfaces__action__Dec_Result),
  Dec_Result__rosidl_typesupport_introspection_c__Dec_Result_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Dec_Result__rosidl_typesupport_introspection_c__Dec_Result_message_type_support_handle = {
  0,
  &Dec_Result__rosidl_typesupport_introspection_c__Dec_Result_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_Result)() {
  if (!Dec_Result__rosidl_typesupport_introspection_c__Dec_Result_message_type_support_handle.typesupport_identifier) {
    Dec_Result__rosidl_typesupport_introspection_c__Dec_Result_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Dec_Result__rosidl_typesupport_introspection_c__Dec_Result_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/dec__struct.h"


// Include directives for member types
// Member `h`
#include "std_msgs/msg/header.h"
// Member `h`
#include "std_msgs/msg/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_member_array[2] = {
  {
    "h",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_Feedback, h),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "yt",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_Feedback, yt),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_members = {
  "interfaces__action",  // message namespace
  "Dec_Feedback",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Dec_Feedback),
  Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_type_support_handle = {
  0,
  &Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_Feedback)() {
  Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_type_support_handle.typesupport_identifier) {
    Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Dec_Feedback__rosidl_typesupport_introspection_c__Dec_Feedback_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/dec__struct.h"


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
#include "unique_identifier_msgs/msg/uuid__rosidl_typesupport_introspection_c.h"
// Member `goal`
#include "interfaces/action/dec.h"
// Member `goal`
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_SendGoal_Request, goal_id),  // bytes offset in struct
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
    offsetof(interfaces__action__Dec_SendGoal_Request, goal),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_members = {
  "interfaces__action",  // message namespace
  "Dec_SendGoal_Request",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Dec_SendGoal_Request),
  Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_type_support_handle = {
  0,
  &Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_SendGoal_Request)() {
  Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_Goal)();
  if (!Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_type_support_handle.typesupport_identifier) {
    Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Dec_SendGoal_Request__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/dec__struct.h"


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/time.h"
// Member `stamp`
#include "builtin_interfaces/msg/time__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_member_array[2] = {
  {
    "accepted",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_SendGoal_Response, accepted),  // bytes offset in struct
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
    offsetof(interfaces__action__Dec_SendGoal_Response, stamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_members = {
  "interfaces__action",  // message namespace
  "Dec_SendGoal_Response",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Dec_SendGoal_Response),
  Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_type_support_handle = {
  0,
  &Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_SendGoal_Response)() {
  Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_type_support_handle.typesupport_identifier) {
    Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Dec_SendGoal_Response__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_generator_c/service_type_support_struct.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_service_members = {
  "interfaces__action",  // service namespace
  "Dec_SendGoal",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_Request_message_type_support_handle,
  NULL  // response message
  // interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_Response_message_type_support_handle
};

static rosidl_service_type_support_t interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_service_type_support_handle = {
  0,
  &interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_SendGoal_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_SendGoal_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_SendGoal)() {
  if (!interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_service_type_support_handle.typesupport_identifier) {
    interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_SendGoal_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_SendGoal_Response)()->data;
  }

  return &interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_SendGoal_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/dec__struct.h"


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

static rosidl_typesupport_introspection_c__MessageMember Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_member_array[1] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_GetResult_Request, goal_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_members = {
  "interfaces__action",  // message namespace
  "Dec_GetResult_Request",  // message name
  1,  // number of fields
  sizeof(interfaces__action__Dec_GetResult_Request),
  Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_type_support_handle = {
  0,
  &Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_GetResult_Request)() {
  Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  if (!Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_type_support_handle.typesupport_identifier) {
    Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Dec_GetResult_Request__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/dec__struct.h"


// Include directives for member types
// Member `result`
// already included above
// #include "interfaces/action/dec.h"
// Member `result`
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_member_array[2] = {
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_GetResult_Response, status),  // bytes offset in struct
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
    offsetof(interfaces__action__Dec_GetResult_Response, result),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_members = {
  "interfaces__action",  // message namespace
  "Dec_GetResult_Response",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Dec_GetResult_Response),
  Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_type_support_handle = {
  0,
  &Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_GetResult_Response)() {
  Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_Result)();
  if (!Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_type_support_handle.typesupport_identifier) {
    Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Dec_GetResult_Response__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include "rosidl_generator_c/service_type_support_struct.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_service_members = {
  "interfaces__action",  // service namespace
  "Dec_GetResult",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_Request_message_type_support_handle,
  NULL  // response message
  // interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_Response_message_type_support_handle
};

static rosidl_service_type_support_t interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_service_type_support_handle = {
  0,
  &interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_GetResult_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_GetResult_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_GetResult)() {
  if (!interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_service_type_support_handle.typesupport_identifier) {
    interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_GetResult_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_GetResult_Response)()->data;
  }

  return &interfaces__action__dec__rosidl_typesupport_introspection_c__Dec_GetResult_service_type_support_handle;
}

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/action/dec__struct.h"


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid.h"
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/uuid__rosidl_typesupport_introspection_c.h"
// Member `feedback`
// already included above
// #include "interfaces/action/dec.h"
// Member `feedback`
// already included above
// #include "interfaces/action/dec__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_member_array[2] = {
  {
    "goal_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__action__Dec_FeedbackMessage, goal_id),  // bytes offset in struct
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
    offsetof(interfaces__action__Dec_FeedbackMessage, feedback),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_members = {
  "interfaces__action",  // message namespace
  "Dec_FeedbackMessage",  // message name
  2,  // number of fields
  sizeof(interfaces__action__Dec_FeedbackMessage),
  Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_type_support_handle = {
  0,
  &Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_FeedbackMessage)() {
  Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, unique_identifier_msgs, msg, UUID)();
  Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, action, Dec_Feedback)();
  if (!Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_type_support_handle.typesupport_identifier) {
    Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Dec_FeedbackMessage__rosidl_typesupport_introspection_c__Dec_FeedbackMessage_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
