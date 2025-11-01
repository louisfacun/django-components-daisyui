from django.conf import settings
from django_components import Component, register

from django_components_daisyui.utils.kwargs_to_attrs import kwargs_to_attrs


@register("alert")
class Alert(Component):
    template_name = "template.html"

    def get_context_data(
        self,
        color: str | None = None,
        title: str | None = None,
        description: str | None = None,
        icon: str | None = None,
        style: str | None = None,
        layout: str | None = None,
        **kwargs,
    ):
        djcd_defaults = getattr(settings, "DJC_DAISYUI_DEFAULTS", {})
        alert_defaults = djcd_defaults.get("alert", {})
        color = color if color is not None else alert_defaults.get("color")
        style = style if style is not None else alert_defaults.get("style")
        layout = layout if layout is not None else alert_defaults.get("layout")
        icon = icon if icon is not None else alert_defaults.get("icon")
        description_class = alert_defaults.get("description_class", "opacity-90")

        # Set default icons based on color
        if icon is None and color:
            icon_defaults = {
                "error": "circle-x",
                "success": "circle-check",
                "warning": "triangle-alert",
                "info": "info",
            }
            icon = icon_defaults.get(color)

        classes = ["alert"]

        if color:
            classes.append(f"alert-{color}")
            classes.append(f"border-{color}")
        if style in ["soft", "outline", "dash"]:
            classes.append(f"alert-{style}")
        if layout in ["vertical", "horizontal"]:
            classes.append(f"alert-{layout}")

        # Add default classes from settings
        default_class = alert_defaults.get("class")
        if default_class:
            classes.extend(default_class.split())

        # Add user-provided class if any
        user_class = kwargs.get("class")
        if user_class:
            classes.extend(user_class.split())
            kwargs = {k: v for k, v in kwargs.items() if k != "class"}

        attrs = kwargs_to_attrs(kwargs) | {"class": " ".join(classes), "role": "alert"}

        return {
            "attrs": attrs,
            "title": title,
            "description": description,
            "description_class": description_class,
            "icon": icon,
        }
