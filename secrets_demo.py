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

    def run(self, data, commit):

        value = os.getenv('TEST')
        if value == None:
            self.log_success(f"Couldn't find ENV VAR: TEST")
        else:
            self.log_success(f"Found ENV VAR: TEST. Value: {value}")

        return value