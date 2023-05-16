extends KinematicBody2D

var velocity = Vector2()
export var speed = 150;
var can_follow = false 

func _physics_process(delta):
	if can_follow == true:
		var player = get_parent().get_node("player")
		velocity = position.direction_to(player.position)*speed
		velocity = move_and_slide(velocity)


func _on_Detector_body_entered(body):
	if body.name == "player":
		can_follow = true

func _on_Detector_body_exited(body):
	if body.name == "player":
		can_follow = false


func _on_Area2D_area_entered(area):
	if area.name == "Kill":
		queue_free()
