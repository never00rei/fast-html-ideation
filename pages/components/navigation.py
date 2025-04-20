from fasthtml.common import (
    Div,
    A,
    Img,
    Input,
    Ul,
    Li,
    Span,
    Details,
    Summary,
    Label,
    H2,
)

from fasthtml.svg import Svg, Path, Circle

"""
This is the main navigation section where we build all of the
components necessary for navigating the site.
"""


def main_navigation_bar():
    navbar = Div(
        Div(
            Div(
                Div(
                    Svg(
                        Path(
                            d="M4 6h16M4 12h8m-8 6h16",
                            stroke_width=2,
                            stroke_linecap="round",
                            stroke_linejoin="round",
                        ),
                        fill="none",
                        stroke="currentColor",
                        viewBox="0 0 24 24",
                        cls="h-5 w-5",
                    ),
                    tabindex="0",
                    role="button",
                    cls="btn btn-ghost lg:hidden",
                ),
                Ul(
                    Li(
                        Details(
                            Summary(
                                "Browse",
                            ),
                            Ul(
                                Li(
                                    A("Recent"),
                                ),
                                Li(
                                    A("Everything"),
                                ),
                                Li(
                                    A("Editor's Pick"),
                                ),
                                Li(
                                    A("Authors"),
                                ),
                                cls="p-2",
                            ),
                        ),
                    ),
                    Li(A("Your Library")),
                    Li(A("Create")),
                    tabindex="0",
                    cls="menu menu-md dropdown-content bg-neutral rounded-box text-neutral-content z-1 mt-3 w-52 p-2 shadow",
                ),
                cls="dropdown",
            ),
            A("Fictionaria", cls="btn btn-ghost text-xl"),
            cls="navbar-start",
        ),
        Div(
            Ul(
                Li(
                    Details(
                        Summary(
                            "Browse",
                        ),
                        Ul(
                            Li(
                                A("Recent"),
                            ),
                            Li(
                                A("Everything"),
                            ),
                            Li(
                                A("Editor's Pick"),
                            ),
                            Li(
                                A("Authors"),
                            ),
                            cls="dropdown-content bg-neutral text-neutral-content w-52 p-2",
                        ),
                        cls="dropdown bg-neutral text-neutral-content",
                    ),
                    cls="dropdown bg-neutral text-neutral-content",
                ),
                Li(
                    A(
                        "Your Library",
                    ),
                ),
                Li(
                    A("Create"),
                ),
                cls="menu menu-md menu-horizontal bg-neutral text-neutral-content px-1",
            ),
            cls="navbar-center hidden lg:flex",
        ),
        Div(
            Div(
                Input(
                    id="search-bar",
                    name="search",
                    placeholder="Search for something...",
                    cls="input input-bordered text-base-content text-opacity-100 hidden md:flex w-24 md:w-auto",
                ),
                Div(
                    Div(
                        Div(
                            Img(
                                src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp",
                                alt="UserPhoto",
                            ),
                            cls="w-10, rounded-full",
                        ),
                        tabindex="0",
                        role="button",
                        cls="btn btn-ghost btn-circle avatar",
                    ),
                    Ul(
                        Li(
                            A(
                                "Profile",
                                Span("New", cls="badge bg-primary text-base-content"),
                                cls="justify-between",
                            ),
                        ),
                        Li(
                            A("Settings"),
                        ),
                        Li(
                            A("Logout"),
                        ),
                        Li(
                            Div(cls="divider"),
                        ),
                        Li(
                            H2("Theme"),
                            Ul(
                                Li(
                                    Label(
                                        Svg(
                                            Circle(cx=12, cy=12, r=5),
                                            Path(
                                                d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"
                                            ),
                                            width="20",
                                            height="20",
                                            viewBox="0 0 24 24",
                                            fill="none",
                                            stroke="currentColor",
                                            stroke_linecap="round",
                                            stroke_linejoin="round",
                                        ),
                                        Input(
                                            type="checkbox",
                                            value="forest",
                                            cls="toggle theme-controller",
                                        ),
                                        Svg(
                                            Path(
                                                d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"
                                            ),
                                            width="20",
                                            height="20",
                                            viewBox="0 0 24 24",
                                            fill="none",
                                            stroke="currentColor",
                                            stroke_linecap="round",
                                            stroke_linejoin="round",
                                        ),
                                        cls="flex cursor-pointer gap-2",
                                    ),
                                ),
                            ),
                        ),
                        cls="menu menu-md dropdown-content bg-neutral rounded-box text-neutral-content z-1 mt-3 w-52 p-2 shadow",
                        tabindex="0",
                    ),
                    cls="dropdown dropdown-end dropdown-bottom",
                ),
                cls="flex gap-2",
            ),
            cls="navbar-end",
        ),
        cls="navbar bg-neutral text-neutral-content shadow-sm",
    )

    return navbar
