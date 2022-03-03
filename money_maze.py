import random as rand

def main():
  # init
  size = 5
  coords = (size // 2, size // 2)
  maze = [
    [
      rand.randint(0, 9)
      for _ in range(size)
    ]
    for _ in range(size)
  ]
  maze[coords[0]][coords[1]] = 0
  score = 0
  
  # ask for move
  while True:
    clear()
    show(maze, coords, score)
    coords, maze, score = move(coords, maze, score)

vectors = {"W": (0, 1), "A": (-1, 0), "S": (0, -1), "D": (1, 0)}
def move(coords, maze, score) -> tuple:
  new_coords = ()
  while len(new_coords) == 0:
    # input
    direction = input("\nEnter a direction (W, A, S, D): ").upper()
    if direction not in vectors.keys():
      continue
    
    # calculate new coords
    movement = vectors[direction]
    new = (coords[0] - movement[1], coords[1] + movement[0])
    # check if coords are valid
    if 0 <= new[0] < len(maze) and 0 <= new[1] < len(maze[0]):
      new_coords = new
  
  # add score
  score += maze[new_coords[0]][new_coords[1]]
  # erase score from new place
  maze[new_coords[0]][new_coords[1]] = 0
  
  return new_coords, maze, score
  
fmt = "\033[31m\33[5m"
end_fmt = "\033[0m"
def show(maze, coords, score):
  for i, row in enumerate(maze):
    for j, val in enumerate(row):
      should_highlight = i == coords[0] and j == coords[1]
      
      if should_highlight:
        print(fmt, end="")
      print(f"{val}", end=" ")
      
      if should_highlight:
        print(end_fmt, end="")
        
    print()
  
  print(f"Score: {score}")

def clear():
  print("\n" * 100)
  
if __name__ == "__main__":
  main()