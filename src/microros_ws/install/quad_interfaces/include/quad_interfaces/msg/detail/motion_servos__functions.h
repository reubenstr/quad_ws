// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from quad_interfaces:msg/MotionServos.idl
// generated code does not contain a copyright notice

#ifndef QUAD_INTERFACES__MSG__DETAIL__MOTION_SERVOS__FUNCTIONS_H_
#define QUAD_INTERFACES__MSG__DETAIL__MOTION_SERVOS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "quad_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "quad_interfaces/msg/detail/motion_servos__struct.h"

/// Initialize msg/MotionServos message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * quad_interfaces__msg__MotionServos
 * )) before or use
 * quad_interfaces__msg__MotionServos__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_quad_interfaces
bool
quad_interfaces__msg__MotionServos__init(quad_interfaces__msg__MotionServos * msg);

/// Finalize msg/MotionServos message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_quad_interfaces
void
quad_interfaces__msg__MotionServos__fini(quad_interfaces__msg__MotionServos * msg);

/// Create msg/MotionServos message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * quad_interfaces__msg__MotionServos__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_quad_interfaces
quad_interfaces__msg__MotionServos *
quad_interfaces__msg__MotionServos__create();

/// Destroy msg/MotionServos message.
/**
 * It calls
 * quad_interfaces__msg__MotionServos__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_quad_interfaces
void
quad_interfaces__msg__MotionServos__destroy(quad_interfaces__msg__MotionServos * msg);


/// Initialize array of msg/MotionServos messages.
/**
 * It allocates the memory for the number of elements and calls
 * quad_interfaces__msg__MotionServos__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_quad_interfaces
bool
quad_interfaces__msg__MotionServos__Sequence__init(quad_interfaces__msg__MotionServos__Sequence * array, size_t size);

/// Finalize array of msg/MotionServos messages.
/**
 * It calls
 * quad_interfaces__msg__MotionServos__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_quad_interfaces
void
quad_interfaces__msg__MotionServos__Sequence__fini(quad_interfaces__msg__MotionServos__Sequence * array);

/// Create array of msg/MotionServos messages.
/**
 * It allocates the memory for the array and calls
 * quad_interfaces__msg__MotionServos__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_quad_interfaces
quad_interfaces__msg__MotionServos__Sequence *
quad_interfaces__msg__MotionServos__Sequence__create(size_t size);

/// Destroy array of msg/MotionServos messages.
/**
 * It calls
 * quad_interfaces__msg__MotionServos__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_quad_interfaces
void
quad_interfaces__msg__MotionServos__Sequence__destroy(quad_interfaces__msg__MotionServos__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // QUAD_INTERFACES__MSG__DETAIL__MOTION_SERVOS__FUNCTIONS_H_