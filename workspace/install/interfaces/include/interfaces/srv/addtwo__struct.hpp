// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/Addtwo.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__ADDTWO__STRUCT_HPP_
#define INTERFACES__SRV__ADDTWO__STRUCT_HPP_

#include <rosidl_generator_cpp/bounded_vector.hpp>
#include <rosidl_generator_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

#ifndef _WIN32
# define DEPRECATED__interfaces__srv__Addtwo_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__Addtwo_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Addtwo_Request_
{
  using Type = Addtwo_Request_<ContainerAllocator>;

  explicit Addtwo_Request_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0l;
      this->y = 0l;
    }
  }

  explicit Addtwo_Request_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0l;
      this->y = 0l;
    }
  }

  // field types and members
  using _x_type =
    int32_t;
  _x_type x;
  using _y_type =
    int32_t;
  _y_type y;

  // setters for named parameter idiom
  Type & set__x(
    const int32_t & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const int32_t & _arg)
  {
    this->y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::Addtwo_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::Addtwo_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::Addtwo_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::Addtwo_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::Addtwo_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::Addtwo_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::Addtwo_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::Addtwo_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::Addtwo_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::Addtwo_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__Addtwo_Request
    std::shared_ptr<interfaces::srv::Addtwo_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__Addtwo_Request
    std::shared_ptr<interfaces::srv::Addtwo_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Addtwo_Request_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    return true;
  }
  bool operator!=(const Addtwo_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Addtwo_Request_

// alias to use template instance with default allocator
using Addtwo_Request =
  interfaces::srv::Addtwo_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

// Protect against ERROR being predefined on Windows, in case somebody defines a
// constant by that name.
#if defined(_WIN32)
  #if defined(ERROR)
    #undef ERROR
  #endif
  #if defined(NO_ERROR)
    #undef NO_ERROR
  #endif
#endif

// Include directives for member types
// Member 'h'
#include "std_msgs/msg/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__srv__Addtwo_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__Addtwo_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Addtwo_Response_
{
  using Type = Addtwo_Response_<ContainerAllocator>;

  explicit Addtwo_Response_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : h(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->b = false;
      this->z = 0ll;
    }
  }

  explicit Addtwo_Response_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : h(_alloc, _init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->b = false;
      this->z = 0ll;
    }
  }

  // field types and members
  using _b_type =
    bool;
  _b_type b;
  using _h_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _h_type h;
  using _z_type =
    int64_t;
  _z_type z;

  // setters for named parameter idiom
  Type & set__b(
    const bool & _arg)
  {
    this->b = _arg;
    return *this;
  }
  Type & set__h(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->h = _arg;
    return *this;
  }
  Type & set__z(
    const int64_t & _arg)
  {
    this->z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::Addtwo_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::Addtwo_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::Addtwo_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::Addtwo_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::Addtwo_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::Addtwo_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::Addtwo_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::Addtwo_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::Addtwo_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::Addtwo_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__Addtwo_Response
    std::shared_ptr<interfaces::srv::Addtwo_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__Addtwo_Response
    std::shared_ptr<interfaces::srv::Addtwo_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Addtwo_Response_ & other) const
  {
    if (this->b != other.b) {
      return false;
    }
    if (this->h != other.h) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    return true;
  }
  bool operator!=(const Addtwo_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Addtwo_Response_

// alias to use template instance with default allocator
using Addtwo_Response =
  interfaces::srv::Addtwo_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct Addtwo
{
  using Request = interfaces::srv::Addtwo_Request;
  using Response = interfaces::srv::Addtwo_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__ADDTWO__STRUCT_HPP_
