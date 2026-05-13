extends CharacterBody2D

func _physics_process(delta: float) -> void: 
	var movement = Input.get_axis("ui_left","ui_right")
