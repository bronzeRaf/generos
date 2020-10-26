// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interfaces:action/Increase.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__ACTION__INCREASE__FUNCTIONS_H_
#define INTERFACES__ACTION__INCREASE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_generator_c/visibility_control.h"
#include "interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "interfaces/action/increase__struct.h"

/// Initialize action/Increase message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Increase_Goal
 * )) before or use
 * interfaces__action__Increase_Goal__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_Goal__init(interfaces__action__Increase_Goal * msg);

/// Finalize action/Increase message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Goal__fini(interfaces__action__Increase_Goal * msg);

/// Create action/Increase message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Increase_Goal__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_Goal *
interfaces__action__Increase_Goal__create();

/// Destroy action/Increase message.
/**
 * It calls
 * interfaces__action__Increase_Goal__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Goal__destroy(interfaces__action__Increase_Goal * msg);


/// Initialize array of action/Increase messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Increase_Goal__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_Goal__Sequence__init(interfaces__action__Increase_Goal__Sequence * array, size_t size);

/// Finalize array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_Goal__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Goal__Sequence__fini(interfaces__action__Increase_Goal__Sequence * array);

/// Create array of action/Increase messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Increase_Goal__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_Goal__Sequence *
interfaces__action__Increase_Goal__Sequence__create(size_t size);

/// Destroy array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_Goal__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Goal__Sequence__destroy(interfaces__action__Increase_Goal__Sequence * array);

/// Initialize action/Increase message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Increase_Result
 * )) before or use
 * interfaces__action__Increase_Result__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_Result__init(interfaces__action__Increase_Result * msg);

/// Finalize action/Increase message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Result__fini(interfaces__action__Increase_Result * msg);

/// Create action/Increase message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Increase_Result__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_Result *
interfaces__action__Increase_Result__create();

/// Destroy action/Increase message.
/**
 * It calls
 * interfaces__action__Increase_Result__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Result__destroy(interfaces__action__Increase_Result * msg);


/// Initialize array of action/Increase messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Increase_Result__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_Result__Sequence__init(interfaces__action__Increase_Result__Sequence * array, size_t size);

/// Finalize array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_Result__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Result__Sequence__fini(interfaces__action__Increase_Result__Sequence * array);

/// Create array of action/Increase messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Increase_Result__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_Result__Sequence *
interfaces__action__Increase_Result__Sequence__create(size_t size);

/// Destroy array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_Result__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Result__Sequence__destroy(interfaces__action__Increase_Result__Sequence * array);

/// Initialize action/Increase message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Increase_Feedback
 * )) before or use
 * interfaces__action__Increase_Feedback__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_Feedback__init(interfaces__action__Increase_Feedback * msg);

/// Finalize action/Increase message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Feedback__fini(interfaces__action__Increase_Feedback * msg);

/// Create action/Increase message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Increase_Feedback__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_Feedback *
interfaces__action__Increase_Feedback__create();

/// Destroy action/Increase message.
/**
 * It calls
 * interfaces__action__Increase_Feedback__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Feedback__destroy(interfaces__action__Increase_Feedback * msg);


/// Initialize array of action/Increase messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Increase_Feedback__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_Feedback__Sequence__init(interfaces__action__Increase_Feedback__Sequence * array, size_t size);

/// Finalize array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_Feedback__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Feedback__Sequence__fini(interfaces__action__Increase_Feedback__Sequence * array);

/// Create array of action/Increase messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Increase_Feedback__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_Feedback__Sequence *
interfaces__action__Increase_Feedback__Sequence__create(size_t size);

/// Destroy array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_Feedback__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_Feedback__Sequence__destroy(interfaces__action__Increase_Feedback__Sequence * array);

/// Initialize action/Increase message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Increase_SendGoal_Request
 * )) before or use
 * interfaces__action__Increase_SendGoal_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_SendGoal_Request__init(interfaces__action__Increase_SendGoal_Request * msg);

/// Finalize action/Increase message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_SendGoal_Request__fini(interfaces__action__Increase_SendGoal_Request * msg);

/// Create action/Increase message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Increase_SendGoal_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_SendGoal_Request *
interfaces__action__Increase_SendGoal_Request__create();

/// Destroy action/Increase message.
/**
 * It calls
 * interfaces__action__Increase_SendGoal_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_SendGoal_Request__destroy(interfaces__action__Increase_SendGoal_Request * msg);


/// Initialize array of action/Increase messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Increase_SendGoal_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_SendGoal_Request__Sequence__init(interfaces__action__Increase_SendGoal_Request__Sequence * array, size_t size);

/// Finalize array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_SendGoal_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_SendGoal_Request__Sequence__fini(interfaces__action__Increase_SendGoal_Request__Sequence * array);

/// Create array of action/Increase messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Increase_SendGoal_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_SendGoal_Request__Sequence *
interfaces__action__Increase_SendGoal_Request__Sequence__create(size_t size);

/// Destroy array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_SendGoal_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_SendGoal_Request__Sequence__destroy(interfaces__action__Increase_SendGoal_Request__Sequence * array);

/// Initialize action/Increase message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Increase_SendGoal_Response
 * )) before or use
 * interfaces__action__Increase_SendGoal_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_SendGoal_Response__init(interfaces__action__Increase_SendGoal_Response * msg);

/// Finalize action/Increase message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_SendGoal_Response__fini(interfaces__action__Increase_SendGoal_Response * msg);

/// Create action/Increase message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Increase_SendGoal_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_SendGoal_Response *
interfaces__action__Increase_SendGoal_Response__create();

/// Destroy action/Increase message.
/**
 * It calls
 * interfaces__action__Increase_SendGoal_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_SendGoal_Response__destroy(interfaces__action__Increase_SendGoal_Response * msg);


/// Initialize array of action/Increase messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Increase_SendGoal_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_SendGoal_Response__Sequence__init(interfaces__action__Increase_SendGoal_Response__Sequence * array, size_t size);

/// Finalize array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_SendGoal_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_SendGoal_Response__Sequence__fini(interfaces__action__Increase_SendGoal_Response__Sequence * array);

/// Create array of action/Increase messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Increase_SendGoal_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_SendGoal_Response__Sequence *
interfaces__action__Increase_SendGoal_Response__Sequence__create(size_t size);

/// Destroy array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_SendGoal_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_SendGoal_Response__Sequence__destroy(interfaces__action__Increase_SendGoal_Response__Sequence * array);

/// Initialize action/Increase message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Increase_GetResult_Request
 * )) before or use
 * interfaces__action__Increase_GetResult_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_GetResult_Request__init(interfaces__action__Increase_GetResult_Request * msg);

/// Finalize action/Increase message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_GetResult_Request__fini(interfaces__action__Increase_GetResult_Request * msg);

/// Create action/Increase message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Increase_GetResult_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_GetResult_Request *
interfaces__action__Increase_GetResult_Request__create();

/// Destroy action/Increase message.
/**
 * It calls
 * interfaces__action__Increase_GetResult_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_GetResult_Request__destroy(interfaces__action__Increase_GetResult_Request * msg);


/// Initialize array of action/Increase messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Increase_GetResult_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_GetResult_Request__Sequence__init(interfaces__action__Increase_GetResult_Request__Sequence * array, size_t size);

/// Finalize array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_GetResult_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_GetResult_Request__Sequence__fini(interfaces__action__Increase_GetResult_Request__Sequence * array);

/// Create array of action/Increase messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Increase_GetResult_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_GetResult_Request__Sequence *
interfaces__action__Increase_GetResult_Request__Sequence__create(size_t size);

/// Destroy array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_GetResult_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_GetResult_Request__Sequence__destroy(interfaces__action__Increase_GetResult_Request__Sequence * array);

/// Initialize action/Increase message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Increase_GetResult_Response
 * )) before or use
 * interfaces__action__Increase_GetResult_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_GetResult_Response__init(interfaces__action__Increase_GetResult_Response * msg);

/// Finalize action/Increase message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_GetResult_Response__fini(interfaces__action__Increase_GetResult_Response * msg);

/// Create action/Increase message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Increase_GetResult_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_GetResult_Response *
interfaces__action__Increase_GetResult_Response__create();

/// Destroy action/Increase message.
/**
 * It calls
 * interfaces__action__Increase_GetResult_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_GetResult_Response__destroy(interfaces__action__Increase_GetResult_Response * msg);


/// Initialize array of action/Increase messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Increase_GetResult_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_GetResult_Response__Sequence__init(interfaces__action__Increase_GetResult_Response__Sequence * array, size_t size);

/// Finalize array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_GetResult_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_GetResult_Response__Sequence__fini(interfaces__action__Increase_GetResult_Response__Sequence * array);

/// Create array of action/Increase messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Increase_GetResult_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_GetResult_Response__Sequence *
interfaces__action__Increase_GetResult_Response__Sequence__create(size_t size);

/// Destroy array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_GetResult_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_GetResult_Response__Sequence__destroy(interfaces__action__Increase_GetResult_Response__Sequence * array);

/// Initialize action/Increase message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * interfaces__action__Increase_FeedbackMessage
 * )) before or use
 * interfaces__action__Increase_FeedbackMessage__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_FeedbackMessage__init(interfaces__action__Increase_FeedbackMessage * msg);

/// Finalize action/Increase message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_FeedbackMessage__fini(interfaces__action__Increase_FeedbackMessage * msg);

/// Create action/Increase message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * interfaces__action__Increase_FeedbackMessage__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_FeedbackMessage *
interfaces__action__Increase_FeedbackMessage__create();

/// Destroy action/Increase message.
/**
 * It calls
 * interfaces__action__Increase_FeedbackMessage__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_FeedbackMessage__destroy(interfaces__action__Increase_FeedbackMessage * msg);


/// Initialize array of action/Increase messages.
/**
 * It allocates the memory for the number of elements and calls
 * interfaces__action__Increase_FeedbackMessage__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
bool
interfaces__action__Increase_FeedbackMessage__Sequence__init(interfaces__action__Increase_FeedbackMessage__Sequence * array, size_t size);

/// Finalize array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_FeedbackMessage__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_FeedbackMessage__Sequence__fini(interfaces__action__Increase_FeedbackMessage__Sequence * array);

/// Create array of action/Increase messages.
/**
 * It allocates the memory for the array and calls
 * interfaces__action__Increase_FeedbackMessage__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
interfaces__action__Increase_FeedbackMessage__Sequence *
interfaces__action__Increase_FeedbackMessage__Sequence__create(size_t size);

/// Destroy array of action/Increase messages.
/**
 * It calls
 * interfaces__action__Increase_FeedbackMessage__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_interfaces
void
interfaces__action__Increase_FeedbackMessage__Sequence__destroy(interfaces__action__Increase_FeedbackMessage__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // INTERFACES__ACTION__INCREASE__FUNCTIONS_H_
