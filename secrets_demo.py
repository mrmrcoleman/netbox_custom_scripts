from extras.scripts import *
from django.utils.text import slugify

from dcim.choices import DeviceStatusChoices, SiteStatusChoices
from dcim.models import Device, DeviceRole, DeviceType, Site

import os


class NewBranchScript(Script):

    class Meta:
        name = "Display ENV VARs"
        description = "Display ENV VARs"

    env_var = StringVar(
        description="Name ENV VAR"
    )
    switch_count = IntegerVar(
        description="Number of access switches to create"
    )
    switch_model = ObjectVar(
        description="Access switch model",
        model=DeviceType
    )
    router_count = IntegerVar(
        description="Number of routers to create"
    )
    router_model = ObjectVar(
        description="Router model",
        model=DeviceType
    )
    ap_count = IntegerVar(
        description="Number of APs to create"
    )
    ap_model = ObjectVar(
        description="AP model",
        model=DeviceType
    )
    server_count = IntegerVar(
        description="Number of servers to create"
    )
    server_model = ObjectVar(
        description="Server model",
        model=DeviceType
    )

    def run(self, data, commit):

        self.log_success(f"Looking for ENV VAR: {env_var}")

        return '\n'.join(env_var)