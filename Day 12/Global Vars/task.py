# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies # try not to modify global scope
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# function without modifying global scope
def increasing_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increasing_enemies(enemies)
print(f"enemies outside function: {enemies}")


