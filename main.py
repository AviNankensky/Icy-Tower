import random
import pygame
import sys
import socket
import threading
import json
import time
from PlatformBlock import PlatformBlock
from Player import Player
from floor import Floor
from Wall import Wall
from create_platforms import create_platforms  # הקפד להשתמש בשם הנכון

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("המשחק שלי")
clock = pygame.time.Clock()

background = pygame.image.load("assets/stoneWall.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


def send_data_to_server(data):
    """Sends player data to the server."""
    global client_socket
    if client_socket:
        try:
            message = json.dumps(data)
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending data: {e}")
            client_socket.close()
            client_socket = None

            
player = pygame.sprite.GroupSingle()
player.add(Player(True, network_sender=send_data_to_server))

player2In = Player(False)
player2 = pygame.sprite.GroupSingle()
player2.add(player2In)


floor = pygame.sprite.Group()
floor.add(Floor(400, 600, 800, 100))

# קירות צדדיים
walls = pygame.sprite.Group()
walls.add(Wall(0, HEIGHT, HEIGHT))      
walls.add(Wall(WIDTH, HEIGHT, HEIGHT))  

# יצירת פלטפורמות רנדומליות
platformBlocks = create_platforms(num_platforms=10, width=100, height=20, screen_width=WIDTH, screen_height=HEIGHT)

# --- Network Client Code ---
client_socket = None

def receive_messages():
    """Handles receiving messages from the server in a separate thread."""
    global client_socket
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                try:
                    # Simple handling for potentially concatenated JSON messages
                    for part in message.strip().replace('}{', '}\n{').split('\n'):
                        if not part:
                            continue
                        data = json.loads(part)
                        # The updatePlayer2 function is already in this file.
                        updatePlayer2(data['x'], data['y'])
                except (json.JSONDecodeError, KeyError) as e:
                    print(f"Error processing received data: {e} - Data: '{message}'")
            else:
                # Server disconnected
                print("Server connection lost.")
                break
        except Exception as e:
            print(f"An error occurred in receive_messages: {e}")
            break
    if client_socket:
        client_socket.close()
        client_socket = None


def initialize_client():
    """Initializes the socket connection and starts the receiving thread."""
    global client_socket
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connecting to the IP you specified
        client_socket.connect(('192.168.1.240', 9999))
        
        # Start a thread to listen for messages from the server
        receive_thread = threading.Thread(target=receive_messages, daemon=True)
        receive_thread.start()
        print("Successfully connected to the server.")
    except Exception as e:
        print(f"Failed to connect to server: {e}")
        client_socket = None
# --- End Network Client Code ---

def onRun():
    if player.sprite.rect.top < HEIGHT // 3:
        scroll_amount = HEIGHT // 3 - player.sprite.rect.top
        player.sprite.rect.top = HEIGHT // 3

        # להזיז את כל הפלטפורמות
        for platform in platformBlocks:
            platform.rect.y += scroll_amount
        for floor_block in floor:
            floor_block.rect.y += scroll_amount

        for platform in list(platformBlocks):
            if platform.rect.top > HEIGHT + 50:  # אם ירדה מתחת למסך
                platformBlocks.remove(platform)   # הסרה
                # יצירת פלטפורמה חדשה למעלה
                new_x = random.randint(50, WIDTH - 50)
                new_y = random.randint(-100, -20)  # מעל המסך
                platformBlocks.add(PlatformBlock(new_x, new_y))

def updatePlayer2(x , y):
    player2In.updatePos(x,y)

initialize_client()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    floor.draw(screen)
    walls.draw(screen)
    platformBlocks.draw(screen)

    player.update(floor, walls, platformBlocks)
    player.draw(screen)

    # example of player 2
    player2.draw(screen)
    # player2In.updatePos(player2In.getX(),player2In.getY() - 1)

    onRun()

    pygame.display.flip()
    clock.tick(60)

if client_socket:
    client_socket.close()
pygame.quit()
sys.exit()
