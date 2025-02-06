import reflex as rx

from rxconfig import config



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.box(
            rx.hstack(
                rx.box(
                    rx.image(
                        src="/header.png",
                        width="500px",
                        height="auto",
                        border_radius="50px 50px 0px 0px",
                    ),
                    rx.box(
                        rx.image(
                            src="/person.jpg",
                            width="130px",
                            height="130px",
                            object_fit="cover",  
                            border_radius="50%",
                            aspect_ratio="1",
                        ),
                        position="absolute",
                        top="35%",
                        left="50%",
                        transform="translate(-50%, -50%)",
                        z_index="1",
                        overflow="hidden",       # Добавлено для обрезки изображения
                    ),
                    position="relative",
                ),
                
                
            ),
            rx.box(
                rx.text(
                    "John Smith",
                    size="7",
                    weight="bold",
                    letter_spacing="5px",
                ),
                rx.text(
                    "@johnsmith",
                    size="4",
                ),
                rx.box(
                    rx.hstack(
                        rx.icon(tag="youtube"),
                        rx.icon(tag="facebook"),
                        rx.icon(tag="github"),
                        rx.icon(tag="twitter"),
                        display="flex",
                        justify="center",
                        margin_top="20px",
                    ),
                    
                    align="center",
                    width="100%"
                    
                ),
                rx.box(
                    rx.text("Full-Stack Developer who thrives on solving complex problems with elegant code. By day, Alex works at a cutting-edge tech startup, building scalable web applications and optimizing backend systems",
                            text_align="center",
                            weight="bold"
                    ),
                    margin_top="20px",
                    padding="20px",
                ),
                rx.box(
                    rx.flex(
                        rx.button(
                            "Follow Me",
                            background_color="#e03f8c",
                            padding="24px 50px",
                            border_radius="50px",
                        ),
                        rx.button(
                            rx.text("Massage",color="#868686"),
                            background="transparent",
                            padding="24px 50px",
                            border_radius="50px",
                            border="1px solid #868686",
                        ),
                        style={"display": "flex", "justify-content": "space-around"},
                    ),
                    margin_top="20px",
                ),
                padding_top="20px",  
            ),
            
            width="500px",
            height="700px",
            border_radius="50px",
            background_color="white",
            style={
                "-webkit-box-shadow": "4px 4px 84px 0px rgba(34, 60, 80, 0.3)",
                "-moz-box-shadow": "4px 4px 84px 0px rgba(34, 60, 850, 0.3)",
                "box-shadow": "4px 4px 84px 0px rgba(34, 60, 80, 0.3)",
            }
        ),
        align="center",
        align_items="center",
        align_self="center",
        background_color="#f1f3c0",
        width="100%",
        height="100vh",  
        text_align="center",
        justify_content="center",
        
        )


app = rx.App(
    style={"font_family":"Roboto Mono, serif"},
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,100..700;1,100..700&display=swap"
    ]
)
app.add_page(index)
