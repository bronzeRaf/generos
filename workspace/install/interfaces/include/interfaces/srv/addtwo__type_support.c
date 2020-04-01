// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interfaces:srv/Addtwo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interfaces/srv/addtwo__rosidl_typesupport_introspection_c.h"
#include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interfaces/srv/addtwo__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Addtwo_Request__rosidl_typesupport_introspection_c__Addtwo_Request_message_member_array[2] = {
  {
    "a",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__srv__Addtwo_Request, a),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "b",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__srv__Addtwo_Request, b),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Addtwo_Request__rosidl_typesupport_introspection_c__Addtwo_Request_message_members = {
  "interfaces__srv",  // message namespace
  "Addtwo_Request",  // message name
  2,  // number of fields
  sizeof(interfaces__srv__Addtwo_Request),
  Addtwo_Request__rosidl_typesupport_introspection_c__Addtwo_Request_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Addtwo_Request__rosidl_typesupport_introspection_c__Addtwo_Request_message_type_support_handle = {
  0,
  &Addtwo_Request__rosidl_typesupport_introspection_c__Addtwo_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, Addtwo_Request)() {
  if (!Addtwo_Request__rosidl_typesupport_introspection_c__Addtwo_Request_message_type_support_handle.typesupport_identifier) {
    Addtwo_Request__rosidl_typesupport_introspection_c__Addtwo_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Addtwo_Request__rosidl_typesupport_introspection_c__Addtwo_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interfaces/srv/addtwo__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interfaces/srv/addtwo__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

static rosidl_typesupport_introspection_c__MessageMember Addtwo_Response__rosidl_typesupport_introspection_c__Addtwo_Response_message_member_array[1] = {
  {
    "c",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interfaces__srv__Addtwo_Response, c),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers Addtwo_Response__rosidl_typesupport_introspection_c__Addtwo_Response_message_members = {
  "interfaces__srv",  // message namespace
  "Addtwo_Response",  // message name
  1,  // number of fields
  sizeof(interfaces__srv__Addtwo_Response),
  Addtwo_Response__rosidl_typesupport_introspection_c__Addtwo_Response_message_member_array  // message members
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t Addtwo_Response__rosidl_typesupport_introspection_c__Addtwo_Response_message_type_support_handle = {
  0,
  &Addtwo_Response__rosidl_typesupport_introspection_c__Addtwo_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, Addtwo_Response)() {
  if (!Addtwo_Response__rosidl_typesupport_introspection_c__Addtwo_Response_message_type_support_handle.typesupport_identifier) {
    Addtwo_Response__rosidl_typesupport_introspection_c__Addtwo_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &Addtwo_Response__rosidl_typesupport_introspection_c__Addtwo_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_generator_c/service_type_support_struct.h"
// already included above
// #include "interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interfaces/srv/addtwo__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_service_members = {
  "interfaces__srv",  // service namespace
  "Addtwo",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_Request_message_type_support_handle,
  NULL  // response message
  // interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_Response_message_type_support_handle
};

static rosidl_service_type_support_t interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_service_type_support_handle = {
  0,
  &interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, Addtwo_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, Addtwo_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, Addtwo)() {
  if (!interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_service_type_support_handle.typesupport_identifier) {
    interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, Addtwo_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interfaces, srv, Addtwo_Response)()->data;
  }

  return &interfaces__srv__addtwo__rosidl_typesupport_introspection_c__Addtwo_service_type_support_handle;
}
