import reflex as rx

from rxconfig import config



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        
        background_color="#f1f3c0",
    )


app = rx.App()
app.add_page(index)
