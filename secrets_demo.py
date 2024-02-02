class PackageCheck(Script):
    class Meta:
        name = "Show single ENV VAR called TEST"
        description = "Shows a single ENV VAR called TEST"

    def run(self, data, commit):
        self.log_success(f"Running Python {os.getenv('TEST')}")
        return f"{os.getenv('API_USER')}"
