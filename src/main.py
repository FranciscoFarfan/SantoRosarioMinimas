import flet as ft

import json
import random
from datetime import datetime
from pathlib import Path


import os

class RosarioApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Santo Rosario"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.theme = ft.Theme(color_scheme_seed=ft.Colors.CYAN)
        self.page.padding = 0
        
        # Paths
        self.base_path = Path(__file__).parent
        # For Flet assets, use relative paths from the assets directory
        # Do not use absolute paths for src properties
        self.audio_path = "/Audios"
        self.image_path = "/Caratulas"
        
        # Load reflections
        with open(self.base_path / "reflections.json", "r", encoding="utf-8") as f:
            self.reflections_data = json.load(f)
        
        # Audio control (will be initialized when needed)
        self.audio = None
        
        # Playlist management
        self.playlist = []
        self.current_track_index = 0
        self.is_playing = False
        self.include_cantos = False
        self.current_duration = 0
        self.current_position = 0
        self.current_position = 0
        self.is_seeking = False
        self.playback_speed = 1.0
        
        # UI Components
        self.setup_ui()
        
    def init_audio(self):
        """Initialize or re-initialize audio control"""
        if self.audio in self.page.overlay:
            self.page.overlay.remove(self.audio)
        
        self.audio = ft.Audio(
            autoplay=False,
            on_state_changed=self.on_audio_state_changed,
            on_position_changed=self.on_position_changed,
            on_duration_changed=self.on_duration_changed,
            playback_rate=self.playback_speed,
        )
        self.page.overlay.append(self.audio)
        self.page.update()

    def list_files(self, startpath):
        text_out = ""
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            text_out += '{}{}/\n'.format(indent, os.path.basename(root))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                text_out += '{}{}\n'.format(subindent, f)
        return text_out

    def show_debug_dialog(self, e):
        files_str = self.list_files(str(self.base_path))
        
        dlg = ft.AlertDialog(
            title=ft.Text("Debug Files"),
            content=ft.Column([
                ft.Text("Base Path: " + str(self.base_path)),
                ft.Text("Assets Dir: " + str(Path(__file__).parent / "assets")),
                ft.Container(
                    content=ft.Text(files_str, size=10, font_family="monospace"),
                    height=300,
                    width=300,
                )
            ], scroll=ft.ScrollMode.AUTO, height=400),
            actions=[
                ft.TextButton("Close", on_click=lambda x: self.page.close(dlg))
            ],
        )
        self.page.open(dlg)

    def setup_ui(self):
        """Setup the main UI"""
        # Main menu view
        self.main_menu = ft.Column(
            controls=[
                ft.Text("Santo Rosario", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Image(
                    src="./Fatima.jpg",
                    width=200,
                    height=200,
                    fit=ft.ImageFit.COVER,
                    border_radius=20,
                ),
                ft.Divider(color=ft.Colors.WHITE24),
                ft.ElevatedButton(
                    "Rosario del Día",
                    icon=ft.Icons.CALENDAR_TODAY,
                    on_click=self.start_daily_rosary,
                    width=300,
                    height=60,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor=ft.Colors.CYAN_700,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                ),
                ft.Text("Seleccionar Rosario:", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Gozosos",
                            on_click=self.start_rosary_gozosos,
                            width=95,
                            height=50,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.LIGHT_BLUE_500,
                                shape=ft.RoundedRectangleBorder(radius=8),
                            ),
                        ),
                        ft.ElevatedButton(
                            "Dolorosos",
                            on_click=self.start_rosary_dolorosos,
                            width=95,
                            height=50,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.BLUE_GREY_500,
                                shape=ft.RoundedRectangleBorder(radius=8),
                            ),
                        ),
                        ft.ElevatedButton(
                            "Gloriosos",
                            on_click=self.start_rosary_gloriosos,
                            width=95,
                            height=50,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.AMBER_600,
                                shape=ft.RoundedRectangleBorder(radius=8),
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                ft.ElevatedButton(
                    "Rezar Misterio Individual",
                    icon=ft.Icons.PLAY_CIRCLE,
                    on_click=self.play_individual_mystery,
                    width=300,
                    height=60,
                    style=ft.ButtonStyle(
                        color=ft.Colors.CYAN_900,
                        bgcolor=ft.Colors.CYAN_100,
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                ),
                ft.Container(
                    content=ft.Checkbox(
                        label="Incluir Cantos",
                        value=False,
                        on_change=self.toggle_cantos,
                        fill_color=ft.Colors.CYAN_700,
                        label_style=ft.TextStyle(color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD, size=16),
                    ),
                    bgcolor=ft.Colors.WHITE24,
                    padding=10,
                    border_radius=10,
                ),
                ft.IconButton(
                    icon=ft.Icons.INFO_OUTLINE,
                    icon_color=ft.Colors.WHITE,
                    on_click=lambda _: self.page.launch_url("https://franciscofarfan.github.io/FSSPX/Rosario/Rosario.html"),
                    tooltip="Acerca de",
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        )
        
        # Player view
        self.album_art = ft.Image(
            src="",
            width=300,
            height=300,
            fit=ft.ImageFit.COVER,
            border_radius=10,
        )
        
        self.track_header = ft.Text("", size=16, color=ft.Colors.CYAN_900, weight=ft.FontWeight.BOLD)
        self.track_title = ft.Text("", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER, color=ft.Colors.BLUE_GREY_900)
        self.reflection_text = ft.Text("", size=14, text_align=ft.TextAlign.CENTER, italic=True)
        
        self.play_pause_button = ft.IconButton(
            icon=ft.Icons.PLAY_ARROW,
            icon_size=50,
            icon_color=ft.Colors.CYAN_700,
            on_click=self.toggle_play_pause,
        )
        
        self.position_slider = ft.Slider(
            min=0,
            max=100,
            value=0,
            active_color=ft.Colors.CYAN_700,
            on_change=self.on_slider_change,
            on_change_end=self.on_slider_change_end,
        )
        
        self.time_text = ft.Text("0:00 / 0:00", size=12)

        self.speed_dropdown = ft.Dropdown(
            width=100,
            value="1.0x",
            options=[
                ft.dropdown.Option("0.85x"),
                ft.dropdown.Option("0.90x"),
                ft.dropdown.Option("0.95x"),
                ft.dropdown.Option("1.0x"),
                ft.dropdown.Option("1.1"),
                ft.dropdown.Option("1.2x"),
                ft.dropdown.Option("1.3x"),
                ft.dropdown.Option("1.4x"),
                ft.dropdown.Option("1.5x"),
            ],
            on_change=self.change_playback_speed,
            text_size=12,
            content_padding=5,
            filled=True,
            bgcolor=ft.Colors.GREY_100,
            border_radius=10,
        )
        
        self.player_view = ft.Column(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    on_click=self.back_to_menu,
                    icon_color=ft.Colors.CYAN_700,
                ),
                # Container for card-like effect on player
                ft.Container(
                    content=ft.Column(
                        controls=[
                            self.album_art,
                            self.track_header,
                            self.track_title,
                            ft.Container(
                                content=self.reflection_text,
                                padding=10,
                                height=100,
                            ),
                            # Progress Roadmap
                            ft.Row(
                                controls=[
                                    self.create_roadmap_item("Inicio", "inicio"),
                                    ft.Icon(ft.Icons.ARROW_RIGHT, size=16, color=ft.Colors.GREY_400),
                                    self.create_roadmap_item("Presentación", "presentacion"),
                                    ft.Icon(ft.Icons.ARROW_RIGHT, size=16, color=ft.Colors.GREY_400),
                                    self.create_roadmap_item("Misterio", "misterio"),
                                    ft.Icon(ft.Icons.ARROW_RIGHT, size=16, color=ft.Colors.GREY_400),
                                    self.create_roadmap_item("Canto", "canto"),
                                    ft.Icon(ft.Icons.ARROW_RIGHT, size=16, color=ft.Colors.GREY_400),
                                    self.create_roadmap_item("Final", "final"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5,
                            ),
                            self.position_slider,
                            ft.Row(
                                controls=[
                                    self.time_text,
                                    ft.Container(expand=True),
                                    ft.Text("Velocidad:", size=12, weight=ft.FontWeight.BOLD),
                                    self.speed_dropdown,
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.SKIP_PREVIOUS,
                                        icon_size=40,
                                        on_click=self.previous_track,
                                    ),
                                    self.play_pause_button,
                                    ft.IconButton(
                                        icon=ft.Icons.SKIP_NEXT,
                                        icon_size=40,
                                        on_click=self.next_track,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=20,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    bgcolor=ft.Colors.WHITE,
                    padding=20,
                    border_radius=20,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.Colors.BLUE_GREY_100,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        )
        
        # Stack layout with background
        self.layout = ft.Stack(
            controls=[
                ft.Image(
                    src="./cielo.jpg",
                    fit=ft.ImageFit.FIT_WIDTH,
                    opacity=1.0,
                    left=0,
                    right=0,
                    top=0,
                ),
                ft.Container(
                    content=self.main_menu,
                    alignment=ft.alignment.center,
                    padding=20,
                ),
                ft.Container(
                    content=self.player_view,
                    alignment=ft.alignment.center,
                    padding=20,
                    visible=False,
                ),
            ],
            expand=True,
        )
        
        # Add to page
        self.page.add(self.layout)

    
    def create_roadmap_item(self, label, tag):
        """Create a roadmap item container"""
        return ft.Container(
            content=ft.Text(label, size=10, weight=ft.FontWeight.BOLD),
            padding=5,
            border_radius=5,
            bgcolor=ft.Colors.GREY_200,
            data=tag,  # Store the tag to identify this item
        )

    def update_roadmap(self, current_type):
        """Update the roadmap highlights"""
      
        player_content_col = self.player_view.controls[1].content
        roadmap_row = player_content_col.controls[4]
        
        for control in roadmap_row.controls:
            if isinstance(control, ft.Container):
                if control.data == current_type:
                    control.bgcolor = ft.Colors.BLUE_200
                    control.content.color = ft.Colors.BLUE_900
                else:
                    control.bgcolor = ft.Colors.GREY_200
                    control.content.color = ft.Colors.BLACK
        
        self.page.update()

    def toggle_cantos(self, e):
        """Toggle the include cantos checkbox"""
        self.include_cantos = e.control.value
    
    def get_mysteries_for_day(self):
        """Get the mysteries for the current day of the week"""
        day = datetime.now().weekday()  # 0=Monday, 6=Sunday
        
        if day in [0, 5]:  # Monday, Saturday
            return "gozosos"
        elif day in [1, 4]:  # Tuesday, Friday
            return "dolorosos"
        elif day in [2, 6]:  # Wednesday, Sunday
            return "gloriosos"
        else:  # Thursday (Luminosos - using Gloriosos as fallback)
            return "gloriosos"
    
    def build_playlist(self, rosary_type):
        """Build the playlist for a complete rosary"""
        self.playlist = []
        
        # Add Inicio
        self.playlist.append({
            "audio": "Inicio.mp3",
            "image": "Inicio.jpg",
            "title": "Inicio del Rosario",
            "header": "Oraciones Iniciales",
            "reflection": "Preparemos nuestro corazón para rezar el Santo Rosario con devoción.",
            "type": "inicio"
        })
        
        # Determine mystery range
        if rosary_type == "gozosos":
            mysteries = range(1, 6)
            canto = "CantoGozosos.mp3"
            canto_img = "CantoGozosos.jpg"
        elif rosary_type == "dolorosos":
            mysteries = range(6, 11)
            canto = "CantoDolorosos.mp3"
            canto_img = "CantoDolorosos.jpg"
        else:  # gloriosos
            mysteries = range(11, 16)
            canto = "CantoGloriosos.mp3"
            canto_img = "CantoGloriosos.jpg"
        
        # Add mysteries: Presentation (M1-M15) -> Mystery itself (M) -> Canto (optional)
        for m in mysteries:
            mystery_key = f"M{m}"
            mystery_data = self.reflections_data[mystery_key]
            selected_reflection = random.choice(mystery_data["reflexiones"])
            mystery_image = f"M{m}.jpg"
            mystery_title = mystery_data["nombre"]
            mystery_header = mystery_data.get("header", "")
            
            # 1. Presentation of the mystery (M1-M15 audio)
            self.playlist.append({
                "audio": f"M{m}.mp3",
                "image": mystery_image,
                "title": mystery_title,
                "header": mystery_header,
                "reflection": selected_reflection,
                "type": "presentacion"
            })
            
            # 2. The mystery itself (M.mp3) - same image and reflection
            self.playlist.append({
                "audio": "M.mp3",
                "image": mystery_image,
                "title": mystery_title,
                "header": mystery_header,
                "reflection": selected_reflection,
                "type": "misterio"
            })
            
            # 3. Canto (if enabled) - same image and reflection
            if self.include_cantos:
                self.playlist.append({
                    "audio": canto,
                    "image": mystery_image,
                    "title": mystery_title,
                    "header": mystery_header,
                    "reflection": selected_reflection,
                    "type": "canto"
                })
        
        # Add Final
        self.playlist.append({
            "audio": "Final.mp3",
            "image": "Final.jpg",
            "title": "Final del Rosario",
            "header": "Oraciones Finales",
            "reflection": "Demos gracias a Dios por este tiempo de oración.",
            "type": "final"
        })
    
    def start_daily_rosary(self, e):
        """Start the rosary for today"""
        rosary_type = self.get_mysteries_for_day()
        self.build_playlist(rosary_type)
        self.start_playback()
    
    
    def start_rosary_gozosos(self, e):
        """Start Gozosos rosary"""
        self.build_playlist("gozosos")
        self.start_playback()
    
    def start_rosary_dolorosos(self, e):
        """Start Dolorosos rosary"""
        self.build_playlist("dolorosos")
        self.start_playback()
    
    def start_rosary_gloriosos(self, e):
        """Start Gloriosos rosary"""
        self.build_playlist("gloriosos")
        self.start_playback()
    
    def play_individual_mystery(self, e):
        """Play the individual mystery M.mp3"""
        mystery_data = self.reflections_data["M"]
        self.playlist = [{
            "audio": "M.mp3",
            "image": "M.jpg",
            "title": mystery_data["nombre"],
            "header": mystery_data.get("header", "Misterio"),
            "reflection": random.choice(mystery_data["reflexiones"]),
            "type": "misterio"
        }]
        self.start_playback()
    
    def start_playback(self):
        """Start playing the playlist"""
        if not self.playlist:
            return
        
        # Initialize fresh audio control
        self.init_audio()
        
        self.current_track_index = 0
        self.show_player()
        self.load_track(0)
        # No need to call play(), load_track handles it with autoplay
    
    def load_track(self, index):
        """Load a track from the playlist"""
        if 0 <= index < len(self.playlist):
            track = self.playlist[index]
            
            # Re-initialize audio to ensure settings like playback_speed are applied correctly
            # Remove existing audio from overlay if present
            if self.audio and self.audio in self.page.overlay:
                self.page.overlay.remove(self.audio)
                self.audio.release()
            
            # Create new audio instance for the track
            audio_file = f"{self.audio_path}/{track['audio']}"
            self.audio = ft.Audio(
                src=audio_file,
                autoplay=True,
                playback_rate=self.playback_speed,
                on_state_changed=self.on_audio_state_changed,
                on_position_changed=self.on_position_changed,
                on_duration_changed=self.on_duration_changed,
            )
            self.page.overlay.append(self.audio)
            self.page.update()
            
            # Update UI
            image_file = f"{self.image_path}/{track['image']}"
            self.album_art.src = image_file
            self.track_header.value = track.get("header", "")
            self.track_title.value = track["title"]
            self.reflection_text.value = track["reflection"]
            
            # Update Roadmap
            self.update_roadmap(track["type"])
            
            self.current_track_index = index
            self.page.update()
    
    def show_player(self):
        """Show the player view and hide the menu"""
        # Toggle container visibility in the stack
        self.layout.controls[1].visible = False # Main Menu Container
        self.layout.controls[2].visible = True  # Player View Container
        self.page.update()
    
    def back_to_menu(self, e):
        """Go back to the main menu"""
        if self.audio:
            if self.is_playing:
                self.audio.pause()
            self.audio.release()
            if self.audio in self.page.overlay:
                self.page.overlay.remove(self.audio)
            self.audio = None
            
        self.playlist = []
        self.current_track_index = 0
        self.is_playing = False
        
        # Toggle container visibility
        self.layout.controls[2].visible = False # Player View
        self.layout.controls[1].visible = True  # Main Menu
        self.page.update()
    
    def toggle_play_pause(self, e):
        """Toggle play/pause"""
        if self.is_playing:
            self.audio.pause()
        else:
            self.audio.resume()
    
    def previous_track(self, e):
        """Go to previous track"""
        if self.current_track_index > 0:
            self.load_track(self.current_track_index - 1)
    
    def next_track(self, e):
        """Go to next track"""
        if self.current_track_index < len(self.playlist) - 1:
            self.load_track(self.current_track_index + 1)
        else:
            # End of playlist
            self.back_to_menu(None)
    
    def on_audio_state_changed(self, e):
        """Handle audio state changes"""
        if e.data == "playing":
            self.is_playing = True
            self.play_pause_button.icon = ft.Icons.PAUSE
        elif e.data == "paused":
            self.is_playing = False
            self.play_pause_button.icon = ft.Icons.PLAY_ARROW
        elif e.data == "completed":
            # Auto-advance to next track
            self.next_track(None)
        
        self.page.update()
    
    def on_position_changed(self, e):
        """Handle position changes"""
        if not self.is_seeking:
            self.current_position = int(e.data)
            if self.current_duration > 0:
                self.position_slider.value = (self.current_position / self.current_duration) * 100
            self.update_time_display()
    
    def on_duration_changed(self, e):
        """Handle duration changes"""
        self.current_duration = int(e.data)
        self.update_time_display()
    
    def on_slider_change(self, e):
        """Handle slider drag"""
        self.is_seeking = True
    
    def on_slider_change_end(self, e):
        """Handle slider release"""
        self.is_seeking = False
        if self.current_duration > 0:
            new_position = int((e.control.value / 100) * self.current_duration)
            self.audio.seek(new_position)
    
    def update_time_display(self):
        """Update the time display"""
        current = self.format_time(self.current_position)
        total = self.format_time(self.current_duration)
        self.time_text.value = f"{current} / {total}"
        self.page.update()
    
    def format_time(self, milliseconds):
        """Format milliseconds to MM:SS"""
        seconds = milliseconds // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds:02d}"
    
    def change_playback_speed(self, e):
        """Change the playback speed"""
        speed_str = e.control.value.replace("x", "")
        try:
            new_speed = float(speed_str)
            self.playback_speed = new_speed
            if self.audio:
                self.audio.playback_rate = new_speed
                self.audio.update()
        except ValueError:
            pass
    



def main(page: ft.Page):
    app = RosarioApp(page)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
