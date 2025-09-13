extends CharacterBody3D

const SPEED := 5.0
const JUMP_VELOCITY := 4.5

@onready var ai_controller: Node3D = $AIController3D

func _physics_process(delta: float) -> void:
	var input_dir = Input.get_vector("left", "right", "forward", "back")
	var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	
	if direction != Vector3.ZERO:
		velocity.x = direction.x * SPEED
		velocity.z = direction.z * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	if not is_on_floor():
		velocity.y -= ProjectSettings.get_setting("physics/3d/default_gravity") * delta
		
	velocity.x = ai_controller.move.x
	velocity.z = ai_controller.move.y

	move_and_slide()


func _on_target_body_entered(body: Node3D) -> void:
	position = Vector3(-2.911, 0.635, 0)
	ai_controller.reward += 1.0

func _on_area_3d_body_entered(body: Node3D) -> void:
	position = Vector3(-2.911, 0.635, 0)
	ai_controller.reward -= 1.0
	ai_controller.reset()
