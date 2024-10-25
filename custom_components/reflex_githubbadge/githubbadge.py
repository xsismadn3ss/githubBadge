"""Reflex custom component Githubbadge."""

# For wrapping react guide, visit https://reflex.dev/docs/wrapping-react/overview/

import reflex as rx
import requests

# Some libraries you want to wrap may require dynamic imports.
# This is because they they may not be compatible with Server-Side Rendering (SSR).
# To handle this in Reflex, all you need to do is subclass `NoSSRComponent` instead.
# For example:
# from reflex.components.component import NoSSRComponent
# class Githubbadge(NoSSRComponent):
#     pass


class Githubbadge(rx.Component):
    """Githubbadge component."""

    # The React library to wrap.
    library = "Fill-Me"

    # The React component tag.
    tag = "Fill-Me"

    data = {
        "username": "",
        "name": "",
        "followers": "",
    }

    # If the tag is the default export from the module, you must set is_default = True.
    # This is normally used when components don't have curly braces around them when importing.
    # is_default = True

    # If you are wrapping another components with the same tag as a component in your project
    # you can use aliases to differentiate between them and avoid naming conflicts.
    # alias = "OtherGithubbadge"

    # The props of the React component.
    # Note: when Reflex compiles the component to Javascript,
    # `snake_case` property names are automatically formatted as `camelCase`.
    # The prop names may be defined in `camelCase` as well.
    # some_prop: rx.Var[str] = "some default value"
    # some_other_prop: rx.Var[int] = 1

    # By default Reflex will install the library you have specified in the library property.
    # However, sometimes you may need to install other libraries to use a component.
    # In this case you can use the lib_dependencies property to specify other libraries to install.
    # lib_dependencies: list[str] = []

    # Event triggers declaration if any.
    # Below is equivalent to merging `{ "on_change": lambda e: [e] }`
    # onto the default event triggers of parent/base Component.
    # The function defined for the `on_change` trigger maps event for the javascript
    # trigger to what will be passed to the backend event handler function.
    # on_change: rx.EventHandler[lambda e: [e]]

    # To add custom code to your component
    # def _get_custom_code(self) -> str:
    #     return "const customCode = 'customCode';"

    def get_user_data(url): ...

    @classmethod
    def create(cls, username: str, description: str):
        dark, light = "#202020", "#d1d1d1"
        github_data = requests.get(f"https://api.github.com/users/{username}").json()

        if "html_url" in github_data:
            name = github_data["name"]
            url = github_data["html_url"]
            if len(name) > 10:
                name = name[0:10] + "..."
            avatar = rx.avatar(
                src=github_data["avatar_url"],
                # radius="full",
                size="7",
                margin_bottom="0.5rem",
            )

        else:
            url = f"https://github.com/{username}"
            name = ""
            avatar = rx.avatar(
                fallback=f"{username[0:2]}".upper(),
                size="7",
                # radius="full",
                margin_bottom="0.5rem",
            )

        return rx.card(
            rx.link(
                rx.flex(
                    rx.inset(
                        rx.box(
                            background=github_data["avatar_url"],
                            height='100%'
                        ),
                        pr="current",
                        width="60%",
                        side="left",
                    ),
                    rx.flex(
                        rx.text(
                            name,
                            size="3",
                            weight="bold",
                            color=rx.color_mode_cond(dark, light),
                        ),
                        rx.text(
                            "@" + username,
                            size="1",
                            weight="regular",
                            color=rx.color_mode_cond(dark, light),
                        ),
                        rx.text(
                            description,
                            size="2",
                            weight="medium",
                            margin_top="0.6rem",
                            color=rx.color_mode_cond(dark, light),
                        ),
                        direction='column'
                    ),
                    spacing="0",
                    align="center",
                    direction="row",
                    width="100%",
                ),
                href=url,
            ),
            width="25vh",
        )


githubbadge = Githubbadge.create
