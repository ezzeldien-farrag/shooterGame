extends KinematicBody2D

export var bullet_speed = 1000
export var fire_rate = 0.1

var bullet = preload("res://bullet.tscn")
var can_fire = true

export (int) var speed=200
var velocity=Vector2()

func _physics_process(delta):
	
	velocity=Vector2()
	look_at(get_global_mouse_position())
	if Input.is_action_pressed("up"):
		velocity.y -=1
	if Input.is_action_pressed("down"):
		velocity.y +=1
	if Input.is_action_pressed("right"):
		velocity.x +=1
	if Input.is_action_pressed("left"):
		velocity.x -=1
	velocity = velocity.normalized() * speed
	velocity = move_and_slide(velocity)
	
	
	if Input.is_action_pressed("fire") and can_fire:
		var bullet_instance = bullet.instance()
		bullet_instance.position = $BulletPoint.get_global_position()
		bullet_instance.rotation_degrees = rotation_degrees
		bullet_instance.apply_impulse(Vector2(),Vector2(bullet_speed,0).rotated(rotation))
		get_tree().get_root().add_child(bullet_instance)
		can_fire = false
		yield(get_tree().create_timer(fire_rate),"timeout")
		can_fire = true


func _on_Area2D_body_entered(body):
	if "enemy" in body.name:
		die()
		
func die():
	get_tree().reload_current_scene()
