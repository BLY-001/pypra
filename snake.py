import tkinter as tk
import random

# --- GAME CONFIGURATION ---
GRID_COUNT = 20          # Number of rows/columns
GRID_SIZE = 25           # Size of each cell in pixels
WINDOW_SIZE = GRID_COUNT * GRID_SIZE
INITIAL_SPEED = 150      # Initial game tick delay in milliseconds
SPEED_INCREMENT = 3      # Speed reduction per food item (makes snake faster)
MIN_SPEED = 40           # Maximum cap on game speed

# Colors for the Nokia Snake Xenzia retro theme
BG_COLOR = "#A3B899"      # Classic monochrome greenish background
SNAKE_COLOR = "#1C2418"   # Dark pixel snake
FOOD_COLOR = "#33422F"    # Dark pixel food

class SnakeXenzia:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Xenzia")
        self.root.resizable(False, False)

        # Main Layout: Score Frame and Game Canvas
        self.score_frame = tk.Frame(root, bg=BG_COLOR)
        self.score_frame.pack(fill="x")
        
        self.score_label = tk.Label(
            self.score_frame, 
            text="SCORE: 0", 
            font=("Courier", 16, "bold"), 
            bg=BG_COLOR, 
            fg=SNAKE_COLOR
        )
        self.score_label.pack(side="left", padx=10, pady=5)

        self.canvas = tk.Canvas(
            root, 
            width=WINDOW_SIZE, 
            height=WINDOW_SIZE, 
            bg=BG_COLOR, 
            highlightthickness=0
        )
        self.canvas.pack()

        # Input Bindings
        self.root.bind("<Up>", lambda e: self.change_direction("UP"))
        self.root.bind("<Down>", lambda e: self.change_direction("DOWN"))
        self.root.bind("<Left>", lambda e: self.change_direction("LEFT"))
        self.root.bind("<Right>", lambda e: self.change_direction("RIGHT"))
        self.root.bind("<space>", lambda e: self.reset_game())

        self.reset_game()

    def reset_game(self):
        # State Initialization
        self.score = 0
        self.speed = INITIAL_SPEED
        self.direction = "RIGHT"
        self.next_direction = "RIGHT"
        self.game_over = False

        # Start snake in the middle (3 blocks long)
        mid = GRID_COUNT // 2
        self.snake = [[mid, mid], [mid - 1, mid], [mid - 2, mid]]
        
        self.score_label.config(text="SCORE: 0")
        self.spawn_food()
        self.game_tick()

    def spawn_food(self):
        while True:
            self.food = [random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1)]
            if self.food not in self.snake:
                break

    def change_direction(self, new_dir):
        # Prevent the snake from turning instantly back into itself
        opposites = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_dir != opposites.get(self.direction):
            self.next_direction = new_dir

    def game_tick(self):
        if self.game_over:
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]

        # Calculate new head position
        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        # Nokia Xenzia Boundary Logic: Wrap around the screen edges
        head_x %= GRID_COUNT
        head_y %= GRID_COUNT

        new_head = [head_x, head_y]

        # Self-Collision Validation
        if new_head in self.snake:
            self.end_game()
            return

        # Move Snake Forward
        self.snake.insert(0, new_head)

        # Food Consumption Validation
        if new_head == self.food:
            self.score += 1
            self.score_label.config(text=f"SCORE: {self.score}")
            # Gradually speed up the game loop
            self.speed = max(MIN_SPEED, self.speed - SPEED_INCREMENT)
            self.spawn_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()

        self.render_frame()
        self.root.after(self.speed, self.game_tick)

    def render_frame(self):
        self.canvas.delete("all")

        # Draw Food
        fx, fy = self.food
        self.canvas.create_rectangle(
            fx * GRID_SIZE + 2, fy * GRID_SIZE + 2,
            (fx + 1) * GRID_SIZE - 2, (fy + 1) * GRID_SIZE - 2,
            fill=FOOD_COLOR, outline=BG_COLOR
        )

        # Draw Snake Body
        for segment in self.snake:
            sx, sy = segment
            self.canvas.create_rectangle(
                sx * GRID_SIZE + 1, sy * GRID_SIZE + 1,
                (sx + 1) * GRID_SIZE - 1, (sy + 1) * GRID_SIZE - 1,
                fill=SNAKE_COLOR, outline=BG_COLOR
            )

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(
            WINDOW_SIZE // 2, WINDOW_SIZE // 2 - 20,
            text="GAME OVER", font=("Courier", 24, "bold"), fill=SNAKE_COLOR
        )
        self.canvas.create_text(
            WINDOW_SIZE // 2, WINDOW_SIZE // 2 + 20,
            text="Press SPACE to Restart", font=("Courier", 14), fill=SNAKE_COLOR
        )

if __name__ == "__main__":
    main_window = tk.Tk()
    app = SnakeXenzia(main_window)
    main_window.mainloop()
