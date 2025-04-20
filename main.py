from fasthtml.common import FastHTML, Script, Link, serve
from pages.components.navigation import main_navigation_bar

tailwindCssLink = Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4")

daisyCssLink = Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@5")
daisyCssThemeLink = Link(
    rel="stylesheet", href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css"
)
app = FastHTML(
    hdrs=(daisyCssLink, daisyCssThemeLink, tailwindCssLink),
    title="An app from james!",
    htmlkw={"data-theme": "bumblebee"},
)


@app.route("/")
async def get():
    return main_navigation_bar()


serve()
