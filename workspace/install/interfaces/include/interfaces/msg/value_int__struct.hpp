// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:msg/ValueInt.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__MSG__VALUE_INT__STRUCT_HPP_
#define INTERFACES__MSG__VALUE_INT__STRUCT_HPP_

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
# define DEPRECATED__interfaces__msg__ValueInt __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__msg__ValueInt __declspec(deprecated)
#endif

namespace interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ValueInt_
{
  using Type = ValueInt_<ContainerAllocator>;

  explicit ValueInt_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0l;
    }
  }

  explicit ValueInt_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0l;
    }
  }

  // field types and members
  using _x_type =
    int32_t;
  _x_type x;

  // setters for named parameter idiom
  Type & set__x(
    const int32_t & _arg)
  {
    this->x = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::msg::ValueInt_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::msg::ValueInt_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::msg::ValueInt_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::msg::ValueInt_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::ValueInt_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::ValueInt_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::msg::ValueInt_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::msg::ValueInt_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::msg::ValueInt_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::msg::ValueInt_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__msg__ValueInt
    std::shared_ptr<interfaces::msg::ValueInt_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__msg__ValueInt
    std::shared_ptr<interfaces::msg::ValueInt_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ValueInt_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    return true;
  }
  bool operator!=(const ValueInt_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ValueInt_

// alias to use template instance with default allocator
using ValueInt =
  interfaces::msg::ValueInt_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interfaces

#endif  // INTERFACES__MSG__VALUE_INT__STRUCT_HPP_
