extends CharacterBody3D

@export var speed := 7.0
@export var gravity := 50.0

var _velocity := Vector3.ZERO

@onready var _spring_arm: SpringArm3D = $SpringArm3D
@onready var _model: CSGBox3D = $CSGBox3D

func _physics_process(delta: float) -> void:
		var move_direction := Vector3.ZERO
		move_direction.x = Input.get_action_raw_strength("right") - Input.get_action_raw_strength("left")
		move_direction.z = Input.get_action_raw_strength("back") - Input.get_action_raw_strength("forward")
		move_direction = move_direction.rotated(Vector3.UP, _spring_arm.rotation.y).normalized()
		
		_velocity.x = move_direction.x * speed
		_velocity.z = move_direction.z * speed
		_velocity.y -= gravity * delta
		
func _process(delta: float) -> void:
	_spring_arm.translation = Translation
	
