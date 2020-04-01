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
      this->a = 0;
      this->b = 0;
    }
  }

  explicit Addtwo_Request_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0;
      this->b = 0;
    }
  }

  // field types and members
  using _a_type =
    int8_t;
  _a_type a;
  using _b_type =
    int8_t;
  _b_type b;

  // setters for named parameter idiom
  Type & set__a(
    const int8_t & _arg)
  {
    this->a = _arg;
    return *this;
  }
  Type & set__b(
    const int8_t & _arg)
  {
    this->b = _arg;
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
    if (this->a != other.a) {
      return false;
    }
    if (this->b != other.b) {
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
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->c = 0;
    }
  }

  explicit Addtwo_Response_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->c = 0;
    }
  }

  // field types and members
  using _c_type =
    int8_t;
  _c_type c;

  // setters for named parameter idiom
  Type & set__c(
    const int8_t & _arg)
  {
    this->c = _arg;
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
    if (this->c != other.c) {
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
