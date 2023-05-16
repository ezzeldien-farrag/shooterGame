extends RigidBody2D

export var speed = 500
var velocity = Vector2.ZERO

func _integrate_forces(state):
	# Move the bullet based on its velocity
	state.linear_velocity = velocity

func _on_VisibilityNotifier2D_screen_exited():
	# Remove the bullet when it goes off-screen
	queue_free()

