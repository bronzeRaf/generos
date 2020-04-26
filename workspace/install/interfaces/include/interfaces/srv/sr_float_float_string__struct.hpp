// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:srv/SrFloatFloatString.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__STRUCT_HPP_
#define INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__STRUCT_HPP_

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
# define DEPRECATED__interfaces__srv__SrFloatFloatString_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__SrFloatFloatString_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SrFloatFloatString_Request_
{
  using Type = SrFloatFloatString_Request_<ContainerAllocator>;

  explicit SrFloatFloatString_Request_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0;
      this->y = 0.0f;
    }
  }

  explicit SrFloatFloatString_Request_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0;
      this->y = 0.0f;
    }
  }

  // field types and members
  using _x_type =
    double;
  _x_type x;
  using _y_type =
    float;
  _y_type y;

  // setters for named parameter idiom
  Type & set__x(
    const double & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const float & _arg)
  {
    this->y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__SrFloatFloatString_Request
    std::shared_ptr<interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__SrFloatFloatString_Request
    std::shared_ptr<interfaces::srv::SrFloatFloatString_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SrFloatFloatString_Request_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    return true;
  }
  bool operator!=(const SrFloatFloatString_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SrFloatFloatString_Request_

// alias to use template instance with default allocator
using SrFloatFloatString_Request =
  interfaces::srv::SrFloatFloatString_Request_<std::allocator<void>>;

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

#ifndef _WIN32
# define DEPRECATED__interfaces__srv__SrFloatFloatString_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__srv__SrFloatFloatString_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SrFloatFloatString_Response_
{
  using Type = SrFloatFloatString_Response_<ContainerAllocator>;

  explicit SrFloatFloatString_Response_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->z = "";
    }
  }

  explicit SrFloatFloatString_Response_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : z(_alloc)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->z = "";
    }
  }

  // field types and members
  using _z_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _z_type z;

  // setters for named parameter idiom
  Type & set__z(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__srv__SrFloatFloatString_Response
    std::shared_ptr<interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__srv__SrFloatFloatString_Response
    std::shared_ptr<interfaces::srv::SrFloatFloatString_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SrFloatFloatString_Response_ & other) const
  {
    if (this->z != other.z) {
      return false;
    }
    return true;
  }
  bool operator!=(const SrFloatFloatString_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SrFloatFloatString_Response_

// alias to use template instance with default allocator
using SrFloatFloatString_Response =
  interfaces::srv::SrFloatFloatString_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interfaces

namespace interfaces
{

namespace srv
{

struct SrFloatFloatString
{
  using Request = interfaces::srv::SrFloatFloatString_Request;
  using Response = interfaces::srv::SrFloatFloatString_Response;
};

}  // namespace srv

}  // namespace interfaces

#endif  // INTERFACES__SRV__SR_FLOAT_FLOAT_STRING__STRUCT_HPP_
