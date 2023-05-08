extends KinematicBody2D

var movespeed=700
var bullet_speed = 2000
var bullet = preload("res://pics/Game/bullet.tscn")
func _ready():
	pass # Replace with function body.

func _physics_process(delta):
	
	var motion=Vector2()
	if Input.is_action_pressed("move_up"):
		motion.y -=1
	if Input.is_action_pressed("move_down"):
		motion.y +=1
	if Input.is_action_pressed("move_right"):
		motion.x +=1
	if Input.is_action_pressed("move-left"):
		motion.x -=1
	motion = motion.normalized()
	motion = move_and_slide(motion * movespeed)
	look_at(get_global_mouse_position())
	
	if Input.is_action_just_pressed("fire"):
		var bullet_instance = bullet.instance()
		bullet_instance.position = get_global_position()
		bullet_instance.rotation_degrees=rotation_degrees
		bullet_instance.apply_impulse(Vector2(),Vector2(bullet_speed,0).rotated(rotation))
		get_tree().get_root().call_deferred("add_child",bullet_instance)
	
	
	
