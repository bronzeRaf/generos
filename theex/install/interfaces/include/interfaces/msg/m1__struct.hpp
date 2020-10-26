// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/M1.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__M1__STRUCT_HPP_
#define INTERFACES__MSG__M1__STRUCT_HPP_

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

// Include directives for member types
// Member 'h'
#include "std_msgs/msg/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__msg__M1 __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__M1 __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct M1_
{
  using Type = M1_<ContainerAllocator>;

  explicit M1_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : h(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0ll;
      this->b = false;
      this->c = false;
      this->s = "";
      this->y = 0.0f;
    }
  }

  explicit M1_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : h(_alloc, _init),
    s(_alloc)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = 0ll;
      this->b = false;
      this->c = false;
      this->s = "";
      this->y = 0.0f;
    }
  }

  // field types and members
  using _a_type =
    int64_t;
  _a_type a;
  using _b_type =
    bool;
  _b_type b;
  using _c_type =
    bool;
  _c_type c;
  using _h_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _h_type h;
  using _s_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _s_type s;
  using _y_type =
    float;
  _y_type y;

  // setters for named parameter idiom
  Type & set__a(
    const int64_t & _arg)
  {
    this->a = _arg;
    return *this;
  }
  Type & set__b(
    const bool & _arg)
  {
    this->b = _arg;
    return *this;
  }
  Type & set__c(
    const bool & _arg)
  {
    this->c = _arg;
    return *this;
  }
  Type & set__h(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->h = _arg;
    return *this;
  }
  Type & set__s(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->s = _arg;
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
    interfaces::msg::M1_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::M1_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::M1_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::M1_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::M1_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::M1_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::M1_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::M1_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::M1_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::M1_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__M1
    std::shared_ptr<interfaces::msg::M1_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__M1
    std::shared_ptr<interfaces::msg::M1_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const M1_ & other) const
  {
    if (this->a != other.a) {
      return false;
    }
    if (this->b != other.b) {
      return false;
    }
    if (this->c != other.c) {
      return false;
    }
    if (this->h != other.h) {
      return false;
    }
    if (this->s != other.s) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    return true;
  }
  bool operator!=(const M1_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct M1_

// alias to use template instance with default allocator
using M1 =
  interfaces::msg::M1_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__M1__STRUCT_HPP_
