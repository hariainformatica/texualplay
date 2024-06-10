from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Header
from textual import on


class QuestionApp(App[str]):
    CSS = """
    Screen {
        layout: grid;
        grid-size: 2;
        grid-gutter: 2;
        padding: 2;
    }
    #question {
        width: 100%;
        height: 100%;
        column-span: 2;
        content-align: center bottom;
        text-style: bold;
    }

    Button {
        width: 100%;
    }
    """

    TITLE = "A Question App"
    SUB_TITLE = "The most important question"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Do you love Textual?", id="question")
        yield Button("Yes", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")

    '''
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)
    '''
    @on(Button.Pressed, selector="#yes")
    def on_yes_pressed(self, event: Button.Pressed) -> None:
        self.exit("yes")

    @on(Button.Pressed, selector="#no")
    def on_no_pressed(self, event: Button.Pressed) -> None:
        self.exit("no")

    def on_mount(self) -> None:
        header = self.query_one(Header)
        header.tall = True


if __name__ == "__main__":
    '''
    app = QuestionApp()
    reply = app.run()
    '''
    print(QuestionApp().run())