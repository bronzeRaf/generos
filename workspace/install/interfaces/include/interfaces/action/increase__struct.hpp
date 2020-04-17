// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interfaces:action/Increase.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__ACTION__INCREASE__STRUCT_HPP_
#define INTERFACES__ACTION__INCREASE__STRUCT_HPP_

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
// Member 'start'
// Member 'goal'
#include "std_msgs/msg/int32__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Increase_Goal __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Increase_Goal __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Increase_Goal_
{
  using Type = Increase_Goal_<ContainerAllocator>;

  explicit Increase_Goal_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : start(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit Increase_Goal_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : start(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _start_type =
    std_msgs::msg::Int32_<ContainerAllocator>;
  _start_type start;
  using _goal_type =
    std_msgs::msg::Int32_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__start(
    const std_msgs::msg::Int32_<ContainerAllocator> & _arg)
  {
    this->start = _arg;
    return *this;
  }
  Type & set__goal(
    const std_msgs::msg::Int32_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Increase_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Increase_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Increase_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Increase_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Increase_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Increase_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Increase_Goal
    std::shared_ptr<interfaces::action::Increase_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Increase_Goal
    std::shared_ptr<interfaces::action::Increase_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Increase_Goal_ & other) const
  {
    if (this->start != other.start) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const Increase_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Increase_Goal_

// alias to use template instance with default allocator
using Increase_Goal =
  interfaces::action::Increase_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

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
# define DEPRECATED__interfaces__action__Increase_Result __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Increase_Result __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Increase_Result_
{
  using Type = Increase_Result_<ContainerAllocator>;

  explicit Increase_Result_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = false;
    }
  }

  explicit Increase_Result_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->a = false;
    }
  }

  // field types and members
  using _a_type =
    bool;
  _a_type a;

  // setters for named parameter idiom
  Type & set__a(
    const bool & _arg)
  {
    this->a = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Increase_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Increase_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Increase_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Increase_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Increase_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Increase_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Increase_Result
    std::shared_ptr<interfaces::action::Increase_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Increase_Result
    std::shared_ptr<interfaces::action::Increase_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Increase_Result_ & other) const
  {
    if (this->a != other.a) {
      return false;
    }
    return true;
  }
  bool operator!=(const Increase_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Increase_Result_

// alias to use template instance with default allocator
using Increase_Result =
  interfaces::action::Increase_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

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
# define DEPRECATED__interfaces__action__Increase_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Increase_Feedback __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Increase_Feedback_
{
  using Type = Increase_Feedback_<ContainerAllocator>;

  explicit Increase_Feedback_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->update = 0ll;
    }
  }

  explicit Increase_Feedback_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->update = 0ll;
    }
  }

  // field types and members
  using _update_type =
    int64_t;
  _update_type update;

  // setters for named parameter idiom
  Type & set__update(
    const int64_t & _arg)
  {
    this->update = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Increase_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Increase_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Increase_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Increase_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Increase_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Increase_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Increase_Feedback
    std::shared_ptr<interfaces::action::Increase_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Increase_Feedback
    std::shared_ptr<interfaces::action::Increase_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Increase_Feedback_ & other) const
  {
    if (this->update != other.update) {
      return false;
    }
    return true;
  }
  bool operator!=(const Increase_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Increase_Feedback_

// alias to use template instance with default allocator
using Increase_Feedback =
  interfaces::action::Increase_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

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
// Member 'goal_id'
#include "unique_identifier_msgs/msg/uuid__struct.hpp"
// Member 'goal'
#include "interfaces/action/increase__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Increase_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Increase_SendGoal_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Increase_SendGoal_Request_
{
  using Type = Increase_SendGoal_Request_<ContainerAllocator>;

  explicit Increase_SendGoal_Request_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit Increase_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    interfaces::action::Increase_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const interfaces::action::Increase_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Increase_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Increase_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Increase_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Increase_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Increase_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Increase_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Increase_SendGoal_Request
    std::shared_ptr<interfaces::action::Increase_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Increase_SendGoal_Request
    std::shared_ptr<interfaces::action::Increase_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Increase_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const Increase_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Increase_SendGoal_Request_

// alias to use template instance with default allocator
using Increase_SendGoal_Request =
  interfaces::action::Increase_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

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
// Member 'stamp'
#include "builtin_interfaces/msg/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Increase_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Increase_SendGoal_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Increase_SendGoal_Response_
{
  using Type = Increase_SendGoal_Response_<ContainerAllocator>;

  explicit Increase_SendGoal_Response_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit Increase_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Increase_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Increase_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Increase_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Increase_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Increase_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Increase_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Increase_SendGoal_Response
    std::shared_ptr<interfaces::action::Increase_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Increase_SendGoal_Response
    std::shared_ptr<interfaces::action::Increase_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Increase_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const Increase_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Increase_SendGoal_Response_

// alias to use template instance with default allocator
using Increase_SendGoal_Response =
  interfaces::action::Increase_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

namespace interfaces
{

namespace action
{

struct Increase_SendGoal
{
  using Request = interfaces::action::Increase_SendGoal_Request;
  using Response = interfaces::action::Increase_SendGoal_Response;
};

}  // namespace action

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
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Increase_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Increase_GetResult_Request __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Increase_GetResult_Request_
{
  using Type = Increase_GetResult_Request_<ContainerAllocator>;

  explicit Increase_GetResult_Request_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit Increase_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Increase_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Increase_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Increase_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Increase_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Increase_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Increase_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Increase_GetResult_Request
    std::shared_ptr<interfaces::action::Increase_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Increase_GetResult_Request
    std::shared_ptr<interfaces::action::Increase_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Increase_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const Increase_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Increase_GetResult_Request_

// alias to use template instance with default allocator
using Increase_GetResult_Request =
  interfaces::action::Increase_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

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
// Member 'result'
// already included above
// #include "interfaces/action/increase__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Increase_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Increase_GetResult_Response __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Increase_GetResult_Response_
{
  using Type = Increase_GetResult_Response_<ContainerAllocator>;

  explicit Increase_GetResult_Response_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit Increase_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_generator_cpp::MessageInitialization::ALL == _init ||
      rosidl_generator_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    interfaces::action::Increase_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const interfaces::action::Increase_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Increase_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Increase_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Increase_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Increase_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Increase_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Increase_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Increase_GetResult_Response
    std::shared_ptr<interfaces::action::Increase_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Increase_GetResult_Response
    std::shared_ptr<interfaces::action::Increase_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Increase_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const Increase_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Increase_GetResult_Response_

// alias to use template instance with default allocator
using Increase_GetResult_Response =
  interfaces::action::Increase_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

namespace interfaces
{

namespace action
{

struct Increase_GetResult
{
  using Request = interfaces::action::Increase_GetResult_Request;
  using Response = interfaces::action::Increase_GetResult_Response;
};

}  // namespace action

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
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "interfaces/action/increase__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interfaces__action__Increase_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__interfaces__action__Increase_FeedbackMessage __declspec(deprecated)
#endif

namespace interfaces
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct Increase_FeedbackMessage_
{
  using Type = Increase_FeedbackMessage_<ContainerAllocator>;

  explicit Increase_FeedbackMessage_(rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit Increase_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_generator_cpp::MessageInitialization _init = rosidl_generator_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    interfaces::action::Increase_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const interfaces::action::Increase_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interfaces::action::Increase_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const interfaces::action::Increase_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interfaces::action::Increase_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interfaces::action::Increase_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interfaces::action::Increase_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interfaces::action::Increase_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interfaces::action::Increase_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interfaces::action::Increase_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interfaces__action__Increase_FeedbackMessage
    std::shared_ptr<interfaces::action::Increase_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interfaces__action__Increase_FeedbackMessage
    std::shared_ptr<interfaces::action::Increase_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Increase_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const Increase_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Increase_FeedbackMessage_

// alias to use template instance with default allocator
using Increase_FeedbackMessage =
  interfaces::action::Increase_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace interfaces

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace interfaces
{

namespace action
{

struct Increase
{
  /// The goal message defined in the action definition.
  using Goal = interfaces::action::Increase_Goal;
  /// The result message defined in the action definition.
  using Result = interfaces::action::Increase_Result;
  /// The feedback message defined in the action definition.
  using Feedback = interfaces::action::Increase_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = interfaces::action::Increase_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = interfaces::action::Increase_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = interfaces::action::Increase_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct Increase Increase;

}  // namespace action

}  // namespace interfaces

#endif  // INTERFACES__ACTION__INCREASE__STRUCT_HPP_
